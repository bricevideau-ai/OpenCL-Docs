# OpenCL cl.xml enum `group` attribution — final review table

Generated 2026-10-06.  Method: each group is a C value-set type name, derived from the
specification (core runtime/platform layers + KHR/EXT/Intel/Arm/Img vendor chapters),
cross-checked against cl.xml's own named containers (which are the C typedef names).
Groups follow the OpenGL registry (gl.xml) convention: the C type name, comma-separated
when a value is valid in several sets.

## Coverage

- Total `<enum>` entries in cl.xml: **1334**
- Assigned one or more groups: **1204**
- Left ungrouped: **130** (GL precedent: gl.xml leaves ~12,000 of 15,392 ungrouped;
  ungrouped = platform constants, opaque-handle values, and other context-dependent values
  whose meaning is defined by the API call site rather than by a named value set)
- Multi-group values: **13** (e.g. ['cl_context_info', 'cl_context_properties'])

## Rule table (how each group is determined)

| Rule | Evidence source | Example |
|---|---|---|
| R1 C typedef container in cl.xml | container name + spec listing | `CL_MAP_READ` → `cl_map_flags` |
| R2a param-name table label → Get-function signature | `List of supported param_names by {clGet<X>Info}` + cl.xml `<command>` | `CL_PLATFORM_NAME` → `cl_platform_info` |
| R2b event command types table | `List of supported event command types` | `CL_COMMAND_NDRANGE_KERNEL` → `cl_command_type` |
| R2c extension *New Enums* summary list | `{cl_X_TYPE}` bullet + child token | `CL_CURRENT_DEVICE_FOR_GL_CONTEXT_KHR` → `cl_gl_context_info` |
| R2d extension *param_name* sentence + #define list | `Accepted value for the _param_name_ parameter to *clGetDeviceInfo*` | `CL_DEVICE_HOST_MEM_CAPABILITIES_INTEL` → `cl_device_info` |
| R2e extension typedef + #define list | `typedef cl_bitfield cl_X;` + `#define CL_...` bit | `CL_UNIFIED_SHARED_MEMORY_ACCESS_INTEL` → `cl_device_unified_shared_memory_capabilities_intel` |
| R3 error codes | cl.xml ErrorCodes block; spec: “same set of error codes returned from API calls” | `CL_INVALID_ACCELERATOR_INTEL` → `ErrorCode` |

## Multi-group values (comma-separated in `group="..."`)

| token | groups | reason (spec evidence) |
|---|---|---|
| `CL_CONTEXT_ADAPTER_D3D9EX_KHR` | `cl_context_info, cl_context_properties` | spec evidence [cl_context_properties] value cell col0 (List of supported context creation properties by {) / spec evidence [cl_context_info] G3 new-enums list |
| `CL_CONTEXT_ADAPTER_D3D9_KHR` | `cl_context_info, cl_context_properties` | spec evidence [cl_context_properties] value cell col0 (List of supported context creation properties by {) / spec evidence [cl_context_info] G3 new-enums list |
| `CL_CONTEXT_ADAPTER_DXVA_KHR` | `cl_context_info, cl_context_properties` | spec evidence [cl_context_properties] value cell col0 (List of supported context creation properties by {) / spec evidence [cl_context_info] G3 new-enums list |
| `CL_MEM_ALLOC_FLAGS_INTEL` | `cl_mem_info_intel, cl_mem_properties_intel` | spec evidence [cl_mem_info_intel] value cell col0 (List of supported param_names by clGetMemAllocInfo) / spec evidence [cl_mem_properties_intel] G4 typedef+defi |
| `CL_QUEUE_FAMILY_INTEL` | `cl_command_queue_info, cl_command_queue_properties` | spec evidence [cl_command_queue_properties] value cell col0 (List of supported queue creation properties by clC) / spec evidence [cl_command_queue_info] G4 sent |
| `CL_QUEUE_INDEX_INTEL` | `cl_command_queue_info, cl_command_queue_properties` | spec evidence [cl_command_queue_properties] value cell col0 (List of supported queue creation properties by clC) / spec evidence [cl_command_queue_info] G4 sent |
| `CL_QUEUE_PRIORITY_KHR` | `cl_command_queue_properties, cl_queue_properties` | spec evidence [cl_command_queue_properties] value cell col0 (List of supported queue creation properties by {cl) / spec evidence [cl_queue_properties] G3 new-en |
| `CL_QUEUE_PROPERTIES` | `cl_command_queue_info, cl_command_queue_properties` | spec evidence [cl_command_queue_properties] value cell col0 (List of supported queue creation properties by {cl) / spec evidence [cl_command_queue_info] value c |
| `CL_QUEUE_SIZE` | `cl_command_queue_info, cl_command_queue_properties` | spec evidence [cl_command_queue_properties] value cell col0 (List of supported queue creation properties by {cl) / spec evidence [cl_command_queue_info] value c |
| `CL_QUEUE_THROTTLE_KHR` | `cl_command_queue_properties, cl_queue_properties` | spec evidence [cl_command_queue_properties] value cell col0 (List of supported queue creation properties by {cl) / spec evidence [cl_queue_properties] G3 new-en |
| `CL_SAMPLER_ADDRESSING_MODE` | `cl_sampler_info, cl_sampler_properties` | spec evidence [cl_sampler_properties] value cell col0 (List of supported sampler creation properties by {) / spec evidence [cl_sampler_info] value cell col0 (Li |
| `CL_SAMPLER_FILTER_MODE` | `cl_sampler_info, cl_sampler_properties` | spec evidence [cl_sampler_properties] value cell col0 (List of supported sampler creation properties by {) / spec evidence [cl_sampler_info] value cell col0 (Li |
| `CL_SAMPLER_NORMALIZED_COORDS` | `cl_sampler_info, cl_sampler_properties` | spec evidence [cl_sampler_properties] value cell col0 (List of supported sampler creation properties by {) / spec evidence [cl_sampler_info] value cell col0 (Li |

## Full assignment table

| token | container | group(s) | evidence |
|---|---|---|---|
| `CL_A` | cl_device_info | `cl_channel_order` | spec evidence [cl_channel_order] value cell col0 (Image Channel Order mapping) |
| `CL_ABGR` | cl_device_info | `cl_channel_order` | spec evidence [cl_channel_order] value cell col0 (Image Channel Order mapping) |
| `CL_ACCELERATOR_CONTEXT_INTEL` | enums.4090 | — (ungrouped, GL precedent) |  |
| `CL_ACCELERATOR_DESCRIPTOR_INTEL` | enums.4090 | — (ungrouped, GL precedent) |  |
| `CL_ACCELERATOR_REFERENCE_COUNT_INTEL` | enums.4090 | — (ungrouped, GL precedent) |  |
| `CL_ACCELERATOR_TYPE_INTEL` | enums.4090 | — (ungrouped, GL precedent) |  |
| `CL_ACCELERATOR_TYPE_MOTION_ESTIMATION_INTEL` | cl_accelerator_type_intel | `cl_accelerator_type_intel` | R1 C typedef container cl_accelerator_type_intel (container-declared) |
| `CL_ACCELERATOR_TYPE_NOT_SUPPORTED_INTEL` | ErrorCodes.1094 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_ADAPTER_D3D9EX_KHR` | enums.2000 | `cl_dx9_media_adapter_type_khr` | spec evidence [cl_dx9_media_adapter_type_khr] G3 new-enums list |
| `CL_ADAPTER_D3D9_KHR` | enums.2000 | `cl_dx9_media_adapter_type_khr` | spec evidence [cl_dx9_media_adapter_type_khr] G3 new-enums list |
| `CL_ADAPTER_DXVA_KHR` | enums.2000 | `cl_dx9_media_adapter_type_khr` | spec evidence [cl_dx9_media_adapter_type_khr] G3 new-enums list |
| `CL_ADDRESS_CLAMP` | cl_device_info | `cl_addressing_mode` | spec evidence [cl_addressing_mode] inline value-set of cl_addressing_mode (row {CL_SAMPLER_ADDRESSING_MODE_anchor}) |
| `CL_ADDRESS_CLAMP_TO_EDGE` | cl_device_info | `cl_addressing_mode` | spec evidence [cl_addressing_mode] inline value-set of cl_addressing_mode (row {CL_SAMPLER_ADDRESSING_MODE_anchor}) |
| `CL_ADDRESS_MIRRORED_REPEAT` | cl_device_info | `cl_addressing_mode` | spec evidence [cl_addressing_mode] inline value-set of cl_addressing_mode (row {CL_SAMPLER_ADDRESSING_MODE_anchor}) |
| `CL_ADDRESS_NONE` | cl_device_info | `cl_addressing_mode` | spec evidence [cl_addressing_mode] inline value-set of cl_addressing_mode (row {CL_SAMPLER_ADDRESSING_MODE_anchor}) |
| `CL_ADDRESS_REPEAT` | cl_device_info | `cl_addressing_mode` | spec evidence [cl_addressing_mode] inline value-set of cl_addressing_mode (row {CL_SAMPLER_ADDRESSING_MODE_anchor}) |
| `CL_AFFINITY_DOMAIN_L1_CACHE_EXT` | cl_affinity_domain_ext | `cl_affinity_domain_ext` | R1 C typedef container cl_affinity_domain_ext (container-declared) |
| `CL_AFFINITY_DOMAIN_L2_CACHE_EXT` | cl_affinity_domain_ext | `cl_affinity_domain_ext` | R1 C typedef container cl_affinity_domain_ext (container-declared) |
| `CL_AFFINITY_DOMAIN_L3_CACHE_EXT` | cl_affinity_domain_ext | `cl_affinity_domain_ext` | R1 C typedef container cl_affinity_domain_ext (container-declared) |
| `CL_AFFINITY_DOMAIN_L4_CACHE_EXT` | cl_affinity_domain_ext | `cl_affinity_domain_ext` | R1 C typedef container cl_affinity_domain_ext (container-declared) |
| `CL_AFFINITY_DOMAIN_NEXT_FISSIONABLE_EXT` | cl_affinity_domain_ext | `cl_affinity_domain_ext` | R1 C typedef container cl_affinity_domain_ext (container-declared) |
| `CL_AFFINITY_DOMAIN_NUMA_EXT` | cl_affinity_domain_ext | `cl_affinity_domain_ext` | R1 C typedef container cl_affinity_domain_ext (container-declared) |
| `CL_ALL_DEVICES_FOR_D3D10_KHR` | enums.4010 | `cl_d3d10_device_set_khr` | spec evidence [cl_d3d10_device_set_khr] G3 new-enums list |
| `CL_ALL_DEVICES_FOR_D3D11_KHR` | enums.4010 | `cl_d3d11_device_set_khr` | spec evidence [cl_d3d11_device_set_khr] G3 new-enums list |
| `CL_ALL_DEVICES_FOR_DX9_INTEL` | enums.4010 | — (ungrouped, GL precedent) |  |
| `CL_ALL_DEVICES_FOR_DX9_MEDIA_ADAPTER_KHR` | enums.2000 | `cl_dx9_media_adapter_set_khr` | spec evidence [cl_dx9_media_adapter_set_khr] G3 new-enums list |
| `CL_ALL_DEVICES_FOR_VA_API_INTEL` | enums.4090 | — (ungrouped, GL precedent) |  |
| `CL_ARGB` | cl_device_info | `cl_channel_order` | spec evidence [cl_channel_order] value cell col0 (Image Channel Order mapping) |
| `CL_AVC_ME_BIDIR_WEIGHT_HALF_INTEL` | cl_intel_device_side_avc_motion_estimation.weight | `cl_intel_device_side_avc_motion_estimation.weight` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.weight (container-declared) |
| `CL_AVC_ME_BIDIR_WEIGHT_QUARTER_INTEL` | cl_intel_device_side_avc_motion_estimation.weight | `cl_intel_device_side_avc_motion_estimation.weight` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.weight (container-declared) |
| `CL_AVC_ME_BIDIR_WEIGHT_THIRD_INTEL` | cl_intel_device_side_avc_motion_estimation.weight | `cl_intel_device_side_avc_motion_estimation.weight` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.weight (container-declared) |
| `CL_AVC_ME_BIDIR_WEIGHT_THREE_QUARTER_INTEL` | cl_intel_device_side_avc_motion_estimation.weight | `cl_intel_device_side_avc_motion_estimation.weight` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.weight (container-declared) |
| `CL_AVC_ME_BIDIR_WEIGHT_TWO_THIRD_INTEL` | cl_intel_device_side_avc_motion_estimation.weight | `cl_intel_device_side_avc_motion_estimation.weight` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.weight (container-declared) |
| `CL_AVC_ME_BLOCK_BASED_SKIP_4x4_INTEL` | cl_intel_device_side_avc_motion_estimation.skip.block.based | `cl_intel_device_side_avc_motion_estimation.skip.block.based` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.skip.block.based (container-declared) |
| `CL_AVC_ME_BLOCK_BASED_SKIP_8x8_INTEL` | cl_intel_device_side_avc_motion_estimation.skip.block.based | `cl_intel_device_side_avc_motion_estimation.skip.block.based` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.skip.block.based (container-declared) |
| `CL_AVC_ME_BORDER_REACHED_BOTTOM_INTEL` | cl_intel_device_side_avc_motion_estimation.border | `cl_intel_device_side_avc_motion_estimation.border` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.border (container-declared) |
| `CL_AVC_ME_BORDER_REACHED_LEFT_INTEL` | cl_intel_device_side_avc_motion_estimation.border | `cl_intel_device_side_avc_motion_estimation.border` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.border (container-declared) |
| `CL_AVC_ME_BORDER_REACHED_RIGHT_INTEL` | cl_intel_device_side_avc_motion_estimation.border | `cl_intel_device_side_avc_motion_estimation.border` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.border (container-declared) |
| `CL_AVC_ME_BORDER_REACHED_TOP_INTEL` | cl_intel_device_side_avc_motion_estimation.border | `cl_intel_device_side_avc_motion_estimation.border` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.border (container-declared) |
| `CL_AVC_ME_CHROMA_PREDICTOR_MODE_DC_INTEL` | cl_intel_device_side_avc_motion_estimation.luma.predictor | `cl_intel_device_side_avc_motion_estimation.luma.predictor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.luma.predictor (container-declared) |
| `CL_AVC_ME_CHROMA_PREDICTOR_MODE_HORIZONTAL_INTEL` | cl_intel_device_side_avc_motion_estimation.luma.predictor | `cl_intel_device_side_avc_motion_estimation.luma.predictor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.luma.predictor (container-declared) |
| `CL_AVC_ME_CHROMA_PREDICTOR_MODE_PLANE_INTEL` | cl_intel_device_side_avc_motion_estimation.luma.predictor | `cl_intel_device_side_avc_motion_estimation.luma.predictor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.luma.predictor (container-declared) |
| `CL_AVC_ME_CHROMA_PREDICTOR_MODE_VERTICAL_INTEL` | cl_intel_device_side_avc_motion_estimation.luma.predictor | `cl_intel_device_side_avc_motion_estimation.luma.predictor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.luma.predictor (container-declared) |
| `CL_AVC_ME_COST_PRECISION_DPEL_INTEL` | cl_intel_device_side_avc_motion_estimation.cost.precision | `cl_intel_device_side_avc_motion_estimation.cost.precision` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.cost.precision (container-declared) |
| `CL_AVC_ME_COST_PRECISION_HPEL_INTEL` | cl_intel_device_side_avc_motion_estimation.cost.precision | `cl_intel_device_side_avc_motion_estimation.cost.precision` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.cost.precision (container-declared) |
| `CL_AVC_ME_COST_PRECISION_PEL_INTEL` | cl_intel_device_side_avc_motion_estimation.cost.precision | `cl_intel_device_side_avc_motion_estimation.cost.precision` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.cost.precision (container-declared) |
| `CL_AVC_ME_COST_PRECISION_QPEL_INTEL` | cl_intel_device_side_avc_motion_estimation.cost.precision | `cl_intel_device_side_avc_motion_estimation.cost.precision` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.cost.precision (container-declared) |
| `CL_AVC_ME_FRAME_BACKWARD_INTEL` | cl_intel_device_side_avc_motion_estimation.frame.dir | `cl_intel_device_side_avc_motion_estimation.frame.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.frame.dir (container-declared) |
| `CL_AVC_ME_FRAME_DUAL_INTEL` | cl_intel_device_side_avc_motion_estimation.frame.dir | `cl_intel_device_side_avc_motion_estimation.frame.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.frame.dir (container-declared) |
| `CL_AVC_ME_FRAME_FORWARD_INTEL` | cl_intel_device_side_avc_motion_estimation.frame.dir | `cl_intel_device_side_avc_motion_estimation.frame.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.frame.dir (container-declared) |
| `CL_AVC_ME_INTERLACED_SCAN_BOTTOM_FIELD_INTEL` | cl_intel_device_side_avc_motion_estimation.scan.dir | `cl_intel_device_side_avc_motion_estimation.scan.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.scan.dir (container-declared) |
| `CL_AVC_ME_INTERLACED_SCAN_TOP_FIELD_INTEL` | cl_intel_device_side_avc_motion_estimation.scan.dir | `cl_intel_device_side_avc_motion_estimation.scan.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.scan.dir (container-declared) |
| `CL_AVC_ME_INTRA_16x16_INTEL` | cl_intel_device_side_avc_motion_estimation.intra | `cl_intel_device_side_avc_motion_estimation.intra` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.intra (container-declared) |
| `CL_AVC_ME_INTRA_4x4_INTEL` | cl_intel_device_side_avc_motion_estimation.intra | `cl_intel_device_side_avc_motion_estimation.intra` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.intra (container-declared) |
| `CL_AVC_ME_INTRA_8x8_INTEL` | cl_intel_device_side_avc_motion_estimation.intra | `cl_intel_device_side_avc_motion_estimation.intra` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.intra (container-declared) |
| `CL_AVC_ME_INTRA_LUMA_PARTITION_MASK_16x16_INTEL` | cl_intel_device_side_avc_motion_estimation.intra.luma | `cl_intel_device_side_avc_motion_estimation.intra.luma` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.intra.luma (container-declared) |
| `CL_AVC_ME_INTRA_LUMA_PARTITION_MASK_4x4_INTEL` | cl_intel_device_side_avc_motion_estimation.intra.luma | `cl_intel_device_side_avc_motion_estimation.intra.luma` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.intra.luma (container-declared) |
| `CL_AVC_ME_INTRA_LUMA_PARTITION_MASK_8x8_INTEL` | cl_intel_device_side_avc_motion_estimation.intra.luma | `cl_intel_device_side_avc_motion_estimation.intra.luma` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.intra.luma (container-declared) |
| `CL_AVC_ME_INTRA_NEIGHBOR_LEFT_MASK_ENABLE_INTEL` | cl_intel_device_side_avc_motion_estimation.intra.neighbor | `cl_intel_device_side_avc_motion_estimation.intra.neighbor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.intra.neighbor (container-declared) |
| `CL_AVC_ME_INTRA_NEIGHBOR_UPPER_LEFT_MASK_ENABLE_INTEL` | cl_intel_device_side_avc_motion_estimation.intra.neighbor | `cl_intel_device_side_avc_motion_estimation.intra.neighbor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.intra.neighbor (container-declared) |
| `CL_AVC_ME_INTRA_NEIGHBOR_UPPER_MASK_ENABLE_INTEL` | cl_intel_device_side_avc_motion_estimation.intra.neighbor | `cl_intel_device_side_avc_motion_estimation.intra.neighbor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.intra.neighbor (container-declared) |
| `CL_AVC_ME_INTRA_NEIGHBOR_UPPER_RIGHT_MASK_ENABLE_INTEL` | cl_intel_device_side_avc_motion_estimation.intra.neighbor | `cl_intel_device_side_avc_motion_estimation.intra.neighbor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.intra.neighbor (container-declared) |
| `CL_AVC_ME_LUMA_PREDICTOR_MODE_DC_INTEL` | cl_intel_device_side_avc_motion_estimation.luma.predictor | `cl_intel_device_side_avc_motion_estimation.luma.predictor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.luma.predictor (container-declared) |
| `CL_AVC_ME_LUMA_PREDICTOR_MODE_DIAGONAL_DOWN_LEFT_INTEL` | cl_intel_device_side_avc_motion_estimation.luma.predictor | `cl_intel_device_side_avc_motion_estimation.luma.predictor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.luma.predictor (container-declared) |
| `CL_AVC_ME_LUMA_PREDICTOR_MODE_DIAGONAL_DOWN_RIGHT_INTEL` | cl_intel_device_side_avc_motion_estimation.luma.predictor | `cl_intel_device_side_avc_motion_estimation.luma.predictor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.luma.predictor (container-declared) |
| `CL_AVC_ME_LUMA_PREDICTOR_MODE_HORIZONTAL_DOWN_INTEL` | cl_intel_device_side_avc_motion_estimation.luma.predictor | `cl_intel_device_side_avc_motion_estimation.luma.predictor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.luma.predictor (container-declared) |
| `CL_AVC_ME_LUMA_PREDICTOR_MODE_HORIZONTAL_INTEL` | cl_intel_device_side_avc_motion_estimation.luma.predictor | `cl_intel_device_side_avc_motion_estimation.luma.predictor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.luma.predictor (container-declared) |
| `CL_AVC_ME_LUMA_PREDICTOR_MODE_HORIZONTAL_UP_INTEL` | cl_intel_device_side_avc_motion_estimation.luma.predictor | `cl_intel_device_side_avc_motion_estimation.luma.predictor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.luma.predictor (container-declared) |
| `CL_AVC_ME_LUMA_PREDICTOR_MODE_PLANE_INTEL` | cl_intel_device_side_avc_motion_estimation.luma.predictor | `cl_intel_device_side_avc_motion_estimation.luma.predictor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.luma.predictor (container-declared) |
| `CL_AVC_ME_LUMA_PREDICTOR_MODE_VERTICAL_INTEL` | cl_intel_device_side_avc_motion_estimation.luma.predictor | `cl_intel_device_side_avc_motion_estimation.luma.predictor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.luma.predictor (container-declared) |
| `CL_AVC_ME_LUMA_PREDICTOR_MODE_VERTICAL_LEFT_INTEL` | cl_intel_device_side_avc_motion_estimation.luma.predictor | `cl_intel_device_side_avc_motion_estimation.luma.predictor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.luma.predictor (container-declared) |
| `CL_AVC_ME_LUMA_PREDICTOR_MODE_VERTICAL_RIGHT_INTEL` | cl_intel_device_side_avc_motion_estimation.luma.predictor | `cl_intel_device_side_avc_motion_estimation.luma.predictor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.luma.predictor (container-declared) |
| `CL_AVC_ME_MAJOR_16x16_INTEL` | cl_intel_device_side_avc_motion_estimation.major | `cl_intel_device_side_avc_motion_estimation.major` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.major (container-declared) |
| `CL_AVC_ME_MAJOR_16x8_INTEL` | cl_intel_device_side_avc_motion_estimation.major | `cl_intel_device_side_avc_motion_estimation.major` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.major (container-declared) |
| `CL_AVC_ME_MAJOR_8x16_INTEL` | cl_intel_device_side_avc_motion_estimation.major | `cl_intel_device_side_avc_motion_estimation.major` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.major (container-declared) |
| `CL_AVC_ME_MAJOR_8x8_INTEL` | cl_intel_device_side_avc_motion_estimation.major | `cl_intel_device_side_avc_motion_estimation.major` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.major (container-declared) |
| `CL_AVC_ME_MAJOR_BACKWARD_INTEL` | cl_intel_device_side_avc_motion_estimation.major.dir | `cl_intel_device_side_avc_motion_estimation.major.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.major.dir (container-declared) |
| `CL_AVC_ME_MAJOR_BIDIRECTIONAL_INTEL` | cl_intel_device_side_avc_motion_estimation.major.dir | `cl_intel_device_side_avc_motion_estimation.major.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.major.dir (container-declared) |
| `CL_AVC_ME_MAJOR_FORWARD_INTEL` | cl_intel_device_side_avc_motion_estimation.major.dir | `cl_intel_device_side_avc_motion_estimation.major.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.major.dir (container-declared) |
| `CL_AVC_ME_MINOR_4x4_INTEL` | cl_intel_device_side_avc_motion_estimation.minor | `cl_intel_device_side_avc_motion_estimation.minor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.minor (container-declared) |
| `CL_AVC_ME_MINOR_4x8_INTEL` | cl_intel_device_side_avc_motion_estimation.minor | `cl_intel_device_side_avc_motion_estimation.minor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.minor (container-declared) |
| `CL_AVC_ME_MINOR_8x4_INTEL` | cl_intel_device_side_avc_motion_estimation.minor | `cl_intel_device_side_avc_motion_estimation.minor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.minor (container-declared) |
| `CL_AVC_ME_MINOR_8x8_INTEL` | cl_intel_device_side_avc_motion_estimation.minor | `cl_intel_device_side_avc_motion_estimation.minor` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.minor (container-declared) |
| `CL_AVC_ME_PARTITION_MASK_16x16_INTEL` | cl_intel_device_side_avc_motion_estimation.partition | `cl_intel_device_side_avc_motion_estimation.partition` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.partition (container-declared) |
| `CL_AVC_ME_PARTITION_MASK_16x8_INTEL` | cl_intel_device_side_avc_motion_estimation.partition | `cl_intel_device_side_avc_motion_estimation.partition` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.partition (container-declared) |
| `CL_AVC_ME_PARTITION_MASK_4x4_INTEL` | cl_intel_device_side_avc_motion_estimation.partition | `cl_intel_device_side_avc_motion_estimation.partition` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.partition (container-declared) |
| `CL_AVC_ME_PARTITION_MASK_4x8_INTEL` | cl_intel_device_side_avc_motion_estimation.partition | `cl_intel_device_side_avc_motion_estimation.partition` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.partition (container-declared) |
| `CL_AVC_ME_PARTITION_MASK_8x16_INTEL` | cl_intel_device_side_avc_motion_estimation.partition | `cl_intel_device_side_avc_motion_estimation.partition` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.partition (container-declared) |
| `CL_AVC_ME_PARTITION_MASK_8x4_INTEL` | cl_intel_device_side_avc_motion_estimation.partition | `cl_intel_device_side_avc_motion_estimation.partition` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.partition (container-declared) |
| `CL_AVC_ME_PARTITION_MASK_8x8_INTEL` | cl_intel_device_side_avc_motion_estimation.partition | `cl_intel_device_side_avc_motion_estimation.partition` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.partition (container-declared) |
| `CL_AVC_ME_PARTITION_MASK_ALL_INTEL` | cl_intel_device_side_avc_motion_estimation.partition | `cl_intel_device_side_avc_motion_estimation.partition` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.partition (container-declared) |
| `CL_AVC_ME_SAD_ADJUST_MODE_HAAR_INTEL` | cl_intel_device_side_avc_motion_estimation.adjust | `cl_intel_device_side_avc_motion_estimation.adjust` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.adjust (container-declared) |
| `CL_AVC_ME_SAD_ADJUST_MODE_NONE_INTEL` | cl_intel_device_side_avc_motion_estimation.adjust | `cl_intel_device_side_avc_motion_estimation.adjust` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.adjust (container-declared) |
| `CL_AVC_ME_SEARCH_WINDOW_16x12_RADIUS_INTEL` | cl_intel_device_side_avc_motion_estimation.window | `cl_intel_device_side_avc_motion_estimation.window` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.window (container-declared) |
| `CL_AVC_ME_SEARCH_WINDOW_2x2_RADIUS_INTEL` | cl_intel_device_side_avc_motion_estimation.window | `cl_intel_device_side_avc_motion_estimation.window` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.window (container-declared) |
| `CL_AVC_ME_SEARCH_WINDOW_4x4_RADIUS_INTEL` | cl_intel_device_side_avc_motion_estimation.window | `cl_intel_device_side_avc_motion_estimation.window` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.window (container-declared) |
| `CL_AVC_ME_SEARCH_WINDOW_CUSTOM_INTEL` | cl_intel_device_side_avc_motion_estimation.window | `cl_intel_device_side_avc_motion_estimation.window` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.window (container-declared) |
| `CL_AVC_ME_SEARCH_WINDOW_DIAMOND_INTEL` | cl_intel_device_side_avc_motion_estimation.window | `cl_intel_device_side_avc_motion_estimation.window` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.window (container-declared) |
| `CL_AVC_ME_SEARCH_WINDOW_EXHAUSTIVE_INTEL` | cl_intel_device_side_avc_motion_estimation.window | `cl_intel_device_side_avc_motion_estimation.window` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.window (container-declared) |
| `CL_AVC_ME_SEARCH_WINDOW_EXTRA_TINY_INTEL` | cl_intel_device_side_avc_motion_estimation.window | `cl_intel_device_side_avc_motion_estimation.window` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.window (container-declared) |
| `CL_AVC_ME_SEARCH_WINDOW_LARGE_DIAMOND_INTEL` | cl_intel_device_side_avc_motion_estimation.window | `cl_intel_device_side_avc_motion_estimation.window` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.window (container-declared) |
| `CL_AVC_ME_SEARCH_WINDOW_RESERVED0_INTEL` | cl_intel_device_side_avc_motion_estimation.window | `cl_intel_device_side_avc_motion_estimation.window` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.window (container-declared) |
| `CL_AVC_ME_SEARCH_WINDOW_RESERVED1_INTEL` | cl_intel_device_side_avc_motion_estimation.window | `cl_intel_device_side_avc_motion_estimation.window` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.window (container-declared) |
| `CL_AVC_ME_SEARCH_WINDOW_SMALL_INTEL` | cl_intel_device_side_avc_motion_estimation.window | `cl_intel_device_side_avc_motion_estimation.window` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.window (container-declared) |
| `CL_AVC_ME_SEARCH_WINDOW_TINY_INTEL` | cl_intel_device_side_avc_motion_estimation.window | `cl_intel_device_side_avc_motion_estimation.window` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.window (container-declared) |
| `CL_AVC_ME_SKIP_BLOCK_16x16_BACKWARD_ENABLE_INTEL` | cl_intel_device_side_avc_motion_estimation.skip.dir | `cl_intel_device_side_avc_motion_estimation.skip.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.skip.dir (container-declared) |
| `CL_AVC_ME_SKIP_BLOCK_16x16_DUAL_ENABLE_INTEL` | cl_intel_device_side_avc_motion_estimation.skip.dir | `cl_intel_device_side_avc_motion_estimation.skip.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.skip.dir (container-declared) |
| `CL_AVC_ME_SKIP_BLOCK_16x16_FORWARD_ENABLE_INTEL` | cl_intel_device_side_avc_motion_estimation.skip.dir | `cl_intel_device_side_avc_motion_estimation.skip.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.skip.dir (container-declared) |
| `CL_AVC_ME_SKIP_BLOCK_8x8_0_BACKWARD_ENABLE_INTEL` | cl_intel_device_side_avc_motion_estimation.skip.dir | `cl_intel_device_side_avc_motion_estimation.skip.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.skip.dir (container-declared) |
| `CL_AVC_ME_SKIP_BLOCK_8x8_0_FORWARD_ENABLE_INTEL` | cl_intel_device_side_avc_motion_estimation.skip.dir | `cl_intel_device_side_avc_motion_estimation.skip.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.skip.dir (container-declared) |
| `CL_AVC_ME_SKIP_BLOCK_8x8_1_BACKWARD_ENABLE_INTEL` | cl_intel_device_side_avc_motion_estimation.skip.dir | `cl_intel_device_side_avc_motion_estimation.skip.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.skip.dir (container-declared) |
| `CL_AVC_ME_SKIP_BLOCK_8x8_1_FORWARD_ENABLE_INTEL` | cl_intel_device_side_avc_motion_estimation.skip.dir | `cl_intel_device_side_avc_motion_estimation.skip.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.skip.dir (container-declared) |
| `CL_AVC_ME_SKIP_BLOCK_8x8_2_BACKWARD_ENABLE_INTEL` | cl_intel_device_side_avc_motion_estimation.skip.dir | `cl_intel_device_side_avc_motion_estimation.skip.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.skip.dir (container-declared) |
| `CL_AVC_ME_SKIP_BLOCK_8x8_2_FORWARD_ENABLE_INTEL` | cl_intel_device_side_avc_motion_estimation.skip.dir | `cl_intel_device_side_avc_motion_estimation.skip.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.skip.dir (container-declared) |
| `CL_AVC_ME_SKIP_BLOCK_8x8_3_BACKWARD_ENABLE_INTEL` | cl_intel_device_side_avc_motion_estimation.skip.dir | `cl_intel_device_side_avc_motion_estimation.skip.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.skip.dir (container-declared) |
| `CL_AVC_ME_SKIP_BLOCK_8x8_3_FORWARD_ENABLE_INTEL` | cl_intel_device_side_avc_motion_estimation.skip.dir | `cl_intel_device_side_avc_motion_estimation.skip.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.skip.dir (container-declared) |
| `CL_AVC_ME_SKIP_BLOCK_8x8_BACKWARD_ENABLE_INTEL` | cl_intel_device_side_avc_motion_estimation.skip.dir | `cl_intel_device_side_avc_motion_estimation.skip.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.skip.dir (container-declared) |
| `CL_AVC_ME_SKIP_BLOCK_8x8_DUAL_ENABLE_INTEL` | cl_intel_device_side_avc_motion_estimation.skip.dir | `cl_intel_device_side_avc_motion_estimation.skip.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.skip.dir (container-declared) |
| `CL_AVC_ME_SKIP_BLOCK_8x8_FORWARD_ENABLE_INTEL` | cl_intel_device_side_avc_motion_estimation.skip.dir | `cl_intel_device_side_avc_motion_estimation.skip.dir` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.skip.dir (container-declared) |
| `CL_AVC_ME_SKIP_BLOCK_PARTITION_16x16_INTEL` | cl_intel_device_side_avc_motion_estimation.skip | `cl_intel_device_side_avc_motion_estimation.skip` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.skip (container-declared) |
| `CL_AVC_ME_SKIP_BLOCK_PARTITION_8x8_INTEL` | cl_intel_device_side_avc_motion_estimation.skip | `cl_intel_device_side_avc_motion_estimation.skip` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.skip (container-declared) |
| `CL_AVC_ME_SLICE_TYPE_BPRED_INTEL` | cl_intel_device_side_avc_motion_estimation.slice | `cl_intel_device_side_avc_motion_estimation.slice` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.slice (container-declared) |
| `CL_AVC_ME_SLICE_TYPE_INTRA_INTEL` | cl_intel_device_side_avc_motion_estimation.slice | `cl_intel_device_side_avc_motion_estimation.slice` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.slice (container-declared) |
| `CL_AVC_ME_SLICE_TYPE_PRED_INTEL` | cl_intel_device_side_avc_motion_estimation.slice | `cl_intel_device_side_avc_motion_estimation.slice` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.slice (container-declared) |
| `CL_AVC_ME_SUBPIXEL_MODE_HPEL_INTEL` | cl_intel_device_side_avc_motion_estimation.subpixel | `cl_intel_device_side_avc_motion_estimation.subpixel` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.subpixel (container-declared) |
| `CL_AVC_ME_SUBPIXEL_MODE_INTEGER_INTEL` | cl_intel_device_side_avc_motion_estimation.subpixel | `cl_intel_device_side_avc_motion_estimation.subpixel` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.subpixel (container-declared) |
| `CL_AVC_ME_SUBPIXEL_MODE_QPEL_INTEL` | cl_intel_device_side_avc_motion_estimation.subpixel | `cl_intel_device_side_avc_motion_estimation.subpixel` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.subpixel (container-declared) |
| `CL_AVC_ME_VERSION_0_INTEL` | cl_intel_device_side_avc_motion_estimation.version | `cl_intel_device_side_avc_motion_estimation.version` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.version (container-declared) |
| `CL_AVC_ME_VERSION_1_INTEL` | cl_intel_device_side_avc_motion_estimation.version | `cl_intel_device_side_avc_motion_estimation.version` | R1 C typedef container cl_intel_device_side_avc_motion_estimation.version (container-declared) |
| `CL_BGRA` | cl_device_info | `cl_channel_order` | spec evidence [cl_channel_order] clean cell col1+ (Compatible Image Channel Orders) |
| `CL_BLOCKING` | cl_bool | `cl_bool` | R1 C typedef container cl_bool (container-declared) |
| `CL_BUFFER_CREATE_TYPE_REGION` | cl_device_info | `cl_buffer_create_type` | spec evidence [cl_buffer_create_type] value cell col0 (List of supported buffer creation types by {clCrea) |
| `CL_BUILD_ERROR` | cl_build_status | `cl_build_status` | R1 C typedef container cl_build_status (spec-listed) |
| `CL_BUILD_IN_PROGRESS` | cl_build_status | `cl_build_status` | R1 C typedef container cl_build_status (spec-listed) |
| `CL_BUILD_NONE` | cl_build_status | `cl_build_status` | R1 C typedef container cl_build_status (spec-listed) |
| `CL_BUILD_PROGRAM_FAILURE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_BUILD_SUCCESS` | cl_build_status | `cl_build_status` | R1 C typedef container cl_build_status (spec-listed) |
| `CL_CANCELLED_IMG` | ErrorCodes.1122 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_CGL_SHAREGROUP_KHR` | enums.2000 | `cl_context_properties` | spec evidence [cl_context_properties] G3 new-enums list |
| `CL_CHAR_BIT` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_CHAR_MAX` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_CHAR_MIN` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_COMMAND_ACQUIRE_D3D10_OBJECTS_KHR` | enums.4010 | `cl_command_type` | spec evidence [cl_command_type] G3 new-enums list |
| `CL_COMMAND_ACQUIRE_D3D11_OBJECTS_KHR` | enums.4010 | `cl_command_type` | spec evidence [cl_command_type] G3 new-enums list |
| `CL_COMMAND_ACQUIRE_D3D9_OBJECTS_INTEL` | enums.4010 | — (ungrouped, GL precedent) |  |
| `CL_COMMAND_ACQUIRE_DX9_MEDIA_SURFACES_KHR` | enums.2000 | `cl_command_type` | spec evidence [cl_command_type] G3 new-enums list |
| `CL_COMMAND_ACQUIRE_DX9_OBJECTS_INTEL` | enums.4010 | — (ungrouped, GL precedent) |  |
| `CL_COMMAND_ACQUIRE_EGL_OBJECTS_KHR` | enums.2000 | `cl_command_type` | spec evidence [cl_command_type] G3 new-enums list |
| `CL_COMMAND_ACQUIRE_EXTERNAL_MEM_OBJECTS_KHR` | enums.2000 | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_ACQUIRE_GL_OBJECTS` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_ACQUIRE_GRALLOC_OBJECTS_IMG` | enums.40D0 | `cl_command_type` | manual: cl_img_use_gralloc_ptr new command type (clEnqueueAcquire/ReleaseGrallocObject) |
| `CL_COMMAND_ACQUIRE_VA_API_MEDIA_SURFACES_INTEL` | enums.4090 | — (ungrouped, GL precedent) |  |
| `CL_COMMAND_BARRIER` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_BUFFER_CAPABILITY_DEVICE_SIDE_ENQUEUE_KHR` | cl_device_command_buffer_capabilities_khr | `cl_device_command_buffer_capabilities_khr` | R1 C typedef container cl_device_command_buffer_capabilities_khr (spec-listed) |
| `CL_COMMAND_BUFFER_CAPABILITY_KERNEL_PRINTF_KHR` | cl_device_command_buffer_capabilities_khr | `cl_device_command_buffer_capabilities_khr` | R1 C typedef container cl_device_command_buffer_capabilities_khr (spec-listed) |
| `CL_COMMAND_BUFFER_CAPABILITY_MULTIPLE_QUEUE_KHR` | cl_device_command_buffer_capabilities_khr | `cl_device_command_buffer_capabilities_khr` | R1 C typedef container cl_device_command_buffer_capabilities_khr (spec-listed) |
| `CL_COMMAND_BUFFER_CAPABILITY_SIMULTANEOUS_USE_KHR` | cl_device_command_buffer_capabilities_khr | `cl_device_command_buffer_capabilities_khr` | R1 C typedef container cl_device_command_buffer_capabilities_khr (spec-listed) |
| `CL_COMMAND_BUFFER_CONTEXT_KHR` | cl_device_info | `cl_command_buffer_info_khr` | spec evidence [cl_command_buffer_info_khr] G3 new-enums list |
| `CL_COMMAND_BUFFER_DEVICE_SIDE_SYNC_KHR` | cl_command_buffer_flags_khr | `cl_command_buffer_flags_khr` | R1 C typedef container cl_command_buffer_flags_khr (spec-listed) |
| `CL_COMMAND_BUFFER_FLAGS_KHR` | cl_device_info | `cl_command_buffer_properties_khr` | spec evidence [cl_command_buffer_properties_khr] G3 new-enums list |
| `CL_COMMAND_BUFFER_MUTABLE_DISPATCH_ASSERTS_KHR` | cl_device_info | `cl_command_buffer_properties_khr` | spec evidence [cl_command_buffer_properties_khr] G3 new-enums list |
| `CL_COMMAND_BUFFER_MUTABLE_KHR` | cl_command_buffer_flags_khr | `cl_command_buffer_flags_khr` | R1 C typedef container cl_command_buffer_flags_khr (spec-listed) |
| `CL_COMMAND_BUFFER_NUM_QUEUES_KHR` | cl_device_info | `cl_command_buffer_info_khr` | spec evidence [cl_command_buffer_info_khr] G3 new-enums list |
| `CL_COMMAND_BUFFER_PLATFORM_AUTOMATIC_REMAP_KHR` | cl_platform_command_buffer_capabilities_khr | `cl_platform_command_buffer_capabilities_khr` | R1 C typedef container cl_platform_command_buffer_capabilities_khr (spec-listed) |
| `CL_COMMAND_BUFFER_PLATFORM_REMAP_QUEUES_KHR` | cl_platform_command_buffer_capabilities_khr | `cl_platform_command_buffer_capabilities_khr` | R1 C typedef container cl_platform_command_buffer_capabilities_khr (spec-listed) |
| `CL_COMMAND_BUFFER_PLATFORM_UNIVERSAL_SYNC_KHR` | cl_platform_command_buffer_capabilities_khr | `cl_platform_command_buffer_capabilities_khr` | R1 C typedef container cl_platform_command_buffer_capabilities_khr (spec-listed) |
| `CL_COMMAND_BUFFER_PROPERTIES_ARRAY_KHR` | cl_device_info | `cl_command_buffer_info_khr` | spec evidence [cl_command_buffer_info_khr] G3 new-enums list |
| `CL_COMMAND_BUFFER_QUEUES_KHR` | cl_device_info | `cl_command_buffer_info_khr` | spec evidence [cl_command_buffer_info_khr] G3 new-enums list |
| `CL_COMMAND_BUFFER_REFERENCE_COUNT_KHR` | cl_device_info | `cl_command_buffer_info_khr` | spec evidence [cl_command_buffer_info_khr] G3 new-enums list |
| `CL_COMMAND_BUFFER_SIMULTANEOUS_USE_KHR` | cl_command_buffer_flags_khr | `cl_command_buffer_flags_khr` | R1 C typedef container cl_command_buffer_flags_khr (spec-listed) |
| `CL_COMMAND_BUFFER_STATE_EXECUTABLE_KHR` | cl_command_buffer_state_khr | `cl_command_buffer_state_khr` | R1 C typedef container cl_command_buffer_state_khr (spec-listed) |
| `CL_COMMAND_BUFFER_STATE_FINALIZED_KHR` | cl_command_buffer_state_khr | `cl_command_buffer_state_khr` | R1 C typedef container cl_command_buffer_state_khr (spec-listed) |
| `CL_COMMAND_BUFFER_STATE_KHR` | cl_device_info | `cl_command_buffer_info_khr` | spec evidence [cl_command_buffer_info_khr] G3 new-enums list |
| `CL_COMMAND_BUFFER_STATE_RECORDING_KHR` | cl_command_buffer_state_khr | `cl_command_buffer_state_khr` | R1 C typedef container cl_command_buffer_state_khr (spec-listed) |
| `CL_COMMAND_COMMAND_BUFFER_KHR` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] G3 new-enums list |
| `CL_COMMAND_COPY_BUFFER` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_COPY_BUFFER_RECT` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_COPY_BUFFER_TO_IMAGE` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_COPY_IMAGE` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_COPY_IMAGE_TO_BUFFER` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_EGL_FENCE_SYNC_OBJECT_KHR` | enums.2000 | `cl_command_type` | spec evidence [cl_command_type] G3 new-enums list |
| `CL_COMMAND_FILL_BUFFER` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_FILL_IMAGE` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_GENERATE_MIPMAP_IMG` | enums.40D0 | `cl_command_type` | manual: cl_img_generate_mipmap new command type (clEnqueueGenerateMipmap) |
| `CL_COMMAND_GL_FENCE_SYNC_OBJECT_KHR` | enums.2000 | `cl_command_type` | spec evidence [cl_command_type] G3 new-enums list |
| `CL_COMMAND_MAP_BUFFER` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_MAP_IMAGE` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_MARKER` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_MEMADVISE_INTEL` | enums.4200 | `cl_kernel_exec_info` | spec evidence [cl_kernel_exec_info] G4 sentence+define |
| `CL_COMMAND_MEMCPY_INTEL` | enums.4200 | `cl_kernel_exec_info` | spec evidence [cl_kernel_exec_info] G4 sentence+define |
| `CL_COMMAND_MEMFILL_INTEL` | enums.4200 | `cl_kernel_exec_info` | spec evidence [cl_kernel_exec_info] G4 sentence+define |
| `CL_COMMAND_MIGRATEMEM_INTEL` | enums.4200 | `cl_kernel_exec_info` | spec evidence [cl_kernel_exec_info] G4 sentence+define |
| `CL_COMMAND_MIGRATE_MEM_OBJECTS` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_MIGRATE_MEM_OBJECT_EXT` | enums.4040 | — (ungrouped, GL precedent) |  |
| `CL_COMMAND_NATIVE_KERNEL` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_NDRANGE_KERNEL` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_ARBITRATION_ALGORITHM_IMG` | enums.4220 | — (ungrouped, GL precedent) |  |
| `CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_ARBITRATION_ALGORITHM_ROUND_ROBIN_IMG` | enums.4220 | — (ungrouped, GL precedent) |  |
| `CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_ARBITRATION_ALGORITHM_TASK_DEMAND_IMG` | enums.4220 | — (ungrouped, GL precedent) |  |
| `CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_EXECUTE_COUNT_IMG` | enums.4220 | — (ungrouped, GL precedent) |  |
| `CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_SCHEDULING_ALGORITHM_IMG` | enums.4220 | — (ungrouped, GL precedent) |  |
| `CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_SCHEDULING_ALGORITHM_LINEAR_ORDER_IMG` | enums.4220 | — (ungrouped, GL precedent) |  |
| `CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_SCHEDULING_ALGORITHM_MORTON_ORDER_IMG` | enums.4220 | — (ungrouped, GL precedent) |  |
| `CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_SCHEDULING_ALGORITHM_THREED_MORTON_ORDER_IMG` | enums.4220 | — (ungrouped, GL precedent) |  |
| `CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_SCHEDULING_ALGORITHM_TWOD_MORTON_ORDER_IMG` | enums.4220 | — (ungrouped, GL precedent) |  |
| `CL_COMMAND_READ_BUFFER` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_READ_BUFFER_RECT` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_READ_HOST_PIPE_INTEL` | enums.4210 | `cl_command_type` | manual: cl_intel_program_scope_host_pipe Table 37 supported event command type |
| `CL_COMMAND_READ_IMAGE` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_RELEASE_D3D10_OBJECTS_KHR` | enums.4010 | `cl_command_type` | spec evidence [cl_command_type] G3 new-enums list |
| `CL_COMMAND_RELEASE_D3D11_OBJECTS_KHR` | enums.4010 | `cl_command_type` | spec evidence [cl_command_type] G3 new-enums list |
| `CL_COMMAND_RELEASE_D3D9_OBJECTS_INTEL` | enums.4010 | — (ungrouped, GL precedent) |  |
| `CL_COMMAND_RELEASE_DX9_MEDIA_SURFACES_KHR` | enums.2000 | `cl_command_type` | spec evidence [cl_command_type] G3 new-enums list |
| `CL_COMMAND_RELEASE_DX9_OBJECTS_INTEL` | enums.4010 | — (ungrouped, GL precedent) |  |
| `CL_COMMAND_RELEASE_EGL_OBJECTS_KHR` | enums.2000 | `cl_command_type` | spec evidence [cl_command_type] G3 new-enums list |
| `CL_COMMAND_RELEASE_EXTERNAL_MEM_OBJECTS_KHR` | enums.2000 | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_RELEASE_GL_OBJECTS` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_RELEASE_GRALLOC_OBJECTS_IMG` | enums.40D0 | `cl_command_type` | manual: cl_img_use_gralloc_ptr new command type |
| `CL_COMMAND_RELEASE_VA_API_MEDIA_SURFACES_INTEL` | enums.4090 | — (ungrouped, GL precedent) |  |
| `CL_COMMAND_SEMAPHORE_SIGNAL_KHR` | enums.2000 | `cl_command_type` | spec evidence [cl_command_type] G3 new-enums list |
| `CL_COMMAND_SEMAPHORE_WAIT_KHR` | enums.2000 | `cl_command_type` | spec evidence [cl_command_type] G3 new-enums list |
| `CL_COMMAND_SVM_FREE` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_SVM_FREE_ARM` | enums.40B0 | — (ungrouped, GL precedent) |  |
| `CL_COMMAND_SVM_MAP` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_SVM_MAP_ARM` | enums.40B0 | — (ungrouped, GL precedent) |  |
| `CL_COMMAND_SVM_MEMCPY` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_SVM_MEMCPY_ARM` | enums.40B0 | — (ungrouped, GL precedent) |  |
| `CL_COMMAND_SVM_MEMFILL` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_SVM_MEMFILL_ARM` | enums.40B0 | — (ungrouped, GL precedent) |  |
| `CL_COMMAND_SVM_MIGRATE_MEM` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_SVM_UNMAP` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_SVM_UNMAP_ARM` | enums.40B0 | — (ungrouped, GL precedent) |  |
| `CL_COMMAND_TASK` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_TERMINATED_ITSELF_WITH_FAILURE_ARM` | ErrorCodes.1108 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_COMMAND_TERMINATION_COMPLETION_ARM` | cl_command_termination_reason_arm | `cl_command_termination_reason_arm` | R1 C typedef container cl_command_termination_reason_arm (spec-listed) |
| `CL_COMMAND_TERMINATION_CONTROLLED_FAILURE_ARM` | cl_command_termination_reason_arm | `cl_command_termination_reason_arm` | R1 C typedef container cl_command_termination_reason_arm (spec-listed) |
| `CL_COMMAND_TERMINATION_CONTROLLED_SUCCESS_ARM` | cl_command_termination_reason_arm | `cl_command_termination_reason_arm` | R1 C typedef container cl_command_termination_reason_arm (spec-listed) |
| `CL_COMMAND_TERMINATION_ERROR_ARM` | cl_command_termination_reason_arm | `cl_command_termination_reason_arm` | R1 C typedef container cl_command_termination_reason_arm (spec-listed) |
| `CL_COMMAND_UNMAP_MEM_OBJECT` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_USER` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_WRITE_BUFFER` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_WRITE_BUFFER_RECT` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMMAND_WRITE_HOST_PIPE_INTEL` | enums.4210 | `cl_command_type` | manual: cl_intel_program_scope_host_pipe Table 37 event command type (clEnqueueWriteHostPipeINTEL) |
| `CL_COMMAND_WRITE_IMAGE` | cl_device_info | `cl_command_type` | spec evidence [cl_command_type] event-type col1-of-fn (List of supported event command types) |
| `CL_COMPILER_NOT_AVAILABLE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_COMPILE_PROGRAM_FAILURE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_COMPLETE` | clCommandExecutionStatus | `clCommandExecutionStatus` | manual: core command-execution-status value set of clGetEventInfo/CL_EVENT_COMMAND_EXECUTION_STATUS (registry type clCommandExecutionStatus; + cl_img_ |
| `CL_CONTEXT_ADAPTER_D3D9EX_KHR` | enums.2000 | `cl_context_info`, `cl_context_properties` | spec evidence [cl_context_info] G3 new-enums list; spec evidence [cl_context_properties] value cell col0 (List of supported context creation propertie |
| `CL_CONTEXT_ADAPTER_D3D9_KHR` | enums.2000 | `cl_context_info`, `cl_context_properties` | spec evidence [cl_context_info] G3 new-enums list; spec evidence [cl_context_properties] value cell col0 (List of supported context creation propertie |
| `CL_CONTEXT_ADAPTER_DXVA_KHR` | enums.2000 | `cl_context_info`, `cl_context_properties` | spec evidence [cl_context_info] G3 new-enums list; spec evidence [cl_context_properties] value cell col0 (List of supported context creation propertie |
| `CL_CONTEXT_D3D10_DEVICE_KHR` | enums.4010 | `cl_context_properties` | spec evidence [cl_context_properties] G3 new-enums list |
| `CL_CONTEXT_D3D10_PREFER_SHARED_RESOURCES_KHR` | enums.4010 | `cl_context_info` | spec evidence [cl_context_info] G3 new-enums list |
| `CL_CONTEXT_D3D11_DEVICE_KHR` | enums.4010 | `cl_context_properties` | spec evidence [cl_context_properties] G3 new-enums list |
| `CL_CONTEXT_D3D11_PREFER_SHARED_RESOURCES_KHR` | enums.4010 | `cl_context_info` | spec evidence [cl_context_info] G3 new-enums list |
| `CL_CONTEXT_D3D9EX_DEVICE_INTEL` | enums.4070 | — (ungrouped, GL precedent) |  |
| `CL_CONTEXT_D3D9_DEVICE_INTEL` | enums.4010 | — (ungrouped, GL precedent) |  |
| `CL_CONTEXT_DEVICES` | cl_device_info | `cl_context_info` | spec evidence [cl_context_info] value cell col0 (List of supported param_names by {clGetContextInfo) |
| `CL_CONTEXT_DIAGNOSTICS_LEVEL_ALL_INTEL` | cl_diagnostic_verbose_level_intel | `cl_diagnostic_verbose_level_intel` | R1 C typedef container cl_diagnostic_verbose_level_intel (container-declared) |
| `CL_CONTEXT_DIAGNOSTICS_LEVEL_BAD_INTEL` | cl_diagnostic_verbose_level_intel | `cl_diagnostic_verbose_level_intel` | R1 C typedef container cl_diagnostic_verbose_level_intel (container-declared) |
| `CL_CONTEXT_DIAGNOSTICS_LEVEL_GOOD_INTEL` | cl_diagnostic_verbose_level_intel | `cl_diagnostic_verbose_level_intel` | R1 C typedef container cl_diagnostic_verbose_level_intel (container-declared) |
| `CL_CONTEXT_DIAGNOSTICS_LEVEL_NEUTRAL_INTEL` | cl_diagnostic_verbose_level_intel | `cl_diagnostic_verbose_level_intel` | R1 C typedef container cl_diagnostic_verbose_level_intel (container-declared) |
| `CL_CONTEXT_DXVA_DEVICE_INTEL` | enums.4070 | — (ungrouped, GL precedent) |  |
| `CL_CONTEXT_ENHANCED_EVENT_EXECUTION_STATUS_IMG` | cl_context_safety_properties_img | `cl_context_safety_properties_img` | R1 C typedef container cl_context_safety_properties_img (container-declared) |
| `CL_CONTEXT_INTEROP_USER_SYNC` | cl_device_info | `cl_context_properties` | spec evidence [cl_context_properties] value cell col0 (List of supported context creation properties by {) |
| `CL_CONTEXT_MEMORY_INITIALIZE_KHR` | enums.2000 | `cl_context_properties` | spec evidence [cl_context_properties] G3 new-enums list |
| `CL_CONTEXT_MEMORY_INITIALIZE_LOCAL_KHR` | cl_context_memory_initialize_khr | `cl_context_memory_initialize_khr` | R1 C typedef container cl_context_memory_initialize_khr (spec-listed) |
| `CL_CONTEXT_MEMORY_INITIALIZE_PRIVATE_KHR` | cl_context_memory_initialize_khr | `cl_context_memory_initialize_khr` | R1 C typedef container cl_context_memory_initialize_khr (spec-listed) |
| `CL_CONTEXT_NUM_DEVICES` | cl_device_info | `cl_context_info` | spec evidence [cl_context_info] value cell col0 (List of supported param_names by {clGetContextInfo) |
| `CL_CONTEXT_PERF_HINT_QCOM` | enums.40C0 | `cl_context_properties` | manual: extensions/cl_qcom_perf_hint.asciidoc L83-88 'Added to the list of supported properties by clCreateContext' -> creation property / param_name; |
| `CL_CONTEXT_PLATFORM` | cl_device_info | `cl_context_properties` | spec evidence [cl_context_properties] value cell col0 (List of supported context creation properties by {) |
| `CL_CONTEXT_PROPERTIES` | cl_device_info | `cl_context_info` | spec evidence [cl_context_info] value cell col0 (List of supported param_names by {clGetContextInfo) |
| `CL_CONTEXT_REFERENCE_COUNT` | cl_device_info | `cl_context_info` | spec evidence [cl_context_info] value cell col0 (List of supported param_names by {clGetContextInfo) |
| `CL_CONTEXT_SAFETY_PROPERTIES_IMG` | enums.40D0 | `cl_context_safety_properties_img` | spec evidence [cl_context_safety_properties_img] G4 typedef+define |
| `CL_CONTEXT_SHOW_DIAGNOSTICS_INTEL` | enums.4100 | — (ungrouped, GL precedent) |  |
| `CL_CONTEXT_TERMINATED_KHR` | ErrorCodes.1121 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values); spec evidence [ErrorCode] G3 new-error-codes list |
| `CL_CONTEXT_TERMINATE_KHR` | enums.2000 | `cl_context_properties` | spec evidence [cl_context_properties] G3 new-enums list |
| `CL_CONTEXT_VA_API_DISPLAY_INTEL` | enums.4090 | — (ungrouped, GL precedent) |  |
| `CL_CONTEXT_WORKGROUP_PROTECTION_IMG` | cl_context_safety_properties_img | `cl_context_safety_properties_img` | R1 C typedef container cl_context_safety_properties_img (container-declared) |
| `CL_CURRENT_DEVICE_FOR_GL_CONTEXT_KHR` | enums.2000 | `cl_gl_context_info` | spec evidence [cl_gl_context_info] G3 new-enums list |
| `CL_D3D10_DEVICE_KHR` | enums.4010 | `cl_d3d10_device_source_khr` | spec evidence [cl_d3d10_device_source_khr] G3 new-enums list |
| `CL_D3D10_DXGI_ADAPTER_KHR` | enums.4010 | `cl_d3d10_device_source_khr` | spec evidence [cl_d3d10_device_source_khr] G3 new-enums list |
| `CL_D3D10_RESOURCE_ALREADY_ACQUIRED_KHR` | ErrorCodes.1002 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values); spec evidence [ErrorCode] G3 new-error-codes list |
| `CL_D3D10_RESOURCE_NOT_ACQUIRED_KHR` | ErrorCodes.1002 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values); spec evidence [ErrorCode] G3 new-error-codes list |
| `CL_D3D11_DEVICE_KHR` | enums.4010 | `cl_d3d11_device_source_khr` | spec evidence [cl_d3d11_device_source_khr] G3 new-enums list |
| `CL_D3D11_DXGI_ADAPTER_KHR` | enums.4010 | `cl_d3d11_device_source_khr` | spec evidence [cl_d3d11_device_source_khr] G3 new-enums list |
| `CL_D3D11_RESOURCE_ALREADY_ACQUIRED_KHR` | ErrorCodes.1002 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values); spec evidence [ErrorCode] G3 new-error-codes list |
| `CL_D3D11_RESOURCE_NOT_ACQUIRED_KHR` | ErrorCodes.1002 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values); spec evidence [ErrorCode] G3 new-error-codes list |
| `CL_D3D9EX_DEVICE_INTEL` | enums.4070 | — (ungrouped, GL precedent) |  |
| `CL_D3D9_DEVICE_INTEL` | enums.4010 | — (ungrouped, GL precedent) |  |
| `CL_DBL_DIG` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_DBL_EPSILON` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_DBL_MANT_DIG` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_DBL_MAX` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_DBL_MAX_10_EXP` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_DBL_MAX_EXP` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_DBL_MIN` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_DBL_MIN_10_EXP` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_DBL_MIN_EXP` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_DBL_RADIX` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_DEPTH` | cl_device_info | `cl_channel_order` | spec evidence [cl_channel_order] value cell col0 (List of supported Image Channel Order Values) |
| `CL_DEPTH_STENCIL` | cl_device_info | `cl_channel_order` | spec evidence [cl_channel_order] G3 new-enums list |
| `CL_DEVICES_FOR_GL_CONTEXT_KHR` | enums.2000 | `cl_gl_context_info` | spec evidence [cl_gl_context_info] G3 new-enums list |
| `CL_DEVICE_ADDRESS_BITS` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_AFFINITY_DOMAINS_EXT` | enums.4050 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_AFFINITY_DOMAIN_L1_CACHE` | cl_device_affinity_domain | `cl_device_affinity_domain` | R1 C typedef container cl_device_affinity_domain (container-declared) |
| `CL_DEVICE_AFFINITY_DOMAIN_L2_CACHE` | cl_device_affinity_domain | `cl_device_affinity_domain` | R1 C typedef container cl_device_affinity_domain (container-declared) |
| `CL_DEVICE_AFFINITY_DOMAIN_L3_CACHE` | cl_device_affinity_domain | `cl_device_affinity_domain` | R1 C typedef container cl_device_affinity_domain (container-declared) |
| `CL_DEVICE_AFFINITY_DOMAIN_L4_CACHE` | cl_device_affinity_domain | `cl_device_affinity_domain` | R1 C typedef container cl_device_affinity_domain (container-declared) |
| `CL_DEVICE_AFFINITY_DOMAIN_NEXT_PARTITIONABLE` | cl_device_affinity_domain | `cl_device_affinity_domain` | R1 C typedef container cl_device_affinity_domain (container-declared) |
| `CL_DEVICE_AFFINITY_DOMAIN_NUMA` | cl_device_affinity_domain | `cl_device_affinity_domain` | R1 C typedef container cl_device_affinity_domain (container-declared) |
| `CL_DEVICE_ATOMIC_FENCE_CAPABILITIES` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_ATOMIC_MEMORY_CAPABILITIES` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_ATOMIC_ORDER_ACQ_REL` | cl_device_atomic_capabilities | `cl_device_atomic_capabilities` | R1 C typedef container cl_device_atomic_capabilities (container-declared) |
| `CL_DEVICE_ATOMIC_ORDER_RELAXED` | cl_device_atomic_capabilities | `cl_device_atomic_capabilities` | R1 C typedef container cl_device_atomic_capabilities (container-declared) |
| `CL_DEVICE_ATOMIC_ORDER_SEQ_CST` | cl_device_atomic_capabilities | `cl_device_atomic_capabilities` | R1 C typedef container cl_device_atomic_capabilities (container-declared) |
| `CL_DEVICE_ATOMIC_SCOPE_ALL_DEVICES` | cl_device_atomic_capabilities | `cl_device_atomic_capabilities` | R1 C typedef container cl_device_atomic_capabilities (container-declared) |
| `CL_DEVICE_ATOMIC_SCOPE_DEVICE` | cl_device_atomic_capabilities | `cl_device_atomic_capabilities` | R1 C typedef container cl_device_atomic_capabilities (container-declared) |
| `CL_DEVICE_ATOMIC_SCOPE_WORK_GROUP` | cl_device_atomic_capabilities | `cl_device_atomic_capabilities` | R1 C typedef container cl_device_atomic_capabilities (container-declared) |
| `CL_DEVICE_ATOMIC_SCOPE_WORK_ITEM` | cl_device_atomic_capabilities | `cl_device_atomic_capabilities` | R1 C typedef container cl_device_atomic_capabilities (container-declared) |
| `CL_DEVICE_AVAILABLE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_AVAILABLE_ASYNC_QUEUES_AMD` | enums.4040 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_AVC_ME_SUPPORTS_PREEMPTION_INTEL` | enums.4100 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_AVC_ME_SUPPORTS_TEXTURE_SAMPLER_USE_INTEL` | enums.4100 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_AVC_ME_VERSION_INTEL` | enums.4100 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_BOARD_NAME_AMD` | enums.4030 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_BUILT_IN_KERNELS` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_BUILT_IN_KERNELS_WITH_VERSION` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_BUILT_IN_KERNELS_WITH_VERSION_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_COMMAND_BUFFER_CAPABILITIES_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_COMMAND_BUFFER_NUM_SYNC_DEVICES_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_COMMAND_BUFFER_REQUIRED_QUEUE_PROPERTIES_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_COMMAND_BUFFER_SUPPORTED_QUEUE_PROPERTIES_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_COMMAND_BUFFER_SYNC_DEVICES_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_COMPILER_AVAILABLE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_COMPUTE_CAPABILITY_MAJOR_NV` | enums.4000 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_COMPUTE_CAPABILITY_MINOR_NV` | enums.4000 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_COMPUTE_UNITS_BITFIELD_ARM` | enums.40B0 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_CONTROLLED_TERMINATION_CAPABILITIES_ARM` | enums.41E0 | `cl_device_info` | manual: cl_arm_controlled_kernel_termination: param_name of clGetDeviceInfo returning cl_device_controlled_termination_capabilities_arm bitfield |
| `CL_DEVICE_CONTROLLED_TERMINATION_FAILURE_ARM` | cl_device_controlled_termination_capabilities_arm | `cl_device_controlled_termination_capabilities_arm` | R1 C typedef container cl_device_controlled_termination_capabilities_arm (container-declared) |
| `CL_DEVICE_CONTROLLED_TERMINATION_QUERY_ARM` | cl_device_controlled_termination_capabilities_arm | `cl_device_controlled_termination_capabilities_arm` | R1 C typedef container cl_device_controlled_termination_capabilities_arm (container-declared) |
| `CL_DEVICE_CONTROLLED_TERMINATION_SUCCESS_ARM` | cl_device_controlled_termination_capabilities_arm | `cl_device_controlled_termination_capabilities_arm` | R1 C typedef container cl_device_controlled_termination_capabilities_arm (container-declared) |
| `CL_DEVICE_CROSS_DEVICE_SHARED_MEM_CAPABILITIES_INTEL` | enums.4190 | `cl_device_info` | spec evidence [cl_device_info] G4 sentence+define |
| `CL_DEVICE_CXX_FOR_OPENCL_NUMERIC_VERSION_EXT` | enums.4230 | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_DEVICE_ENQUEUE_CAPABILITIES` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_DEVICE_MEM_CAPABILITIES_INTEL` | enums.4190 | `cl_device_info` | spec evidence [cl_device_info] G4 sentence+define |
| `CL_DEVICE_DOUBLE_FP_ATOMIC_CAPABILITIES_EXT` | enums.4230 | `cl_device_info` | spec evidence [cl_device_info] G4 sentence+define |
| `CL_DEVICE_DOUBLE_FP_CONFIG` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_ENDIAN_LITTLE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_ERROR_CORRECTION_SUPPORT` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_EXECUTION_CAPABILITIES` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_EXTENSIONS` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_EXTENSIONS_WITH_VERSION` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_EXTENSIONS_WITH_VERSION_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_EXTERNAL_MEMORY_IMPORT_ASSUME_LINEAR_IMAGES_HANDLE_TYPES_KHR` | enums.2000 | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_EXTERNAL_MEMORY_IMPORT_HANDLE_TYPES_KHR` | enums.2000 | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_EXT_MEM_PADDING_IN_BYTES_QCOM` | enums.40A0 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_FEATURE_CAPABILITIES_INTEL` | enums.4250 | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by clGetDeviceInfo) |
| `CL_DEVICE_FEATURE_FLAG_DP4A_INTEL` | cl_device_feature_capabilities_intel | `cl_device_feature_capabilities_intel` | R1 C typedef container cl_device_feature_capabilities_intel (container-declared) |
| `CL_DEVICE_FEATURE_FLAG_DPAS_INTEL` | cl_device_feature_capabilities_intel | `cl_device_feature_capabilities_intel` | R1 C typedef container cl_device_feature_capabilities_intel (container-declared) |
| `CL_DEVICE_GENERIC_ADDRESS_SPACE_SUPPORT` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_GFXIP_MAJOR_AMD` | enums.4040 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_GFXIP_MINOR_AMD` | enums.4040 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_GLOBAL_FP_ATOMIC_ADD_EXT` | cl_device_fp_atomic_capabilities_ext | `cl_device_fp_atomic_capabilities_ext` | R1 C typedef container cl_device_fp_atomic_capabilities_ext (container-declared) |
| `CL_DEVICE_GLOBAL_FP_ATOMIC_LOAD_STORE_EXT` | cl_device_fp_atomic_capabilities_ext | `cl_device_fp_atomic_capabilities_ext` | R1 C typedef container cl_device_fp_atomic_capabilities_ext (container-declared) |
| `CL_DEVICE_GLOBAL_FP_ATOMIC_MIN_MAX_EXT` | cl_device_fp_atomic_capabilities_ext | `cl_device_fp_atomic_capabilities_ext` | R1 C typedef container cl_device_fp_atomic_capabilities_ext (container-declared) |
| `CL_DEVICE_GLOBAL_FREE_MEMORY_AMD` | enums.4030 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_GLOBAL_MEM_CACHELINE_SIZE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_GLOBAL_MEM_CACHE_SIZE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_GLOBAL_MEM_CACHE_TYPE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_GLOBAL_MEM_CHANNELS_AMD` | enums.4040 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_GLOBAL_MEM_CHANNEL_BANKS_AMD` | enums.4040 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_GLOBAL_MEM_CHANNEL_BANK_WIDTH_AMD` | enums.4040 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_GLOBAL_MEM_SIZE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_GLOBAL_VARIABLE_PREFERRED_TOTAL_SIZE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_GPU_OVERLAP_NV` | enums.4000 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_HALF_FP_ATOMIC_CAPABILITIES_EXT` | enums.4230 | `cl_device_info` | spec evidence [cl_device_info] G4 sentence+define |
| `CL_DEVICE_HALF_FP_CONFIG` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_HOST_MEM_CAPABILITIES_INTEL` | enums.4190 | `cl_device_info` | spec evidence [cl_device_info] G4 sentence+define |
| `CL_DEVICE_HOST_UNIFIED_MEMORY` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_ID_INTEL` | enums.4250 | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by clGetDeviceInfo) |
| `CL_DEVICE_ILS_WITH_VERSION` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_ILS_WITH_VERSION_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_IL_VERSION` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_IL_VERSION_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_IMAGE2D_MAX_HEIGHT` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_IMAGE2D_MAX_WIDTH` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_IMAGE3D_MAX_DEPTH` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_IMAGE3D_MAX_HEIGHT` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_IMAGE3D_MAX_WIDTH` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_IMAGE_BASE_ADDRESS_ALIGNMENT` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_IMAGE_BASE_ADDRESS_ALIGNMENT_KHR` | cl_device_info | `cl_device_info` | manual: cl_khr_image2d_from_buffer New API Enums param_name of clGetDeviceInfo; cl_device_info mega-container token; no spec value-set found — left un |
| `CL_DEVICE_IMAGE_MAX_ARRAY_SIZE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_IMAGE_MAX_BUFFER_SIZE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_IMAGE_PITCH_ALIGNMENT` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_IMAGE_PITCH_ALIGNMENT_KHR` | cl_device_info | `cl_device_info` | manual: cl_khr_image2d_from_buffer New API Enums param_name of clGetDeviceInfo; cl_device_info mega-container token; no spec value-set found — left un |
| `CL_DEVICE_IMAGE_SUPPORT` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_INTEGER_DOT_PRODUCT_ACCELERATION_PROPERTIES_4x8BIT_PACKED` | cl_device_info | `cl_device_info` | manual: core-inherited of _KHR variant; sibling _8BIT_ already cl_device_info; cl_device_info mega-container token; no spec value-set found — left ung |
| `CL_DEVICE_INTEGER_DOT_PRODUCT_ACCELERATION_PROPERTIES_4x8BIT_PACKED_KHR` | cl_device_info | `cl_device_info` | manual: cl_khr_integer_dot_product Table 5 OpenCL Device Queries; sibling _8BIT_ already cl_device_info; cl_device_info mega-container token; no spec  |
| `CL_DEVICE_INTEGER_DOT_PRODUCT_ACCELERATION_PROPERTIES_8BIT` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_INTEGER_DOT_PRODUCT_ACCELERATION_PROPERTIES_8BIT_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_INTEGER_DOT_PRODUCT_CAPABILITIES` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_INTEGER_DOT_PRODUCT_CAPABILITIES_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_INTEGER_DOT_PRODUCT_INPUT_4x8BIT` | cl_device_integer_dot_product_capabilities | `cl_device_integer_dot_product_capabilities` | R1 C typedef container cl_device_integer_dot_product_capabilities (container-declared) |
| `CL_DEVICE_INTEGER_DOT_PRODUCT_INPUT_4x8BIT_KHR` | cl_device_integer_dot_product_capabilities_khr | `cl_device_integer_dot_product_capabilities_khr` | R1 C typedef container cl_device_integer_dot_product_capabilities_khr (container-declared) |
| `CL_DEVICE_INTEGER_DOT_PRODUCT_INPUT_4x8BIT_PACKED` | cl_device_integer_dot_product_capabilities | `cl_device_integer_dot_product_capabilities` | R1 C typedef container cl_device_integer_dot_product_capabilities (container-declared) |
| `CL_DEVICE_INTEGER_DOT_PRODUCT_INPUT_4x8BIT_PACKED_KHR` | cl_device_integer_dot_product_capabilities_khr | `cl_device_integer_dot_product_capabilities_khr` | R1 C typedef container cl_device_integer_dot_product_capabilities_khr (container-declared) |
| `CL_DEVICE_INTEGRATED_MEMORY_NV` | enums.4000 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_IP_VERSION_INTEL` | enums.4250 | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by clGetDeviceInfo) |
| `CL_DEVICE_JOB_SLOTS_ARM` | enums.41E0 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_KERNEL_CLOCK_CAPABILITIES_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_KERNEL_CLOCK_SCOPE_DEVICE_KHR` | cl_device_kernel_clock_capabilities_khr | `cl_device_kernel_clock_capabilities_khr` | R1 C typedef container cl_device_kernel_clock_capabilities_khr (spec-listed) |
| `CL_DEVICE_KERNEL_CLOCK_SCOPE_SUB_GROUP_KHR` | cl_device_kernel_clock_capabilities_khr | `cl_device_kernel_clock_capabilities_khr` | R1 C typedef container cl_device_kernel_clock_capabilities_khr (spec-listed) |
| `CL_DEVICE_KERNEL_CLOCK_SCOPE_WORK_GROUP_KHR` | cl_device_kernel_clock_capabilities_khr | `cl_device_kernel_clock_capabilities_khr` | R1 C typedef container cl_device_kernel_clock_capabilities_khr (spec-listed) |
| `CL_DEVICE_KERNEL_EXEC_TIMEOUT_NV` | enums.4000 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_LATEST_CONFORMANCE_VERSION_PASSED` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_LINKER_AVAILABLE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_LOCAL_FP_ATOMIC_ADD_EXT` | cl_device_fp_atomic_capabilities_ext | `cl_device_fp_atomic_capabilities_ext` | R1 C typedef container cl_device_fp_atomic_capabilities_ext (container-declared) |
| `CL_DEVICE_LOCAL_FP_ATOMIC_LOAD_STORE_EXT` | cl_device_fp_atomic_capabilities_ext | `cl_device_fp_atomic_capabilities_ext` | R1 C typedef container cl_device_fp_atomic_capabilities_ext (container-declared) |
| `CL_DEVICE_LOCAL_FP_ATOMIC_MIN_MAX_EXT` | cl_device_fp_atomic_capabilities_ext | `cl_device_fp_atomic_capabilities_ext` | R1 C typedef container cl_device_fp_atomic_capabilities_ext (container-declared) |
| `CL_DEVICE_LOCAL_MEM_BANKS_AMD` | enums.4040 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_LOCAL_MEM_SIZE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_LOCAL_MEM_SIZE_PER_COMPUTE_UNIT_AMD` | enums.4040 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_LOCAL_MEM_TYPE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_LUID` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_LUID_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_LUID_VALID` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_LUID_VALID_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_MAX_CLOCK_FREQUENCY` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_MAX_COMPUTE_UNITS` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_MAX_CONSTANT_ARGS` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_MAX_CONSTANT_BUFFER_SIZE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_MAX_GLOBAL_VARIABLE_SIZE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_MAX_HOST_READ_PIPES_INTEL` | enums.4210 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_MAX_HOST_WRITE_PIPES_INTEL` | enums.4210 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_MAX_MEM_ALLOC_SIZE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_MAX_NAMED_BARRIER_COUNT_KHR` | enums.2000 | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_MAX_NUM_SUB_GROUPS` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_MAX_ON_DEVICE_EVENTS` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_MAX_ON_DEVICE_QUEUES` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_MAX_PARAMETER_SIZE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_MAX_PIPE_ARGS` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_MAX_READ_IMAGE_ARGS` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_MAX_READ_WRITE_IMAGE_ARGS` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_MAX_SAMPLERS` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_MAX_WARP_COUNT_ARM` | enums.41E0 | `cl_device_info` | manual: cl_arm_scheduling_controls L49-66 param_name of clGetDeviceInfo |
| `CL_DEVICE_MAX_WORK_GROUP_SIZE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_MAX_WORK_GROUP_SIZES` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_MAX_WORK_GROUP_SIZE_AMD` | enums.4030 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_MAX_WORK_ITEM_DIMENSIONS` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_MAX_WORK_ITEM_SIZES` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_MAX_WRITE_IMAGE_ARGS` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_MEMORY_CAPABILITIES_IMG` | enums.40D0 | `cl_device_info` | manual: cl_img_mem_properties 'List of supported param name by clGetDeviceInfo' |
| `CL_DEVICE_MEM_BASE_ADDR_ALIGN` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_ME_VERSION_INTEL` | enums.4070 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_MIN_DATA_TYPE_ALIGN_SIZE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_MUTABLE_DISPATCH_CAPABILITIES_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_NAME` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_NATIVE_VECTOR_WIDTH_CHAR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value chain col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_NATIVE_VECTOR_WIDTH_DOUBLE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value chain col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_NATIVE_VECTOR_WIDTH_FLOAT` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value chain col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_NATIVE_VECTOR_WIDTH_HALF` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value chain col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_NATIVE_VECTOR_WIDTH_INT` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value chain col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_NATIVE_VECTOR_WIDTH_LONG` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value chain col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_NATIVE_VECTOR_WIDTH_SHORT` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value chain col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_NODE_MASK` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_NODE_MASK_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_NON_UNIFORM_WORK_GROUP_SUPPORT` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_NOT_AVAILABLE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_DEVICE_NOT_FOUND` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_DEVICE_NUMERIC_VERSION` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_NUMERIC_VERSION_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_NUM_EUS_PER_SUB_SLICE_INTEL` | enums.4250 | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by clGetDeviceInfo) |
| `CL_DEVICE_NUM_SIMULTANEOUS_INTEROPS_INTEL` | enums.4100 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_NUM_SLICES_INTEL` | enums.4250 | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by clGetDeviceInfo) |
| `CL_DEVICE_NUM_SUB_SLICES_PER_SLICE_INTEL` | enums.4250 | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by clGetDeviceInfo) |
| `CL_DEVICE_NUM_THREADS_PER_EU_INTEL` | enums.4250 | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by clGetDeviceInfo) |
| `CL_DEVICE_OPENCL_C_ALL_VERSIONS` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_OPENCL_C_FEATURES` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_OPENCL_C_NUMERIC_VERSION_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_OPENCL_C_VERSION` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PAGE_SIZE_QCOM` | enums.40A0 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_PARENT_DEVICE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PARENT_DEVICE_EXT` | enums.4050 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_PARTITION_AFFINITY_DOMAIN` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PARTITION_BY_AFFINITY_DOMAIN` | cl_device_info | `cl_device_partition_property` | spec evidence [cl_device_partition_property] value cell col0 (List of supported partition schemes by {clCreateSu) |
| `CL_DEVICE_PARTITION_BY_AFFINITY_DOMAIN_EXT` | enums.4050 | `cl_device_partition_property` | manual: legacy alias of CL_DEVICE_PARTITION_BY_AFFINITY_DOMAIN (cl_ext_device_fission; core member already cl_device_partition_property) |
| `CL_DEVICE_PARTITION_BY_COUNTS` | cl_device_info | `cl_device_partition_property` | spec evidence [cl_device_partition_property] value cell col0 (List of supported partition schemes by {clCreateSu) |
| `CL_DEVICE_PARTITION_BY_COUNTS_EXT` | enums.4050 | `cl_device_partition_property` | manual: legacy alias of CL_DEVICE_PARTITION_BY_COUNTS (cl_ext_device_fission; core member already cl_device_partition_property) |
| `CL_DEVICE_PARTITION_BY_COUNTS_LIST_END` | MiscNumbers | `cl_device_partition_property` | manual: core spec: list terminator for cl_device_partition_property (CL_DEVICE_PARTITION_BY_COUNTS_EXT) |
| `CL_DEVICE_PARTITION_BY_NAMES_EXT` | enums.4050 | `cl_device_partition_property` | manual: legacy alias of CL_DEVICE_PARTITION_BY_NAMES (cl_ext_device_fission) |
| `CL_DEVICE_PARTITION_BY_NAMES_INTEL` | enums.4050 | `cl_device_partition_property` | manual: legacy alias of CL_DEVICE_PARTITION_BY_NAMES (cl_intel_device_partition_by_names; same value 0x4052) |
| `CL_DEVICE_PARTITION_EQUALLY` | cl_device_info | `cl_device_partition_property` | spec evidence [cl_device_partition_property] value cell col0 (List of supported partition schemes by {clCreateSu) |
| `CL_DEVICE_PARTITION_EQUALLY_EXT` | enums.4050 | `cl_device_partition_property` | manual: legacy alias of CL_DEVICE_PARTITION_EQUALLY (cl_ext_device_fission; core member already cl_device_partition_property) |
| `CL_DEVICE_PARTITION_FAILED` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_DEVICE_PARTITION_FAILED_EXT` | ErrorCodes.1057 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_DEVICE_PARTITION_MAX_SUB_DEVICES` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PARTITION_PROPERTIES` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PARTITION_STYLE_EXT` | enums.4050 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_PARTITION_TYPE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PARTITION_TYPES_EXT` | enums.4050 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_PCIE_ID_AMD` | enums.4030 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_PCI_BUS_INFO_KHR` | enums.4100 | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_PIPE_MAX_ACTIVE_RESERVATIONS` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PIPE_MAX_PACKET_SIZE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PIPE_SUPPORT` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PLANAR_YUV_MAX_HEIGHT_INTEL` | enums.4170 | `cl_device_info` | spec evidence [cl_device_info] G4 sentence+define |
| `CL_DEVICE_PLANAR_YUV_MAX_WIDTH_INTEL` | enums.4170 | `cl_device_info` | spec evidence [cl_device_info] G4 sentence+define |
| `CL_DEVICE_PLATFORM` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PREFERRED_CONSTANT_BUFFER_SIZE_AMD` | enums.4030 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_PREFERRED_GLOBAL_ATOMIC_ALIGNMENT` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PREFERRED_INTEROP_USER_SYNC` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PREFERRED_LOCAL_ATOMIC_ALIGNMENT` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PREFERRED_PLATFORM_ATOMIC_ALIGNMENT` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PREFERRED_VECTOR_WIDTH_CHAR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value chain col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PREFERRED_VECTOR_WIDTH_DOUBLE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value chain col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PREFERRED_VECTOR_WIDTH_FLOAT` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value chain col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PREFERRED_VECTOR_WIDTH_HALF` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value chain col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PREFERRED_VECTOR_WIDTH_INT` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value chain col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PREFERRED_VECTOR_WIDTH_LONG` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value chain col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PREFERRED_VECTOR_WIDTH_SHORT` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value chain col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PREFERRED_WORK_GROUP_SIZE_AMD` | enums.4030 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_PREFERRED_WORK_GROUP_SIZE_MULTIPLE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PRINTF_BUFFER_SIZE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PROFILE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_PROFILING_TIMER_OFFSET_AMD` | enums.4030 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_PROFILING_TIMER_RESOLUTION` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_QUEUE_FAMILY_PROPERTIES_INTEL` | enums.4180 | `cl_device_info` | spec evidence [cl_device_info] G4 sentence+define |
| `CL_DEVICE_QUEUE_ON_DEVICE_MAX_SIZE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_QUEUE_ON_DEVICE_PREFERRED_SIZE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_QUEUE_ON_DEVICE_PROPERTIES` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_QUEUE_ON_HOST_PROPERTIES` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_QUEUE_PROPERTIES` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_QUEUE_REPLACEABLE_DEFAULT` | cl_device_device_enqueue_capabilities | `cl_device_device_enqueue_capabilities` | R1 C typedef container cl_device_device_enqueue_capabilities (container-declared) |
| `CL_DEVICE_QUEUE_SUPPORTED` | cl_device_device_enqueue_capabilities | `cl_device_device_enqueue_capabilities` | R1 C typedef container cl_device_device_enqueue_capabilities (container-declared) |
| `CL_DEVICE_REFERENCE_COUNT` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_REFERENCE_COUNT_EXT` | enums.4050 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_REGISTERS_PER_BLOCK_NV` | enums.4000 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_SAFETY_MEM_SIZE_IMG` | enums.40D0 | `cl_device_info` | manual: cl_img_safety_mechanisms L80-85 + Table 5 param_names of clGetDeviceInfo |
| `CL_DEVICE_SCHEDULING_COMPUTE_UNIT_BATCH_QUEUE_SIZE_ARM` | cl_device_scheduling_controls_capabilities_arm | `cl_device_scheduling_controls_capabilities_arm` | R1 C typedef container cl_device_scheduling_controls_capabilities_arm (container-declared) |
| `CL_DEVICE_SCHEDULING_COMPUTE_UNIT_LIMIT_ARM` | cl_device_scheduling_controls_capabilities_arm | `cl_device_scheduling_controls_capabilities_arm` | R1 C typedef container cl_device_scheduling_controls_capabilities_arm (container-declared) |
| `CL_DEVICE_SCHEDULING_CONTROLS_CAPABILITIES_ARM` | enums.41E0 | `cl_device_info` | manual: cl_arm_scheduling_controls L49-66 param_name of clGetDeviceInfo |
| `CL_DEVICE_SCHEDULING_CONTROLS_CAPABILITIES_IMG` | enums.4220 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_SCHEDULING_DEFERRED_FLUSH_ARM` | cl_device_scheduling_controls_capabilities_arm | `cl_device_scheduling_controls_capabilities_arm` | R1 C typedef container cl_device_scheduling_controls_capabilities_arm (container-declared) |
| `CL_DEVICE_SCHEDULING_KERNEL_BATCHING_ARM` | cl_device_scheduling_controls_capabilities_arm | `cl_device_scheduling_controls_capabilities_arm` | R1 C typedef container cl_device_scheduling_controls_capabilities_arm (container-declared) |
| `CL_DEVICE_SCHEDULING_REGISTER_ALLOCATION_ARM` | cl_device_scheduling_controls_capabilities_arm | `cl_device_scheduling_controls_capabilities_arm` | R1 C typedef container cl_device_scheduling_controls_capabilities_arm (container-declared) |
| `CL_DEVICE_SCHEDULING_WARP_THROTTLING_ARM` | cl_device_scheduling_controls_capabilities_arm | `cl_device_scheduling_controls_capabilities_arm` | R1 C typedef container cl_device_scheduling_controls_capabilities_arm (container-declared) |
| `CL_DEVICE_SCHEDULING_WORKGROUP_BATCH_SIZE_ARM` | cl_device_scheduling_controls_capabilities_arm | `cl_device_scheduling_controls_capabilities_arm` | R1 C typedef container cl_device_scheduling_controls_capabilities_arm (container-declared) |
| `CL_DEVICE_SCHEDULING_WORKGROUP_BATCH_SIZE_MODIFIER_ARM` | cl_device_scheduling_controls_capabilities_arm | `cl_device_scheduling_controls_capabilities_arm` | R1 C typedef container cl_device_scheduling_controls_capabilities_arm (container-declared) |
| `CL_DEVICE_SEMAPHORE_EXPORT_HANDLE_TYPES_KHR` | enums.2000 | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_SEMAPHORE_IMPORT_HANDLE_TYPES_KHR` | enums.2000 | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_SEMAPHORE_TYPES_KHR` | enums.2000 | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_SHARED_SYSTEM_MEM_CAPABILITIES_INTEL` | enums.4190 | `cl_device_info` | spec evidence [cl_device_info] G4 sentence+define |
| `CL_DEVICE_SIMD_INSTRUCTION_WIDTH_AMD` | enums.4040 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_SIMD_PER_COMPUTE_UNIT_AMD` | enums.4040 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_SIMD_WIDTH_AMD` | enums.4040 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_SIMULTANEOUS_INTEROPS_INTEL` | enums.4100 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_SINGLE_DEVICE_SHARED_MEM_CAPABILITIES_INTEL` | enums.4190 | `cl_device_info` | spec evidence [cl_device_info] G4 sentence+define |
| `CL_DEVICE_SINGLE_FP_ATOMIC_CAPABILITIES_EXT` | enums.4230 | `cl_device_info` | spec evidence [cl_device_info] G4 sentence+define |
| `CL_DEVICE_SINGLE_FP_CONFIG` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_SPIRV_CAPABILITIES` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_SPIRV_CAPABILITIES_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_SPIRV_EXTENDED_INSTRUCTION_SETS` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_SPIRV_EXTENDED_INSTRUCTION_SETS_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_SPIRV_EXTENSIONS` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_SPIRV_EXTENSIONS_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_SPIR_VERSIONS` | enums.40E0 | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_SUB_GROUP_INDEPENDENT_FORWARD_PROGRESS` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_SUB_GROUP_SIZES_INTEL` | enums.4100 | `cl_device_info` | manual: cl_intel_required_subgroup_size L102-112 Additions to Table 4.3 cl_device_info |
| `CL_DEVICE_SUPPORTED_REGISTER_ALLOCATIONS_ARM` | enums.41E0 | `cl_device_info` | manual: cl_arm_scheduling_controls L49-66 param_name of clGetDeviceInfo |
| `CL_DEVICE_SVM_ATOMICS` | cl_device_svm_capabilities | `cl_device_svm_capabilities` | R1 C typedef container cl_device_svm_capabilities (container-declared) |
| `CL_DEVICE_SVM_ATOMICS_ARM` | cl_arm_device_svm_capabilities.flags | `cl_arm_device_svm_capabilities.flags` | R1 C typedef container cl_arm_device_svm_capabilities.flags (container-declared) |
| `CL_DEVICE_SVM_CAPABILITIES` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_SVM_CAPABILITIES_ARM` | enums.40B0 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_SVM_COARSE_GRAIN_BUFFER` | cl_device_svm_capabilities | `cl_device_svm_capabilities` | R1 C typedef container cl_device_svm_capabilities (container-declared) |
| `CL_DEVICE_SVM_COARSE_GRAIN_BUFFER_ARM` | cl_arm_device_svm_capabilities.flags | `cl_arm_device_svm_capabilities.flags` | R1 C typedef container cl_arm_device_svm_capabilities.flags (container-declared) |
| `CL_DEVICE_SVM_FINE_GRAIN_BUFFER` | cl_device_svm_capabilities | `cl_device_svm_capabilities` | R1 C typedef container cl_device_svm_capabilities (container-declared) |
| `CL_DEVICE_SVM_FINE_GRAIN_BUFFER_ARM` | cl_arm_device_svm_capabilities.flags | `cl_arm_device_svm_capabilities.flags` | R1 C typedef container cl_arm_device_svm_capabilities.flags (container-declared) |
| `CL_DEVICE_SVM_FINE_GRAIN_SYSTEM` | cl_device_svm_capabilities | `cl_device_svm_capabilities` | R1 C typedef container cl_device_svm_capabilities (container-declared) |
| `CL_DEVICE_SVM_FINE_GRAIN_SYSTEM_ARM` | cl_arm_device_svm_capabilities.flags | `cl_arm_device_svm_capabilities.flags` | R1 C typedef container cl_arm_device_svm_capabilities.flags (container-declared) |
| `CL_DEVICE_SVM_TYPE_CAPABILITIES_KHR` | cl_device_info | `cl_device_info` | manual: cl_khr_unified_svm param_name of clGetDeviceInfo; cl_device_info mega-container token; no spec value-set found — left ungrouped |
| `CL_DEVICE_TERMINATE_CAPABILITY_CONTEXT_KHR` | cl_device_terminate_capability_khr | `cl_device_terminate_capability_khr` | R1 C typedef container cl_device_terminate_capability_khr (spec-listed) |
| `CL_DEVICE_TERMINATE_CAPABILITY_KHR` | enums.2000 | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_THREAD_TRACE_SUPPORTED_AMD` | enums.4040 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_TOPOLOGY_AMD` | enums.4030 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_TYPE` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_TYPE_ACCELERATOR` | cl_device_type | `cl_device_type` | R1 C typedef container cl_device_type (spec-listed) |
| `CL_DEVICE_TYPE_ALL` | cl_device_type | `cl_device_type` | R1 C typedef container cl_device_type (spec-listed) |
| `CL_DEVICE_TYPE_CPU` | cl_device_type | `cl_device_type` | R1 C typedef container cl_device_type (spec-listed) |
| `CL_DEVICE_TYPE_CUSTOM` | cl_device_type | `cl_device_type` | R1 C typedef container cl_device_type (spec-listed) |
| `CL_DEVICE_TYPE_DEFAULT` | cl_device_type | `cl_device_type` | R1 C typedef container cl_device_type (spec-listed) |
| `CL_DEVICE_TYPE_GPU` | cl_device_type | `cl_device_type` | R1 C typedef container cl_device_type (spec-listed) |
| `CL_DEVICE_TYPE_RESERVED0_QCOM` | cl_device_type | `cl_device_type` | R1 C typedef container cl_device_type (container-declared) |
| `CL_DEVICE_UUID` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_UUID_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DEVICE_VENDOR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_VENDOR_ID` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_VERSION` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_WARP_SIZE_NV` | enums.4000 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_WAVEFRONT_WIDTH_AMD` | enums.4040 | — (ungrouped, GL precedent) |  |
| `CL_DEVICE_WORKGROUP_PROTECTION_DEVICE_ENQUEUE_CAPABILITIES_IMG` | enums.40D0 | `cl_device_info` | manual: cl_img_safety_mechanisms L80-85 + Table 5 param_names of clGetDeviceInfo |
| `CL_DEVICE_WORKGROUP_PROTECTION_SVM_CAPABILITIES_IMG` | enums.40D0 | `cl_device_info` | manual: cl_img_safety_mechanisms L80-85 + Table 5 param_names of clGetDeviceInfo |
| `CL_DEVICE_WORK_GROUP_ARBITRATION_ALGORITHM_ROUND_ROBIN_IMG` | cl_device_scheduling_controls_capabilities_img | `cl_device_scheduling_controls_capabilities_img` | R1 C typedef container cl_device_scheduling_controls_capabilities_img (container-declared) |
| `CL_DEVICE_WORK_GROUP_ARBITRATION_ALGORITHM_TASK_DEMAND_IMG` | cl_device_scheduling_controls_capabilities_img | `cl_device_scheduling_controls_capabilities_img` | R1 C typedef container cl_device_scheduling_controls_capabilities_img (container-declared) |
| `CL_DEVICE_WORK_GROUP_COLLECTIVE_FUNCTIONS_SUPPORT` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DEVICE_WORK_GROUP_EXECUTE_COUNT_IMG` | cl_device_scheduling_controls_capabilities_img | `cl_device_scheduling_controls_capabilities_img` | R1 C typedef container cl_device_scheduling_controls_capabilities_img (container-declared) |
| `CL_DEVICE_WORK_GROUP_SCHEDULING_ALGORITHM_LINEAR_ORDER_IMG` | cl_device_scheduling_controls_capabilities_img | `cl_device_scheduling_controls_capabilities_img` | R1 C typedef container cl_device_scheduling_controls_capabilities_img (container-declared) |
| `CL_DEVICE_WORK_GROUP_SCHEDULING_ALGORITHM_MORTON_ORDER_IMG` | cl_device_scheduling_controls_capabilities_img | `cl_device_scheduling_controls_capabilities_img` | R1 C typedef container cl_device_scheduling_controls_capabilities_img (container-declared) |
| `CL_DEVICE_WORK_GROUP_SCHEDULING_ALGORITHM_THREED_MORTON_ORDER_IMG` | cl_device_scheduling_controls_capabilities_img | `cl_device_scheduling_controls_capabilities_img` | R1 C typedef container cl_device_scheduling_controls_capabilities_img (container-declared) |
| `CL_DEVICE_WORK_GROUP_SCHEDULING_ALGORITHM_TWOD_MORTON_ORDER_IMG` | cl_device_scheduling_controls_capabilities_img | `cl_device_scheduling_controls_capabilities_img` | R1 C typedef container cl_device_scheduling_controls_capabilities_img (container-declared) |
| `CL_DRIVER_UUID` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DRIVER_UUID_KHR` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] G3 new-enums list |
| `CL_DRIVER_VERSION` | cl_device_info | `cl_device_info` | spec evidence [cl_device_info] value cell col0 (List of supported param_names by {clGetDeviceInfo}) |
| `CL_DX9_MEDIA_SURFACE_ALREADY_ACQUIRED_KHR` | ErrorCodes.1002 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values); spec evidence [ErrorCode] G3 new-error-codes list |
| `CL_DX9_MEDIA_SURFACE_NOT_ACQUIRED_KHR` | ErrorCodes.1002 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values); spec evidence [ErrorCode] G3 new-error-codes list |
| `CL_DX9_RESOURCE_ALREADY_ACQUIRED_INTEL` | ErrorCodes.1002 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_DX9_RESOURCE_NOT_ACQUIRED_INTEL` | ErrorCodes.1002 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_DXVA_DEVICE_INTEL` | enums.4070 | — (ungrouped, GL precedent) |  |
| `CL_ECC_RECOVERED_IMG` | enums.40D0 | `clCommandExecutionStatus` | manual: core command-execution-status value set of clGetEventInfo/CL_EVENT_COMMAND_EXECUTION_STATUS (registry type clCommandExecutionStatus; + cl_img_ |
| `CL_ECC_UNRECOVERED_IMG` | ErrorCodes.1122 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_EGL_DISPLAY_KHR` | enums.2000 | `cl_context_properties` | spec evidence [cl_context_properties] G3 new-enums list |
| `CL_EGL_RESOURCE_NOT_ACQUIRED_KHR` | ErrorCodes.1092 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values); spec evidence [ErrorCode] G3 new-error-codes list |
| `CL_EGL_YUV_PLANE_INTEL` | enums.4100 | — (ungrouped, GL precedent) |  |
| `CL_ERROR_RESERVED0_IMG` | ErrorCodes.1122 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_ERROR_RESERVED1_IMG` | ErrorCodes.1122 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_ERROR_RESERVED2_IMG` | ErrorCodes.1122 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_ERROR_RESERVED3_IMG` | ErrorCodes.1122 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_EVENT_COMMAND_EXECUTION_STATUS` | cl_device_info | `cl_event_info` | spec evidence [cl_event_info] value cell col0 (List of supported param_names by {clGetEventInfo}) |
| `CL_EVENT_COMMAND_QUEUE` | cl_device_info | `cl_event_info` | spec evidence [cl_event_info] value cell col0 (List of supported param_names by {clGetEventInfo}) |
| `CL_EVENT_COMMAND_TERMINATION_REASON_ARM` | enums.41E0 | `cl_event_info` | manual: cl_arm_controlled_kernel_termination param_name of clGetEventInfo (query key, not a bit value) |
| `CL_EVENT_COMMAND_TYPE` | cl_device_info | `cl_event_info` | spec evidence [cl_event_info] value cell col0 (List of supported param_names by {clGetEventInfo}) |
| `CL_EVENT_CONTEXT` | cl_device_info | `cl_event_info` | spec evidence [cl_event_info] value cell col0 (List of supported param_names by {clGetEventInfo}) |
| `CL_EVENT_REFERENCE_COUNT` | cl_device_info | `cl_event_info` | spec evidence [cl_event_info] value cell col0 (List of supported param_names by {clGetEventInfo}) |
| `CL_EXEC_KERNEL` | cl_device_exec_capabilities | `cl_device_exec_capabilities` | R1 C typedef container cl_device_exec_capabilities (container-declared) |
| `CL_EXEC_NATIVE_KERNEL` | cl_device_exec_capabilities | `cl_device_exec_capabilities` | R1 C typedef container cl_device_exec_capabilities (container-declared) |
| `CL_EXEC_STATUS_ERROR_FOR_EVENTS_IN_WAIT_LIST` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_EXTERNAL_MEMORY_HANDLE_ANDROID_HARDWARE_BUFFER_KHR` | enums.2000 | `cl_external_memory_handle_type_khr` | spec evidence [cl_external_memory_handle_type_khr] G3 new-enums list |
| `CL_EXTERNAL_MEMORY_HANDLE_DMA_BUF_KHR` | enums.2000 | `cl_external_memory_handle_type_khr` | spec evidence [cl_external_memory_handle_type_khr] G3 new-enums list |
| `CL_EXTERNAL_MEMORY_HANDLE_OPAQUE_FD_KHR` | enums.2000 | `cl_external_memory_handle_type_khr` | spec evidence [cl_external_memory_handle_type_khr] G3 new-enums list |
| `CL_EXTERNAL_MEMORY_HANDLE_OPAQUE_WIN32_KHR` | enums.2000 | `cl_external_memory_handle_type_khr` | spec evidence [cl_external_memory_handle_type_khr] G3 new-enums list |
| `CL_EXTERNAL_MEMORY_HANDLE_OPAQUE_WIN32_KMT_KHR` | enums.2000 | `cl_external_memory_handle_type_khr` | spec evidence [cl_external_memory_handle_type_khr] G3 new-enums list |
| `CL_EXTERNAL_MEMORY_HANDLE_OPAQUE_WIN32_NAME_KHR` | enums.2000 | `cl_external_memory_handle_type_khr` | spec evidence [cl_external_memory_handle_type_khr] G3 new-enums list |
| `CL_FALSE` | cl_bool | `cl_bool` | R1 C typedef container cl_bool (container-declared) |
| `CL_FILTER_LINEAR` | cl_device_info | `cl_filter_mode` | spec evidence [cl_filter_mode] inline value-set of cl_filter_mode (row {CL_SAMPLER_FILTER_MODE_anchor}) |
| `CL_FILTER_NEAREST` | cl_device_info | `cl_filter_mode` | spec evidence [cl_filter_mode] inline value-set of cl_filter_mode (row {CL_SAMPLER_FILTER_MODE_anchor}) |
| `CL_FLOAT` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_FLT_DIG` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_FLT_EPSILON` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_FLT_MANT_DIG` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_FLT_MAX` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_FLT_MAX_10_EXP` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_FLT_MAX_EXP` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_FLT_MIN` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_FLT_MIN_10_EXP` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_FLT_MIN_EXP` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_FLT_RADIX` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_FP_CORRECTLY_ROUNDED_DIVIDE_SQRT` | cl_device_fp_config | `cl_device_fp_config` | R1 C typedef container cl_device_fp_config (container-declared) |
| `CL_FP_DENORM` | cl_device_fp_config | `cl_device_fp_config` | R1 C typedef container cl_device_fp_config (container-declared) |
| `CL_FP_FMA` | cl_device_fp_config | `cl_device_fp_config` | R1 C typedef container cl_device_fp_config (container-declared) |
| `CL_FP_INF_NAN` | cl_device_fp_config | `cl_device_fp_config` | R1 C typedef container cl_device_fp_config (container-declared) |
| `CL_FP_ROUND_TO_INF` | cl_device_fp_config | `cl_device_fp_config` | R1 C typedef container cl_device_fp_config (container-declared) |
| `CL_FP_ROUND_TO_NEAREST` | cl_device_fp_config | `cl_device_fp_config` | R1 C typedef container cl_device_fp_config (container-declared) |
| `CL_FP_ROUND_TO_ZERO` | cl_device_fp_config | `cl_device_fp_config` | R1 C typedef container cl_device_fp_config (container-declared) |
| `CL_FP_SOFT_FLOAT` | cl_device_fp_config | `cl_device_fp_config` | R1 C typedef container cl_device_fp_config (container-declared) |
| `CL_GENERAL_FAULT_IMG` | ErrorCodes.1122 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_GLOBAL` | cl_device_local_mem_type | `cl_device_local_mem_type` | R1 C typedef container cl_device_local_mem_type (container-declared) |
| `CL_GLX_DISPLAY_KHR` | enums.2000 | `cl_context_properties` | spec evidence [cl_context_properties] G3 new-enums list |
| `CL_GL_CONTEXT_KHR` | enums.2000 | `cl_context_properties` | spec evidence [cl_context_properties] G3 new-enums list |
| `CL_GL_MIPMAP_LEVEL` | enums.2000 | `cl_gl_texture_info` | spec evidence [cl_gl_texture_info] G3 new-enums list |
| `CL_GL_NUM_SAMPLES` | enums.2000 | `cl_gl_texture_info` | spec evidence [cl_gl_texture_info] G3 new-enums list |
| `CL_GL_OBJECT_BUFFER` | enums.2000 | `cl_gl_object_type` | spec evidence [cl_gl_object_type] G3 new-enums list |
| `CL_GL_OBJECT_RENDERBUFFER` | enums.2000 | `cl_gl_object_type` | spec evidence [cl_gl_object_type] G3 new-enums list |
| `CL_GL_OBJECT_TEXTURE1D` | enums.2000 | `cl_gl_object_type` | spec evidence [cl_gl_object_type] G3 new-enums list |
| `CL_GL_OBJECT_TEXTURE1D_ARRAY` | enums.2000 | `cl_gl_object_type` | spec evidence [cl_gl_object_type] G3 new-enums list |
| `CL_GL_OBJECT_TEXTURE2D` | enums.2000 | `cl_gl_object_type` | spec evidence [cl_gl_object_type] G3 new-enums list |
| `CL_GL_OBJECT_TEXTURE2D_ARRAY` | enums.2000 | `cl_gl_object_type` | spec evidence [cl_gl_object_type] G3 new-enums list |
| `CL_GL_OBJECT_TEXTURE3D` | enums.2000 | `cl_gl_object_type` | spec evidence [cl_gl_object_type] G3 new-enums list |
| `CL_GL_OBJECT_TEXTURE_BUFFER` | enums.2000 | `cl_gl_object_type` | spec evidence [cl_gl_object_type] G3 new-enums list |
| `CL_GL_TEXTURE_TARGET` | enums.2000 | `cl_gl_texture_info` | spec evidence [cl_gl_texture_info] G3 new-enums list |
| `CL_GRALLOC_RESOURCE_NOT_ACQUIRED_IMG` | enums.40D0 | `ErrorCode` | manual: cl_img_use_gralloc_ptr error return code |
| `CL_HALF_DIG` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_HALF_EPSILON` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_HALF_FLOAT` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_HALF_MANT_DIG` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_HALF_MAX` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_HALF_MAX_10_EXP` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_HALF_MAX_EXP` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_HALF_MIN` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_HALF_MIN_10_EXP` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_HALF_MIN_EXP` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_HALF_RADIX` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_HUGE_VAL` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_HUGE_VALF` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_ICDL_NAME` | cl_icdl_info | `cl_icdl_info` | R1 C typedef container cl_icdl_info (spec-listed) |
| `CL_ICDL_OCL_VERSION` | cl_icdl_info | `cl_icdl_info` | R1 C typedef container cl_icdl_info (spec-listed) |
| `CL_ICDL_VENDOR` | cl_icdl_info | `cl_icdl_info` | R1 C typedef container cl_icdl_info (spec-listed) |
| `CL_ICDL_VERSION` | cl_icdl_info | `cl_icdl_info` | R1 C typedef container cl_icdl_info (spec-listed) |
| `CL_IMAGE_ARRAY_SIZE` | cl_device_info | `cl_image_info` | spec evidence [cl_image_info] value cell col0 (List of supported param_names by {clGetImageInfo}) |
| `CL_IMAGE_BUFFER` | cl_device_info | `cl_image_info` | spec evidence [cl_image_info] value cell col0 (List of supported param_names by {clGetImageInfo}) |
| `CL_IMAGE_D3D10_SUBRESOURCE_KHR` | enums.4010 | `cl_image_info` | spec evidence [cl_image_info] G3 new-enums list |
| `CL_IMAGE_D3D11_SUBRESOURCE_KHR` | enums.4010 | `cl_image_info` | spec evidence [cl_image_info] G3 new-enums list |
| `CL_IMAGE_DEPTH` | cl_device_info | `cl_image_info` | spec evidence [cl_image_info] value cell col0 (List of supported param_names by {clGetImageInfo}) |
| `CL_IMAGE_DX9_MEDIA_PLANE_KHR` | enums.2000 | `cl_image_info` | spec evidence [cl_image_info] G3 new-enums list |
| `CL_IMAGE_DX9_PLANE_INTEL` | enums.4070 | — (ungrouped, GL precedent) |  |
| `CL_IMAGE_ELEMENT_SIZE` | cl_device_info | `cl_image_info` | spec evidence [cl_image_info] value cell col0 (List of supported param_names by {clGetImageInfo}) |
| `CL_IMAGE_FORMAT` | cl_device_info | `cl_image_info` | spec evidence [cl_image_info] value cell col0 (List of supported param_names by {clGetImageInfo}) |
| `CL_IMAGE_FORMAT_MISMATCH` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_IMAGE_FORMAT_NOT_SUPPORTED` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_IMAGE_HEIGHT` | cl_device_info | `cl_image_info` | spec evidence [cl_image_info] value cell col0 (List of supported param_names by {clGetImageInfo}) |
| `CL_IMAGE_NUM_MIP_LEVELS` | cl_device_info | `cl_image_info` | spec evidence [cl_image_info] value cell col0 (List of supported param_names by {clGetImageInfo}) |
| `CL_IMAGE_NUM_SAMPLES` | cl_device_info | `cl_image_info` | spec evidence [cl_image_info] value cell col0 (List of supported param_names by {clGetImageInfo}) |
| `CL_IMAGE_REQUIREMENTS_BASE_ADDRESS_ALIGNMENT_EXT` | cl_device_info | `cl_image_requirements_info_ext` | spec evidence [cl_image_requirements_info_ext] value cell col0 (List of supported param_names by {clGetImageRequir) |
| `CL_IMAGE_REQUIREMENTS_MAX_ARRAY_SIZE_EXT` | cl_device_info | `cl_image_requirements_info_ext` | spec evidence [cl_image_requirements_info_ext] value cell col0 (List of supported param_names by {clGetImageRequir) |
| `CL_IMAGE_REQUIREMENTS_MAX_DEPTH_EXT` | cl_device_info | `cl_image_requirements_info_ext` | spec evidence [cl_image_requirements_info_ext] value cell col0 (List of supported param_names by {clGetImageRequir) |
| `CL_IMAGE_REQUIREMENTS_MAX_HEIGHT_EXT` | cl_device_info | `cl_image_requirements_info_ext` | spec evidence [cl_image_requirements_info_ext] value cell col0 (List of supported param_names by {clGetImageRequir) |
| `CL_IMAGE_REQUIREMENTS_MAX_WIDTH_EXT` | cl_device_info | `cl_image_requirements_info_ext` | spec evidence [cl_image_requirements_info_ext] value cell col0 (List of supported param_names by {clGetImageRequir) |
| `CL_IMAGE_REQUIREMENTS_ROW_PITCH_ALIGNMENT_EXT` | cl_device_info | `cl_image_requirements_info_ext` | spec evidence [cl_image_requirements_info_ext] value cell col0 (List of supported param_names by {clGetImageRequir) |
| `CL_IMAGE_REQUIREMENTS_SIZE_EXT` | cl_device_info | `cl_image_requirements_info_ext` | spec evidence [cl_image_requirements_info_ext] value cell col0 (List of supported param_names by {clGetImageRequir) |
| `CL_IMAGE_REQUIREMENTS_SLICE_PITCH_ALIGNMENT_EXT` | cl_device_info | `cl_image_requirements_info_ext` | spec evidence [cl_image_requirements_info_ext] value cell col0 (List of supported param_names by {clGetImageRequir) |
| `CL_IMAGE_ROW_ALIGNMENT_QCOM` | enums.40A0 | — (ungrouped, GL precedent) |  |
| `CL_IMAGE_ROW_PITCH` | cl_device_info | `cl_image_info` | spec evidence [cl_image_info] value cell col0 (List of supported param_names by {clGetImageInfo}) |
| `CL_IMAGE_SLICE_ALIGNMENT_QCOM` | enums.40A0 | — (ungrouped, GL precedent) |  |
| `CL_IMAGE_SLICE_PITCH` | cl_device_info | `cl_image_info` | spec evidence [cl_image_info] value cell col0 (List of supported param_names by {clGetImageInfo}) |
| `CL_IMAGE_VA_API_PLANE_INTEL` | enums.4090 | — (ungrouped, GL precedent) |  |
| `CL_IMAGE_WIDTH` | cl_device_info | `cl_image_info` | spec evidence [cl_image_info] value cell col0 (List of supported param_names by {clGetImageInfo}) |
| `CL_IMPORT_ANDROID_HARDWARE_BUFFER_LAYER_INDEX_ARM` | enums.41E0 | — (ungrouped, GL precedent) |  |
| `CL_IMPORT_ANDROID_HARDWARE_BUFFER_PLANE_INDEX_ARM` | enums.41E0 | — (ungrouped, GL precedent) |  |
| `CL_IMPORT_DMA_BUF_DATA_CONSISTENCY_WITH_HOST_ARM` | enums.41E0 | — (ungrouped, GL precedent) |  |
| `CL_IMPORT_MEMORY_WHOLE_ALLOCATION_ARM` | Constants.cl_arm_import_memory | — (ungrouped, GL precedent) |  |
| `CL_IMPORT_TYPE_ANDROID_HARDWARE_BUFFER_ARM` | enums.41E0 | — (ungrouped, GL precedent) |  |
| `CL_IMPORT_TYPE_ARM` | enums.40B0 | — (ungrouped, GL precedent) |  |
| `CL_IMPORT_TYPE_DMA_BUF_ARM` | enums.40B0 | — (ungrouped, GL precedent) |  |
| `CL_IMPORT_TYPE_HOST_ARM` | enums.40B0 | — (ungrouped, GL precedent) |  |
| `CL_IMPORT_TYPE_PROTECTED_ARM` | enums.40B0 | — (ungrouped, GL precedent) |  |
| `CL_INCOMPATIBLE_COMMAND_QUEUE_KHR` | ErrorCodes.1138 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values); spec evidence [ErrorCode] G3 new-error-codes list |
| `CL_INFINITY` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_INTENSITY` | cl_device_info | `cl_channel_order` | spec evidence [cl_channel_order] value cell col0 (List of supported Image Channel Order Values) |
| `CL_INT_MAX` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_INT_MIN` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_INVALID_ACCELERATOR_DESCRIPTOR_INTEL` | ErrorCodes.1094 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_ACCELERATOR_INTEL` | ErrorCodes.1094 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_ACCELERATOR_TYPE_INTEL` | ErrorCodes.1094 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_ARG_INDEX` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_ARG_SIZE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_ARG_VALUE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_BINARY` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_BUFFER_SIZE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_BUILD_OPTIONS` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_COMMAND_BUFFER_KHR` | ErrorCodes.1138 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values); spec evidence [ErrorCode] G3 new-error-codes list |
| `CL_INVALID_COMMAND_QUEUE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_COMPILER_OPTIONS` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_CONTEXT` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_D3D10_DEVICE_KHR` | ErrorCodes.1002 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values); spec evidence [ErrorCode] G3 new-error-codes list |
| `CL_INVALID_D3D10_RESOURCE_KHR` | ErrorCodes.1002 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values); spec evidence [ErrorCode] G3 new-error-codes list |
| `CL_INVALID_D3D11_DEVICE_KHR` | ErrorCodes.1002 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values); spec evidence [ErrorCode] G3 new-error-codes list |
| `CL_INVALID_D3D11_RESOURCE_KHR` | ErrorCodes.1002 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values); spec evidence [ErrorCode] G3 new-error-codes list |
| `CL_INVALID_DEVICE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_DEVICE_PARTITION_COUNT` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_DEVICE_QUEUE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_DEVICE_TYPE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_DX9_DEVICE_INTEL` | ErrorCodes.1002 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_DX9_MEDIA_ADAPTER_KHR` | ErrorCodes.1002 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values); spec evidence [ErrorCode] G3 new-error-codes list |
| `CL_INVALID_DX9_MEDIA_SURFACE_KHR` | ErrorCodes.1002 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values); spec evidence [ErrorCode] G3 new-error-codes list |
| `CL_INVALID_DX9_RESOURCE_INTEL` | ErrorCodes.1002 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_EGL_OBJECT_KHR` | ErrorCodes.1092 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values); spec evidence [ErrorCode] G3 new-error-codes list |
| `CL_INVALID_EVENT` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_EVENT_WAIT_LIST` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_GLOBAL_OFFSET` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_GLOBAL_WORK_SIZE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_GL_OBJECT` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_GL_SHAREGROUP_REFERENCE_KHR` | ErrorCodes.1000 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values); spec evidence [ErrorCode] G3 new-error-codes list |
| `CL_INVALID_GRALLOC_OBJECT_IMG` | enums.40D0 | `ErrorCode` | manual: cl_img_use_gralloc_ptr error return code |
| `CL_INVALID_HOST_PTR` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_IMAGE_DESCRIPTOR` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_IMAGE_FORMAT_DESCRIPTOR` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_IMAGE_SIZE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_KERNEL` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_KERNEL_ARGS` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_KERNEL_DEFINITION` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_KERNEL_NAME` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_LINKER_OPTIONS` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_MEM_OBJECT` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_MIP_LEVEL` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_MUTABLE_COMMAND_KHR` | ErrorCodes.1138 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values); spec evidence [ErrorCode] G3 new-error-codes list |
| `CL_INVALID_OPERATION` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_PARTITION_COUNT_EXT` | ErrorCodes.1057 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_PARTITION_NAME_EXT` | ErrorCodes.1057 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_PIPE_SIZE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_PLATFORM` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_PROGRAM` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_PROGRAM_EXECUTABLE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_PROPERTY` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_QUEUE_PROPERTIES` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_SAMPLER` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_SEMAPHORE_KHR` | ErrorCodes.1142 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values); spec evidence [ErrorCode] G3 new-error-codes list |
| `CL_INVALID_SPEC_ID` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_SYNC_POINT_WAIT_LIST_KHR` | ErrorCodes.1138 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values); spec evidence [ErrorCode] G3 new-error-codes list |
| `CL_INVALID_VALUE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_VA_API_MEDIA_ADAPTER_INTEL` | ErrorCodes.1094 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_VA_API_MEDIA_SURFACE_INTEL` | ErrorCodes.1094 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_WORK_DIMENSION` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_WORK_GROUP_SIZE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_INVALID_WORK_ITEM_SIZE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_KERNEL_ALLOCATIONS_INFO_INTEL` | enums.4250 | `cl_kernel_work_group_info` | spec evidence [cl_kernel_work_group_info] G4 sentence+define |
| `CL_KERNEL_ARG_ACCESS_NONE` | cl_device_info | `cl_kernel_arg_access_qualifier` | spec evidence [cl_kernel_arg_access_qualifier] inline value-set of cl_kernel_arg_access_qualifier (row {CL_KERNEL_ARG_ACCESS_QUALIFIER_anchor}) |
| `CL_KERNEL_ARG_ACCESS_QUALIFIER` | cl_device_info | `cl_kernel_arg_info` | spec evidence [cl_kernel_arg_info] value cell col0 (List of supported param_names by {clGetKernelArgIn) |
| `CL_KERNEL_ARG_ACCESS_READ_ONLY` | cl_device_info | `cl_kernel_arg_access_qualifier` | spec evidence [cl_kernel_arg_access_qualifier] inline value-set of cl_kernel_arg_access_qualifier (row {CL_KERNEL_ARG_ACCESS_QUALIFIER_anchor}) |
| `CL_KERNEL_ARG_ACCESS_READ_WRITE` | cl_device_info | `cl_kernel_arg_access_qualifier` | spec evidence [cl_kernel_arg_access_qualifier] inline value-set of cl_kernel_arg_access_qualifier (row {CL_KERNEL_ARG_ACCESS_QUALIFIER_anchor}) |
| `CL_KERNEL_ARG_ACCESS_WRITE_ONLY` | cl_device_info | `cl_kernel_arg_access_qualifier` | spec evidence [cl_kernel_arg_access_qualifier] inline value-set of cl_kernel_arg_access_qualifier (row {CL_KERNEL_ARG_ACCESS_QUALIFIER_anchor}) |
| `CL_KERNEL_ARG_ADDRESS_CONSTANT` | cl_device_info | `cl_kernel_arg_address_qualifier` | spec evidence [cl_kernel_arg_address_qualifier] inline value-set of cl_kernel_arg_address_qualifier (row {CL_KERNEL_ARG_ADDRESS_QUALIFIER_anchor}) |
| `CL_KERNEL_ARG_ADDRESS_GLOBAL` | cl_device_info | `cl_kernel_arg_address_qualifier` | spec evidence [cl_kernel_arg_address_qualifier] inline value-set of cl_kernel_arg_address_qualifier (row {CL_KERNEL_ARG_ADDRESS_QUALIFIER_anchor}) |
| `CL_KERNEL_ARG_ADDRESS_LOCAL` | cl_device_info | `cl_kernel_arg_address_qualifier` | spec evidence [cl_kernel_arg_address_qualifier] inline value-set of cl_kernel_arg_address_qualifier (row {CL_KERNEL_ARG_ADDRESS_QUALIFIER_anchor}) |
| `CL_KERNEL_ARG_ADDRESS_PRIVATE` | cl_device_info | `cl_kernel_arg_address_qualifier` | spec evidence [cl_kernel_arg_address_qualifier] inline value-set of cl_kernel_arg_address_qualifier (row {CL_KERNEL_ARG_ADDRESS_QUALIFIER_anchor}) |
| `CL_KERNEL_ARG_ADDRESS_QUALIFIER` | cl_device_info | `cl_kernel_arg_info` | spec evidence [cl_kernel_arg_info] value cell col0 (List of supported param_names by {clGetKernelArgIn) |
| `CL_KERNEL_ARG_HOST_ACCESSIBLE_PIPE_INTEL` | enums.4210 | — (ungrouped, GL precedent) |  |
| `CL_KERNEL_ARG_INFO_NOT_AVAILABLE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_KERNEL_ARG_NAME` | cl_device_info | `cl_kernel_arg_info` | spec evidence [cl_kernel_arg_info] value cell col0 (List of supported param_names by {clGetKernelArgIn) |
| `CL_KERNEL_ARG_TYPE_CONST` | cl_kernel_arg_type_qualifier | `cl_kernel_arg_type_qualifier` | R1 C typedef container cl_kernel_arg_type_qualifier (container-declared) |
| `CL_KERNEL_ARG_TYPE_NAME` | cl_device_info | `cl_kernel_arg_info` | spec evidence [cl_kernel_arg_info] value cell col0 (List of supported param_names by {clGetKernelArgIn) |
| `CL_KERNEL_ARG_TYPE_NONE` | cl_kernel_arg_type_qualifier | `cl_kernel_arg_type_qualifier` | R1 C typedef container cl_kernel_arg_type_qualifier (container-declared) |
| `CL_KERNEL_ARG_TYPE_PIPE` | cl_kernel_arg_type_qualifier | `cl_kernel_arg_type_qualifier` | R1 C typedef container cl_kernel_arg_type_qualifier (container-declared) |
| `CL_KERNEL_ARG_TYPE_QUALIFIER` | cl_device_info | `cl_kernel_arg_info` | spec evidence [cl_kernel_arg_info] value cell col0 (List of supported param_names by {clGetKernelArgIn) |
| `CL_KERNEL_ARG_TYPE_RESTRICT` | cl_kernel_arg_type_qualifier | `cl_kernel_arg_type_qualifier` | R1 C typedef container cl_kernel_arg_type_qualifier (container-declared) |
| `CL_KERNEL_ARG_TYPE_VOLATILE` | cl_kernel_arg_type_qualifier | `cl_kernel_arg_type_qualifier` | R1 C typedef container cl_kernel_arg_type_qualifier (container-declared) |
| `CL_KERNEL_ATTRIBUTES` | cl_device_info | `cl_kernel_info` | spec evidence [cl_kernel_info] value cell col0 (List of supported param_names by {clGetKernelInfo}) |
| `CL_KERNEL_COMPILE_NUM_SUB_GROUPS` | cl_device_info | `cl_kernel_sub_group_info` | spec evidence [cl_kernel_sub_group_info] value cell col0 (List of supported param_names by {clGetKernelSubGr) |
| `CL_KERNEL_COMPILE_SUB_GROUP_SIZE_INTEL` | enums.4100 | `cl_kernel_sub_group_info` | manual: cl_intel_required_subgroup_size L83-89 param_name of clGetKernelSubGroupInfo + Table 5.22 |
| `CL_KERNEL_COMPILE_WORK_GROUP_SIZE` | cl_device_info | `cl_kernel_work_group_info` | spec evidence [cl_kernel_work_group_info] value cell col0 (List of supported param_names by {clGetKernelWorkG) |
| `CL_KERNEL_CONTEXT` | cl_device_info | `cl_kernel_info` | spec evidence [cl_kernel_info] value cell col0 (List of supported param_names by {clGetKernelInfo}) |
| `CL_KERNEL_EXEC_INFO_COMPUTE_UNIT_MAX_QUEUED_BATCHES_ARM` | enums.41E0 | `cl_kernel_exec_info` | manual: cl_arm_scheduling_controls L69-76 + Table 31 param_names of clSetKernelExecInfo |
| `CL_KERNEL_EXEC_INFO_DEVICE_PTRS_EXT` | enums.5000 | `cl_kernel_exec_info` | manual: cl_ext_buffer_device_address / opencl_runtime_layer param_name of clSetKernelExecInfo |
| `CL_KERNEL_EXEC_INFO_INDIRECT_DEVICE_ACCESS_INTEL` | enums.4200 | `cl_kernel_exec_info` | spec evidence [cl_kernel_exec_info] G4 sentence+define |
| `CL_KERNEL_EXEC_INFO_INDIRECT_HOST_ACCESS_INTEL` | enums.4200 | `cl_kernel_exec_info` | spec evidence [cl_kernel_exec_info] G4 sentence+define |
| `CL_KERNEL_EXEC_INFO_INDIRECT_SHARED_ACCESS_INTEL` | enums.4200 | `cl_kernel_exec_info` | spec evidence [cl_kernel_exec_info] G4 sentence+define |
| `CL_KERNEL_EXEC_INFO_SVM_FINE_GRAIN_SYSTEM` | cl_device_info | `cl_kernel_exec_info` | manual: cl_khr_unified_svm / opencl_runtime_layer param_name of clSetKernelExecInfo; cl_device_info mega-container token; no spec value-set found — le |
| `CL_KERNEL_EXEC_INFO_SVM_FINE_GRAIN_SYSTEM_ARM` | enums.40B0 | — (ungrouped, GL precedent) |  |
| `CL_KERNEL_EXEC_INFO_SVM_INDIRECT_ACCESS_KHR` | cl_device_info | `cl_kernel_exec_info` | manual: cl_khr_unified_svm / opencl_runtime_layer param_name of clSetKernelExecInfo; cl_device_info mega-container token; no spec value-set found — le |
| `CL_KERNEL_EXEC_INFO_SVM_PTRS` | cl_device_info | `cl_kernel_exec_info` | manual: cl_khr_unified_svm / opencl_runtime_layer param_name of clSetKernelExecInfo; cl_device_info mega-container token; no spec value-set found — le |
| `CL_KERNEL_EXEC_INFO_SVM_PTRS_ARM` | enums.40B0 | — (ungrouped, GL precedent) |  |
| `CL_KERNEL_EXEC_INFO_USM_PTRS_INTEL` | enums.4200 | `cl_kernel_exec_info` | spec evidence [cl_kernel_exec_info] G4 sentence+define |
| `CL_KERNEL_EXEC_INFO_WARP_COUNT_LIMIT_ARM` | enums.41E0 | `cl_kernel_exec_info` | manual: cl_arm_scheduling_controls L69-76 + Table 31 param_names of clSetKernelExecInfo |
| `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM` | enums.41E0 | `cl_kernel_exec_info` | manual: cl_arm_scheduling_controls L69-76 + Table 31 param_names of clSetKernelExecInfo |
| `CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_MODIFIER_ARM` | enums.41E0 | `cl_kernel_exec_info` | manual: cl_arm_scheduling_controls L69-76 + Table 31 param_names of clSetKernelExecInfo |
| `CL_KERNEL_FUNCTION_NAME` | cl_device_info | `cl_kernel_info` | spec evidence [cl_kernel_info] value cell col0 (List of supported param_names by {clGetKernelInfo}) |
| `CL_KERNEL_GLOBAL_WORK_SIZE` | cl_device_info | `cl_kernel_work_group_info` | spec evidence [cl_kernel_work_group_info] value cell col0 (List of supported param_names by {clGetKernelWorkG) |
| `CL_KERNEL_LOCAL_MEM_SIZE` | cl_device_info | `cl_kernel_work_group_info` | spec evidence [cl_kernel_work_group_info] value cell col0 (List of supported param_names by {clGetKernelWorkG) |
| `CL_KERNEL_LOCAL_SIZE_FOR_SUB_GROUP_COUNT` | cl_device_info | `cl_kernel_sub_group_info` | spec evidence [cl_kernel_sub_group_info] value cell col0 (List of supported param_names by {clGetKernelSubGr) |
| `CL_KERNEL_MAX_NUM_SUB_GROUPS` | cl_device_info | `cl_kernel_sub_group_info` | spec evidence [cl_kernel_sub_group_info] value cell col0 (List of supported param_names by {clGetKernelSubGr) |
| `CL_KERNEL_MAX_SUB_GROUP_SIZE_FOR_NDRANGE` | enums.2000 | `cl_kernel_sub_group_info` | spec evidence [cl_kernel_sub_group_info] value cell col0 (List of supported param_names by {clGetKernelSubGr) |
| `CL_KERNEL_MAX_SUB_GROUP_SIZE_FOR_NDRANGE_KHR` | enums.2000 | `cl_kernel_sub_group_info` | spec evidence [cl_kernel_sub_group_info] G3 new-enums list |
| `CL_KERNEL_MAX_WARP_COUNT_ARM` | enums.41E0 | `cl_kernel_info` | manual: cl_arm_scheduling_controls L87-92 + Table 32 param_names of clGetKernelInfo |
| `CL_KERNEL_NUM_ARGS` | cl_device_info | `cl_kernel_info` | spec evidence [cl_kernel_info] value cell col0 (List of supported param_names by {clGetKernelInfo}) |
| `CL_KERNEL_PREFERRED_WORK_GROUP_SIZE_MULTIPLE` | cl_device_info | `cl_kernel_work_group_info` | spec evidence [cl_kernel_work_group_info] value cell col0 (List of supported param_names by {clGetKernelWorkG) |
| `CL_KERNEL_PRIVATE_MEM_SIZE` | cl_device_info | `cl_kernel_work_group_info` | spec evidence [cl_kernel_work_group_info] value cell col0 (List of supported param_names by {clGetKernelWorkG) |
| `CL_KERNEL_PROGRAM` | cl_device_info | `cl_kernel_info` | spec evidence [cl_kernel_info] value cell col0 (List of supported param_names by {clGetKernelInfo}) |
| `CL_KERNEL_REFERENCE_COUNT` | cl_device_info | `cl_kernel_info` | spec evidence [cl_kernel_info] value cell col0 (List of supported param_names by {clGetKernelInfo}) |
| `CL_KERNEL_SPILL_MEM_SIZE_INTEL` | enums.4100 | `cl_kernel_work_group_info` | manual: cl_intel_required_subgroup_size L76-81 param_name of clGetKernelWorkGroupInfo + Table 5.21 |
| `CL_KERNEL_SUB_GROUP_COUNT_FOR_NDRANGE` | enums.2000 | `cl_kernel_sub_group_info` | spec evidence [cl_kernel_sub_group_info] value cell col0 (List of supported param_names by {clGetKernelSubGr) |
| `CL_KERNEL_SUB_GROUP_COUNT_FOR_NDRANGE_KHR` | enums.2000 | `cl_kernel_sub_group_info` | spec evidence [cl_kernel_sub_group_info] G3 new-enums list |
| `CL_KERNEL_WORK_GROUP_SIZE` | cl_device_info | `cl_kernel_work_group_info` | spec evidence [cl_kernel_work_group_info] value cell col0 (List of supported param_names by {clGetKernelWorkG) |
| `CL_KHRONOS_VENDOR_ID_CODEPLAY` | cl_khronos_vendor_id | `cl_khronos_vendor_id` | R1 C typedef container cl_khronos_vendor_id (container-declared) |
| `CL_KHRONOS_VENDOR_ID_POCL` | cl_khronos_vendor_id | `cl_khronos_vendor_id` | R1 C typedef container cl_khronos_vendor_id (container-declared) |
| `CL_LAYER_API_VERSION` | enums.4240 | `cl_layer_properties` | spec evidence [cl_layer_properties] G4 typedef+define |
| `CL_LAYER_API_VERSION_100` | Constants.cl_loader_layers | `cl_layer_properties` | manual: cl_loader_layers L109 'CL_LAYER_API_VERSION_100 100' legacy alias of CL_LAYER_API_VERSION (0x4240, group cl_layer_properties) |
| `CL_LAYER_NAME` | enums.4240 | `cl_layer_properties` | spec evidence [cl_layer_properties] G4 typedef+define |
| `CL_LAYER_PROPERTIES_LIST_END` | Constants.cl_loader_layers | `cl_layer_properties` | manual: cl_loader_layers L117 'CL_LAYER_PROPERTIES_LIST_END ((cl_layer_properties)0)' list terminator; L239-240 'list is terminated with CL_LAYER_PROP |
| `CL_LINKER_NOT_AVAILABLE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_LINK_PROGRAM_FAILURE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_LOCAL` | cl_device_local_mem_type | `cl_device_local_mem_type` | R1 C typedef container cl_device_local_mem_type (container-declared) |
| `CL_LONG_MAX` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_LONG_MIN` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_LUID_SIZE` | Constants.uuid | — (ungrouped, GL precedent) |  |
| `CL_LUID_SIZE_KHR` | Constants.cl_khr_device_uuid | — (ungrouped, GL precedent) |  |
| `CL_LUMINANCE` | cl_device_info | `cl_channel_order` | spec evidence [cl_channel_order] value cell col0 (List of supported Image Channel Order Values) |
| `CL_MAP_FAILURE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_MAP_READ` | cl_map_flags | `cl_map_flags` | R1 C typedef container cl_map_flags (spec-listed) |
| `CL_MAP_WRITE` | cl_map_flags | `cl_map_flags` | R1 C typedef container cl_map_flags (spec-listed) |
| `CL_MAP_WRITE_INVALIDATE_REGION` | cl_map_flags | `cl_map_flags` | R1 C typedef container cl_map_flags (spec-listed) |
| `CL_MAXFLOAT` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_MAX_SIZE_RESTRICTION_EXCEEDED` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_MEM_ACCESS_FLAGS_UNRESTRICTED_INTEL` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (spec-listed) |
| `CL_MEM_ALLOC_BASE_PTR_INTEL` | enums.4190 | `cl_mem_info_intel` | spec evidence [cl_mem_info_intel] G4 sentence+define |
| `CL_MEM_ALLOC_BUFFER_LOCATION_INTEL` | enums.4190 | `cl_mem_info_intel` | spec evidence [cl_mem_info_intel] value cell col0 (List of supported param_names by clGetMemAllocInfo) |
| `CL_MEM_ALLOC_CPU_LOCAL_IMG` | cl_mem_alloc_flags_img | `cl_mem_alloc_flags_img` | R1 C typedef container cl_mem_alloc_flags_img (container-declared) |
| `CL_MEM_ALLOC_DEVICE_INTEL` | enums.4190 | `cl_mem_info_intel` | spec evidence [cl_mem_info_intel] G4 sentence+define |
| `CL_MEM_ALLOC_FLAGS_IMG` | enums.40D0 | `cl_mem_alloc_flags_img` | spec evidence [cl_mem_alloc_flags_img] G4 typedef+define |
| `CL_MEM_ALLOC_FLAGS_INTEL` | enums.4190 | `cl_mem_info_intel`, `cl_mem_properties_intel` | spec evidence [cl_mem_info_intel] value cell col0 (List of supported param_names by clGetMemAllocInfo); spec evidence [cl_mem_properties_intel] G4 typ |
| `CL_MEM_ALLOC_GPU_CACHED_IMG` | cl_mem_alloc_flags_img | `cl_mem_alloc_flags_img` | R1 C typedef container cl_mem_alloc_flags_img (container-declared) |
| `CL_MEM_ALLOC_GPU_LOCAL_IMG` | cl_mem_alloc_flags_img | `cl_mem_alloc_flags_img` | R1 C typedef container cl_mem_alloc_flags_img (container-declared) |
| `CL_MEM_ALLOC_GPU_PRIVATE_IMG` | cl_mem_alloc_flags_img | `cl_mem_alloc_flags_img` | R1 C typedef container cl_mem_alloc_flags_img (container-declared) |
| `CL_MEM_ALLOC_GPU_WRITE_COMBINE_IMG` | cl_mem_alloc_flags_img | `cl_mem_alloc_flags_img` | R1 C typedef container cl_mem_alloc_flags_img (container-declared) |
| `CL_MEM_ALLOC_HOST_PTR` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (spec-listed) |
| `CL_MEM_ALLOC_INITIAL_PLACEMENT_DEVICE_INTEL` | cl_mem_alloc_flags_intel | `cl_mem_alloc_flags_intel` | R1 C typedef container cl_mem_alloc_flags_intel (container-declared) |
| `CL_MEM_ALLOC_INITIAL_PLACEMENT_HOST_INTEL` | cl_mem_alloc_flags_intel | `cl_mem_alloc_flags_intel` | R1 C typedef container cl_mem_alloc_flags_intel (container-declared) |
| `CL_MEM_ALLOC_RELAX_REQUIREMENTS_IMG` | cl_mem_alloc_flags_img | `cl_mem_alloc_flags_img` | R1 C typedef container cl_mem_alloc_flags_img (container-declared) |
| `CL_MEM_ALLOC_SIZE_INTEL` | enums.4190 | `cl_mem_info_intel` | spec evidence [cl_mem_info_intel] G4 sentence+define |
| `CL_MEM_ALLOC_TYPE_INTEL` | enums.4190 | `cl_mem_info_intel` | spec evidence [cl_mem_info_intel] G4 sentence+define |
| `CL_MEM_ALLOC_WRITE_COMBINED_INTEL` | cl_mem_alloc_flags_intel | `cl_mem_alloc_flags_intel` | R1 C typedef container cl_mem_alloc_flags_intel (container-declared) |
| `CL_MEM_ANDROID_NATIVE_BUFFER_HOST_PTR_QCOM` | enums.40C0 | — (ungrouped, GL precedent) |  |
| `CL_MEM_ASSOCIATED_MEMOBJECT` | cl_device_info | `cl_mem_info` | spec evidence [cl_mem_info] value cell col0 (List of supported param_names by {clGetMemObjectIn) |
| `CL_MEM_CHANNEL_INTEL` | enums.4210 | `cl_mem_properties_intel` | manual: cl_intel_mem_channel_property: property for clCreateBufferWithPropertiesINTEL |
| `CL_MEM_CONTEXT` | cl_device_info | `cl_mem_info` | spec evidence [cl_mem_info] value cell col0 (List of supported param_names by {clGetMemObjectIn) |
| `CL_MEM_COPY_HOST_PTR` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (spec-listed) |
| `CL_MEM_COPY_OVERLAP` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_MEM_D3D10_RESOURCE_KHR` | enums.4010 | `cl_mem_info` | spec evidence [cl_mem_info] G3 new-enums list |
| `CL_MEM_D3D11_RESOURCE_KHR` | enums.4010 | `cl_mem_info` | spec evidence [cl_mem_info] G3 new-enums list |
| `CL_MEM_DEVICE_ADDRESS_EXT` | enums.5000 | `cl_mem_info` | spec evidence [cl_mem_info] value cell col0 (List of supported param_names by {clGetMemObjectIn) |
| `CL_MEM_DEVICE_HANDLE_LIST_END_KHR` | MiscNumbers | `cl_mem_properties` | spec evidence [cl_mem_properties] G3 new-enums list |
| `CL_MEM_DEVICE_HANDLE_LIST_KHR` | enums.2000 | `cl_mem_properties` | manual: cl_khr_external_memory.asciidoc L60-61: listed under cl_mem_properties_TYPE; cl_image_properties is not a cl.xml type (removed); spec evidence |
| `CL_MEM_DEVICE_ID_INTEL` | enums.4210 | — (ungrouped, GL precedent) |  |
| `CL_MEM_DEVICE_PRIVATE_ADDRESS_EXT` | enums.5000 | `cl_mem_properties` | manual: cl_ext_buffer_device_address: clCreateBufferWithProperties creation property flag |
| `CL_MEM_DX9_MEDIA_ADAPTER_TYPE_KHR` | enums.2000 | `cl_mem_info` | spec evidence [cl_mem_info] G3 new-enums list |
| `CL_MEM_DX9_MEDIA_SURFACE_INFO_KHR` | enums.2000 | `cl_mem_info` | spec evidence [cl_mem_info] G3 new-enums list |
| `CL_MEM_DX9_RESOURCE_INTEL` | enums.4010 | — (ungrouped, GL precedent) |  |
| `CL_MEM_DX9_SHARED_HANDLE_INTEL` | enums.4070 | — (ungrouped, GL precedent) |  |
| `CL_MEM_EXT_HOST_PTR_QCOM` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (container-declared) |
| `CL_MEM_FLAGS` | cl_device_info | `cl_mem_info` | spec evidence [cl_mem_info] value cell col0 (List of supported param_names by {clGetMemObjectIn) |
| `CL_MEM_FORCE_HOST_MEMORY_INTEL` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (spec-listed) |
| `CL_MEM_HOST_IOCOHERENT_QCOM` | enums.40A0 | — (ungrouped, GL precedent) |  |
| `CL_MEM_HOST_NO_ACCESS` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (spec-listed) |
| `CL_MEM_HOST_PTR` | cl_device_info | `cl_mem_info` | spec evidence [cl_mem_info] value cell col0 (List of supported param_names by {clGetMemObjectIn) |
| `CL_MEM_HOST_READ_ONLY` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (spec-listed) |
| `CL_MEM_HOST_UNCACHED_QCOM` | enums.40A0 | — (ungrouped, GL precedent) |  |
| `CL_MEM_HOST_WRITEBACK_QCOM` | enums.40A0 | — (ungrouped, GL precedent) |  |
| `CL_MEM_HOST_WRITETHROUGH_QCOM` | enums.40A0 | — (ungrouped, GL precedent) |  |
| `CL_MEM_HOST_WRITE_COMBINING_QCOM` | enums.40A0 | — (ungrouped, GL precedent) |  |
| `CL_MEM_HOST_WRITE_ONLY` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (spec-listed) |
| `CL_MEM_IMMUTABLE_EXT` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (spec-listed) |
| `CL_MEM_ION_HOST_PTR_QCOM` | enums.40A0 | — (ungrouped, GL precedent) |  |
| `CL_MEM_KERNEL_READ_AND_WRITE` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (spec-listed) |
| `CL_MEM_LOCALLY_UNCACHED_RESOURCE_INTEL` | enums.4210 | — (ungrouped, GL precedent) |  |
| `CL_MEM_MAP_COUNT` | cl_device_info | `cl_mem_info` | spec evidence [cl_mem_info] value cell col0 (List of supported param_names by {clGetMemObjectIn) |
| `CL_MEM_NO_ACCESS_INTEL` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (spec-listed) |
| `CL_MEM_OBJECT_ALLOCATION_FAILURE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_MEM_OBJECT_BUFFER` | cl_device_info | `cl_mem_object_type` | manual: core spec: value set of cl_mem_object_type (image_type param of clCreateImage / clCreateImage2D); cl_device_info mega-container token; no spec |
| `CL_MEM_OBJECT_IMAGE1D` | cl_device_info | `cl_mem_object_type` | manual: core spec: value set of cl_mem_object_type (image_type param of clCreateImage / clCreateImage2D); cl_device_info mega-container token; no spec |
| `CL_MEM_OBJECT_IMAGE1D_ARRAY` | cl_device_info | `cl_mem_object_type` | manual: core spec: value set of cl_mem_object_type (image_type param of clCreateImage / clCreateImage2D); cl_device_info mega-container token; no spec |
| `CL_MEM_OBJECT_IMAGE1D_BUFFER` | cl_device_info | `cl_mem_object_type` | manual: core spec: value set of cl_mem_object_type (image_type param of clCreateImage / clCreateImage2D); cl_device_info mega-container token; no spec |
| `CL_MEM_OBJECT_IMAGE2D` | cl_device_info | `cl_mem_object_type` | manual: core spec: value set of cl_mem_object_type (image_type param of clCreateImage / clCreateImage2D); cl_device_info mega-container token; no spec |
| `CL_MEM_OBJECT_IMAGE2D_ARRAY` | cl_device_info | `cl_mem_object_type` | manual: core spec: value set of cl_mem_object_type (image_type param of clCreateImage / clCreateImage2D); cl_device_info mega-container token; no spec |
| `CL_MEM_OBJECT_IMAGE3D` | cl_device_info | `cl_mem_object_type` | manual: core spec: value set of cl_mem_object_type (image_type param of clCreateImage / clCreateImage2D); cl_device_info mega-container token; no spec |
| `CL_MEM_OBJECT_PIPE` | cl_device_info | `cl_mem_object_type` | manual: core spec: value set of cl_mem_object_type (image_type param of clCreateImage / clCreateImage2D); cl_device_info mega-container token; no spec |
| `CL_MEM_OFFSET` | cl_device_info | `cl_mem_info` | spec evidence [cl_mem_info] value cell col0 (List of supported param_names by {clGetMemObjectIn) |
| `CL_MEM_PROPERTIES` | cl_device_info | `cl_mem_info` | spec evidence [cl_mem_info] value cell col0 (List of supported param_names by {clGetMemObjectIn) |
| `CL_MEM_PROTECTED_ALLOC_ARM` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (container-declared) |
| `CL_MEM_READ_ONLY` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (spec-listed) |
| `CL_MEM_READ_WRITE` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (spec-listed) |
| `CL_MEM_REFERENCE_COUNT` | cl_device_info | `cl_mem_info` | spec evidence [cl_mem_info] value cell col0 (List of supported param_names by {clGetMemObjectIn) |
| `CL_MEM_RESERVED0_ARM` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (container-declared) |
| `CL_MEM_RESERVED0_QCOM` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (container-declared) |
| `CL_MEM_RESERVED1_ARM` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (container-declared) |
| `CL_MEM_RESERVED1_QCOM` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (container-declared) |
| `CL_MEM_RESERVED21_INTEL` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (container-declared) |
| `CL_MEM_RESERVED22_INTEL` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (container-declared) |
| `CL_MEM_RESERVED2_ARM` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (container-declared) |
| `CL_MEM_RESERVED2_QCOM` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (container-declared) |
| `CL_MEM_RESERVED3_ARM` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (container-declared) |
| `CL_MEM_RESERVED3_QCOM` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (container-declared) |
| `CL_MEM_SIZE` | cl_device_info | `cl_mem_info` | spec evidence [cl_mem_info] value cell col0 (List of supported param_names by {clGetMemObjectIn) |
| `CL_MEM_SVM_ATOMICS` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (spec-listed) |
| `CL_MEM_SVM_ATOMICS_ARM` | cl_arm_svm_alloc.flags | `cl_arm_svm_alloc.flags` | R1 C typedef container cl_arm_svm_alloc.flags (container-declared) |
| `CL_MEM_SVM_FINE_GRAIN_BUFFER` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (spec-listed) |
| `CL_MEM_SVM_FINE_GRAIN_BUFFER_ARM` | cl_arm_svm_alloc.flags | `cl_arm_svm_alloc.flags` | R1 C typedef container cl_arm_svm_alloc.flags (container-declared) |
| `CL_MEM_TYPE` | cl_device_info | `cl_mem_info` | spec evidence [cl_mem_info] value cell col0 (List of supported param_names by {clGetMemObjectIn) |
| `CL_MEM_TYPE_DEVICE_INTEL` | enums.4190 | `cl_unified_shared_memory_type_intel` | spec evidence [cl_unified_shared_memory_type_intel] G4 typedef+define |
| `CL_MEM_TYPE_HOST_INTEL` | enums.4190 | `cl_unified_shared_memory_type_intel` | spec evidence [cl_unified_shared_memory_type_intel] G4 typedef+define |
| `CL_MEM_TYPE_SHARED_INTEL` | enums.4190 | `cl_unified_shared_memory_type_intel` | spec evidence [cl_unified_shared_memory_type_intel] G4 typedef+define |
| `CL_MEM_TYPE_UNKNOWN_INTEL` | enums.4190 | `cl_unified_shared_memory_type_intel` | spec evidence [cl_unified_shared_memory_type_intel] G4 typedef+define |
| `CL_MEM_USES_SVM_POINTER` | cl_device_info | `cl_mem_info` | spec evidence [cl_mem_info] value cell col0 (List of supported param_names by {clGetMemObjectIn) |
| `CL_MEM_USES_SVM_POINTER_ARM` | enums.40B0 | — (ungrouped, GL precedent) |  |
| `CL_MEM_USE_CACHED_CPU_MEMORY_IMG` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (container-declared) |
| `CL_MEM_USE_GRALLOC_PTR_IMG` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (container-declared) |
| `CL_MEM_USE_HOST_PTR` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (spec-listed) |
| `CL_MEM_USE_UNCACHED_CPU_MEMORY_IMG` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (container-declared) |
| `CL_MEM_VA_API_MEDIA_SURFACE_INTEL` | enums.4090 | — (ungrouped, GL precedent) |  |
| `CL_MEM_WRITE_ONLY` | cl_mem_flags | `cl_mem_flags` | R1 C typedef container cl_mem_flags (spec-listed) |
| `CL_ME_BACKWARD_INPUT_MODE_INTEL` | cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel | `cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel` | R1 C typedef container cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel (container-declared) |
| `CL_ME_BIDIRECTION_INPUT_MODE_INTEL` | cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel | `cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel` | R1 C typedef container cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel (container-declared) |
| `CL_ME_BIDIR_WEIGHT_HALF_INTEL` | cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel.2 | `cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel.2` | R1 C typedef container cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel.2 (container-declared) |
| `CL_ME_BIDIR_WEIGHT_QUARTER_INTEL` | cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel.2 | `cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel.2` | R1 C typedef container cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel.2 (container-declared) |
| `CL_ME_BIDIR_WEIGHT_THIRD_INTEL` | cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel.2 | `cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel.2` | R1 C typedef container cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel.2 (container-declared) |
| `CL_ME_BIDIR_WEIGHT_THREE_QUARTER_INTEL` | cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel.2 | `cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel.2` | R1 C typedef container cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel.2 (container-declared) |
| `CL_ME_BIDIR_WEIGHT_TWO_THIRD_INTEL` | cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel.2 | `cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel.2` | R1 C typedef container cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel.2 (container-declared) |
| `CL_ME_CHROMA_INTRA_PREDICT_ENABLED_INTEL` | cl_intel_advanced_motion_estimation.flags | `cl_intel_advanced_motion_estimation.flags` | R1 C typedef container cl_intel_advanced_motion_estimation.flags (container-declared) |
| `CL_ME_CHROMA_PREDICTOR_MODE_DC_INTEL` | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.chroma_block | `cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.chroma_block` | R1 C typedef container cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.chroma_block (container-declared) |
| `CL_ME_CHROMA_PREDICTOR_MODE_HORIZONTAL_INTEL` | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.chroma_block | `cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.chroma_block` | R1 C typedef container cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.chroma_block (container-declared) |
| `CL_ME_CHROMA_PREDICTOR_MODE_PLANE_INTEL` | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.chroma_block | `cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.chroma_block` | R1 C typedef container cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.chroma_block (container-declared) |
| `CL_ME_CHROMA_PREDICTOR_MODE_VERTICAL_INTEL` | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.chroma_block | `cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.chroma_block` | R1 C typedef container cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.chroma_block (container-declared) |
| `CL_ME_COST_PENALTY_HIGH_INTEL` | cl_intel_advanced_motion_estimation.search_cost_penalty | `cl_intel_advanced_motion_estimation.search_cost_penalty` | R1 C typedef container cl_intel_advanced_motion_estimation.search_cost_penalty (container-declared) |
| `CL_ME_COST_PENALTY_LOW_INTEL` | cl_intel_advanced_motion_estimation.search_cost_penalty | `cl_intel_advanced_motion_estimation.search_cost_penalty` | R1 C typedef container cl_intel_advanced_motion_estimation.search_cost_penalty (container-declared) |
| `CL_ME_COST_PENALTY_NONE_INTEL` | cl_intel_advanced_motion_estimation.search_cost_penalty | `cl_intel_advanced_motion_estimation.search_cost_penalty` | R1 C typedef container cl_intel_advanced_motion_estimation.search_cost_penalty (container-declared) |
| `CL_ME_COST_PENALTY_NORMAL_INTEL` | cl_intel_advanced_motion_estimation.search_cost_penalty | `cl_intel_advanced_motion_estimation.search_cost_penalty` | R1 C typedef container cl_intel_advanced_motion_estimation.search_cost_penalty (container-declared) |
| `CL_ME_COST_PRECISION_DPEL_INTEL` | cl_intel_advanced_motion_estimation.search_cost_precision | `cl_intel_advanced_motion_estimation.search_cost_precision` | R1 C typedef container cl_intel_advanced_motion_estimation.search_cost_precision (container-declared) |
| `CL_ME_COST_PRECISION_HPEL_INTEL` | cl_intel_advanced_motion_estimation.search_cost_precision | `cl_intel_advanced_motion_estimation.search_cost_precision` | R1 C typedef container cl_intel_advanced_motion_estimation.search_cost_precision (container-declared) |
| `CL_ME_COST_PRECISION_PEL_INTEL` | cl_intel_advanced_motion_estimation.search_cost_precision | `cl_intel_advanced_motion_estimation.search_cost_precision` | R1 C typedef container cl_intel_advanced_motion_estimation.search_cost_precision (container-declared) |
| `CL_ME_COST_PRECISION_QPEL_INTEL` | cl_intel_advanced_motion_estimation.search_cost_precision | `cl_intel_advanced_motion_estimation.search_cost_precision` | R1 C typedef container cl_intel_advanced_motion_estimation.search_cost_precision (container-declared) |
| `CL_ME_FORWARD_INPUT_MODE_INTEL` | cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel | `cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel` | R1 C typedef container cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel (container-declared) |
| `CL_ME_LUMA_INTRA_PREDICT_ENABLED_INTEL` | cl_intel_advanced_motion_estimation.flags | `cl_intel_advanced_motion_estimation.flags` | R1 C typedef container cl_intel_advanced_motion_estimation.flags (container-declared) |
| `CL_ME_LUMA_PREDICTOR_MODE_DC_INTEL` | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block | `cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block` | R1 C typedef container cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block (container-declared) |
| `CL_ME_LUMA_PREDICTOR_MODE_DIAGONAL_DOWN_LEFT_INTEL` | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block | `cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block` | R1 C typedef container cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block (container-declared) |
| `CL_ME_LUMA_PREDICTOR_MODE_DIAGONAL_DOWN_RIGHT_INTEL` | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block | `cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block` | R1 C typedef container cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block (container-declared) |
| `CL_ME_LUMA_PREDICTOR_MODE_HORIZONTAL_DOWN_INTEL` | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block | `cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block` | R1 C typedef container cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block (container-declared) |
| `CL_ME_LUMA_PREDICTOR_MODE_HORIZONTAL_INTEL` | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block | `cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block` | R1 C typedef container cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block (container-declared) |
| `CL_ME_LUMA_PREDICTOR_MODE_HORIZONTAL_UP_INTEL` | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block | `cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block` | R1 C typedef container cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block (container-declared) |
| `CL_ME_LUMA_PREDICTOR_MODE_PLANE_INTEL` | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block | `cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block` | R1 C typedef container cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block (container-declared) |
| `CL_ME_LUMA_PREDICTOR_MODE_VERTICAL_INTEL` | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block | `cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block` | R1 C typedef container cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block (container-declared) |
| `CL_ME_LUMA_PREDICTOR_MODE_VERTICAL_LEFT_INTEL` | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block | `cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block` | R1 C typedef container cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block (container-declared) |
| `CL_ME_LUMA_PREDICTOR_MODE_VERTICAL_RIGHT_INTEL` | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block | `cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block` | R1 C typedef container cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block (container-declared) |
| `CL_ME_MB_TYPE_16x16_INTEL` | cl_motion_estimation_desc_intel.mb_block_type | `cl_motion_estimation_desc_intel.mb_block_type` | R1 C typedef container cl_motion_estimation_desc_intel.mb_block_type (container-declared) |
| `CL_ME_MB_TYPE_4x4_INTEL` | cl_motion_estimation_desc_intel.mb_block_type | `cl_motion_estimation_desc_intel.mb_block_type` | R1 C typedef container cl_motion_estimation_desc_intel.mb_block_type (container-declared) |
| `CL_ME_MB_TYPE_8x8_INTEL` | cl_motion_estimation_desc_intel.mb_block_type | `cl_motion_estimation_desc_intel.mb_block_type` | R1 C typedef container cl_motion_estimation_desc_intel.mb_block_type (container-declared) |
| `CL_ME_SAD_ADJUST_MODE_HAAR_INTEL` | cl_motion_estimation_desc_intel.sad_adjust_mode | `cl_motion_estimation_desc_intel.sad_adjust_mode` | R1 C typedef container cl_motion_estimation_desc_intel.sad_adjust_mode (container-declared) |
| `CL_ME_SAD_ADJUST_MODE_NONE_INTEL` | cl_motion_estimation_desc_intel.sad_adjust_mode | `cl_motion_estimation_desc_intel.sad_adjust_mode` | R1 C typedef container cl_motion_estimation_desc_intel.sad_adjust_mode (container-declared) |
| `CL_ME_SEARCH_PATH_RADIUS_16_12_INTEL` | cl_motion_estimation_desc_intel.search_path_type | `cl_motion_estimation_desc_intel.search_path_type` | R1 C typedef container cl_motion_estimation_desc_intel.search_path_type (container-declared) |
| `CL_ME_SEARCH_PATH_RADIUS_2_2_INTEL` | cl_motion_estimation_desc_intel.search_path_type | `cl_motion_estimation_desc_intel.search_path_type` | R1 C typedef container cl_motion_estimation_desc_intel.search_path_type (container-declared) |
| `CL_ME_SEARCH_PATH_RADIUS_4_4_INTEL` | cl_motion_estimation_desc_intel.search_path_type | `cl_motion_estimation_desc_intel.search_path_type` | R1 C typedef container cl_motion_estimation_desc_intel.search_path_type (container-declared) |
| `CL_ME_SKIP_BLOCK_TYPE_16x16_INTEL` | cl_intel_advanced_motion_estimation.skip_block_type | `cl_intel_advanced_motion_estimation.skip_block_type` | R1 C typedef container cl_intel_advanced_motion_estimation.skip_block_type (container-declared) |
| `CL_ME_SKIP_BLOCK_TYPE_8x8_INTEL` | cl_intel_advanced_motion_estimation.skip_block_type | `cl_intel_advanced_motion_estimation.skip_block_type` | R1 C typedef container cl_intel_advanced_motion_estimation.skip_block_type (container-declared) |
| `CL_ME_SUBPIXEL_MODE_HPEL_INTEL` | cl_motion_estimation_desc_intel.subpixel_mode | `cl_motion_estimation_desc_intel.subpixel_mode` | R1 C typedef container cl_motion_estimation_desc_intel.subpixel_mode (container-declared) |
| `CL_ME_SUBPIXEL_MODE_INTEGER_INTEL` | cl_motion_estimation_desc_intel.subpixel_mode | `cl_motion_estimation_desc_intel.subpixel_mode` | R1 C typedef container cl_motion_estimation_desc_intel.subpixel_mode (container-declared) |
| `CL_ME_SUBPIXEL_MODE_QPEL_INTEL` | cl_motion_estimation_desc_intel.subpixel_mode | `cl_motion_estimation_desc_intel.subpixel_mode` | R1 C typedef container cl_motion_estimation_desc_intel.subpixel_mode (container-declared) |
| `CL_ME_VERSION_ADVANCED_VER_1_INTEL` | cl_intel_advanced_motion_estimation.device_me_version | `cl_intel_advanced_motion_estimation.device_me_version` | R1 C typedef container cl_intel_advanced_motion_estimation.device_me_version (container-declared) |
| `CL_ME_VERSION_ADVANCED_VER_2_INTEL` | cl_intel_advanced_motion_estimation.device_me_version | `cl_intel_advanced_motion_estimation.device_me_version` | R1 C typedef container cl_intel_advanced_motion_estimation.device_me_version (container-declared) |
| `CL_ME_VERSION_LEGACY_INTEL` | cl_intel_advanced_motion_estimation.device_me_version | `cl_intel_advanced_motion_estimation.device_me_version` | R1 C typedef container cl_intel_advanced_motion_estimation.device_me_version (container-declared) |
| `CL_MIGRATE_MEM_OBJECT_CONTENT_UNDEFINED` | cl_mem_migration_flags | `cl_mem_migration_flags` | R1 C typedef container cl_mem_migration_flags (spec-listed) |
| `CL_MIGRATE_MEM_OBJECT_HOST` | cl_mem_migration_flags | `cl_mem_migration_flags` | R1 C typedef container cl_mem_migration_flags (spec-listed) |
| `CL_MIGRATE_MEM_OBJECT_HOST_EXT` | cl_mem_migration_flags | `cl_mem_migration_flags` | R1 C typedef container cl_mem_migration_flags (container-declared) |
| `CL_MIPMAP_FILTER_ANY_IMG` | cl_mipmap_filter_mode_img | `cl_mipmap_filter_mode_img` | R1 C typedef container cl_mipmap_filter_mode_img (container-declared) |
| `CL_MIPMAP_FILTER_BOX_IMG` | cl_mipmap_filter_mode_img | `cl_mipmap_filter_mode_img` | R1 C typedef container cl_mipmap_filter_mode_img (container-declared) |
| `CL_MISALIGNED_SUB_BUFFER_OFFSET` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_MUTABLE_COMMAND_COMMAND_BUFFER_KHR` | cl_device_info | `cl_mutable_command_info_khr` | spec evidence [cl_mutable_command_info_khr] G3 new-enums list |
| `CL_MUTABLE_COMMAND_COMMAND_QUEUE_KHR` | cl_device_info | `cl_mutable_command_info_khr` | spec evidence [cl_mutable_command_info_khr] G3 new-enums list |
| `CL_MUTABLE_COMMAND_COMMAND_TYPE_KHR` | cl_device_info | `cl_mutable_command_info_khr` | spec evidence [cl_mutable_command_info_khr] G3 new-enums list |
| `CL_MUTABLE_COMMAND_PROPERTIES_ARRAY_KHR` | cl_device_info | `cl_mutable_command_info_khr` | spec evidence [cl_mutable_command_info_khr] G3 new-enums list |
| `CL_MUTABLE_DISPATCH_ARGUMENTS_KHR` | cl_mutable_dispatch_fields_khr | `cl_mutable_dispatch_fields_khr` | R1 C typedef container cl_mutable_dispatch_fields_khr (spec-listed) |
| `CL_MUTABLE_DISPATCH_ASSERTS_KHR` | cl_device_info | `cl_command_properties_khr` | spec evidence [cl_command_properties_khr] G3 new-enums list |
| `CL_MUTABLE_DISPATCH_ASSERT_NO_ADDITIONAL_WORK_GROUPS_KHR` | cl_mutable_dispatch_asserts_khr | `cl_mutable_dispatch_asserts_khr` | R1 C typedef container cl_mutable_dispatch_asserts_khr (spec-listed) |
| `CL_MUTABLE_DISPATCH_DIMENSIONS_KHR` | cl_device_info | `cl_mutable_command_info_khr` | spec evidence [cl_mutable_command_info_khr] G3 new-enums list |
| `CL_MUTABLE_DISPATCH_EXEC_INFO_KHR` | cl_mutable_dispatch_fields_khr | `cl_mutable_dispatch_fields_khr` | R1 C typedef container cl_mutable_dispatch_fields_khr (spec-listed) |
| `CL_MUTABLE_DISPATCH_GLOBAL_OFFSET_KHR` | cl_mutable_dispatch_fields_khr | `cl_mutable_dispatch_fields_khr` | R1 C typedef container cl_mutable_dispatch_fields_khr (spec-listed) |
| `CL_MUTABLE_DISPATCH_GLOBAL_SIZE_KHR` | cl_mutable_dispatch_fields_khr | `cl_mutable_dispatch_fields_khr` | R1 C typedef container cl_mutable_dispatch_fields_khr (spec-listed) |
| `CL_MUTABLE_DISPATCH_GLOBAL_WORK_OFFSET_KHR` | cl_device_info | `cl_mutable_command_info_khr` | spec evidence [cl_mutable_command_info_khr] G3 new-enums list |
| `CL_MUTABLE_DISPATCH_GLOBAL_WORK_SIZE_KHR` | cl_device_info | `cl_mutable_command_info_khr` | spec evidence [cl_mutable_command_info_khr] G3 new-enums list |
| `CL_MUTABLE_DISPATCH_KERNEL_KHR` | cl_device_info | `cl_mutable_command_info_khr` | spec evidence [cl_mutable_command_info_khr] G3 new-enums list |
| `CL_MUTABLE_DISPATCH_LOCAL_SIZE_KHR` | cl_mutable_dispatch_fields_khr | `cl_mutable_dispatch_fields_khr` | R1 C typedef container cl_mutable_dispatch_fields_khr (spec-listed) |
| `CL_MUTABLE_DISPATCH_LOCAL_WORK_SIZE_KHR` | cl_device_info | `cl_mutable_command_info_khr` | spec evidence [cl_mutable_command_info_khr] G3 new-enums list |
| `CL_MUTABLE_DISPATCH_UPDATABLE_FIELDS_KHR` | cl_device_info | `cl_command_properties_khr` | spec evidence [cl_command_properties_khr] G3 new-enums list |
| `CL_M_1_PI` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_1_PI_F` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_2_PI` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_2_PI_F` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_2_SQRTPI` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_2_SQRTPI_F` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_E` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_E_F` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_LN10` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_LN10_F` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_LN2` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_LN2_F` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_LOG10E` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_LOG10E_F` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_LOG2E` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_LOG2E_F` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_PI` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_PI_2` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_PI_2_F` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_PI_4` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_PI_4_F` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_PI_F` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_SQRT1_2` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_SQRT1_2_F` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_SQRT2` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_M_SQRT2_F` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_NAME_VERSION_MAX_NAME_SIZE` | Constants.Versioning | — (ungrouped, GL precedent) |  |
| `CL_NAME_VERSION_MAX_NAME_SIZE_KHR` | Constants.cl_khr_extended_versioning | — (ungrouped, GL precedent) |  |
| `CL_NAN` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_NONE` | cl_device_mem_cache_type | `cl_device_mem_cache_type` | R1 C typedef container cl_device_mem_cache_type (spec-listed) |
| `CL_NON_BLOCKING` | cl_bool | `cl_bool` | R1 C typedef container cl_bool (container-declared) |
| `CL_NV12_INTEL` | enums.4100 | `cl_channel_order` | spec evidence [cl_channel_order] value cell col0 (List of supported Image Channel Order Values) |
| `CL_NV21` | enums.40D0 | `cl_channel_order` | manual: cl_img_yuv_image image_channel_order (or deprecated pre-IMG alias) |
| `CL_NV21_IMG` | enums.40D0 | `cl_channel_order` | manual: cl_img_yuv_image image_channel_order (or deprecated pre-IMG alias) |
| `CL_OUT_OF_HOST_MEMORY` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_OUT_OF_RESOURCES` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_PAGE_FAULT_IMG` | ErrorCodes.1122 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_PARTITION_BY_COUNTS_LIST_END_EXT` | MiscNumbers | `cl_device_partition_property` | manual: KHR-inherited: list terminator for cl_device_partition_property |
| `CL_PARTITION_BY_NAMES_LIST_END_EXT` | MiscNumbers | `cl_device_partition_property` | manual: list terminator of the EXT partition-property list; value cast to cl_device_partition_property_ext; sibling _COUNTS_ already cl_device_partiti |
| `CL_PARTITION_BY_NAMES_LIST_END_INTEL` | MiscNumbers | `cl_device_partition_property` | manual: list terminator of the INTEL partition-property list; sibling CL_PARTITION_BY_COUNTS_LIST_END_EXT already cl_device_partition_property |
| `CL_PERF_HINT_HIGH_QCOM` | enums.40C0 | `cl_perf_hint_qcom` | manual: extensions/cl_qcom_perf_hint.asciidoc L90-98 'New list of supported values for CL_CONTEXT_PERF_HINT_QCOM property'; L137-142 Table 13a, member |
| `CL_PERF_HINT_LOW_QCOM` | enums.40C0 | `cl_perf_hint_qcom` | manual: extensions/cl_qcom_perf_hint.asciidoc L90-98 'New list of supported values for CL_CONTEXT_PERF_HINT_QCOM property'; L137-142 Table 13a, member |
| `CL_PERF_HINT_NORMAL_QCOM` | enums.40C0 | `cl_perf_hint_qcom` | manual: extensions/cl_qcom_perf_hint.asciidoc L90-98 'New list of supported values for CL_CONTEXT_PERF_HINT_QCOM property'; L137-142 Table 13a, member |
| `CL_PIPE_EMPTY_INTEL` | ErrorCodes.1106 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_PIPE_FULL_INTEL` | ErrorCodes.1106 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_PIPE_MAX_PACKETS` | cl_device_info | `cl_pipe_info` | spec evidence [cl_pipe_info] value cell col0 (List of supported param_names by {clGetPipeInfo}) |
| `CL_PIPE_PACKET_SIZE` | cl_device_info | `cl_pipe_info` | spec evidence [cl_pipe_info] value cell col0 (List of supported param_names by {clGetPipeInfo}) |
| `CL_PIPE_PROPERTIES` | cl_device_info | `cl_pipe_info` | spec evidence [cl_pipe_info] value cell col0 (List of supported param_names by {clGetPipeInfo}) |
| `CL_PLATFORM_COMMAND_BUFFER_CAPABILITIES_KHR` | cl_platform_info | `cl_platform_info` | R1 C typedef container cl_platform_info (spec-listed) |
| `CL_PLATFORM_EXTENSIONS` | cl_platform_info | `cl_platform_info` | R1 C typedef container cl_platform_info (spec-listed) |
| `CL_PLATFORM_EXTENSIONS_WITH_VERSION` | cl_platform_info | `cl_platform_info` | R1 C typedef container cl_platform_info (spec-listed) |
| `CL_PLATFORM_EXTENSIONS_WITH_VERSION_KHR` | cl_platform_info | `cl_platform_info` | R1 C typedef container cl_platform_info (spec-listed) |
| `CL_PLATFORM_EXTERNAL_MEMORY_IMPORT_HANDLE_TYPES_KHR` | enums.2000 | `cl_platform_info` | spec evidence [cl_platform_info] G3 new-enums list |
| `CL_PLATFORM_HOST_TIMER_RESOLUTION` | cl_platform_info | `cl_platform_info` | R1 C typedef container cl_platform_info (spec-listed) |
| `CL_PLATFORM_ICD_SUFFIX_KHR` | cl_platform_info | `cl_platform_info` | R1 C typedef container cl_platform_info (spec-listed) |
| `CL_PLATFORM_NAME` | cl_platform_info | `cl_platform_info` | R1 C typedef container cl_platform_info (spec-listed) |
| `CL_PLATFORM_NOT_FOUND_KHR` | ErrorCodes.1000 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_PLATFORM_NUMERIC_VERSION` | cl_platform_info | `cl_platform_info` | R1 C typedef container cl_platform_info (spec-listed) |
| `CL_PLATFORM_NUMERIC_VERSION_KHR` | cl_platform_info | `cl_platform_info` | R1 C typedef container cl_platform_info (spec-listed) |
| `CL_PLATFORM_PROFILE` | cl_platform_info | `cl_platform_info` | R1 C typedef container cl_platform_info (spec-listed) |
| `CL_PLATFORM_SEMAPHORE_EXPORT_HANDLE_TYPES_KHR` | enums.2000 | `cl_platform_info` | spec evidence [cl_platform_info] G3 new-enums list |
| `CL_PLATFORM_SEMAPHORE_IMPORT_HANDLE_TYPES_KHR` | enums.2000 | `cl_platform_info` | spec evidence [cl_platform_info] G3 new-enums list |
| `CL_PLATFORM_SEMAPHORE_TYPES_KHR` | enums.2000 | `cl_platform_info` | spec evidence [cl_platform_info] G3 new-enums list |
| `CL_PLATFORM_SVM_TYPE_CAPABILITIES_KHR` | cl_platform_info | `cl_platform_info` | R1 C typedef container cl_platform_info (container-declared) |
| `CL_PLATFORM_UNLOADABLE_KHR` | cl_platform_info | `cl_platform_info` | R1 C typedef container cl_platform_info (spec-listed) |
| `CL_PLATFORM_VENDOR` | cl_platform_info | `cl_platform_info` | R1 C typedef container cl_platform_info (spec-listed) |
| `CL_PLATFORM_VERSION` | cl_platform_info | `cl_platform_info` | R1 C typedef container cl_platform_info (spec-listed) |
| `CL_PREFERRED_DEVICES_FOR_D3D10_KHR` | enums.4010 | `cl_d3d10_device_set_khr` | spec evidence [cl_d3d10_device_set_khr] G3 new-enums list |
| `CL_PREFERRED_DEVICES_FOR_D3D11_KHR` | enums.4010 | `cl_d3d11_device_set_khr` | spec evidence [cl_d3d11_device_set_khr] G3 new-enums list |
| `CL_PREFERRED_DEVICES_FOR_DX9_INTEL` | enums.4010 | — (ungrouped, GL precedent) |  |
| `CL_PREFERRED_DEVICES_FOR_DX9_MEDIA_ADAPTER_KHR` | enums.2000 | `cl_dx9_media_adapter_set_khr` | spec evidence [cl_dx9_media_adapter_set_khr] G3 new-enums list |
| `CL_PREFERRED_DEVICES_FOR_VA_API_INTEL` | enums.4090 | — (ungrouped, GL precedent) |  |
| `CL_PRINTF_BUFFERSIZE_ARM` | enums.40B0 | `cl_context_properties` | manual: cl_arm_printf: context creation property value (size_t) |
| `CL_PRINTF_CALLBACK_ARM` | enums.40B0 | `cl_context_properties` | manual: cl_arm_printf: context creation property (Table 7 param_name + value pair) |
| `CL_PROFILING_COMMAND_COMPLETE` | cl_device_info | `cl_profiling_info` | spec evidence [cl_profiling_info] value cell col0 (List of supported param_names by {clGetEventProfil) |
| `CL_PROFILING_COMMAND_END` | cl_device_info | `cl_profiling_info` | spec evidence [cl_profiling_info] value cell col0 (List of supported param_names by {clGetEventProfil) |
| `CL_PROFILING_COMMAND_QUEUED` | cl_device_info | `cl_profiling_info` | spec evidence [cl_profiling_info] value cell col0 (List of supported param_names by {clGetEventProfil) |
| `CL_PROFILING_COMMAND_START` | cl_device_info | `cl_profiling_info` | spec evidence [cl_profiling_info] value cell col0 (List of supported param_names by {clGetEventProfil) |
| `CL_PROFILING_COMMAND_SUBMIT` | cl_device_info | `cl_profiling_info` | spec evidence [cl_profiling_info] value cell col0 (List of supported param_names by {clGetEventProfil) |
| `CL_PROFILING_INFO_NOT_AVAILABLE` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_PROGRAM_BINARIES` | cl_device_info | `cl_program_info` | spec evidence [cl_program_info] value cell col0 (List of supported param_names by {clGetProgramInfo) |
| `CL_PROGRAM_BINARY_SIZES` | cl_device_info | `cl_program_info` | spec evidence [cl_program_info] value cell col0 (List of supported param_names by {clGetProgramInfo) |
| `CL_PROGRAM_BINARY_TYPE` | cl_device_info | `cl_program_build_info` | spec evidence [cl_program_build_info] value cell col0 (List of supported param_names by {clGetProgramBuil) |
| `CL_PROGRAM_BINARY_TYPE_COMPILED_OBJECT` | cl_program_binary_type | `cl_program_binary_type` | R1 C typedef container cl_program_binary_type (spec-listed) |
| `CL_PROGRAM_BINARY_TYPE_EXECUTABLE` | cl_program_binary_type | `cl_program_binary_type` | R1 C typedef container cl_program_binary_type (spec-listed) |
| `CL_PROGRAM_BINARY_TYPE_INTERMEDIATE` | enums.40E0 | `cl_program_binary_type` | spec evidence [cl_program_binary_type] G3 new-enums list |
| `CL_PROGRAM_BINARY_TYPE_LIBRARY` | cl_program_binary_type | `cl_program_binary_type` | R1 C typedef container cl_program_binary_type (spec-listed) |
| `CL_PROGRAM_BINARY_TYPE_NONE` | cl_program_binary_type | `cl_program_binary_type` | R1 C typedef container cl_program_binary_type (spec-listed) |
| `CL_PROGRAM_BUILD_GLOBAL_VARIABLE_TOTAL_SIZE` | cl_device_info | `cl_program_build_info` | spec evidence [cl_program_build_info] value cell col0 (List of supported param_names by {clGetProgramBuil) |
| `CL_PROGRAM_BUILD_LOG` | cl_device_info | `cl_program_build_info` | spec evidence [cl_program_build_info] value cell col0 (List of supported param_names by {clGetProgramBuil) |
| `CL_PROGRAM_BUILD_OPTIONS` | cl_device_info | `cl_program_build_info` | spec evidence [cl_program_build_info] value cell col0 (List of supported param_names by {clGetProgramBuil) |
| `CL_PROGRAM_BUILD_STATUS` | cl_device_info | `cl_program_build_info` | spec evidence [cl_program_build_info] value cell col0 (List of supported param_names by {clGetProgramBuil) |
| `CL_PROGRAM_CONTEXT` | cl_device_info | `cl_program_info` | spec evidence [cl_program_info] value cell col0 (List of supported param_names by {clGetProgramInfo) |
| `CL_PROGRAM_DEVICES` | cl_device_info | `cl_program_info` | spec evidence [cl_program_info] value cell col0 (List of supported param_names by {clGetProgramInfo) |
| `CL_PROGRAM_HOST_PIPE_NAMES_INTEL` | enums.4210 | `cl_program_info` | manual: cl_intel_program_scope_host_pipe param_name of clGetProgramInfo |
| `CL_PROGRAM_IL` | cl_device_info | `cl_program_info` | spec evidence [cl_program_info] value cell col0 (List of supported param_names by {clGetProgramInfo) |
| `CL_PROGRAM_IL_KHR` | cl_device_info | `cl_platform_info` | spec evidence [cl_platform_info] G3 new-enums list |
| `CL_PROGRAM_KERNEL_NAMES` | cl_device_info | `cl_program_info` | spec evidence [cl_program_info] value cell col0 (List of supported param_names by {clGetProgramInfo) |
| `CL_PROGRAM_NUM_DEVICES` | cl_device_info | `cl_program_info` | spec evidence [cl_program_info] value cell col0 (List of supported param_names by {clGetProgramInfo) |
| `CL_PROGRAM_NUM_HOST_PIPES_INTEL` | enums.4210 | `cl_program_info` | manual: cl_intel_program_scope_host_pipe param_name of clGetProgramInfo |
| `CL_PROGRAM_NUM_KERNELS` | cl_device_info | `cl_program_info` | spec evidence [cl_program_info] value cell col0 (List of supported param_names by {clGetProgramInfo) |
| `CL_PROGRAM_REFERENCE_COUNT` | cl_device_info | `cl_program_info` | spec evidence [cl_program_info] value cell col0 (List of supported param_names by {clGetProgramInfo) |
| `CL_PROGRAM_SCOPE_GLOBAL_CTORS_PRESENT` | cl_device_info | `cl_program_info` | spec evidence [cl_program_info] value cell col0 (List of supported param_names by {clGetProgramInfo) |
| `CL_PROGRAM_SCOPE_GLOBAL_DTORS_PRESENT` | cl_device_info | `cl_program_info` | spec evidence [cl_program_info] value cell col0 (List of supported param_names by {clGetProgramInfo) |
| `CL_PROGRAM_SOURCE` | cl_device_info | `cl_program_info` | spec evidence [cl_program_info] value cell col0 (List of supported param_names by {clGetProgramInfo) |
| `CL_PROPERTIES_LIST_END_EXT` | MiscNumbers | — (ungrouped, GL precedent) |  |
| `CL_QUEUED` | clCommandExecutionStatus | `clCommandExecutionStatus` | manual: core command-execution-status value set of clGetEventInfo/CL_EVENT_COMMAND_EXECUTION_STATUS (registry type clCommandExecutionStatus; + cl_img_ |
| `CL_QUEUE_CAPABILITY_BARRIER_INTEL` | cl_command_queue_capabilities_intel | `cl_command_queue_capabilities_intel` | R1 C typedef container cl_command_queue_capabilities_intel (container-declared) |
| `CL_QUEUE_CAPABILITY_CREATE_CROSS_QUEUE_EVENTS_INTEL` | cl_command_queue_capabilities_intel | `cl_command_queue_capabilities_intel` | R1 C typedef container cl_command_queue_capabilities_intel (container-declared) |
| `CL_QUEUE_CAPABILITY_CREATE_SINGLE_QUEUE_EVENTS_INTEL` | cl_command_queue_capabilities_intel | `cl_command_queue_capabilities_intel` | R1 C typedef container cl_command_queue_capabilities_intel (container-declared) |
| `CL_QUEUE_CAPABILITY_CROSS_QUEUE_EVENT_WAIT_LIST_INTEL` | cl_command_queue_capabilities_intel | `cl_command_queue_capabilities_intel` | R1 C typedef container cl_command_queue_capabilities_intel (container-declared) |
| `CL_QUEUE_CAPABILITY_FILL_BUFFER_INTEL` | cl_command_queue_capabilities_intel | `cl_command_queue_capabilities_intel` | R1 C typedef container cl_command_queue_capabilities_intel (container-declared) |
| `CL_QUEUE_CAPABILITY_FILL_IMAGE_INTEL` | cl_command_queue_capabilities_intel | `cl_command_queue_capabilities_intel` | R1 C typedef container cl_command_queue_capabilities_intel (container-declared) |
| `CL_QUEUE_CAPABILITY_KERNEL_INTEL` | cl_command_queue_capabilities_intel | `cl_command_queue_capabilities_intel` | R1 C typedef container cl_command_queue_capabilities_intel (container-declared) |
| `CL_QUEUE_CAPABILITY_MAP_BUFFER_INTEL` | cl_command_queue_capabilities_intel | `cl_command_queue_capabilities_intel` | R1 C typedef container cl_command_queue_capabilities_intel (container-declared) |
| `CL_QUEUE_CAPABILITY_MAP_IMAGE_INTEL` | cl_command_queue_capabilities_intel | `cl_command_queue_capabilities_intel` | R1 C typedef container cl_command_queue_capabilities_intel (container-declared) |
| `CL_QUEUE_CAPABILITY_MARKER_INTEL` | cl_command_queue_capabilities_intel | `cl_command_queue_capabilities_intel` | R1 C typedef container cl_command_queue_capabilities_intel (container-declared) |
| `CL_QUEUE_CAPABILITY_SINGLE_QUEUE_EVENT_WAIT_LIST_INTEL` | cl_command_queue_capabilities_intel | `cl_command_queue_capabilities_intel` | R1 C typedef container cl_command_queue_capabilities_intel (container-declared) |
| `CL_QUEUE_CAPABILITY_TRANSFER_BUFFER_IMAGE_INTEL` | cl_command_queue_capabilities_intel | `cl_command_queue_capabilities_intel` | R1 C typedef container cl_command_queue_capabilities_intel (container-declared) |
| `CL_QUEUE_CAPABILITY_TRANSFER_BUFFER_INTEL` | cl_command_queue_capabilities_intel | `cl_command_queue_capabilities_intel` | R1 C typedef container cl_command_queue_capabilities_intel (container-declared) |
| `CL_QUEUE_CAPABILITY_TRANSFER_BUFFER_RECT_INTEL` | cl_command_queue_capabilities_intel | `cl_command_queue_capabilities_intel` | R1 C typedef container cl_command_queue_capabilities_intel (container-declared) |
| `CL_QUEUE_CAPABILITY_TRANSFER_IMAGE_BUFFER_INTEL` | cl_command_queue_capabilities_intel | `cl_command_queue_capabilities_intel` | R1 C typedef container cl_command_queue_capabilities_intel (container-declared) |
| `CL_QUEUE_CAPABILITY_TRANSFER_IMAGE_INTEL` | cl_command_queue_capabilities_intel | `cl_command_queue_capabilities_intel` | R1 C typedef container cl_command_queue_capabilities_intel (container-declared) |
| `CL_QUEUE_COMPUTE_UNIT_LIMIT_ARM` | enums.41E0 | `cl_command_queue_properties` | manual: cl_arm_scheduling_controls L79-85 + Table 9 queue creation properties |
| `CL_QUEUE_CONTEXT` | cl_device_info | `cl_command_queue_info` | spec evidence [cl_command_queue_info] value cell col0 (List of supported param_names by {clGetCommandQueu) |
| `CL_QUEUE_DEFAULT_CAPABILITIES_INTEL` | Constants.cl_intel_command_queue_families | `cl_command_queue_capabilities_intel` | spec evidence [cl_command_queue_capabilities_intel] G4 typedef+define |
| `CL_QUEUE_DEFERRED_FLUSH_ARM` | enums.41E0 | `cl_command_queue_properties` | manual: cl_arm_scheduling_controls L79-85 + Table 9 queue creation properties |
| `CL_QUEUE_DEVICE` | cl_device_info | `cl_command_queue_info` | spec evidence [cl_command_queue_info] value cell col0 (List of supported param_names by {clGetCommandQueu) |
| `CL_QUEUE_DEVICE_DEFAULT` | cl_device_info | `cl_command_queue_info` | spec evidence [cl_command_queue_info] value cell col0 (List of supported param_names by {clGetCommandQueu) |
| `CL_QUEUE_FAMILY_INTEL` | enums.4180 | `cl_command_queue_info`, `cl_command_queue_properties` | spec evidence [cl_command_queue_info] G4 sentence+define; spec evidence [cl_command_queue_properties] value cell col0 (List of supported queue creatio |
| `CL_QUEUE_FAMILY_MAX_NAME_SIZE_INTEL` | Constants.cl_intel_command_queue_families | `cl_command_queue_info` | spec evidence [cl_command_queue_info] G4 sentence+define |
| `CL_QUEUE_INDEX_INTEL` | enums.4180 | `cl_command_queue_info`, `cl_command_queue_properties` | spec evidence [cl_command_queue_info] G4 sentence+define; spec evidence [cl_command_queue_properties] value cell col0 (List of supported queue creatio |
| `CL_QUEUE_JOB_SLOT_ARM` | enums.41E0 | — (ungrouped, GL precedent) |  |
| `CL_QUEUE_KERNEL_BATCHING_ARM` | enums.41E0 | `cl_command_queue_properties` | manual: cl_arm_scheduling_controls L79-85 + Table 9 queue creation properties |
| `CL_QUEUE_NO_SYNC_OPERATIONS_INTEL` | cl_command_queue_properties | `cl_command_queue_properties` | R1 C typedef container cl_command_queue_properties (container-declared) |
| `CL_QUEUE_ON_DEVICE` | cl_command_queue_properties | `cl_command_queue_properties` | R1 C typedef container cl_command_queue_properties (container-declared) |
| `CL_QUEUE_ON_DEVICE_DEFAULT` | cl_command_queue_properties | `cl_command_queue_properties` | R1 C typedef container cl_command_queue_properties (container-declared) |
| `CL_QUEUE_OUT_OF_ORDER_EXEC_MODE_ENABLE` | cl_command_queue_properties | `cl_command_queue_properties` | R1 C typedef container cl_command_queue_properties (spec-listed) |
| `CL_QUEUE_PRIORITY_HIGH_KHR` | cl_queue_priority_khr | `cl_queue_priority_khr` | R1 C typedef container cl_queue_priority_khr (spec-listed) |
| `CL_QUEUE_PRIORITY_KHR` | cl_device_info | `cl_command_queue_properties`, `cl_queue_properties` | spec evidence [cl_command_queue_properties] value cell col0 (List of supported queue creation properties by {cl); spec evidence [cl_queue_properties]  |
| `CL_QUEUE_PRIORITY_LOW_KHR` | cl_queue_priority_khr | `cl_queue_priority_khr` | R1 C typedef container cl_queue_priority_khr (spec-listed) |
| `CL_QUEUE_PRIORITY_MED_KHR` | cl_queue_priority_khr | `cl_queue_priority_khr` | R1 C typedef container cl_queue_priority_khr (spec-listed) |
| `CL_QUEUE_PROFILING_ENABLE` | cl_command_queue_properties | `cl_command_queue_properties` | R1 C typedef container cl_command_queue_properties (spec-listed) |
| `CL_QUEUE_PROPERTIES` | cl_device_info | `cl_command_queue_info`, `cl_command_queue_properties` | spec evidence [cl_command_queue_info] value cell col0 (List of supported param_names by {clGetCommandQueu); spec evidence [cl_command_queue_properties |
| `CL_QUEUE_PROPERTIES_ARRAY` | cl_device_info | `cl_command_queue_info` | spec evidence [cl_command_queue_info] value cell col0 (List of supported param_names by {clGetCommandQueu) |
| `CL_QUEUE_REFERENCE_COUNT` | cl_device_info | `cl_command_queue_info` | spec evidence [cl_command_queue_info] value cell col0 (List of supported param_names by {clGetCommandQueu) |
| `CL_QUEUE_RESERVED_QCOM` | cl_command_queue_properties | `cl_command_queue_properties` | R1 C typedef container cl_command_queue_properties (container-declared) |
| `CL_QUEUE_SIZE` | cl_device_info | `cl_command_queue_info`, `cl_command_queue_properties` | spec evidence [cl_command_queue_info] value cell col0 (List of supported param_names by {clGetCommandQueu); spec evidence [cl_command_queue_properties |
| `CL_QUEUE_THREAD_LOCAL_EXEC_ENABLE_INTEL` | cl_command_queue_properties | `cl_command_queue_properties` | R1 C typedef container cl_command_queue_properties (container-declared) |
| `CL_QUEUE_THROTTLE_HIGH_KHR` | cl_queue_throttle_khr | `cl_queue_throttle_khr` | R1 C typedef container cl_queue_throttle_khr (spec-listed) |
| `CL_QUEUE_THROTTLE_KHR` | cl_device_info | `cl_command_queue_properties`, `cl_queue_properties` | spec evidence [cl_command_queue_properties] value cell col0 (List of supported queue creation properties by {cl); spec evidence [cl_queue_properties]  |
| `CL_QUEUE_THROTTLE_LOW_KHR` | cl_queue_throttle_khr | `cl_queue_throttle_khr` | R1 C typedef container cl_queue_throttle_khr (spec-listed) |
| `CL_QUEUE_THROTTLE_MED_KHR` | cl_queue_throttle_khr | `cl_queue_throttle_khr` | R1 C typedef container cl_queue_throttle_khr (spec-listed) |
| `CL_R` | cl_device_info | `cl_channel_order` | spec evidence [cl_channel_order] value cell col0 (List of supported Image Channel Order Values) |
| `CL_RA` | cl_device_info | `cl_channel_order` | spec evidence [cl_channel_order] value cell col0 (Image Channel Order mapping) |
| `CL_READ_ONLY_CACHE` | cl_device_mem_cache_type | `cl_device_mem_cache_type` | R1 C typedef container cl_device_mem_cache_type (spec-listed) |
| `CL_READ_WRITE_CACHE` | cl_device_mem_cache_type | `cl_device_mem_cache_type` | R1 C typedef container cl_device_mem_cache_type (spec-listed) |
| `CL_RG` | cl_device_info | `cl_channel_order` | spec evidence [cl_channel_order] value cell col0 (List of supported Image Channel Order Values) |
| `CL_RGB` | cl_device_info | `cl_channel_order` | spec evidence [cl_channel_order] value cell col0 (List of supported Image Channel Order Values) |
| `CL_RGBA` | cl_device_info | `cl_channel_order` | spec evidence [cl_channel_order] value cell col0 (List of supported Image Channel Order Values) |
| `CL_RGBx` | cl_device_info | `cl_channel_order` | manual: core spec image channel order value set; appendix_e 'Optional image formats'; cl_device_info mega-container token; no spec value-set found — l |
| `CL_RGx` | cl_device_info | `cl_channel_order` | manual: core spec image channel order value set; appendix_e 'Optional image formats'; cl_device_info mega-container token; no spec value-set found — l |
| `CL_RUNNING` | clCommandExecutionStatus | `clCommandExecutionStatus` | manual: core command-execution-status value set of clGetEventInfo/CL_EVENT_COMMAND_EXECUTION_STATUS (registry type clCommandExecutionStatus; + cl_img_ |
| `CL_Rx` | cl_device_info | `cl_channel_order` | manual: core spec image channel order value set; appendix_e 'Optional image formats'; cl_device_info mega-container token; no spec value-set found — l |
| `CL_SAFETY_FAULT_IMG` | ErrorCodes.1122 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_SAMPLER_ADDRESSING_MODE` | cl_device_info | `cl_sampler_info`, `cl_sampler_properties` | spec evidence [cl_sampler_info] value cell col0 (List of supported param_names by {clGetSamplerInfo); spec evidence [cl_sampler_properties] value cell |
| `CL_SAMPLER_CONTEXT` | cl_device_info | `cl_sampler_info` | spec evidence [cl_sampler_info] value cell col0 (List of supported param_names by {clGetSamplerInfo) |
| `CL_SAMPLER_FILTER_MODE` | cl_device_info | `cl_sampler_info`, `cl_sampler_properties` | spec evidence [cl_sampler_info] value cell col0 (List of supported param_names by {clGetSamplerInfo); spec evidence [cl_sampler_properties] value cell |
| `CL_SAMPLER_LOD_MAX` | cl_device_info | `cl_sampler_properties` | manual: opencl_runtime_layer L8782+: 'List of supported sampler creation properties by clCreateSamplerWithProperties' (KHR-inherited, sibling _KHR var |
| `CL_SAMPLER_LOD_MAX_KHR` | cl_device_info | `cl_sampler_properties` | spec evidence [cl_sampler_properties] value cell col0 (List of supported sampler creation properties by {) |
| `CL_SAMPLER_LOD_MIN` | cl_device_info | `cl_sampler_properties` | manual: opencl_runtime_layer L8782+: 'List of supported sampler creation properties by clCreateSamplerWithProperties' (KHR-inherited, sibling _KHR var |
| `CL_SAMPLER_LOD_MIN_KHR` | cl_device_info | `cl_sampler_properties` | spec evidence [cl_sampler_properties] value cell col0 (List of supported sampler creation properties by {) |
| `CL_SAMPLER_MIP_FILTER_MODE` | cl_device_info | `cl_sampler_properties` | manual: opencl_runtime_layer: sampler creation property (KHR-inherited, sibling _KHR already cl_sampler_properties); cl_device_info mega-container tok |
| `CL_SAMPLER_MIP_FILTER_MODE_KHR` | cl_device_info | `cl_sampler_properties` | spec evidence [cl_sampler_properties] value cell col0 (List of supported sampler creation properties by {) |
| `CL_SAMPLER_NORMALIZED_COORDS` | cl_device_info | `cl_sampler_info`, `cl_sampler_properties` | spec evidence [cl_sampler_info] value cell col0 (List of supported param_names by {clGetSamplerInfo); spec evidence [cl_sampler_properties] value cell |
| `CL_SAMPLER_PROPERTIES` | cl_device_info | `cl_sampler_info` | spec evidence [cl_sampler_info] value cell col0 (List of supported param_names by {clGetSamplerInfo) |
| `CL_SAMPLER_REFERENCE_COUNT` | cl_device_info | `cl_sampler_info` | spec evidence [cl_sampler_info] value cell col0 (List of supported param_names by {clGetSamplerInfo) |
| `CL_SCHAR_MAX` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_SCHAR_MIN` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_SEMAPHORE_CONTEXT_KHR` | enums.2000 | `cl_semaphore_info_khr` | spec evidence [cl_semaphore_info_khr] G3 new-enums list |
| `CL_SEMAPHORE_DEVICE_HANDLE_LIST_END_KHR` | MiscNumbers | `cl_semaphore_info_khr` | spec evidence [cl_semaphore_info_khr] G3 new-enums list |
| `CL_SEMAPHORE_DEVICE_HANDLE_LIST_KHR` | enums.2000 | `cl_semaphore_info_khr` | spec evidence [cl_semaphore_info_khr] G3 new-enums list |
| `CL_SEMAPHORE_EXPORTABLE_KHR` | enums.2000 | `cl_semaphore_info_khr` | spec evidence [cl_semaphore_info_khr] G3 new-enums list |
| `CL_SEMAPHORE_EXPORT_HANDLE_TYPES_KHR` | enums.2000 | `cl_semaphore_properties_khr` | spec evidence [cl_semaphore_properties_khr] G3 new-enums list |
| `CL_SEMAPHORE_EXPORT_HANDLE_TYPES_LIST_END_KHR` | MiscNumbers | `cl_semaphore_properties_khr` | spec evidence [cl_semaphore_properties_khr] G3 new-enums list |
| `CL_SEMAPHORE_FAST_PATH_IMG` | enums.4220 | — (ungrouped, GL precedent) |  |
| `CL_SEMAPHORE_HANDLE_D3D12_FENCE_KHR` | enums.2000 | `cl_external_semaphore_handle_type_khr` | spec evidence [cl_external_semaphore_handle_type_khr] G3 new-enums list |
| `CL_SEMAPHORE_HANDLE_OPAQUE_FD_KHR` | enums.2000 | `cl_external_semaphore_handle_type_khr` | spec evidence [cl_external_semaphore_handle_type_khr] G3 new-enums list |
| `CL_SEMAPHORE_HANDLE_OPAQUE_WIN32_KHR` | enums.2000 | `cl_external_semaphore_handle_type_khr` | spec evidence [cl_external_semaphore_handle_type_khr] G3 new-enums list |
| `CL_SEMAPHORE_HANDLE_OPAQUE_WIN32_KMT_KHR` | enums.2000 | `cl_external_semaphore_handle_type_khr` | spec evidence [cl_external_semaphore_handle_type_khr] G3 new-enums list |
| `CL_SEMAPHORE_HANDLE_OPAQUE_WIN32_NAME_KHR` | enums.2000 | `cl_external_semaphore_handle_type_khr` | spec evidence [cl_external_semaphore_handle_type_khr] G3 new-enums list |
| `CL_SEMAPHORE_HANDLE_SYNC_FD_KHR` | enums.2000 | `cl_external_semaphore_handle_type_khr` | spec evidence [cl_external_semaphore_handle_type_khr] G3 new-enums list |
| `CL_SEMAPHORE_PAYLOAD_KHR` | enums.2000 | `cl_semaphore_info_khr` | spec evidence [cl_semaphore_info_khr] G3 new-enums list |
| `CL_SEMAPHORE_PROPERTIES_KHR` | enums.2000 | `cl_semaphore_info_khr` | spec evidence [cl_semaphore_info_khr] G3 new-enums list |
| `CL_SEMAPHORE_REFERENCE_COUNT_KHR` | enums.2000 | `cl_semaphore_info_khr` | spec evidence [cl_semaphore_info_khr] G3 new-enums list |
| `CL_SEMAPHORE_TYPE_BINARY_KHR` | cl_semaphore_type_khr | `cl_semaphore_type_khr` | R1 C typedef container cl_semaphore_type_khr (spec-listed) |
| `CL_SEMAPHORE_TYPE_KHR` | enums.2000 | `cl_semaphore_info_khr` | spec evidence [cl_semaphore_info_khr] G3 new-enums list |
| `CL_SHRT_MAX` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_SHRT_MIN` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_SIGNED_INT16` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_SIGNED_INT32` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_SIGNED_INT8` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_SNORM_INT16` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_SNORM_INT8` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_STRUCTURE_TYPE_MUTABLE_DISPATCH_CONFIG_KHR` | cl_command_buffer_update_type_khr | `cl_command_buffer_update_type_khr` | R1 C typedef container cl_command_buffer_update_type_khr (spec-listed) |
| `CL_SUBMITTED` | clCommandExecutionStatus | `clCommandExecutionStatus` | manual: core command-execution-status value set of clGetEventInfo/CL_EVENT_COMMAND_EXECUTION_STATUS (registry type clCommandExecutionStatus; + cl_img_ |
| `CL_SUCCESS` | ErrorCodes.0 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_SVM_ALLOC_ACCESS_DEVICE_NOREAD_KHR` | cl_svm_alloc_access_flags_khr | `cl_svm_alloc_access_flags_khr` | R1 C typedef container cl_svm_alloc_access_flags_khr (container-declared) |
| `CL_SVM_ALLOC_ACCESS_DEVICE_NOWRITE_KHR` | cl_svm_alloc_access_flags_khr | `cl_svm_alloc_access_flags_khr` | R1 C typedef container cl_svm_alloc_access_flags_khr (container-declared) |
| `CL_SVM_ALLOC_ACCESS_FLAGS_KHR` | enums.2000 | `cl_svm_alloc_properties_khr` | manual: cl_khr_unified_svm accepted as properties of clSVMAlloc |
| `CL_SVM_ALLOC_ACCESS_HOST_NOREAD_KHR` | cl_svm_alloc_access_flags_khr | `cl_svm_alloc_access_flags_khr` | R1 C typedef container cl_svm_alloc_access_flags_khr (container-declared) |
| `CL_SVM_ALLOC_ACCESS_HOST_NOWRITE_KHR` | cl_svm_alloc_access_flags_khr | `cl_svm_alloc_access_flags_khr` | R1 C typedef container cl_svm_alloc_access_flags_khr (container-declared) |
| `CL_SVM_ALLOC_ALIGNMENT_KHR` | enums.2000 | `cl_svm_alloc_properties_khr` | manual: cl_khr_unified_svm accepted as properties of clSVMAlloc |
| `CL_SVM_ALLOC_ASSOCIATED_DEVICE_HANDLE_KHR` | enums.2000 | `cl_svm_alloc_properties_khr` | manual: cl_khr_unified_svm accepted as properties of clSVMAlloc |
| `CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_IMG` | enums.4220 | `cl_svm_alloc_properties_khr` | manual: cl_img_unified_svm_external_memory_dma_buf: new row in SVM Allocation Properties table |
| `CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_VIRTUAL_ADDRESS_IMG` | enums.4220 | `cl_svm_alloc_properties_khr` | manual: cl_img_unified_svm_external_memory_dma_buf: new row in SVM Allocation Properties table |
| `CL_SVM_CAPABILITY_CONCURRENT_ACCESS_KHR` | cl_svm_capabilities_khr | `cl_svm_capabilities_khr` | R1 C typedef container cl_svm_capabilities_khr (container-declared) |
| `CL_SVM_CAPABILITY_CONCURRENT_ATOMIC_ACCESS_KHR` | cl_svm_capabilities_khr | `cl_svm_capabilities_khr` | R1 C typedef container cl_svm_capabilities_khr (container-declared) |
| `CL_SVM_CAPABILITY_CONTEXT_ACCESS_KHR` | cl_svm_capabilities_khr | `cl_svm_capabilities_khr` | R1 C typedef container cl_svm_capabilities_khr (container-declared) |
| `CL_SVM_CAPABILITY_DEVICE_ATOMIC_ACCESS_KHR` | cl_svm_capabilities_khr | `cl_svm_capabilities_khr` | R1 C typedef container cl_svm_capabilities_khr (container-declared) |
| `CL_SVM_CAPABILITY_DEVICE_OWNED_KHR` | cl_svm_capabilities_khr | `cl_svm_capabilities_khr` | R1 C typedef container cl_svm_capabilities_khr (container-declared) |
| `CL_SVM_CAPABILITY_DEVICE_READ_KHR` | cl_svm_capabilities_khr | `cl_svm_capabilities_khr` | R1 C typedef container cl_svm_capabilities_khr (container-declared) |
| `CL_SVM_CAPABILITY_DEVICE_UNASSOCIATED_KHR` | cl_svm_capabilities_khr | `cl_svm_capabilities_khr` | R1 C typedef container cl_svm_capabilities_khr (container-declared) |
| `CL_SVM_CAPABILITY_DEVICE_WRITE_KHR` | cl_svm_capabilities_khr | `cl_svm_capabilities_khr` | R1 C typedef container cl_svm_capabilities_khr (container-declared) |
| `CL_SVM_CAPABILITY_HOST_MAP_KHR` | cl_svm_capabilities_khr | `cl_svm_capabilities_khr` | R1 C typedef container cl_svm_capabilities_khr (container-declared) |
| `CL_SVM_CAPABILITY_HOST_OWNED_KHR` | cl_svm_capabilities_khr | `cl_svm_capabilities_khr` | R1 C typedef container cl_svm_capabilities_khr (container-declared) |
| `CL_SVM_CAPABILITY_HOST_READ_KHR` | cl_svm_capabilities_khr | `cl_svm_capabilities_khr` | R1 C typedef container cl_svm_capabilities_khr (container-declared) |
| `CL_SVM_CAPABILITY_HOST_WRITE_KHR` | cl_svm_capabilities_khr | `cl_svm_capabilities_khr` | R1 C typedef container cl_svm_capabilities_khr (container-declared) |
| `CL_SVM_CAPABILITY_INDIRECT_ACCESS_KHR` | cl_svm_capabilities_khr | `cl_svm_capabilities_khr` | R1 C typedef container cl_svm_capabilities_khr (container-declared) |
| `CL_SVM_CAPABILITY_SINGLE_ADDRESS_SPACE_KHR` | cl_svm_capabilities_khr | `cl_svm_capabilities_khr` | R1 C typedef container cl_svm_capabilities_khr (container-declared) |
| `CL_SVM_CAPABILITY_SYSTEM_ALLOCATED_KHR` | cl_svm_capabilities_khr | `cl_svm_capabilities_khr` | R1 C typedef container cl_svm_capabilities_khr (container-declared) |
| `CL_SVM_INFO_ACCESS_FLAGS_KHR` | enums.2000 | `cl_svm_pointer_info_khr` | manual: cl_khr_unified_svm: member of cl_svm_pointer_info_khr value set (param_names of clSVMGetInfo) |
| `CL_SVM_INFO_ASSOCIATED_DEVICE_HANDLE_KHR` | enums.4190 | `cl_svm_pointer_info_khr` | manual: cl_khr_unified_svm: member of cl_svm_pointer_info_khr value set (param_names of clSVMGetInfo) |
| `CL_SVM_INFO_BASE_PTR_KHR` | enums.4190 | `cl_svm_pointer_info_khr` | manual: cl_khr_unified_svm: member of cl_svm_pointer_info_khr (param_names of clSVMGetInfo) |
| `CL_SVM_INFO_CAPABILITIES_KHR` | enums.2000 | `cl_svm_pointer_info_khr` | manual: cl_khr_unified_svm: member of cl_svm_pointer_info_khr (param_names of clSVMGetInfo) |
| `CL_SVM_INFO_PROPERTIES_KHR` | enums.2000 | `cl_svm_pointer_info_khr` | manual: cl_khr_unified_svm: member of cl_svm_pointer_info_khr (param_names of clSVMGetInfo) |
| `CL_SVM_INFO_SIZE_KHR` | enums.4190 | `cl_svm_pointer_info_khr` | manual: cl_khr_unified_svm: member of cl_svm_pointer_info_khr (param_names of clSVMGetInfo) |
| `CL_SVM_INFO_TYPE_INDEX_KHR` | enums.2000 | `cl_svm_pointer_info_khr` | manual: cl_khr_unified_svm: member of cl_svm_pointer_info_khr (param_names of clSVMGetInfo) |
| `CL_TRUE` | cl_bool | `cl_bool` | R1 C typedef container cl_bool (container-declared) |
| `CL_UCHAR_MAX` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_UINT_MAX` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_ULONG_MAX` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_UNIFIED_SHARED_MEMORY_ACCESS_INTEL` | cl_device_unified_shared_memory_capabilities_intel | `cl_device_unified_shared_memory_capabilities_intel` | R1 C typedef container cl_device_unified_shared_memory_capabilities_intel (container-declared) |
| `CL_UNIFIED_SHARED_MEMORY_ATOMIC_ACCESS_INTEL` | cl_device_unified_shared_memory_capabilities_intel | `cl_device_unified_shared_memory_capabilities_intel` | R1 C typedef container cl_device_unified_shared_memory_capabilities_intel (container-declared) |
| `CL_UNIFIED_SHARED_MEMORY_CONCURRENT_ACCESS_INTEL` | cl_device_unified_shared_memory_capabilities_intel | `cl_device_unified_shared_memory_capabilities_intel` | R1 C typedef container cl_device_unified_shared_memory_capabilities_intel (container-declared) |
| `CL_UNIFIED_SHARED_MEMORY_CONCURRENT_ATOMIC_ACCESS_INTEL` | cl_device_unified_shared_memory_capabilities_intel | `cl_device_unified_shared_memory_capabilities_intel` | R1 C typedef container cl_device_unified_shared_memory_capabilities_intel (container-declared) |
| `CL_UNORM_INT10X6_EXT` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_UNORM_INT12X4_EXT` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_UNORM_INT14X2_EXT` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_UNORM_INT16` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_UNORM_INT24` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] G3 new-enums list |
| `CL_UNORM_INT8` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_UNORM_INT_101010` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_UNORM_INT_101010_2` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_UNORM_INT_2_101010_EXT` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_UNORM_SHORT_555` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_UNORM_SHORT_565` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_UNSIGNED_INT10X6_EXT` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_UNSIGNED_INT12X4_EXT` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_UNSIGNED_INT14X2_EXT` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_UNSIGNED_INT16` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_UNSIGNED_INT32` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_UNSIGNED_INT8` | cl_device_info | `cl_channel_type` | spec evidence [cl_channel_type] value cell col0 (List of supported Image Channel Data Types) |
| `CL_UNSIGNED_INT_RAW10_EXT` | cl_device_info | `cl_channel_type` | manual: cl_ext_image_raw10_raw12: member of image channel data type value set (cl_channel_type); cl_device_info mega-container token; no spec value-se |
| `CL_UNSIGNED_INT_RAW12_EXT` | cl_device_info | `cl_channel_type` | manual: cl_ext_image_raw10_raw12: member of image channel data type value set (cl_channel_type); cl_device_info mega-container token; no spec value-se |
| `CL_USHRT_MAX` | Constants | `C99MathConstants` | manual: api/appendix_c.asciidoc: C99 standard mathematical constants (CL_FLT_*/CL_DBL_*/CL_M_*/...) |
| `CL_UUID_SIZE` | Constants.uuid | — (ungrouped, GL precedent) |  |
| `CL_UUID_SIZE_KHR` | Constants.cl_khr_device_uuid | — (ungrouped, GL precedent) |  |
| `CL_UYVY_INTEL` | enums.4070 | `cl_channel_order` | manual: cl_intel_packed_yuv L81 image_channel_order value set |
| `CL_VA_API_DISPLAY_INTEL` | enums.4090 | — (ungrouped, GL precedent) |  |
| `CL_VA_API_MEDIA_SURFACE_ALREADY_ACQUIRED_INTEL` | ErrorCodes.1094 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_VA_API_MEDIA_SURFACE_NOT_ACQUIRED_INTEL` | ErrorCodes.1094 | `ErrorCode` | R3 cl.xml ErrorCodes container (GL precedent group=ErrorCode; spec: same set as API return values) |
| `CL_VERSION_MAJOR_BITS` | Constants.Versioning | — (ungrouped, GL precedent) |  |
| `CL_VERSION_MAJOR_BITS_KHR` | Constants.cl_khr_extended_versioning | — (ungrouped, GL precedent) |  |
| `CL_VERSION_MINOR_BITS` | Constants.Versioning | — (ungrouped, GL precedent) |  |
| `CL_VERSION_MINOR_BITS_KHR` | Constants.cl_khr_extended_versioning | — (ungrouped, GL precedent) |  |
| `CL_VERSION_PATCH_BITS` | Constants.Versioning | — (ungrouped, GL precedent) |  |
| `CL_VERSION_PATCH_BITS_KHR` | Constants.cl_khr_extended_versioning | — (ungrouped, GL precedent) |  |
| `CL_VYUY_INTEL` | enums.4070 | `cl_channel_order` | manual: cl_intel_packed_yuv L81 image_channel_order value set |
| `CL_WGL_HDC_KHR` | enums.2000 | `cl_context_properties` | spec evidence [cl_context_properties] G3 new-enums list |
| `CL_YUYV_INTEL` | enums.4070 | `cl_channel_order` | manual: cl_intel_packed_yuv L81 image_channel_order value set; spec evidence [cl_channel_order] value cell col0 (List of supported Image Channel Order |
| `CL_YV12` | enums.40D0 | `cl_channel_order` | manual: cl_img_yuv_image image_channel_order (or deprecated pre-IMG alias) |
| `CL_YV12_IMG` | enums.40D0 | `cl_channel_order` | manual: cl_img_yuv_image image_channel_order (or deprecated pre-IMG alias) |
| `CL_YVYU_INTEL` | enums.4070 | `cl_channel_order` | manual: cl_intel_packed_yuv L81 image_channel_order value set |
| `CL_sBGRA` | cl_device_info | `cl_channel_order` | manual: core spec image channel order value set; appendix_e 'Optional image formats'; cl_device_info mega-container token; no spec value-set found — l |
| `CL_sRGB` | cl_device_info | `cl_channel_order` | manual: core spec image channel order value set; appendix_e 'Optional image formats'; cl_device_info mega-container token; no spec value-set found — l |
| `CL_sRGBA` | cl_device_info | `cl_channel_order` | manual: core spec image channel order value set; appendix_e 'Optional image formats'; cl_device_info mega-container token; no spec value-set found — l |
| `CL_sRGBx` | cl_device_info | `cl_channel_order` | manual: core spec image channel order value set; appendix_e 'Optional image formats'; cl_device_info mega-container token; no spec value-set found — l |