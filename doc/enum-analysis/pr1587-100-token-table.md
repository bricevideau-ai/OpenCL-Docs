# PR #1587 cross-check — the 100 tokens they grouped that we left ungrouped

Generated 2026-10-08. Sources: **KhronosGroup/OpenCL-Registry** spec
chapters (fetched 2026-10-08, `all/` working copy in /tmp/regspec) + this
repo's `extensions/` dirs. Verdicts follow this repo's cl.xml grouping
conventions (creation properties, query keys, cl_command_type members,
value sets).

Legend: ✅ = agree with PR#1587 (spec-verified); ❌ = PR#1587 **wrong**,
correct group given; ⚠ = no spec found in any source — cannot verify.

## ✅ Agree — spec-verified, PR#1587 correct (82)

| token | their group | spec source (chapter + sentence) |
|---|---|---|
| CL_ACCELERATOR_CONTEXT_INTEL | cl_accelerator_info_intel | intel/cl_intel_accelerator.txt — "Accepted as the \<param_name\> parameter of clGetAcceleratorInfoINTEL" |
| CL_ACCELERATOR_DESCRIPTOR_INTEL | cl_accelerator_info_intel | same |
| CL_ACCELERATOR_REFERENCE_COUNT_INTEL | cl_accelerator_info_intel | same |
| CL_ACCELERATOR_TYPE_INTEL | cl_accelerator_info_intel | same |
| CL_ALL_DEVICES_FOR_DX9_INTEL | cl_dx9_device_set_intel | intel/cl_intel_dx9_media_sharing.txt — parameter of clGetDeviceIDsFromDX9INTEL |
| CL_ALL_DEVICES_FOR_VA_API_INTEL | cl_va_api_device_set_intel | intel/cl_intel_va_api_media_sharing.txt — parameter of clGetDeviceIDsFromVA_APIMediaAdapterINTEL |
| CL_COMMAND_ACQUIRE_VA_API_MEDIA_SURFACES_INTEL | cl_command_type | intel/cl_intel_va_api_media_sharing.txt — "Returned in the param_value of clGetEventInfo when param_name is CL_EVENT_COMMAND_TYPE" |
| CL_COMMAND_MIGRATE_MEM_OBJECT_EXT | cl_command_type | ext/cl_ext_migrate_memobject.txt — returned by clGetEventInfo under CL_EVENT_COMMAND_TYPE |
| CL_COMMAND_RELEASE_VA_API_MEDIA_SURFACES_INTEL | cl_command_type | intel/cl_intel_va_api_media_sharing.txt — same |
| CL_COMMAND_SVM_FREE_ARM | cl_command_type | arm/cl_arm_shared_virtual_memory.txt — "To be used by clGetEventInfo" (command) |
| CL_COMMAND_SVM_MAP_ARM | cl_command_type | same |
| CL_COMMAND_SVM_MEMCPY_ARM | cl_command_type | same |
| CL_COMMAND_SVM_MEMFILL_ARM | cl_command_type | same |
| CL_COMMAND_SVM_UNMAP_ARM | cl_command_type | same |
| CL_CONTEXT_D3D9EX_DEVICE_INTEL | cl_context_properties | intel/cl_intel_dx9_media_sharing.txt — "Accepted as a property name in the \<properties\> parameter of clCreateContext" |
| CL_CONTEXT_DXVA_DEVICE_INTEL | cl_context_properties | intel/cl_intel_simultaneous_sharing.txt — listed among context-creation properties |
| CL_CONTEXT_SHOW_DIAGNOSTICS_INTEL | cl_context_properties | intel/cl_intel_driver_diagnostics.txt — property of clCreateContext/clCreateContextFromType |
| CL_CONTEXT_VA_API_DISPLAY_INTEL | cl_context_properties | intel/cl_intel_va_api_media_sharing.txt — property of clCreateContext |
| CL_D3D9EX_DEVICE_INTEL | cl_dx9_device_source_intel | intel/cl_intel_dx9_media_sharing.txt — parameter of clGetDeviceIDsFromDX9INTEL |
| CL_D3D9_DEVICE_INTEL | cl_dx9_device_source_intel | intel/cl_intel_dx9_media_sharing.txt — parameter of clGetDeviceIDsFromDX9INTEL |
| CL_DEVICE_AFFINITY_DOMAINS_EXT | cl_device_info | ext/cl_ext_device_fission.txt — "clGetDeviceInfo" |
| CL_DEVICE_AVAILABLE_ASYNC_QUEUES_AMD | cl_device_info | amd/cl_amd_device_attribute_query.txt — "Accepted as the \<param_name\> parameter of clGetDeviceInfo" |
| CL_DEVICE_AVC_ME_SUPPORTS_PREEMPTION_INTEL | cl_device_info | intel/cl_intel_device_side_avc_motion_estimation.txt — "Accepted as arguments to clGetDeviceInfo" |
| CL_DEVICE_AVC_ME_SUPPORTS_TEXTURE_SAMPLER_USE_INTEL | cl_device_info | same |
| CL_DEVICE_AVC_ME_VERSION_INTEL | cl_device_info | same |
| CL_DEVICE_BOARD_NAME_AMD | cl_device_info | amd/cl_amd_device_attribute_query.txt |
| CL_DEVICE_COMPUTE_CAPABILITY_MAJOR_NV | cl_device_info | nv/cl_nv_device_attribute_query.txt — "extends table 4.3 ... Returns the major revision number that defines the CUDA compute capability" |
| CL_DEVICE_COMPUTE_CAPABILITY_MINOR_NV | cl_device_info | same |
| CL_DEVICE_COMPUTE_UNITS_BITFIELD_ARM | cl_device_info | arm/cl_arm_core_id.txt — "Device Info query" |
| CL_DEVICE_EXT_MEM_PADDING_IN_BYTES_QCOM | cl_device_info | qcom/cl_qcom_ext_host_ptr.txt — "Accepted by the \<param_name\> argument of clGetDeviceInfo" |
| CL_DEVICE_GFXIP_MAJOR_AMD | cl_device_info | amd/cl_amd_device_attribute_query.txt |
| CL_DEVICE_GFXIP_MINOR_AMD | cl_device_info | same |
| CL_DEVICE_GLOBAL_FREE_MEMORY_AMD | cl_device_info | same |
| CL_DEVICE_GLOBAL_MEM_CHANNELS_AMD | cl_device_info | same |
| CL_DEVICE_GLOBAL_MEM_CHANNEL_BANKS_AMD | cl_device_info | same |
| CL_DEVICE_GLOBAL_MEM_CHANNEL_BANK_WIDTH_AMD | cl_device_info | same |
| CL_DEVICE_GPU_OVERLAP_NV | cl_device_info | nv/cl_nv_device_attribute_query.txt — "Returns CL_TRUE if the device can concurrently copy memory" |
| CL_DEVICE_INTEGRATED_MEMORY_NV | cl_device_info | same |
| CL_DEVICE_JOB_SLOTS_ARM | cl_device_info | arm/cl_arm_job_slot_selection.txt — "Device Info query" |
| CL_DEVICE_KERNEL_EXEC_TIMEOUT_NV | cl_device_info | nv/cl_nv_device_attribute_query.txt |
| CL_DEVICE_LOCAL_MEM_BANKS_AMD | cl_device_info | amd/cl_amd_device_attribute_query.txt |
| CL_DEVICE_LOCAL_MEM_SIZE_PER_COMPUTE_UNIT_AMD | cl_device_info | same |
| CL_DEVICE_MAX_WORK_GROUP_SIZE_AMD | cl_device_info | same |
| CL_DEVICE_ME_VERSION_INTEL | cl_device_info | intel/cl_intel_advanced_motion_estimation.txt — "Accepted as arguments to clGetDeviceInfo" |
| CL_DEVICE_NUM_SIMULTANEOUS_INTEROPS_INTEL | cl_device_info | intel/cl_intel_simultaneous_sharing.txt — "of clGetDeviceInfo" |
| CL_DEVICE_PAGE_SIZE_QCOM | cl_device_info | qcom/cl_qcom_ext_host_ptr.txt — "Accepted by the \<param_name\> argument of clGetDeviceInfo" |
| CL_DEVICE_PARENT_DEVICE_EXT | cl_device_info | ext/cl_ext_device_fission.txt |
| CL_DEVICE_PARTITION_STYLE_EXT | cl_device_info | ext/cl_ext_device_fission.txt |
| CL_DEVICE_PARTITION_TYPES_EXT | cl_device_info | ext/cl_ext_device_fission.txt |
| CL_DEVICE_PCIE_ID_AMD | cl_device_info | amd/cl_amd_device_attribute_query.txt |
| CL_DEVICE_PREFERRED_CONSTANT_BUFFER_SIZE_AMD | cl_device_info | same |
| CL_DEVICE_PREFERRED_WORK_GROUP_SIZE_AMD | cl_device_info | same |
| CL_DEVICE_PROFILING_TIMER_OFFSET_AMD | cl_device_info | same |
| CL_DEVICE_REFERENCE_COUNT_EXT | cl_device_info | ext/cl_ext_device_fission.txt |
| CL_DEVICE_REGISTERS_PER_BLOCK_NV | cl_device_info | nv/cl_nv_device_attribute_query.txt — "Maximum number of 32-bit registers available to a thread" |
| CL_DEVICE_SIMD_INSTRUCTION_WIDTH_AMD | cl_device_info | amd/cl_amd_device_attribute_query.txt |
| CL_DEVICE_SIMD_PER_COMPUTE_UNIT_AMD | cl_device_info | same |
| CL_DEVICE_SIMD_WIDTH_AMD | cl_device_info | same |
| CL_DEVICE_SIMULTANEOUS_INTEROPS_INTEL | cl_device_info | intel/cl_intel_simultaneous_sharing.txt |
| CL_DEVICE_SVM_CAPABILITIES_ARM | cl_device_info | arm/cl_arm_shared_virtual_memory.txt — "Flag values returned by clGetDeviceInfo" |
| CL_DEVICE_THREAD_TRACE_SUPPORTED_AMD | cl_device_info | amd/cl_amd_device_attribute_query.txt |
| CL_DEVICE_TOPOLOGY_AMD | cl_device_info | same |
| CL_DEVICE_WARP_SIZE_NV | cl_device_info | nv/cl_nv_device_attribute_query.txt |
| CL_DEVICE_WAVEFRONT_WIDTH_AMD | cl_device_info | amd/cl_amd_device_attribute_query.txt |
| CL_DXVA_DEVICE_INTEL | cl_dx9_device_source_intel | intel/cl_intel_dx9_media_sharing.txt — parameter of clGetDeviceIDsFromDX9INTEL |
| CL_EGL_YUV_PLANE_INTEL | cl_image_info | intel/cl_intel_egl_image_yuv.txt — "as \<param_name\> parameter of function clGetImageInfo" |
| CL_IMAGE_DX9_PLANE_INTEL | cl_image_info | intel/cl_intel_dx9_media_sharing.txt — "parameter of clGetImageInfo" |
| CL_IMAGE_ROW_ALIGNMENT_QCOM | cl_image_pitch_info_qcom | qcom/cl_qcom_ext_host_ptr.txt — "Accepted by the \<param_name\> argument of clGetDeviceImageInfoQCOM" |
| CL_IMAGE_SLICE_ALIGNMENT_QCOM | cl_image_pitch_info_qcom | same |
| CL_IMAGE_VA_API_PLANE_INTEL | cl_image_info | intel/cl_intel_va_api_media_sharing.txt — "parameter of clGetImageInfo" |
| CL_IMPORT_ANDROID_HARDWARE_BUFFER_LAYER_INDEX_ARM | cl_import_properties_arm | arm/cl_arm_import_memory.txt — "Valid \<properties\> are:" list |
| CL_IMPORT_ANDROID_HARDWARE_BUFFER_PLANE_INDEX_ARM | cl_import_properties_arm | same |
| CL_IMPORT_DMA_BUF_DATA_CONSISTENCY_WITH_HOST_ARM | cl_import_properties_arm | same |
| CL_IMPORT_TYPE_ARM | cl_import_properties_arm | same |
| CL_IMPORT_TYPE_ANDROID_HARDWARE_BUFFER_ARM | cl_import_properties_arm | arm/cl_arm_import_memory.txt L120-122 — listed among "Valid values for CL_IMPORT_TYPE_ARM", the same property family as the other five |
| CL_IMPORT_TYPE_PROTECTED_ARM | cl_import_properties_arm | same |
| CL_KERNEL_EXEC_INFO_SVM_FINE_GRAIN_SYSTEM_ARM | cl_kernel_exec_info_arm | arm/cl_arm_shared_virtual_memory.txt — "The **cl_kernel_exec_info_arm** type uses the new tokens CL_KERNEL_EXEC_INFO_SVM_PTRS_ARM and CL_KERNEL_EXEC_INFO_SVM_FINE_GRAIN_SYSTEM_ARM" |
| CL_KERNEL_EXEC_INFO_SVM_PTRS_ARM | cl_kernel_exec_info_arm | same |
| CL_MEM_DX9_RESOURCE_INTEL | cl_mem_info | intel/cl_intel_dx9_media_sharing.txt — "parameter of clGetMemObjectInfo" |
| CL_MEM_DX9_SHARED_HANDLE_INTEL | cl_mem_info | same |
| CL_MEM_VA_API_MEDIA_SURFACE_INTEL | cl_mem_info | intel/cl_intel_va_api_media_sharing.txt — "parameter of clGetMemObjectInfo" |
| CL_PREFERRED_DEVICES_FOR_DX9_INTEL | cl_dx9_device_set_intel | intel/cl_intel_dx9_media_sharing.txt |
| CL_PREFERRED_DEVICES_FOR_VA_API_INTEL | cl_va_api_device_set_intel | intel/cl_intel_va_api_media_sharing.txt |
| CL_QUEUE_JOB_SLOT_ARM | cl_queue_properties | arm/cl_arm_job_slot_selection.txt — "Command queue property" |
| CL_VA_API_DISPLAY_INTEL | cl_va_api_device_source_intel | intel/cl_intel_va_api_media_sharing.txt — parameter of clGetDeviceIDsFromVA_APIMediaAdapterINTEL |

## ❌ Disagree — PR#1587 attribution is WRONG / invalid (4)

| token | their group (✗) | correct per this repo's conventions | spec evidence |
|---|---|---|---|
| CL_CONTEXT_D3D9_DEVICE_INTEL | cl_context_info | **cl_context_properties** | intel/cl_intel_dx9_media_sharing.txt L98-99: "Accepted as a **property name** in the \<properties\> parameter of clCreateContext" (their sibling CL_CONTEXT_D3D9EX_DEVICE_INTEL in cl_context_properties is correct — the pair is split inconsistently) |
| CL_MEM_USES_SVM_POINTER_ARM | cl_device_info | **cl_mem_info** | arm/cl_arm_shared_virtual_memory.txt L178: "The **clGetMemObjectInfo** will accept a param_name of CL_MEM_USES_SVM_POINTER_ARM" — a mem-object query key, not a device query |
| CL_IMPORT_TYPE_HOST_ARM | cl_import_type_arm | **cl_import_properties_arm** | group name resolves to **no typedef** in the registry (checked `cl.xml`); arm/cl_arm_import_memory.txt L118-122: "Valid values for CL_IMPORT_TYPE_ARM are: …" i.e. property-family values, same list type as the other CL_IMPORT_* tokens |
| CL_IMPORT_TYPE_DMA_BUF_ARM | cl_import_type_arm | **cl_import_properties_arm** | same evidence as above |

(Correction to my first draft: CL_IMPORT_TYPE_ANDROID_HARDWARE_BUFFER_ARM in
`cl_import_properties_arm` is the *consistent* choice — it is also a value of
CL_IMPORT_TYPE_ARM — so it stays in the agree bucket. The HOST/DMA_BUF pair
only differ because their group name is a nonexistent type.)

## ⚠ No spec anywhere (11) — ungrouped is the *only* defensible position

No chapter in KhronosGroup/OpenCL-Registry (99 chapters downloaded) and no
chapter in this repo's extensions/ defines these tokens:

CL_COMMAND_ACQUIRE_D3D9_OBJECTS_INTEL, CL_COMMAND_RELEASE_D3D9_OBJECTS_INTEL
(Note: the 2011 cl_intel_dx9_media_sharing spec uses the names
CL_COMMAND_ACQUIRE_/RELEASE_DX9_OBJECTS_INTEL 0x402A/0x402B — the D3D9-named
variants exist only in cl.xml itself.)
CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_ARBITRATION_ALGORITHM_IMG
CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_EXECUTE_COUNT_IMG
CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_SCHEDULING_ALGORITHM_IMG
CL_DEVICE_SCHEDULING_CONTROLS_CAPABILITIES_IMG
CL_DEVICE_MAX_HOST_READ_PIPES_INTEL
CL_DEVICE_MAX_HOST_WRITE_PIPES_INTEL
CL_KERNEL_ARG_HOST_ACCESSIBLE_PIPE_INTEL
CL_MEM_DEVICE_ID_INTEL
CL_MEM_LOCALLY_UNCACHED_RESOURCE_INTEL

(cl.xml's require-block `comment=` field on some of these *does* carry intended
group names — see the provenance section below.)

## Provenance via git blame (2026-10-08) — resolving the 11

Traced each to its introducing commit in full history (repo unshallowed, 921 commits):

**6 of 11 carry the registry's own `<require comment=...>` group, authored by the extension authors themselves — registry-level provenance, matched by PR#1587, now applied (labeled *registry-provenance*, a distinct tier below spec-cited):**

| token | origin | author-stated group (cl.xml require block) |
|---|---|---|
| CL_DEVICE_SCHEDULING_CONTROLS_CAPABILITIES_IMG | paulfradgley, #1469 "Add cl_img_scheduling_controls to cl.xml", 2025-10-21 | `cl_device_info` |
| CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_SCHEDULING_ALGORITHM_IMG | same #1469 | `cl_queue_properties` |
| CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_ARBITRATION_ALGORITHM_IMG | same #1469 | `cl_queue_properties` |
| CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_EXECUTE_COUNT_IMG | same #1469 | `cl_queue_properties` |
| CL_MEM_DEVICE_ID_INTEL | Mike Kinsner (Intel), #858 "Allocate enums for upcoming Intel memory property extension", 2022-11-08 | `cl_mem_properties` — commit message: *"Add comment indicating which type the enums apply to"* |
| CL_MEM_LOCALLY_UNCACHED_RESOURCE_INTEL | same #858 | `cl_mem_properties` |

(The IMG algorithm value-set tokens (…_LINEAR_ORDER/_MORTON_ORDER/…) that the same #1469 block puts under `cl_device_scheduling_controls_capabilities_img` were already handled by our engine — the typedef is declared by the author in that commit.)

**5 remain unverifiable — deliberately left ungrouped, PR#1587's groups NOT adopted:**

| token | origin | why unresolvable |
|---|---|---|
| CL_DEVICE_MAX_HOST_READ_PIPES_INTEL / _WRITE_PIPES_INTEL / CL_KERNEL_ARG_HOST_ACCESSIBLE_PIPE_INTEL | Mike Kinsner (Intel), #144 "Allocate ranges/enums for Intel extension", 2019-10-23 | Allocated as bare enum names for an *upcoming* extension that never produced a spec chapter in this repo; the local host-pipe chapter (`cl_intel_program_scope_host_pipe`) defines 0x4214-0x4217, not these (0x4210-0x4212), and has no require block for them |
| CL_COMMAND_ACQUIRE_D3D9_OBJECTS_INTEL / CL_COMMAND_RELEASE_D3D9_OBJECTS_INTEL | Jon Leech, #67 "Extract refpages from C/API spec sources", 2019-04-05 | Naming drift: the 2011 official `cl_intel_dx9_media_sharing` spec defines **CL_COMMAND_ACQUIRE/RELEASE_DX9_OBJECTS_INTEL** at 0x402A/0x402B; the D3D9-named pair exists only in extracted headers, with no require block in cl.xml |

Caveat on the 6: `<require comment=>` is registry author-intent, not published spec text.
It is the only available source, it is authored by the extension owners, and it matches
PR#1587 in all 6 cases — but a future spec publication could revise it.

## Summary

| bucket | count |
|---|---|
| Agree with PR#1587, spec-verified (applied) | 85 |
| Agree with PR#1587 via author-committed registry provenance (applied, labeled) | 6 |
| PR#1587 wrong or invalid (verified against spec text + registry typedefs; corrected, applied) | 4 |
| No spec source, no author provenance — ungrouped (PR#1587's groups NOT adopted) | 5 |
| tokens | **100** |
