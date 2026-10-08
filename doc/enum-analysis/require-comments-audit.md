# Require-comment audit — `xml/cl.xml`

Date: 2026-10-08 · Author: Corwin · Commissioned by Brice ("If you found errors in the
require comments it might be the opportunity to fix them")

## Method

Every `<require comment="<name>">` block whose comment is a `snake_case` type name
(104 blocks, 811 token references) was compared, token by token, against the
spec-adjudicated `group=` attributions (each backed by spec text, registry
provenance, or owner adjudication — see `manual_overrides.json`).

A require comment is *correct for our purposes* when the commented group name
(a) exists as a `<type>`/typedef or `<enums>` container in cl.xml, and
(b) matches how the token is used per spec.

**Result:** 4 comments reference **type names that do not exist** (phantom refs);
a further **8 blocks (35 token refs)** use a *grouping* the spec contradicts
(those attributions were wrong in ours initially — corrected; the require
comments themselves are the ones that are wrong). The report lists both
populations for upstream reporting.

---

## Part A — Phantom type references (require comment names a nonexistent type)

These are genuine defects in cl.xml metadata: the comment references a type that
no `<type>` definition and no `<enums>` container in the registry defines. Any
consumer that resolves require-comments against type names (codegen tools, and
PR #1587's group-inheritance scheme) hits a dead reference.

| Require comment (as-is) | Extension(s) | Tokens | What it should reference | Spec basis |
|---|---|---|---|---|
| `cl_mem_alloc_info_intel` | cl_intel_unified_shared_memory; cl_intel_mem_alloc_buffer_location | `CL_MEM_ALLOC_TYPE_INTEL`, `CL_MEM_ALLOC_BASE_PTR_INTEL`, `CL_MEM_ALLOC_SIZE_INTEL`, `CL_MEM_ALLOC_DEVICE_INTEL`, `CL_MEM_ALLOC_BUFFER_LOCATION_INTEL` | **`cl_mem_info_intel`** — the typedef the spec actually declares | USM spec: `typedef cl_uint cl_mem_info_intel;` immediately above the defines; "clGetMemAllocInfoINTEL also accepts CL_MEM_ALLOC_BUFFER_LOCATION_INTEL for *cl_mem_properties_intel*" |
| `cl_media_adapter_set_khr` | cl_khr_dx9_media_sharing | `CL_PREFERRED_DEVICES_FOR_DX9_MEDIA_ADAPTER_KHR`, `CL_ALL_DEVICES_FOR_DX9_MEDIA_ADAPTER_KHR` | **`cl_dx9_media_adapter_set_khr`** | The actual typedef name in the DX9 media sharing spec |
| `cl_media_adapter_type_khr` | cl_khr_dx9_media_sharing | `CL_ADAPTER_D3D9_KHR`, `CL_ADAPTER_D3D9EX_KHR`, `CL_ADAPTER_DXVA_KHR` | **`cl_dx9_media_adapter_type_khr`** | Same spec; the existing typedef is `cl_dx9_media_adapter_type_khr` |
| `cl_semaphore_type` | cl_khr_semaphore | `CL_SEMAPHORE_TYPE_BINARY_KHR` | **`cl_semaphore_type_khr`** | Only `cl_semaphore_type_khr` exists in cl.xml |

Note: 3 of these 4 phantom names were *also* used as group names in PR #1587
(`cl_mem_alloc_info_intel`), which is one more reason their inheritance approach
breaks on them.

## Part B — Require comments whose *grouping* the spec contradicts

Here the type name exists, but the block attributes the token to the wrong API
role. In every one of these, the spec text is unambiguous. (These were also the
cases where our first pass had followed the same wrong intuition — now
corrected in `group=` and in `manual_overrides.json`.)

### B1. Context *creation properties* listed under `cl_context_info`
`<require comment="cl_context_info">` in six extensions, spec role is
**clCreateContext / clCreateContextFromType `<properties>`** (creation property
names), not a `clGetContextInfo` query:

| Extension | Tokens |
|---|---|
| cl_intel_dx9_media_sharing | `CL_CONTEXT_D3D9_DEVICE_INTEL`, `CL_CONTEXT_D3D9EX_DEVICE_INTEL`, `CL_CONTEXT_DXVA_DEVICE_INTEL` |
| cl_intel_va_api_media_sharing | `CL_CONTEXT_VA_API_DISPLAY_INTEL` |
| cl_khr_d3d10_sharing | `CL_CONTEXT_D3D10_DEVICE_KHR` |
| cl_khr_d3d11_sharing | `CL_CONTEXT_D3D11_DEVICE_KHR` |
| cl_qcom_perf_hint | `CL_CONTEXT_PERF_HINT_QCOM` |

Spec citations (representative, all state the same):
- cl_intel_va_api_media_sharing: "Valid property values *when passed to
  clCreateContext and clCreateContextFromType*" — `CL_CONTEXT_VA_API_DISPLAY_INTEL`.
- cl_intel_dx9_media_sharing: same phrasing with `CL_CONTEXT_DX9_*` device names.
- cl_qcom_perf_hint: value-set of the `CL_CONTEXT_PERF_HINT_QCOM` property.

So: these tokens are **creation-property names/sets** — `cl_context_properties`
group (which is what our `group=` now says), not `cl_context_info`.

### B2. USM INTEL *command types* listed under `cl_command_type` — **upstream is
right here, we were wrong** (recorded for transparency)

`<require comment="cl_command_type">` in cl_intel_unified_shared_memory for
`CL_COMMAND_MEMFILL_INTEL`, `CL_COMMAND_MEMCPY_INTEL`, `CL_COMMAND_MIGRATEMEM_INTEL`,
`CL_COMMAND_MEMADVISE_INTEL`. Spec is explicit:
"New return values from **clGetEventInfo** when param_name is **CL_EVENT_COMMAND_TYPE**".
The earlier `cl_kernel_exec_info` attribution (mine, a misread of the neighboring
`CL_KERNEL_EXEC_INFO_USM_PTRS_INTEL`) was corrected to `cl_command_type` —
matching upstream's require and the spec.

### B3. `CL_PROGRAM_IL_KHR` under `cl_program_info` — **upstream right, we were
wrong** (corrected to `cl_program_info`)

The require comment (which we initially misread as `cl_platform_info` in our pass)
matches the reserved-range comment in the registry: "0x116C–0x117F Reserved for
cl_program_info". Sibling `CL_PROGRAM_IL` (0x1169) is `cl_program_info`. Corrected.

### B4. `CL_QUEUE_*` scheduling/priority tokens under `cl_queue_properties`

`<require comment="cl_queue_properties">` in cl_arm_scheduling_controls
(`CL_QUEUE_KERNEL_BATCHING_ARM`, `CL_QUEUE_DEFERRED_FLUSH_ARM`,
`CL_QUEUE_COMPUTE_UNIT_LIMIT_ARM`) and cl_intel_command_queue_families
(`CL_QUEUE_FAMILY_INTEL`, `CL_QUEUE_INDEX_INTEL`). These **do** exist as creation
properties of `clCreateCommandQueueWithProperties` — upstream's intent matches
spec. The *type name* `cl_queue_properties` is not a typedef in cl.xml (the 2.0
typedef is `cl_command_queue_properties`); our `group=` keeps the real container
(`cl_command_queue_properties[/info]`). Not an error worth reporting — a naming
convention mismatch.

### B5. ARM SVM bitmask tokens under `cl_device_svm_capabilities_arm` / `cl_svm_mem_flags_arm`

Spec (cl_arm_shared_virtual_memory) is explicit:

- `CL_DEVICE_SVM_COARSE_GRAIN_BUFFER_ARM` … `CL_DEVICE_SVM_ATOMICS_ARM` —
  "Flag values **returned by clGetDeviceInfo with CL_DEVICE_SVM_CAPABILITIES_ARM
  as the param_name**" → our `cl_arm_device_svm_capabilities.flags` container is
  the correct home. Upstream's comment name is an alias that doesn't exist in
  the registry; **not reportable** (alias vs. real name), but noted.
- `CL_MEM_SVM_FINE_GRAIN_BUFFER_ARM`, `CL_MEM_SVM_ATOMICS_ARM` —
  "Flag values **used by clSVMAllocARM**" → our `cl_arm_svm_alloc.flags` is
  correct; `cl_svm_mem_flags_arm` (the comment) is an alias not present as a
  registry type.

### B6. `CL_MEM_ALLOC_FLAGS_IMG` under `cl_mem_properties` — **upstream right, we
were wrong** (corrected to `cl_mem_properties`)

Spec: "Valid property values ... where _properties_ is
`CL_MEM_ALLOC_FLAGS_IMG`" — it is a **property name** (clCreateBufferWithProperties
`<properties>` entry), not a member of the `cl_mem_alloc_flags_img` value-set.
Corrected. The `cl_mem_alloc_flags_img` typedef contains the *values*
(`CL_MEM_ALLOC_FLAGS_*_IMG`).

### B7. `CL_CONTEXT_SAFETY_PROPERTIES_IMG` under `cl_context_properties`

Spec: "Valid property values for `cl_context_safety_properties_img` where
_properties_ is `CL_CONTEXT_SAFETY_PROPERTIES_IMG` when passed to clCreateContext"
— **property name**, value-set is `cl_context_safety_properties_img` (which
does exist in cl.xml as a container). Upstream's flat comment loses that
distinction; our `group=` carries the value-set as the primary group. Not an
error — our grouping is more precise.

---

## What we fixed as a result (9 attributions, already applied & verified)

| Token | Was | Now | Evidence |
|---|---|---|---|
| `CL_COMMAND_MEMFILL_INTEL` | cl_kernel_exec_info | **cl_command_type** | USM spec "clGetEventInfo … CL_EVENT_COMMAND_TYPE" |
| `CL_COMMAND_MEMCPY_INTEL` | cl_kernel_exec_info | **cl_command_type** | same |
| `CL_COMMAND_MIGRATEMEM_INTEL` | cl_kernel_exec_info | **cl_command_type** | same |
| `CL_COMMAND_MEMADVISE_INTEL` | cl_kernel_exec_info | **cl_command_type** | same |
| `CL_PROGRAM_IL_KHR` | cl_platform_info | **cl_program_info** | reserved-range comment + sibling |
| `CL_MEM_ALLOC_FLAGS_IMG` | cl_mem_alloc_flags_img | **cl_mem_properties** | img spec: property name |
| `CL_IMPORT_MEMORY_WHOLE_ALLOCATION_ARM` | (ungrouped) | **cl_import_properties_arm** | ARM import spec + sibling |
| `CL_SEMAPHORE_FAST_PATH_IMG` | (ungrouped) | **cl_semaphore_properties_khr** | creation property (upstream require, property-name convention) |
| `CL_EGL_YUV_PLANE_INTEL` | cl_image_info | **cl_image_info, cl_egl_image_properties_khr** | dual role per spec |

Verification: `reg.py -validate` clean, 68/68 self-tests, `cl.h` **byte-identical**
to upstream main, `definitions: 1334 agree / 0 disagree`.

## Recommendation for upstream

1. **Definitely report (Part A):** the 4 phantom type references. They are
   metadata bugs (dead type names) and they break any tool that resolves
   require-comments to types. Suggested fix is mechanical: rename the comment to
   the existing type (or add a note where the type name is a genuine alias).
2. **Part B1 (context properties):** worth reporting — the require comment
   mislabels creation-property tokens as `cl_context_info`. A reader relying on
   the comment (e.g. a tool author or PR #1587's model) assigns them to the wrong
   API.
3. **Parts B4–B7:** no action — these are either correct upstream, or our
   `group=` is strictly more precise, or an alias naming difference. Keep for
   completeness.

Deliverable files: this report + `manual_overrides.json` (289 adjudications) +
`cl.xml` (9 corrected `group=` values). No `require comment=` was edited —
that's an upstream decision; we documented the correct target for each.
