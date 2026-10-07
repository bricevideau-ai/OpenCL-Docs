# Enum `group` attribution for cl.xml

Goal: add a `group` attribute to every `<enum>` entry in `xml/cl.xml` where one
is safely determinable, mirroring the OpenGL registry convention
(`OpenGL-Registry/xml/gl.xml`, where each enum carries `group="C Type Name"` and
multi-membership is comma-separated, e.g. `GL_DEPTH_BUFFER_BIT` →
`group="ClearBufferMask,AttribMask"`).

## Files in this directory

| File | What it is | Status |
|---|---|---|
| `attribute_final.py` | Attribution engine: per-token spec evidence, self-tests, writes the JSON/MD outputs | active |
| `apply_groups.py` | Surgical applier: inserts ` group="A,B"` after `name="..."` on **definition** `<enum>` lines only (those carrying `value=`/`bitpos=`); require-reference lines untouched. Idempotent, self-verifying | active |
| `attribution-final.json` | Per-token result: container, value, groups, evidence trail | generated |
| `attribution-table.md` | Human review table (coverage, rules, multi-membership, full table) | generated |
| `attribute_v2.py`, `attribute_v3.py` | Earlier iterations kept as the audit trail of how the rules evolved | superseded |
| `value_lists.py`, `value-lists.json`, `enum-contexts.json`, `extract_contexts.py`, `attribute.py` | First-generation spec mining (grid-table parser) — kept for reference | superseded |

## Ground-truth references used

- `xml/cl.xml`            — registry: 1,334 enum entries; 149 containers
- `xml/registry.rnc`      — RNC schema (needs the `group` attribute added)
- `OpenGL-Registry/xml/gl.xml` + `xml/registry.rnc` — the convention being mirrored
  (verified: groups are C type names; multi-membership comma-separated;
  error codes → `ErrorCode`; and gl.xml itself leaves 12,153 of 15,392 enums
  ungrouped → "ungrouped" is the norm, not a defect)
- `api/opencl_runtime_layer.asciidoc`, `api/opencl_platform_layer.asciidoc`
- `api/cl_khr_*.asciidoc` (75 chapters), `api/cl_ext_*.asciidoc` (11 chapters)
- `extensions/*.asciidoc` (53 vendor chapters: Intel / Arm / Img / AMD / QCOM)

## Rule set (v4)

- **R1** Named container whose name is a C type in cl.xml (`cl_mem_flags`,
  `cl_device_type`, `clCommandExecutionStatus`, ...) → `group = container name`
  (these containers *are* the C value sets; gl.xml groups are the same thing).
- **R2** The 334-token mega-container `cl_device_info` (cl.xml packs *all*
  param-name queries in it): `group = the C type the spec documents the token
  under`, resolved per evidence:
  - R2a `List of supported param_names by {clGet<X>Info}` table label → the
        `param_name` C type declared on that function's signature in cl.xml
  - R2b `List of supported event command types` table → `cl_command_type`
  - R2c extension *New Enums* summary lists: token listed under a
        `{cl_X_TYPE}` bullet → `cl_X`
  - R2d extension sentence `Accepted value for the _param_name_ parameter to
        *clGetDeviceInfo*` + following `#define` list → `cl_device_info`
  - R2e `typedef cl_bitfield cl_X;` + following `#define` bit list → `cl_X`
- **R3** cl.xml `ErrorCodes.*` containers → `group="ErrorCode"` (direct GL
  precedent: `GL_NO_ERROR` → `group=...ErrorCode`; cl.xml itself notes the
  values are "the same set of error codes returned from the API calls").
- **Ungrouped** by design (GL precedent): platform constants (`CL_CHAR_BIT`),
  vendor reserved-range tokens without a spec chapter in this repo,
  opaque-handle values, and other context-dependent values. Every unassigned
  token is listed with its container in the review table so each can be
  adjudicated.

Only evidence that names a C type (a value-set token row, a typedef, or a
Get-function's declared `param_name` parameter) is accepted — description
cells and prose are *not* used to assign, which is what killed the earlier
attempts (cross-contamination like `CL_FALSE` landing in 10 sets).

## Self-tests

`attribute_final.py`'s self-tests assert a positive set (token → expected group, subset check)
including the hard ones — `CL_COMMAND_NDRANGE_KERNEL` → `cl_command_type`,
`CL_EVENT_REFERENCE_COUNT` → `cl_event_info`, `CL_DEVICE_TYPE` →
`cl_device_info` (it is a query key, *not* the `cl_device_type` value set),
`CL_CONTEXT_PLATFORM` → `cl_context_properties` — plus negative assertions to
catch regressions (`CL_TRUE ⊆ {cl_bool}`, ...). Failures abort before any
write.

## Verification (run on the landed state)

- `git diff` shows only the intended insertion: one ` group="..."` attribute per
  assigned definition line, no other byte changed.
- All 27 self-tests pass.
- Schema: `rnc2rng xml/registry.rnc` + `lxml RelaxNG` — cl.xml **valid** against
  the extended `registry.rnc` (`attribute group { text } ?` added to `Enum`).
- Registry loader: `scripts/reg.py -registry cl.xml -validate` — exit 0.
- Header generation: `scripts/gencl.py -registry cl.xml cl.h` produces a
  **byte-identical** `cl.h` versus unmodified main (the attribute is
  generator-invisible, as in OpenGL).
- Scope: only definition `<enum>` lines (those with `value=`/`bitpos=`) receive
  the attribute; the 1,313 bare `<enum name="X"/>` require-reference lines are
  untouched — matching gl.xml, where groups live on definitions.
- `make -C xml validate` (CI entrypoint) runs `jing -c registry.rnc cl.xml`;
  the jing binary is not present in this environment, so the equivalent
  rnc2rng + RelaxNG validation above is the local stand-in.
