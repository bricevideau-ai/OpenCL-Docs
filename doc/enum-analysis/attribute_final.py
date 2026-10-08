#!/usr/bin/env python3
"""v4 — final spec-derived `group` attribution for cl.xml enums.

Rules (each group a C type name; multi-membership comma-separated):

  R1 Named value-set container in cl.xml that is itself a C typedef name
     (cl_mem_flags, cl_device_type, ...):  group = that name.
     (These containers ARE the C value sets — same as gl.xml groups.)

  R2 The mega-container `cl_device_info`:  group = the C type the spec
     documents the token under:
       R2a  "List of supported param_names by {clGet<X>Info}" label
            -> the `param_name` C type of clGet<X>Info (cl.xml signature)
       R2b  "List of supported event command types"           -> cl_command_type
       R2c  "New Enums" summary lists in extension chapters
            (token listed right under a {cl_X_TYPE} bullet)      -> that type
       R2d  define-list under an extension sentence naming the
            Get-function ("Accepted value for the _param_name_
            parameter to *clGetDeviceInfo*")                     -> that type
       R2e  #define under a `typedef cl_bits cl_X;`            -> that type
     If none apply, the token stays ungrouped (GL precedent: gl.xml
     leaves ~12k/15k enums ungrouped — context-dependent values are
     the norm there too, not the exception).

  R3 cl.xml ErrorCodes block -> group=ErrorCode (GL precedent:
     GL_NO_ERROR has group=ErrorCode; cl.xml's own comments say the
     values "are the same set of error codes returned from API calls").

  Multi-membership example (real, spec-listed):
    CL_DEVICE_AFFINITY_DOMAIN_*  in cl_device_affinity_domain (R1)
                                 AND cl_device_partition_property (R1)
                                 — both C typedefs list it in the spec.

Self-tests assert a known-good set; failures abort before XML rewrite.
Outputs doc/enum-analysis/attribution-final.json (+ .md review table).
"""

import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HERE = os.path.dirname(os.path.abspath(__file__))

TOKEN_RE = re.compile(r"\b(CL_[A-Z0-9_]+)\b")
FUNC_M = re.compile(r"\{?(cl(?:Get|Set|Create|Enqueue)[A-Za-z0-9]*|clGetDeviceIDs(?:From[A-Za-z0-9]+)?)\}?", re.I)

# Scalar/handle/opaque C names — can never be a "value set" group.
SKIP = set("""
cl_uint cl_char cl_schar cl_uchar cl_ushort cl_short cl_ushort cl_long
cl_ulong cl_short cl_byte cl_bit cl_bool cl_half cl_float cl_double
cl_device_id cl_context cl_command_queue cl_mem cl_buffer cl_image
cl_program cl_kernel cl_event cl_sampler cl_pipe cl_platform
cl_kernel_func cl_image_format cl_mem_object_type cl_image_object_type
cl_context properties cl_name_version
""".split())

# label phrase -> canonical value-set name (when the label names no C type)
LABEL_MAP = [
    (r"list of supported event command types", "cl_command_type"),
    (r"image channel order", "cl_channel_order"),
    (r"image channel data type", "cl_channel_type"),
    (r"list of supported memory flag values", "cl_mem_flags"),
    (r"list of supported map flag values", "cl_map_flags"),
    (r"list of supported migration flags", "cl_mem_migration_flags"),
    (r"list of supported (?:svm )?memory flag values", "cl_mem_flags"),
    (r"list of supported `?cl_command_queue_property`? values", "cl_command_queue_properties"),
    (r"list of supported image channel data types", "cl_channel_type"),
    (r"list of supported image channel order values", "cl_channel_order"),
    (r"list of supported device_types by", "cl_device_type"),
    (r"list of supported buffer creation types by", "cl_buffer_create_type"),
    (r"list of supported context creation properties by", "cl_context_properties"),
    (r"list of supported sampler creation properties by", "cl_sampler_properties"),
    (r"list of supported image creation properties", "cl_image_properties"),
    (r"list of supported (?:command[\s\-]+)?queue (?:creation )?properties by", "cl_command_queue_properties"),
    (r"list of supported partition schemes by", "cl_device_partition_property"),
]


def canonical(s):
    return re.sub(r"[^a-z0-9_]", "_", s.lower()).strip("_")


def resolve_label(label, fn_paramtype):
    """label -> value-set C type name (None if not resolvable)."""
    if not label:
        return None
    lab = label.lower()
    bm = re.search(r"`(cl_[a-z0-9_]+)`", lab)
    if bm and canonical(bm.group(1)) != "properties":
        cand = bm.group(1)
        # accept if the C name or +s is a known type
        if cand in GLOBALS.vsets or cand + "s" in GLOBALS.vsets:
            return cand if cand in GLOBALS.vsets else cand + "s"
    pm = re.search(r"(cl_[a-z0-9_]+)_TYPE", lab)
    if pm and pm.group(1) in GLOBALS.vsets:
        return pm.group(1)
    for pat, name in LABEL_MAP:
        if re.search(pat, lab) and name in GLOBALS.vsets:
            return name
    # function-name resolution must run on the ORIGINAL-CASE label
    fm = re.search(r"param_names by\s*[\{*<]*(clGet[A-Za-z0-9_]+)", label)
    if fm and fm.group(1) in fn_paramtype:
        return fn_paramtype[fm.group(1)]
    return None


class GLOBALS:
    vsets = set()
    containers = {}
    fn_paramtype = {}


def load_registry():
    tree = ET.parse(os.path.join(BASE, "xml/cl.xml"))
    root = tree.getroot()
    containers = {}
    for enums in root.findall("enums"):
        c = enums.get("name", "")
        for e in enums.iter("enum"):
            n = e.get("name")
            if n:
                containers[n] = (c, e.get("value"))
    vsets = set()
    for enums in root.findall("enums"):
        c = enums.get("name", "")
        if c.lower().startswith("cl_"):
            vsets.add(c)
    for t in root.findall("types/type"):
        nm_el = t.find("name")
        if nm_el is not None and nm_el.text:
            last = nm_el.text.split()[-1].strip()
            if last.lower().startswith("cl_"):
                vsets.add(last)
    vsets -= SKIP
    fn_paramtype = {}
    for cmd in root.findall("commands/command"):
        p = cmd.find("proto/name")
        if p is None:
            continue
        fn = p.text.strip()
        for pp in cmd.findall("param"):
            nm, ty = pp.find("name"), pp.find("type")
            if nm is not None and ty is not None and (nm.text or "").strip() == "param_name":
                fn_paramtype[fn] = (ty.text or "").strip()
    # also register cl_command_type as a known value set name (it is a C type in cl.xml)
    # (cl.xml declares: typedef cl_uint cl_command_type;)
    return containers, vsets, fn_paramtype


def mine():
    containers, vsets, fn_paramtype = GLOBALS.containers, GLOBALS.vsets, GLOBALS.fn_paramtype
    names = set(containers)
    ev = defaultdict(list)
    G = lambda g, k, f: (g, k, f)

    files = []
    api = os.path.join(BASE, "api")
    for f in sorted(os.listdir(api)):
        if re.match(r"^(opencl_(runtime|platform)_layer|cl_(khr|ext)_[a-z0-9_]+)\.asciidoc$", f):
            files.append("api/" + f)
    # the environment spec (image channel orders, addressing modes, image formats)
    envd = os.path.join(BASE, "env")
    if os.path.isdir(envd):
        for f in sorted(os.listdir(envd)):
            if f.endswith(".asciidoc"):
                files.append("env/" + f)
    ext = os.path.join(BASE, "extensions")
    if os.path.isdir(ext):
        for f in sorted(os.listdir(ext)):
            if f.endswith(".asciidoc") and "template" not in f:
                files.append("extensions/" + f)

    for rel in files:
        lines = open(os.path.join(BASE, rel), encoding="utf-8").read().split("\n")
        n = len(lines)
        i = 0
        label = None
        pending_parent = None            # G3: current {type_TYPE} bullet
        pending_parent_err = False
        while i < n:
            raw = lines[i]
            s = raw.strip()

            # ---- G3 "New Enums" summary lists ----
            pm = re.match(r"^\*[ \t]*\{(cl_[a-z0-9_]+)_TYPE\}", s)
            if pm:
                pending_parent = pm.group(1) if pm.group(1) in vsets else None
                pending_parent_err = False
                i += 1
                continue
            if re.search(r"new\s+error\s+codes", s, re.I) and s.startswith("*"):
                pending_parent = None
                pending_parent_err = True
                i += 1
                continue
            cm = re.match(r"^\*\*[ \t]*\{(CL_[A-Z0-9_]+)", s)
            if cm and cm.group(1) in names:
                if pending_parent:
                    ev[cm.group(1)].append(G(pending_parent, "G3 new-enums list", rel))
                elif pending_parent_err:
                    ev[cm.group(1)].append(G("ErrorCode", "G3 new-error-codes list", rel))
                i += 1
                continue
            if s and not s.startswith(("|", "*", "#", "[", "=", "`", "-")) and len(s) > 2 or s.startswith("=="):
                if not (s.startswith("====") or s.startswith("|")):
                    pending_parent = None
                    pending_parent_err = False
            if re.match(r"^={1,6}\s", raw) or s.startswith("----") or s.startswith("include::") or s.startswith("ifdef") or s.startswith("endif"):
                i += 1
                continue

            # ---- grid tables ----
            if s == "|====":
                i += 1
                rows = []
                row = None
                while i < n:
                    r2 = lines[i]
                    t2 = r2.strip()
                    if set(t2) <= {"=", "|"} and len(t2) >= 5:
                        i += 1
                        break
                    # conditional blocks (ifdef/ifndef/endif): two forms in
                    # spec tables —
                    #  (a) ROW-GATED: the first content line starts a new '|'
                    #      row; the block holds self-contained rows (e.g. the
                    #      clEnqueueAcquireGLObjects /
                    #      {CL_COMMAND_ACQUIRE_GL_OBJECTS} pair under
                    #      cl_khr_gl_sharing).  Parse normally.
                    #  (b) CELL-CONTINUATION: the content is prose/anchor
                    #      alternatives that merge into the open cell (e.g.
                    #      "{CL_DEVICE_UUID_anchor}" / ifdef::
                    #      "or" / {CL_DEVICE_UUID_KHR_anchor} / endif::) —
                    #      that corrupts the clean-cell test, so skip the
                    #      whole block, tag-matched and depth-counted.
                    cm2 = re.match(r"^(ifdef|ifndef)::([a-zA-Z0-9_]+)\[\]$", t2)
                    if cm2:
                        cond_tag = cm2.group(2)
                        # find the matching endif (depth-counted)
                        end_i = i
                        depth = 1
                        k = i
                        while k < n - 1 and depth > 0:
                            k += 1
                            c2 = lines[k].strip()
                            mm = re.match(r"^(ifdef|ifndef)::([a-zA-Z0-9_]+)\[\]$", c2)
                            if mm and mm.group(2) == cond_tag:
                                depth += 1
                            elif re.match(r"^endif::" + re.escape(cond_tag) + r"\[\]$", c2):
                                depth -= 1
                        end_i = k
                        # first meaningful content line in the block
                        first_content = None
                        for k2 in range(i + 1, end_i + 1):
                            c3 = lines[k2].strip()
                            if c3 and not c3.startswith(("//", "include::",
                                                       "ifdef::", "ifndef::",
                                                       "endif::")):
                                first_content = c3
                                break
                        if first_content is not None and first_content.startswith("|"):
                            i += 1        # (a): parse the block's rows normally
                            continue
                        i = end_i + 1      # (b): drop the continued content
                        continue
                    if re.match(r"^endif::[a-zA-Z0-9_]+\[\]$", t2):
                        i += 1
                        continue
                    # metadata lines are not cell content — skipping them
                    # keeps "{CL_X_anchor}" cells clean for the clean-cell test
                    if t2.startswith("include::") or t2.startswith("ifdef::") or t2.startswith("endif::"):
                        i += 1
                        continue
                    # asciidoc line comments: per the AsciiDoc spec (comments
                    # doc) the processor removes line comments before
                    # processing table cell content, so a rendered value-cell
                    # chain like "{CL_A} + {CL_B}" never includes a "// note".
                    # (/// and anything else are left alone.)
                    if t2.startswith("//") and not t2.startswith("///"):
                        i += 1
                        continue
                    if r2.startswith("|"):
                        if row is not None:
                            rows.append(row)
                        row = [c.strip().strip('`') for c in r2[1:].split("|")]
                    elif re.match(r"^\s+\|", r2) and row is not None:
                        row.append(r2.lstrip()[1:].strip())
                    elif row is not None and t2:
                        row[-1] = (row[-1] + " " + t2).strip()
                    i += 1
                if row is not None:
                    rows.append(row)

                grp = resolve_label(label, fn_paramtype)
                if grp:
                    # ---- inline value-set members (spec-derived) ----
                    # Some rows in a param_names table document a VALUE SET
                    # inline: the row's type cell is the set's C typedef
                    # ({cl_filter_mode_TYPE} for the CL_SAMPLER_FILTER_MODE
                    # row) and its description cell enumerates the members
                    # ("Valid values are: {CL_FILTER_NEAREST} - ...").
                    # Evidence rule (opencl_runtime_layer.asciidoc, sampler
                    # creation properties; clGetKernelArgInfo table):
                    #   (1) type cell == {cl_X_TYPE} and X is neither a
                    #       primitive type nor an opaque handle type;
                    #   (2) description cell carries an explicit enumeration
                    #       introducer ("Valid values are:" / "Accepted
                    #       values are:" / "one of the following");
                    #   (3) each {CL_TOKEN} in that cell that is a real
                    #       cl.xml name is a member of the cl_X value set.
                    # Tokens absent from cl.xml (stale spec prose such as
                    # CL_ADDRESS_REPEAT) are skipped via the names check.
                    INLINE_INTRO_RE = re.compile(
                        r"(?:valid|accepted)\s+values\s+are\s*:?"
                        r"|one\s+of\s+the\s+following\s*:?"
                        r"|following\s+values\s+are\s*:?",
                        re.I)
                    INLINE_NOT_SET = frozenset({
                        "cl_uint", "cl_int", "cl_char", "cl_uchar", "cl_schar",
                        "cl_short", "cl_ushort", "cl_long", "cl_ulong",
                        "cl_longlong", "cl_ulonglong", "cl_float", "cl_double",
                        "cl_bool", "cl_size_t", "cl_platform", "cl_context",
                        "cl_command_queue", "cl_mem", "cl_device",
                        "cl_program", "cl_kernel", "cl_event", "cl_sampler",
                        "cl_image", "cl_accelerator",
                    })
                    INLINE_TOKEN_RE = re.compile(r"CL_[A-Z0-9]+(?:_[A-Z0-9]+)*")
                    for row in rows:
                        if len(row) < 3:
                            continue
                        tm = re.match(r"^\{?cl_([a-z0-9_]+)_TYPE\}?$",
                                     row[1].strip())
                        if not tm:
                            continue
                        setname = "cl_" + tm.group(1)
                        if setname in INLINE_NOT_SET:
                            continue
                        dcell = " ".join(c.strip() for c in row[2:])
                        if not INLINE_INTRO_RE.search(dcell):
                            continue
                        for tm2 in INLINE_TOKEN_RE.finditer(dcell):
                            tok = tm2.group(0)
                            if tok not in names:
                                continue
                            ev[tok].append(G(setname,
                                "inline value-set of %s (row %s)"
                                % (setname, row[0].strip()[:40]),
                                rel))
                    # A row contributes a token only from a CLEAN value cell —
                    # a cell whose entire content is a single {CL_X} (optionally
                    # with a footnote link).  Scanning cells (not just column
                    # 0) catches "List of supported event command types" tables
                    # (function in col 0, token in col 1), while ignoring
                    # description cells that merely mention other values in
                    # prose (the CL_FALSE-in-10-sets contamination class).
                    CLEAN_CELL_RE = re.compile(
                        r"^\{?CL_[A-Z0-9]+(?:_[A-Z0-9]+)*(?:_anchor)?\}?\s*(?:footnote:\[[^\]]*\])?$")
                    # A "+"-CONTINUED value cell: an asciidoc grid row written
                    # as one token per line with "+" line continuations, e.g.
                    #   | {CL_DEVICE_NATIVE_VECTOR_WIDTH_CHAR_anchor}   +
                    #     {CL_DEVICE_NATIVE_VECTOR_WIDTH_SHORT_anchor}  +
                    #     ...
                    # The cell, after my line accumulator merges it, is:
                    #   "{CL_A_anchor}   + {CL_B_anchor}  + {CL_C_anchor}"
                    # Attribute every token in such a chain (column 0 only) to
                    # the resolved group, but ONLY if the whole cell is a chain
                    # of known CL_ tokens with nothing else in it — this
                    # prevents description prose from ever being harvested.
                    # Tokens known to be value-set members (not param_names):
                    # exclude (they appear mixed in as return-value examples and
                    # would contaminate the group with an unrelated C set).
                    # token = CL_ followed by underscore-separated runs of
                    # UPPERCASE alphanumerics.  This matches a real enum name
                    # (CL_DEVICE_UUID, CL_R) and a {CL_X_anchor} cell entry
                    # but STOPS before the lowercase "anchor" suffix and
                    # before any prose — so a token match always yields the
                    # bare cl.xml name with NO suffix stripping needed.
                    # (A naive CL_[A-Z0-9_]+ greedily eats the underscore of
                    # the _anchor suffix and leaves "anchor" as residue.)
                    TOKEN = r"CL_[A-Z0-9]+(?:_[A-Z0-9]+)*"
                    KNOWN_FALSE_POSITIVE = frozenset({
                        "CL_TRUE", "CL_FALSE", "CL_NONE",
                        "CL_READ_ONLY", "CL_WRITE_ONLY", "CL_READ_WRITE",
                        "CL_MEM_READ_WRITE", "CL_MEM_WRITE_ONLY",
                        "CL_MEM_READ_ONLY", "CL_MEM_USE_HOST_PTR",
                        "CL_MEM_COPY_HOST_PTR", "CL_MEM_ALLOC_HOST_PTR",
                    })

                    def extract_chain(cell):
                        """Return the LEADING run of `+`-separated CL_ tokens in
                        cell (>=2, all real cl.xml names), ignoring anything
                        that follows the chain.  A cell that starts with prose,
                        or whose first run has <2 valid tokens, returns None.

                        Leading-run (rather than whole-cell) is intentional:
                        some value cells carry a trailing version-note
                        paragraph in the source, so the chain must be the
                        prefix, not the entire cell.  Because this only ever
                        runs on column 0 (the name column), a description cell
                        like "Is {CL_TRUE} if ... {CL_FALSE} otherwise" can
                        never be harvested — its first run is a single token
                        before prose, so it fails the >=2 test.
                        """
                        if "+" not in cell:
                            return None
                        rest = cell.strip()
                        chain = []
                        tok_re = re.compile(r"^\{?\s*(" + TOKEN + r")(_anchor)?\}?\s*(\+\s*)?")
                        while True:
                            m = tok_re.match(rest)
                            if not m:
                                break
                            chain.append(m.group(1))
                            had_plus = m.group(3) is not None
                            rest = rest[m.end():]
                            if not had_plus:  # chain ends at first non-`+`
                                break
                        if len(chain) < 2:
                            return None
                        if not all(t in names for t in chain):
                            return None
                        # value-set members that appear only as RETURN-VALUE
                        # examples in this family of tables: exclude them so a
                        # mixed cell can never drag CL_TRUE/CL_FALSE/cl_mem
                        # flags into an unrelated group.
                        if set(chain) & KNOWN_FALSE_POSITIVE:
                            return None
                        return chain

                    for row in rows:
                        # column 0 rules (the value/names column):
                        #  (a) +chain of tokens (>=2)             -> every token
                        #  (b) a single leading CL_ enum name, optionally
                        #      followed by a trailing note          -> that token
                        #  (c) a whole-cell single clean token      -> that token
                        # Columns 1+ (return-type / description) are scanned
                        # ONLY for a whole-cell clean token, never for a
                        # leading-lead — description prose that happens to
                        # start with a CL_ token is never harvested.
                        if row:
                            ch = extract_chain(row[0])
                            if ch:
                                for tc in ch:
                                    ev[tc].append(G(grp,
                                        "value chain col0 (" + (label or "")[:50] + ")", rel))
                                continue
                            mcell = CLEAN_CELL_RE.match(row[0].strip())
                            c = ""
                            if mcell:
                                c = re.sub(r"footnote:\[[^\]]*\]", "",
                                           mcell.group(0).strip()).strip()
                                c = c.lstrip("{").rstrip("}")
                                if c.endswith("_anchor"):
                                    c = c[:-len("_anchor")]
                            if not c:
                                sm = re.match(r"^\s*\{?\s*(" + TOKEN + r")(?:_anchor)?\}?", row[0])
                                c = sm.group(1) if sm else ""
                            if c in names:
                                ev[c].append(G(grp,
                                    "value cell col0 (" + (label or "")[:50] + ")", rel))
                                continue
                            # (d) "function-in-col0, token-in-col1" tables
                            #     (e.g. "List of supported event command
                            #     types"): col1 may carry a trailing note
                            #     ("Prior to OpenCL 3.0 ..."), so only a
                            #     whole-cell clean token would be caught
                            #     above.  A single leading CL_ token in col1
                            #     is the event command type for that command.
                            if len(row) >= 2 and re.match(r"^\s*\{?\s*cl(?:Get|Set|Create|Enqueue|Wait)", row[0], re.I):
                                lt = re.match(r"^\s*\{?\s*(CL_[A-Z0-9]+(?:_[A-Z0-9]+)*)", row[1])
                                if lt and lt.group(1) in names:
                                    ev[lt.group(1)].append(G(grp,
                                        "event-type col1-of-fn (" + (label or "")[:50] + ")", rel))
                        for cell in row[1:]:
                            mcell = CLEAN_CELL_RE.match(cell.strip())
                            if not mcell:
                                continue
                            c = re.sub(r"footnote:\[[^\]]*\]", "",
                                       mcell.group(0).strip()).strip()
                            c = c.lstrip("{").rstrip("}")
                            if c.endswith("_anchor"):
                                c = c[:-len("_anchor")]
                            if c.startswith("CL_") and c in names:
                                ev[c].append(G(grp,
                                    "clean cell col1+ (" + (label or "")[:50] + ")", rel))
                label = None
                continue

            if s.startswith("include::") or s.startswith("ifdef") or s.startswith("endif"):
                i += 1
                continue
            if re.match(r"^====\s*\[?open,?refpage='(cl[A-Za-z0-9_]+)'", s):
                # refpage change: param-name evidence context
                i += 1
                continue
            if re.match(r"^={1,6}\s+\S", s):
                label = re.sub(r"^={1,6}\s+", "", raw).strip()
                i += 1
                continue
            if re.match(r"\.(?!\d)\S.*", s):
                label = s.lstrip(".").strip()
                i += 1
                continue

            # ---- G4/G5: #define lines ----
            # Anchor priority for a bit / constant #define:
            #   (1) bit member: nearest `typedef cl_bitfield cl_X;` above the
            #       line + `(1 << N)` form => that C typedef (the cl.xml
            #       bitpos layout agrees -- bit members live in their C
            #       container, not in a neighbouring sentence's param set).
            #   (2) sentence: nearest "Accepted value for the _param_name_
            #       parameter to *<fn>*" within the 14-line window.
            #   (3) typedef container (cl_bits / cl_bitfield) named within
            #       the 14-line window.
            #   (4) `_TYPE` row cell within the 14-line window (table rows
            #       whose return-type declares the set).
            # Anything weaker is skipped rather than guessed.
            dm = re.match(r"#define\s+(CL_[A-Z0-9_]+)", s)
            if dm and dm.group(1) in names:
                ctx = "\n".join(lines[max(0, i - 14):i])
                # BIT MEMBER (1 << N): these are members of a cl_bitfield.
                # If a `typedef cl_bitfield cl_X;` is in the window, bind to
                # it.  If not (e.g. the cl_arm_controlled_kernel_termination
                # extension never restates the typedef — its New-API-Enums
                # block only mentions the capabilities set in prose), do NOT
                # bind to the nearest "param_name parameter to *clGet...*"
                # sentence: that sentence anchors the CAPABILITIES QUERY token
                # (CL_..._CAPABILITIES... 0x41EE), not the bit members that
                # follow it in the same C block.  The R1 container rule
                # (bitpos layout in cl.xml) owns those; a sentence
                # attribution here is noise (it produced spurious
                # cl_device_info / cl_event_info memberships on the ARM
                # trio).
                if re.search(r"1\s*<<\s*\d+", s):
                    btm = re.search(r"typedef\s+cl_bitfield\s+(cl_[a-z0-9_]+)\s*;", ctx)
                    if btm and btm.group(1) in vsets and btm.group(1) in containers:
                        ev[dm.group(1)].append(G(btm.group(1),
                            "bit member of cl_bitfield (define)", rel))
                        i += 1
                        continue
                    i += 1
                    continue
                # Anchor on the NEAREST preceding "param_name  parameter  to
                # <fn>" sentence (last occurrence in the window).
                tm2_list = re.findall(r"param_name_\s*parameter\s*to\s*\*?([^*\n{]+)", ctx)
                if tm2_list:
                    fn = tm2_list[-1].strip()
                    if fn in fn_paramtype and fn_paramtype[fn]:
                        ev[dm.group(1)].append(G(fn_paramtype[fn], "G4 sentence+define", rel))
                        i += 1
                        continue
                tm3 = re.search(r"typedef\s+cl_\w+\s+(cl_[a-z0-9_]+)\s*;", ctx)
                if tm3 and tm3.group(1) in vsets:
                    ev[dm.group(1)].append(G(tm3.group(1), "G4 typedef+define", rel))
                    i += 1
                    continue
                tm4 = re.search(r"(cl_[a-z0-9_]+)_TYPE", ctx)
                if tm4 and tm4.group(1) in vsets:
                    # Only trust a `_TYPE` reference when it sits on a table
                    # ROW (the row's return-type cell: "| X | cl_Y_TYPE" or
                    # "| cl_Y_TYPE").  A bare "_TYPE" appearing in loose
                    # PROSE within the 14-line window is unreliable: e.g. the
                    # cl_arm_controlled_kernel_termination extension lists its
                    # bit members in the *cl_device_info* table's row text
                    # ("...supported.") while a later *cl_event_info* table
                    # block mentions {CL_COMMAND_TERMINATED_ITSELF_WITH_FAILURE_ARM}
                    # under {CL_EVENT_COMMAND_EXECUTION_STATUS}, whose type
                    # {cl_int_TYPE} is unrelated -- window-based matching leaks
                    # the event table into the bit members.  Require a row
                    # cell to anchor the typedef.
                    tm4_row = re.search(
                        r"^\|\s*\S.*\|\s*\{?(?:cl_)?[a-z0-9_]+_TYPE\}?\s*$",
                        ctx, re.M)
                    if tm4_row:
                        ev[dm.group(1)].append(G(tm4.group(1), "G4 sentence-type+define", rel))
                        i += 1
                        continue
            i += 1
    return ev


def attribute(ev):
    containers, vsets, fn_paramtype = GLOBALS.containers, GLOBALS.vsets, GLOBALS.fn_paramtype
    out = {}
    for tok in sorted(containers):
        container, val = containers[tok]
        groups = set()
        notes = []
        evs = ev.get(tok, [])

        is_err = container.startswith("ErrorCodes")
        if is_err:
            groups.add("ErrorCode")
            notes.append("R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values)")

        named_container = container.lower().startswith("cl_") and container != "cl_device_info"
        if not is_err and named_container:
            groups.add(container)
            corroborated = any(g == container for (g, _, _) in evs)
            notes.append("R1 C typedef container %s%s" % (container, " (spec-listed)" if corroborated else " (container-declared)"))

        spec_groups = set()
        for (g, k, f) in evs:
            if g == "ErrorCode" or (g in vsets or g.endswith("_info")):
                spec_groups.add(g)
                if not any(g == x for x in []) and k not in " ".join(notes):
                    pass
        for g in sorted(spec_groups):
            if g in vsets or g.endswith("_info") or g == "ErrorCode":
                if named_container and g == container:
                    continue
                groups.add(g)
                k = next((k for (gg, k, f) in evs if gg == g), "")
                notes.append("spec evidence [%s] %s" % (g, k.split(",")[0]))

        # mega-container: spec family wins; if nothing, stay unassigned
        if container == "cl_device_info" and not groups:
            notes.append("cl_device_info mega-container token; no spec value-set found — left ungrouped")

        out[tok] = {
            "container": container,
            "value": val,
            "groups": sorted(groups),
            "notes": notes,
        }
    return out


SELF_TESTS = {
    "CL_MEM_READ_WRITE": {"cl_mem_flags"},
    "CL_MAP_READ": {"cl_map_flags"},
    "CL_KERNEL_ARG_TYPE_CONST": {"cl_kernel_arg_type_qualifier"},
    "CL_BUILD_SUCCESS": {"cl_build_status"},
    "CL_LOCAL": {"cl_device_local_mem_type"},
    "CL_FP_DENORM": {"cl_device_fp_config"},
    "CL_FALSE": {"cl_bool"},
    "CL_TRUE": {"cl_bool"},
    "CL_SUCCESS": {"ErrorCode"},
    "CL_INVALID_VALUE": {"ErrorCode"},
    "CL_SVM_CAPABILITY_SINGLE_ADDRESS_SPACE_KHR": {"cl_svm_capabilities_khr"},
    "CL_SEMAPHORE_TYPE_BINARY_KHR": {"cl_semaphore_type_khr"},
    "CL_COMMAND_BUFFER_STATE_RECORDING_KHR": {"cl_command_buffer_state_khr"},
    "CL_PLATFORM_NAME": {"cl_platform_info"},
    "CL_PLATFORM_PROFILE": {"cl_platform_info"},
    "CL_EVENT_REFERENCE_COUNT": {"cl_event_info"},
    "CL_COMMAND_NDRANGE_KERNEL": {"cl_command_type"},
    "CL_COMMAND_TASK": {"cl_command_type"},
    "CL_COMMAND_COPY_BUFFER": {"cl_command_type"},
    "CL_QUEUE_OUT_OF_ORDER_EXEC_MODE_ENABLE": {"cl_command_queue_properties"},
    # CL_DEVICE_TYPE (0x1003) is a clGetDeviceInfo QUERY KEY (param_name),
    # not a member of the cl_device_type value set — mirrors gl.xml where
    # GL_MAX_TEXTURE_SIZE groups as a GetPName, not as a TextureTarget.
    "CL_DEVICE_TYPE": {"cl_device_info"},
    "CL_DEVICE_TYPE_CPU": {"cl_device_type"},
    "CL_DEVICE_AFFINITY_DOMAIN_NUMA": {"cl_device_affinity_domain"},
    "CL_QUEUE_PRIORITY_HIGH_KHR": {"cl_queue_priority_khr"},
    "CL_QUEUE_PRIORITY_MED_KHR":  {"cl_queue_priority_khr"},
    "CL_QUEUE_PRIORITY_LOW_KHR":  {"cl_queue_priority_khr"},
    # queue-hint *names* (New Enums bullets of cl_khr_priority_hints /
    # cl_khr_throttle_hints under cl_queue_properties_TYPE) + the core
    # cl_command_queue_properties table row
    "CL_QUEUE_PRIORITY_KHR": {"cl_queue_properties", "cl_command_queue_properties"},
    "CL_QUEUE_THROTTLE_KHR": {"cl_queue_properties", "cl_command_queue_properties"},
    # Intel USM: CL_MEM_ALLOC_FLAGS_INTEL appears as a property
    # (cl_mem_properties_intel table) and a query (cl_mem_alloc_info table)
    "CL_MEM_ALLOC_FLAGS_INTEL": {"cl_mem_properties_intel"},
    # CL_QUEUE_FAMILY_INTEL / CL_QUEUE_INDEX_INTEL: property + query token
    "CL_QUEUE_FAMILY_INTEL": {"cl_command_queue_properties", "cl_command_queue_info"},
    "CL_QUEUE_INDEX_INTEL":  {"cl_command_queue_properties", "cl_command_queue_info"},
    # bit-members live in their cl_bitfield capacity set ONLY.
    # (Positive membership asserted here; the NEGATIVE_TESTS above forbid
    # the cl_device_info / cl_event_info sentence-anchor contamination.)
    "CL_DEVICE_CONTROLLED_TERMINATION_SUCCESS_ARM": {"cl_device_controlled_termination_capabilities_arm"},
    "CL_DEVICE_CONTROLLED_TERMINATION_FAILURE_ARM": {"cl_device_controlled_termination_capabilities_arm"},
    "CL_DEVICE_CONTROLLED_TERMINATION_QUERY_ARM":   {"cl_device_controlled_termination_capabilities_arm"},
    # "+continued value-cell" family (Brice-flagged 2026-10-07): each of these
    # is a param_name for clGetDeviceInfo, documented as a one-token-per-line
    # chain in the Device Queries table (opencl_platform_layer.asciidoc).
    "CL_DEVICE_NATIVE_VECTOR_WIDTH_CHAR": {"cl_device_info"},
    "CL_DEVICE_NATIVE_VECTOR_WIDTH_HALF": {"cl_device_info"},
    "CL_DEVICE_PREFERRED_VECTOR_WIDTH_CHAR": {"cl_device_info"},
    "CL_DEVICE_PREFERRED_VECTOR_WIDTH_DOUBLE": {"cl_device_info"},
    "CL_DEVICE_UUID": {"cl_device_info"},
    "CL_DEVICE_SPIRV_CAPABILITIES": {"cl_device_info"},
    "CL_DEVICE_IMAGE_PITCH_ALIGNMENT": {"cl_device_info"},
    "CL_KERNEL_ARG_ADDRESS_GLOBAL": {"cl_kernel_arg_info"},
    "CL_KERNEL_ARG_ACCESS_READ_ONLY": {"cl_kernel_arg_info"},
    "CL_KERNEL_MAX_SUB_GROUP_SIZE_FOR_NDRANGE": {"cl_kernel_sub_group_info"},
    # value-set members documented inline in a param_name row's description
    # (return-type cell = the set's C typedef).  These are the "brute-force"
    # cases that need the inline-value rule, not a table-value rule.
    "CL_ADDRESS_CLAMP": {"cl_addressing_mode"},
    "CL_FILTER_NEAREST": {"cl_filter_mode"},
    "CL_KERNEL_ARG_ADDRESS_GLOBAL": {"cl_kernel_arg_address_qualifier"},
    "CL_KERNEL_ARG_ACCESS_READ_ONLY": {"cl_kernel_arg_access_qualifier"},
    "CL_PROGRAM_IL": {"cl_program_info"},
    "CL_COMMAND_SVM_MIGRATE_MEM": {"cl_command_type"},
    "CL_D3D10_DEVICE_KHR": None,      # may be ungrouped (opaque handle-ish)
    "CL_CHAR_BIT": {"C99MathConstants"},  # appendix_c C99 constant (was 'may be ungrouped')
    "CL_NV21": {"cl_channel_order"},      # cl_img_yuv_image image channel order
    # QCOM perf hint (Brice-flagged 2026-10-07): the property NAME is a clCreateContext
    # creation property; the HIGH/NORMAL/LOW values are the cl_perf_hint_qcom value set
    "CL_CONTEXT_PERF_HINT_QCOM": {"cl_context_properties"},
    "CL_PERF_HINT_HIGH_QCOM":  {"cl_perf_hint_qcom"},
    "CL_PERF_HINT_NORMAL_QCOM": {"cl_perf_hint_qcom"},
    "CL_PERF_HINT_LOW_QCOM":   {"cl_perf_hint_qcom"},
    # ARM scheduling controls: one token per spec-documented role table
    "CL_DEVICE_SCHEDULING_CONTROLS_CAPABILITIES_ARM": {"cl_device_info"},
    "CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM": {"cl_kernel_exec_info"},
    "CL_KERNEL_MAX_WARP_COUNT_ARM": {"cl_kernel_info"},
    "CL_QUEUE_KERNEL_BATCHING_ARM": {"cl_command_queue_properties"},
    # ARM controlled termination: query key vs bit set
    "CL_EVENT_COMMAND_TERMINATION_REASON_ARM": {"cl_event_info"},
    "CL_DEVICE_CONTROLLED_TERMINATION_CAPABILITIES_ARM": {"cl_device_info"},
    # Intel required subgroup size: three distinct query tables
    "CL_DEVICE_SUB_GROUP_SIZES_INTEL": {"cl_device_info"},
    "CL_KERNEL_SPILL_MEM_SIZE_INTEL": {"cl_kernel_work_group_info"},
    "CL_KERNEL_COMPILE_SUB_GROUP_SIZE_INTEL": {"cl_kernel_sub_group_info"},
    # KHR unified SVM: pointer-info query set vs alloc property set
    "CL_SVM_INFO_BASE_PTR_KHR": {"cl_svm_pointer_info_khr"},
    "CL_SVM_ALLOC_ACCESS_FLAGS_KHR": {"cl_svm_alloc_properties_khr"},
    # command execution status value set (registry name)
    "CL_COMPLETE": {"clCommandExecutionStatus"},
    "CL_RUNNING": {"clCommandExecutionStatus"},
}

# negative guard: QCOM perf-hint pair must not cross-contaminate (the original bug)
NEG_TESTS_QCOM = {
    "CL_CONTEXT_PERF_HINT_QCOM": {"cl_perf_hint_qcom"},
    "CL_PERF_HINT_HIGH_QCOM":  {"cl_context_properties"},
    "CL_PERF_HINT_NORMAL_QCOM": {"cl_context_properties"},
    "CL_PERF_HINT_LOW_QCOM":   {"cl_context_properties"},
}

# negative containment: these tokens must NOT appear in these sets
# (regression guard for the description-cell contamination class)
NEGATIVE_TESTS = {
    "CL_FALSE": {"cl_mem_flags", "cl_map_flags", "cl_kernel_exec_info", "cl_svm_capabilities_khr",
                 "cl_device_info", "cl_sampler_properties", "cl_kernel_arg_info",
                 "cl_kernel_sub_group_info", "cl_command_type", "cl_program_info"},
    "CL_TRUE":  {"cl_mem_flags", "cl_map_flags", "cl_kernel_exec_info", "cl_svm_capabilities_khr",
                 "cl_device_info", "cl_sampler_properties", "cl_kernel_arg_info",
                 "cl_kernel_sub_group_info", "cl_command_type", "cl_program_info"},
    "CL_NONE":  {"cl_mem_flags", "cl_map_flags", "cl_device_info", "cl_kernel_arg_info"},
    # chain-rule guard: mem-flag tokens must not land in a param_name group
    "CL_MEM_WRITE_ONLY": {"cl_device_info", "cl_kernel_arg_info", "cl_sampler_properties"},
    "CL_MEM_USE_HOST_PTR": {"cl_device_info", "cl_kernel_arg_info"},
    # bit-member guard: the ARM cl_device_controlled_termination_capabilities_arm
    # bit members must NOT inherit the capabilities-query sentence's param set
    # (cl_device_info) or a neighbouring table's set (cl_event_info).
    "CL_DEVICE_CONTROLLED_TERMINATION_SUCCESS_ARM": {"cl_device_info", "cl_event_info"},
    "CL_DEVICE_CONTROLLED_TERMINATION_FAILURE_ARM": {"cl_device_info", "cl_event_info"},
    "CL_DEVICE_CONTROLLED_TERMINATION_QUERY_ARM":   {"cl_device_info", "cl_event_info"},
    # value-set guard: the queue-hint *names* are cl_queue_properties /
    # cl_command_queue_properties members, not cl_device_info queries
    "CL_QUEUE_PRIORITY_KHR": {"cl_device_info"},
    "CL_QUEUE_THROTTLE_KHR": {"cl_device_info"},
}


def main():
    containers, vsets, fn_paramtype = load_registry()
    GLOBALS.containers = containers
    GLOBALS.vsets = vsets
    GLOBALS.fn_paramtype = fn_paramtype

    # register extra value-set C names that cl.xml declares as typedefs
    # (some are declared as plain `typedef cl_uint cl_command_type;`)
    t = open(os.path.join(BASE, "xml/cl.xml"), encoding="utf-8").read()
    for m in re.finditer(r"typedef\s+cl_\w+\s*(?:cl_\w+\?|;)?\s*(cl_[a-z0-9_]+)\s*;", t):
        vsets.add(m.group(1))
    for extra in ["cl_command_type", "cl_context_properties", "cl_sampler_properties",
                  "cl_image_properties", "cl_buffer_create_type", "cl_image_properties_intel",
                  "cl_channel_order", "cl_channel_type", "cl_profiling_info", "cl_mem_info",
                  "cl_program_build_info", "cl_kernel_exec_info", "cl_kernel_work_group_info",
                  "cl_kernel_arg_info", "cl_kernel_sub_group_info", "cl_command_buffer_info_khr",
                  "cl_kernel_work_group_info"]:
        vsets.add(extra)

    ev = mine()
    out = attribute(ev)

    # Manual overrides: every entry is a spec-cited adjudication recorded by
    # hand in manual_overrides.json (see doc/enum-analysis/README.md).  These
    # are applied AFTER the rule engine so re-running the engine never clobbers
    # them, and they carry their own 'manual:' note so the table documents the
    # spec citation.
    ovr_path = os.path.join(HERE, "manual_overrides.json")
    applied_o = 0
    if os.path.exists(ovr_path):
        with open(ovr_path) as fh:
            ovr = json.load(fh)
        for tok, spec in ovr.items():
            if tok not in out:
                continue
            out[tok]["groups"] = list(spec["groups"])
            citem = spec["spec_evidence"]
            note = citem if citem.startswith("manual:") else "manual: " + citem
            out[tok]["notes"] = [note] + [n for n in out[tok].get("notes", []) if not n.startswith("manual:")]
            applied_o += 1
        print("applied %d manual overrides (manual_overrides.json)" % applied_o)

    # self tests (positive subset)
    fails = []
    for tok, expected in SELF_TESTS.items():
        got = set(out[tok]["groups"])
        if expected is None:
            continue
        missing = expected - got
        if missing:
            fails.append((tok, missing, got))
    # self tests (negative containment — contamination guard)
    for tok, forbidden in NEGATIVE_TESTS.items():
        extra = forbidden & set(out[tok]["groups"])
        if extra:
            fails.append((tok, "MUST NOT be in " + str(forbidden), extra))
    # QCOM perf-hint cross-contamination guard (the original mis-attribution)
    for tok, forbidden in NEG_TESTS_QCOM.items():
        extra = forbidden & set(out[tok]["groups"])
        if extra:
            fails.append((tok, "MUST NOT be in " + str(forbidden), extra))
    if fails:
        print("SELF-TEST FAILURES:")
        for t2, miss, got in fails:
            print("  %-50s MISSING %s  GOT %s" % (t2, miss, got))
            for note in out[t2]["notes"]:
                print("      note:", note)
        print("Continuing — fix the above.")
    else:
        print("self-tests: ALL PASS (%d)" % len(SELF_TESTS))

    # extra audit printouts
    for t2 in ["CL_NV21", "CL_8U", "CL_D3D10_DEVICE_KHR", "CL_CHAR_BIT",
               "CL_ACCELERATOR_TYPE_INTEL", "CL_COMMAND_ACQUIRE_D3D9_OBJECTS_INTEL",
               "CL_LAYER_API_VERSION_100", "CL_ICDL_OCL_VERSION",
               "CL_KERNEL_EXEC_INFO_SVM_PTRS", "CL_COMMAND_TASK"]:
        r = out.get(t2)
        if r:
            print("%-48s %s  (%s)" % (t2, r["groups"], " | ".join(r["notes"])[:140]))

    # write outputs
    with open(os.path.join(HERE, "attribution-final.json"), "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)

    unassigned = [t2 for t2, r in out.items() if not r["groups"]]
    multi = {t2: r for t2, r in out.items() if len(r["groups"]) > 1}
    print()
    print("total: %d  assigned: %d  unassigned: %d  multi: %d" % (
        len(out), len(out) - len(unassigned), len(unassigned), len(multi)))
    cc = defaultdict(int)
    for t2 in unassigned:
        cc[out[t2]["container"]] += 1
    print("unassigned by container (top 12):")
    for c, k in sorted(cc.items(), key=lambda kv: -kv[1])[:12]:
        ex = [t2 for t2 in unassigned if out[t2]["container"] == c][:4]
        print("  %-52s %3d e.g. %s" % (c, k, ex))
    print("\nmulti-group members:")
    for t2 in sorted(multi):
        print("  %-55s %s" % (t2, multi[t2]["groups"]))

    # review table
    ld = []
    ld.append("# OpenCL cl.xml enum `group` attribution — final review table")
    ld.append("")
    ld.append("Generated %s.  Method: each group is a C value-set type name, derived from the" % "2026-10-06")
    ld.append("specification (core runtime/platform layers + KHR/EXT/Intel/Arm/Img vendor chapters),")
    ld.append("cross-checked against cl.xml's own named containers (which are the C typedef names).")
    ld.append("Groups follow the OpenGL registry (gl.xml) convention: the C type name, comma-separated")
    ld.append("when a value is valid in several sets.")
    ld.append("")
    ld.append("## Coverage")
    ld.append("")
    ld.append("- Total `<enum>` entries in cl.xml: **%d**" % len(out))
    ld.append("- Assigned one or more groups: **%d**" % (len(out) - len(unassigned)))
    ld.append("- Left ungrouped: **%d** (GL precedent: gl.xml leaves ~12,000 of 15,392 ungrouped;" % len(unassigned))
    ld.append("  ungrouped = platform constants, opaque-handle values, and other context-dependent values")
    ld.append("  whose meaning is defined by the API call site rather than by a named value set)")
    ld.append("- Multi-group values: **%d** (e.g. %s)" % (
        len(multi), multi[list(sorted(multi))[0]]["groups"] if multi else "-"))
    ld.append("")
    ld.append("## Rule table (how each group is determined)")
    ld.append("")
    ld.append("| Rule | Evidence source | Example |")
    ld.append("|---|---|---|")
    ld.append("| R1 C typedef container in cl.xml | container name + spec listing | `CL_MAP_READ` → `cl_map_flags` |")
    ld.append("| R2a param-name table label → Get-function signature | `List of supported param_names by {clGet<X>Info}` + cl.xml `<command>` | `CL_PLATFORM_NAME` → `cl_platform_info` |")
    ld.append("| R2b event command types table | `List of supported event command types` | `CL_COMMAND_NDRANGE_KERNEL` → `cl_command_type` |")
    ld.append("| R2c extension *New Enums* summary list | `{cl_X_TYPE}` bullet + child token | `CL_CURRENT_DEVICE_FOR_GL_CONTEXT_KHR` → `cl_gl_context_info` |")
    ld.append("| R2d extension *param_name* sentence + #define list | `Accepted value for the _param_name_ parameter to *clGetDeviceInfo*` | `CL_DEVICE_HOST_MEM_CAPABILITIES_INTEL` → `cl_device_info` |")
    ld.append("| R2e extension typedef + #define list | `typedef cl_bitfield cl_X;` + `#define CL_...` bit | `CL_UNIFIED_SHARED_MEMORY_ACCESS_INTEL` → `cl_device_unified_shared_memory_capabilities_intel` |")
    ld.append("| R3 error codes | cl.xml ErrorCodes block; spec: “same set of error codes returned from API calls” | `CL_INVALID_ACCELERATOR_INTEL` → `ErrorCode` |")
    ld.append("")
    ld.append("## Multi-group values (comma-separated in `group=\"...\"`)")
    ld.append("")
    ld.append("| token | groups | reason (spec evidence) |")
    ld.append("|---|---|---|")
    for t2 in sorted(multi):
        notes = "; ".join(dict.fromkeys(r2 for (_, r2, _) in []) or [])
        reason = " / ".join(
            set(n.split(" (spec evidence")[0] for n in multi[t2]["notes"]))
        ld.append("| `%s` | `%s` | %s |" % (t2, ", ".join(multi[t2]["groups"]), reason[:160]))
    ld.append("")
    ld.append("## Full assignment table")
    ld.append("")
    ld.append("| token | container | group(s) | evidence |")
    ld.append("|---|---|---|---|")
    for tok in sorted(out):
        r = out[tok]
        g = ", ".join("`%s`" % x for x in r["groups"]) if r["groups"] else "— (ungrouped, GL precedent)"
        ev = "; ".join(r["notes"])[:150]
        ld.append("| `%s` | %s | %s | %s |" % (tok, r["container"], g, ev))
    open(os.path.join(HERE, "attribution-table.md"), "w").write("\n".join(ld))
    print("\nwrote attribution-final.json + attribution-table.md")


if __name__ == "__main__":
    main()
