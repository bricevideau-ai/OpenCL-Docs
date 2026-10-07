# OpenCL cl.xml enum `group` attribution — review table

Generated 2026-10-06 from cl.xml + spec sources (core + extension chapters).

## Summary

- Total enums: 1334
- Multi-group assignments: 12
- Assigned: 909; unassigned: 425

## Multi-group members (cross-cutting) — highest review priority

| token | groups | confidence | evidence |
|---|---|---|---|
| CL_COMMAND_BUFFER_CAPABILITY_SIMULTANEOUS_USE_KHR | cl_command_buffer_flags_khr, cl_device_command_buffer_capabilities_khr | high | spec corroborates member of cl_device_command_buffer_capabilities_khr; spec value-set cl_device_command_buffer_capabilities_khr (clGetDeviceInfo); spec value-set cl_command_buffer_flags_khr (clCreateC |
| CL_DEVICE_ATOMIC_MEMORY_CAPABILITIES | cl_device_atomic_capabilities, cl_device_info | high | declared container cl_device_info (no direct spec list found); spec value-set cl_device_atomic_capabilities (clGetDeviceInfo) |
| CL_DEVICE_COMMAND_BUFFER_SYNC_DEVICES_KHR | cl_command_buffer_flags_khr, cl_device_info | high | declared container cl_device_info (no direct spec list found); spec value-set cl_command_buffer_flags_khr (clCreateCommandBufferKHR) |
| CL_DEVICE_DEVICE_ENQUEUE_CAPABILITIES | cl_device_device_enqueue_capabilities, cl_device_info | high | declared container cl_device_info (no direct spec list found); spec value-set cl_device_device_enqueue_capabilities (clGetDeviceInfo) |
| CL_DEVICE_GENERIC_ADDRESS_SPACE_SUPPORT | cl_device_device_enqueue_capabilities, cl_device_info | high | declared container cl_device_info (no direct spec list found); spec value-set cl_device_device_enqueue_capabilities (clGetDeviceInfo) |
| CL_DEVICE_MUTABLE_DISPATCH_CAPABILITIES_KHR | cl_device_info, cl_mutable_dispatch_fields_khr | high | declared container cl_device_info (no direct spec list found); spec value-set cl_mutable_dispatch_fields_khr (clCommandNDRangeKernelKHR) |
| CL_DEVICE_PARTITION_BY_AFFINITY_DOMAIN | cl_device_affinity_domain, cl_device_info | high | declared container cl_device_info (no direct spec list found); spec value-set cl_device_affinity_domain (clGetDeviceInfo) |
| CL_DEVICE_SVM_ATOMICS | cl_device_atomic_capabilities, cl_device_svm_capabilities | high | declared container cl_device_svm_capabilities (no direct spec list found); spec value-set cl_device_atomic_capabilities (clGetDeviceInfo) |
| CL_KERNEL_ARG_TYPE_QUALIFIER | cl_device_info, cl_kernel_arg_type_qualifier | high | declared container cl_device_info (no direct spec list found); spec value-set cl_kernel_arg_type_qualifier (clGetKernelArgInfo) |
| CL_MEM_SVM_ATOMICS | cl_device_atomic_capabilities, cl_mem_flags | high | declared container cl_mem_flags (no direct spec list found); spec value-set cl_device_atomic_capabilities (clGetDeviceInfo) |
| CL_QUEUE_OUT_OF_ORDER_EXEC_MODE_ENABLE | cl_command_queue_properties, cl_program_binary_type | high | spec corroborates member of cl_command_queue_properties; spec value-set cl_command_queue_properties (clCreateCommandQueueWithProperties); spec value-set cl_command_queue_properties (clGetDeviceInfo);  |
| CL_QUEUE_PROPERTIES | cl_command_queue_properties, cl_device_info | high | declared container cl_device_info (no direct spec list found); spec value-set cl_command_queue_properties (clCreateCommandQueueWithProperties) |

## Unassigned (no safe group found in spec) — needs decision

- **CL_ACCELERATOR_CONTEXT_INTEL** (container=enums.4090)
- **CL_ACCELERATOR_DESCRIPTOR_INTEL** (container=enums.4090)
- **CL_ACCELERATOR_REFERENCE_COUNT_INTEL** (container=enums.4090)
- **CL_ACCELERATOR_TYPE_INTEL** (container=enums.4090)
- **CL_ADAPTER_D3D9EX_KHR** (container=enums.2000)
- **CL_ADAPTER_D3D9_KHR** (container=enums.2000)
- **CL_ADAPTER_DXVA_KHR** (container=enums.2000)
- **CL_ALL_DEVICES_FOR_D3D10_KHR** (container=enums.4010)
- **CL_ALL_DEVICES_FOR_D3D11_KHR** (container=enums.4010)
- **CL_ALL_DEVICES_FOR_DX9_INTEL** (container=enums.4010)
- **CL_ALL_DEVICES_FOR_DX9_MEDIA_ADAPTER_KHR** (container=enums.2000)
- **CL_ALL_DEVICES_FOR_VA_API_INTEL** (container=enums.4090)
- **CL_CGL_SHAREGROUP_KHR** (container=enums.2000)
- **CL_CHAR_BIT** (container=Constants)
- **CL_CHAR_MAX** (container=Constants)
- **CL_CHAR_MIN** (container=Constants)
- **CL_COMMAND_ACQUIRE_D3D10_OBJECTS_KHR** (container=enums.4010)
- **CL_COMMAND_ACQUIRE_D3D11_OBJECTS_KHR** (container=enums.4010)
- **CL_COMMAND_ACQUIRE_D3D9_OBJECTS_INTEL** (container=enums.4010)
- **CL_COMMAND_ACQUIRE_DX9_MEDIA_SURFACES_KHR** (container=enums.2000)
- **CL_COMMAND_ACQUIRE_DX9_OBJECTS_INTEL** (container=enums.4010)
- **CL_COMMAND_ACQUIRE_EGL_OBJECTS_KHR** (container=enums.2000)
- **CL_COMMAND_ACQUIRE_EXTERNAL_MEM_OBJECTS_KHR** (container=enums.2000)
- **CL_COMMAND_ACQUIRE_GRALLOC_OBJECTS_IMG** (container=enums.40D0)
- **CL_COMMAND_ACQUIRE_VA_API_MEDIA_SURFACES_INTEL** (container=enums.4090)
- **CL_COMMAND_EGL_FENCE_SYNC_OBJECT_KHR** (container=enums.2000)
- **CL_COMMAND_GENERATE_MIPMAP_IMG** (container=enums.40D0)
- **CL_COMMAND_GL_FENCE_SYNC_OBJECT_KHR** (container=enums.2000)
- **CL_COMMAND_MEMADVISE_INTEL** (container=enums.4200)
- **CL_COMMAND_MEMCPY_INTEL** (container=enums.4200)
- **CL_COMMAND_MEMFILL_INTEL** (container=enums.4200)
- **CL_COMMAND_MIGRATEMEM_INTEL** (container=enums.4200)
- **CL_COMMAND_MIGRATE_MEM_OBJECT_EXT** (container=enums.4040)
- **CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_ARBITRATION_ALGORITHM_IMG** (container=enums.4220)
- **CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_ARBITRATION_ALGORITHM_ROUND_ROBIN_IMG** (container=enums.4220)
- **CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_ARBITRATION_ALGORITHM_TASK_DEMAND_IMG** (container=enums.4220)
- **CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_EXECUTE_COUNT_IMG** (container=enums.4220)
- **CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_SCHEDULING_ALGORITHM_IMG** (container=enums.4220)
- **CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_SCHEDULING_ALGORITHM_LINEAR_ORDER_IMG** (container=enums.4220)
- **CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_SCHEDULING_ALGORITHM_MORTON_ORDER_IMG** (container=enums.4220)
- **CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_SCHEDULING_ALGORITHM_THREED_MORTON_ORDER_IMG** (container=enums.4220)
- **CL_COMMAND_QUEUE_SCHEDULING_WORK_GROUP_SCHEDULING_ALGORITHM_TWOD_MORTON_ORDER_IMG** (container=enums.4220)
- **CL_COMMAND_READ_HOST_PIPE_INTEL** (container=enums.4210)
- **CL_COMMAND_RELEASE_D3D10_OBJECTS_KHR** (container=enums.4010)
- **CL_COMMAND_RELEASE_D3D11_OBJECTS_KHR** (container=enums.4010)
- **CL_COMMAND_RELEASE_D3D9_OBJECTS_INTEL** (container=enums.4010)
- **CL_COMMAND_RELEASE_DX9_MEDIA_SURFACES_KHR** (container=enums.2000)
- **CL_COMMAND_RELEASE_DX9_OBJECTS_INTEL** (container=enums.4010)
- **CL_COMMAND_RELEASE_EGL_OBJECTS_KHR** (container=enums.2000)
- **CL_COMMAND_RELEASE_EXTERNAL_MEM_OBJECTS_KHR** (container=enums.2000)
- **CL_COMMAND_RELEASE_GRALLOC_OBJECTS_IMG** (container=enums.40D0)
- **CL_COMMAND_RELEASE_VA_API_MEDIA_SURFACES_INTEL** (container=enums.4090)
- **CL_COMMAND_SEMAPHORE_SIGNAL_KHR** (container=enums.2000)
- **CL_COMMAND_SEMAPHORE_WAIT_KHR** (container=enums.2000)
- **CL_COMMAND_SVM_FREE_ARM** (container=enums.40B0)
- **CL_COMMAND_SVM_MAP_ARM** (container=enums.40B0)
- **CL_COMMAND_SVM_MEMCPY_ARM** (container=enums.40B0)
- **CL_COMMAND_SVM_MEMFILL_ARM** (container=enums.40B0)
- **CL_COMMAND_SVM_UNMAP_ARM** (container=enums.40B0)
- **CL_COMMAND_WRITE_HOST_PIPE_INTEL** (container=enums.4210)
- **CL_CONTEXT_ADAPTER_D3D9EX_KHR** (container=enums.2000)
- **CL_CONTEXT_ADAPTER_D3D9_KHR** (container=enums.2000)
- **CL_CONTEXT_ADAPTER_DXVA_KHR** (container=enums.2000)
- **CL_CONTEXT_D3D10_DEVICE_KHR** (container=enums.4010)
- **CL_CONTEXT_D3D10_PREFER_SHARED_RESOURCES_KHR** (container=enums.4010)
- **CL_CONTEXT_D3D11_DEVICE_KHR** (container=enums.4010)
- **CL_CONTEXT_D3D11_PREFER_SHARED_RESOURCES_KHR** (container=enums.4010)
- **CL_CONTEXT_D3D9EX_DEVICE_INTEL** (container=enums.4070)
- **CL_CONTEXT_D3D9_DEVICE_INTEL** (container=enums.4010)
- **CL_CONTEXT_DXVA_DEVICE_INTEL** (container=enums.4070)
- **CL_CONTEXT_MEMORY_INITIALIZE_KHR** (container=enums.2000)
- **CL_CONTEXT_PERF_HINT_QCOM** (container=enums.40C0)
- **CL_CONTEXT_SAFETY_PROPERTIES_IMG** (container=enums.40D0)
- **CL_CONTEXT_SHOW_DIAGNOSTICS_INTEL** (container=enums.4100)
- **CL_CONTEXT_TERMINATE_KHR** (container=enums.2000)
- **CL_CONTEXT_VA_API_DISPLAY_INTEL** (container=enums.4090)
- **CL_CURRENT_DEVICE_FOR_GL_CONTEXT_KHR** (container=enums.2000)
- **CL_D3D10_DEVICE_KHR** (container=enums.4010)
- **CL_D3D10_DXGI_ADAPTER_KHR** (container=enums.4010)
- **CL_D3D11_DEVICE_KHR** (container=enums.4010)
- **CL_D3D11_DXGI_ADAPTER_KHR** (container=enums.4010)
- **CL_D3D9EX_DEVICE_INTEL** (container=enums.4070)
- **CL_D3D9_DEVICE_INTEL** (container=enums.4010)
- **CL_DBL_DIG** (container=Constants)
- **CL_DBL_EPSILON** (container=Constants)
- **CL_DBL_MANT_DIG** (container=Constants)
- **CL_DBL_MAX** (container=Constants)
- **CL_DBL_MAX_10_EXP** (container=Constants)
- **CL_DBL_MAX_EXP** (container=Constants)
- **CL_DBL_MIN** (container=Constants)
- **CL_DBL_MIN_10_EXP** (container=Constants)
- **CL_DBL_MIN_EXP** (container=Constants)
- **CL_DBL_RADIX** (container=Constants)
- **CL_DEVICES_FOR_GL_CONTEXT_KHR** (container=enums.2000)
- **CL_DEVICE_AFFINITY_DOMAINS_EXT** (container=enums.4050)
- **CL_DEVICE_AVAILABLE_ASYNC_QUEUES_AMD** (container=enums.4040)
- **CL_DEVICE_AVC_ME_SUPPORTS_PREEMPTION_INTEL** (container=enums.4100)
- **CL_DEVICE_AVC_ME_SUPPORTS_TEXTURE_SAMPLER_USE_INTEL** (container=enums.4100)
- **CL_DEVICE_AVC_ME_VERSION_INTEL** (container=enums.4100)
- **CL_DEVICE_BOARD_NAME_AMD** (container=enums.4030)
- **CL_DEVICE_COMPUTE_CAPABILITY_MAJOR_NV** (container=enums.4000)
- **CL_DEVICE_COMPUTE_CAPABILITY_MINOR_NV** (container=enums.4000)
- **CL_DEVICE_COMPUTE_UNITS_BITFIELD_ARM** (container=enums.40B0)
- **CL_DEVICE_CONTROLLED_TERMINATION_CAPABILITIES_ARM** (container=enums.41E0)
- **CL_DEVICE_CROSS_DEVICE_SHARED_MEM_CAPABILITIES_INTEL** (container=enums.4190)
- **CL_DEVICE_CXX_FOR_OPENCL_NUMERIC_VERSION_EXT** (container=enums.4230)
- **CL_DEVICE_DEVICE_MEM_CAPABILITIES_INTEL** (container=enums.4190)
- **CL_DEVICE_DOUBLE_FP_ATOMIC_CAPABILITIES_EXT** (container=enums.4230)
- **CL_DEVICE_EXTERNAL_MEMORY_IMPORT_ASSUME_LINEAR_IMAGES_HANDLE_TYPES_KHR** (container=enums.2000)
- **CL_DEVICE_EXTERNAL_MEMORY_IMPORT_HANDLE_TYPES_KHR** (container=enums.2000)
- **CL_DEVICE_EXT_MEM_PADDING_IN_BYTES_QCOM** (container=enums.40A0)
- **CL_DEVICE_FEATURE_CAPABILITIES_INTEL** (container=enums.4250)
- **CL_DEVICE_GFXIP_MAJOR_AMD** (container=enums.4040)
- **CL_DEVICE_GFXIP_MINOR_AMD** (container=enums.4040)
- **CL_DEVICE_GLOBAL_FREE_MEMORY_AMD** (container=enums.4030)
- **CL_DEVICE_GLOBAL_MEM_CHANNELS_AMD** (container=enums.4040)
- **CL_DEVICE_GLOBAL_MEM_CHANNEL_BANKS_AMD** (container=enums.4040)
- **CL_DEVICE_GLOBAL_MEM_CHANNEL_BANK_WIDTH_AMD** (container=enums.4040)
- **CL_DEVICE_GPU_OVERLAP_NV** (container=enums.4000)
- **CL_DEVICE_HALF_FP_ATOMIC_CAPABILITIES_EXT** (container=enums.4230)
- **CL_DEVICE_HOST_MEM_CAPABILITIES_INTEL** (container=enums.4190)
- **CL_DEVICE_ID_INTEL** (container=enums.4250)
- **CL_DEVICE_INTEGRATED_MEMORY_NV** (container=enums.4000)
- **CL_DEVICE_IP_VERSION_INTEL** (container=enums.4250)
- **CL_DEVICE_JOB_SLOTS_ARM** (container=enums.41E0)
- **CL_DEVICE_KERNEL_EXEC_TIMEOUT_NV** (container=enums.4000)
- **CL_DEVICE_LOCAL_MEM_BANKS_AMD** (container=enums.4040)
- **CL_DEVICE_LOCAL_MEM_SIZE_PER_COMPUTE_UNIT_AMD** (container=enums.4040)
- **CL_DEVICE_MAX_HOST_READ_PIPES_INTEL** (container=enums.4210)
- **CL_DEVICE_MAX_HOST_WRITE_PIPES_INTEL** (container=enums.4210)
- **CL_DEVICE_MAX_NAMED_BARRIER_COUNT_KHR** (container=enums.2000)
- **CL_DEVICE_MAX_WARP_COUNT_ARM** (container=enums.41E0)
- **CL_DEVICE_MAX_WORK_GROUP_SIZE_AMD** (container=enums.4030)
- **CL_DEVICE_MEMORY_CAPABILITIES_IMG** (container=enums.40D0)
- **CL_DEVICE_ME_VERSION_INTEL** (container=enums.4070)
- **CL_DEVICE_NUM_EUS_PER_SUB_SLICE_INTEL** (container=enums.4250)
- **CL_DEVICE_NUM_SIMULTANEOUS_INTEROPS_INTEL** (container=enums.4100)
- **CL_DEVICE_NUM_SLICES_INTEL** (container=enums.4250)
- **CL_DEVICE_NUM_SUB_SLICES_PER_SLICE_INTEL** (container=enums.4250)
- **CL_DEVICE_NUM_THREADS_PER_EU_INTEL** (container=enums.4250)
- **CL_DEVICE_PAGE_SIZE_QCOM** (container=enums.40A0)
- **CL_DEVICE_PARENT_DEVICE_EXT** (container=enums.4050)
- **CL_DEVICE_PARTITION_BY_AFFINITY_DOMAIN_EXT** (container=enums.4050)
- **CL_DEVICE_PARTITION_BY_COUNTS_EXT** (container=enums.4050)
- **CL_DEVICE_PARTITION_BY_COUNTS_LIST_END** (container=MiscNumbers)
- **CL_DEVICE_PARTITION_BY_NAMES_EXT** (container=enums.4050)
- **CL_DEVICE_PARTITION_BY_NAMES_INTEL** (container=enums.4050)
- **CL_DEVICE_PARTITION_EQUALLY_EXT** (container=enums.4050)
- **CL_DEVICE_PARTITION_STYLE_EXT** (container=enums.4050)
- **CL_DEVICE_PARTITION_TYPES_EXT** (container=enums.4050)
- **CL_DEVICE_PCIE_ID_AMD** (container=enums.4030)
- **CL_DEVICE_PCI_BUS_INFO_KHR** (container=enums.4100)
- **CL_DEVICE_PLANAR_YUV_MAX_HEIGHT_INTEL** (container=enums.4170)
- **CL_DEVICE_PLANAR_YUV_MAX_WIDTH_INTEL** (container=enums.4170)
- **CL_DEVICE_PREFERRED_CONSTANT_BUFFER_SIZE_AMD** (container=enums.4030)
- **CL_DEVICE_PREFERRED_WORK_GROUP_SIZE_AMD** (container=enums.4030)
- **CL_DEVICE_PROFILING_TIMER_OFFSET_AMD** (container=enums.4030)
- **CL_DEVICE_QUEUE_FAMILY_PROPERTIES_INTEL** (container=enums.4180)
- **CL_DEVICE_REFERENCE_COUNT_EXT** (container=enums.4050)
- **CL_DEVICE_REGISTERS_PER_BLOCK_NV** (container=enums.4000)
- **CL_DEVICE_SAFETY_MEM_SIZE_IMG** (container=enums.40D0)
- **CL_DEVICE_SCHEDULING_CONTROLS_CAPABILITIES_ARM** (container=enums.41E0)
- **CL_DEVICE_SCHEDULING_CONTROLS_CAPABILITIES_IMG** (container=enums.4220)
- **CL_DEVICE_SEMAPHORE_EXPORT_HANDLE_TYPES_KHR** (container=enums.2000)
- **CL_DEVICE_SEMAPHORE_IMPORT_HANDLE_TYPES_KHR** (container=enums.2000)
- **CL_DEVICE_SEMAPHORE_TYPES_KHR** (container=enums.2000)
- **CL_DEVICE_SHARED_SYSTEM_MEM_CAPABILITIES_INTEL** (container=enums.4190)
- **CL_DEVICE_SIMD_INSTRUCTION_WIDTH_AMD** (container=enums.4040)
- **CL_DEVICE_SIMD_PER_COMPUTE_UNIT_AMD** (container=enums.4040)
- **CL_DEVICE_SIMD_WIDTH_AMD** (container=enums.4040)
- **CL_DEVICE_SIMULTANEOUS_INTEROPS_INTEL** (container=enums.4100)
- **CL_DEVICE_SINGLE_DEVICE_SHARED_MEM_CAPABILITIES_INTEL** (container=enums.4190)
- **CL_DEVICE_SINGLE_FP_ATOMIC_CAPABILITIES_EXT** (container=enums.4230)
- **CL_DEVICE_SPIR_VERSIONS** (container=enums.40E0)
- **CL_DEVICE_SUB_GROUP_SIZES_INTEL** (container=enums.4100)
- **CL_DEVICE_SUPPORTED_REGISTER_ALLOCATIONS_ARM** (container=enums.41E0)
- **CL_DEVICE_SVM_CAPABILITIES_ARM** (container=enums.40B0)
- **CL_DEVICE_TERMINATE_CAPABILITY_KHR** (container=enums.2000)
- **CL_DEVICE_THREAD_TRACE_SUPPORTED_AMD** (container=enums.4040)
- **CL_DEVICE_TOPOLOGY_AMD** (container=enums.4030)
- **CL_DEVICE_WARP_SIZE_NV** (container=enums.4000)
- **CL_DEVICE_WAVEFRONT_WIDTH_AMD** (container=enums.4040)
- **CL_DEVICE_WORKGROUP_PROTECTION_DEVICE_ENQUEUE_CAPABILITIES_IMG** (container=enums.40D0)
- **CL_DEVICE_WORKGROUP_PROTECTION_SVM_CAPABILITIES_IMG** (container=enums.40D0)
- **CL_DXVA_DEVICE_INTEL** (container=enums.4070)
- **CL_ECC_RECOVERED_IMG** (container=enums.40D0)
- **CL_EGL_DISPLAY_KHR** (container=enums.2000)
- **CL_EGL_YUV_PLANE_INTEL** (container=enums.4100)
- **CL_EVENT_COMMAND_TERMINATION_REASON_ARM** (container=enums.41E0)
- **CL_EXTERNAL_MEMORY_HANDLE_ANDROID_HARDWARE_BUFFER_KHR** (container=enums.2000)
- **CL_EXTERNAL_MEMORY_HANDLE_DMA_BUF_KHR** (container=enums.2000)
- **CL_EXTERNAL_MEMORY_HANDLE_OPAQUE_FD_KHR** (container=enums.2000)
- **CL_EXTERNAL_MEMORY_HANDLE_OPAQUE_WIN32_KHR** (container=enums.2000)
- **CL_EXTERNAL_MEMORY_HANDLE_OPAQUE_WIN32_KMT_KHR** (container=enums.2000)
- **CL_EXTERNAL_MEMORY_HANDLE_OPAQUE_WIN32_NAME_KHR** (container=enums.2000)
- **CL_FLT_DIG** (container=Constants)
- **CL_FLT_EPSILON** (container=Constants)
- **CL_FLT_MANT_DIG** (container=Constants)
- **CL_FLT_MAX** (container=Constants)
- **CL_FLT_MAX_10_EXP** (container=Constants)
- **CL_FLT_MAX_EXP** (container=Constants)
- **CL_FLT_MIN** (container=Constants)
- **CL_FLT_MIN_10_EXP** (container=Constants)
- **CL_FLT_MIN_EXP** (container=Constants)
- **CL_FLT_RADIX** (container=Constants)
- **CL_GLX_DISPLAY_KHR** (container=enums.2000)
- **CL_GL_CONTEXT_KHR** (container=enums.2000)
- **CL_GL_MIPMAP_LEVEL** (container=enums.2000)
- **CL_GL_NUM_SAMPLES** (container=enums.2000)
- **CL_GL_OBJECT_BUFFER** (container=enums.2000)
- **CL_GL_OBJECT_RENDERBUFFER** (container=enums.2000)
- **CL_GL_OBJECT_TEXTURE1D** (container=enums.2000)
- **CL_GL_OBJECT_TEXTURE1D_ARRAY** (container=enums.2000)
- **CL_GL_OBJECT_TEXTURE2D** (container=enums.2000)
- **CL_GL_OBJECT_TEXTURE2D_ARRAY** (container=enums.2000)
- **CL_GL_OBJECT_TEXTURE3D** (container=enums.2000)
- **CL_GL_OBJECT_TEXTURE_BUFFER** (container=enums.2000)
- **CL_GL_TEXTURE_TARGET** (container=enums.2000)
- **CL_GRALLOC_RESOURCE_NOT_ACQUIRED_IMG** (container=enums.40D0)
- **CL_HALF_DIG** (container=Constants)
- **CL_HALF_EPSILON** (container=Constants)
- **CL_HALF_MANT_DIG** (container=Constants)
- **CL_HALF_MAX** (container=Constants)
- **CL_HALF_MAX_10_EXP** (container=Constants)
- **CL_HALF_MAX_EXP** (container=Constants)
- **CL_HALF_MIN** (container=Constants)
- **CL_HALF_MIN_10_EXP** (container=Constants)
- **CL_HALF_MIN_EXP** (container=Constants)
- **CL_HALF_RADIX** (container=Constants)
- **CL_HUGE_VAL** (container=Constants)
- **CL_HUGE_VALF** (container=Constants)
- **CL_IMAGE_D3D10_SUBRESOURCE_KHR** (container=enums.4010)
- **CL_IMAGE_D3D11_SUBRESOURCE_KHR** (container=enums.4010)
- **CL_IMAGE_DX9_MEDIA_PLANE_KHR** (container=enums.2000)
- **CL_IMAGE_DX9_PLANE_INTEL** (container=enums.4070)
- **CL_IMAGE_ROW_ALIGNMENT_QCOM** (container=enums.40A0)
- **CL_IMAGE_SLICE_ALIGNMENT_QCOM** (container=enums.40A0)
- **CL_IMAGE_VA_API_PLANE_INTEL** (container=enums.4090)
- **CL_IMPORT_ANDROID_HARDWARE_BUFFER_LAYER_INDEX_ARM** (container=enums.41E0)
- **CL_IMPORT_ANDROID_HARDWARE_BUFFER_PLANE_INDEX_ARM** (container=enums.41E0)
- **CL_IMPORT_DMA_BUF_DATA_CONSISTENCY_WITH_HOST_ARM** (container=enums.41E0)
- **CL_IMPORT_MEMORY_WHOLE_ALLOCATION_ARM** (container=Constants.cl_arm_import_memory)
- **CL_IMPORT_TYPE_ANDROID_HARDWARE_BUFFER_ARM** (container=enums.41E0)
- **CL_IMPORT_TYPE_ARM** (container=enums.40B0)
- **CL_IMPORT_TYPE_DMA_BUF_ARM** (container=enums.40B0)
- **CL_IMPORT_TYPE_HOST_ARM** (container=enums.40B0)
- **CL_IMPORT_TYPE_PROTECTED_ARM** (container=enums.40B0)
- **CL_INFINITY** (container=Constants)
- **CL_INT_MAX** (container=Constants)
- **CL_INT_MIN** (container=Constants)
- **CL_INVALID_GRALLOC_OBJECT_IMG** (container=enums.40D0)
- **CL_KERNEL_ALLOCATIONS_INFO_INTEL** (container=enums.4250)
- **CL_KERNEL_ARG_HOST_ACCESSIBLE_PIPE_INTEL** (container=enums.4210)
- **CL_KERNEL_COMPILE_SUB_GROUP_SIZE_INTEL** (container=enums.4100)
- **CL_KERNEL_EXEC_INFO_COMPUTE_UNIT_MAX_QUEUED_BATCHES_ARM** (container=enums.41E0)
- **CL_KERNEL_EXEC_INFO_DEVICE_PTRS_EXT** (container=enums.5000)
- **CL_KERNEL_EXEC_INFO_INDIRECT_DEVICE_ACCESS_INTEL** (container=enums.4200)
- **CL_KERNEL_EXEC_INFO_INDIRECT_HOST_ACCESS_INTEL** (container=enums.4200)
- **CL_KERNEL_EXEC_INFO_INDIRECT_SHARED_ACCESS_INTEL** (container=enums.4200)
- **CL_KERNEL_EXEC_INFO_SVM_FINE_GRAIN_SYSTEM_ARM** (container=enums.40B0)
- **CL_KERNEL_EXEC_INFO_SVM_PTRS_ARM** (container=enums.40B0)
- **CL_KERNEL_EXEC_INFO_USM_PTRS_INTEL** (container=enums.4200)
- **CL_KERNEL_EXEC_INFO_WARP_COUNT_LIMIT_ARM** (container=enums.41E0)
- **CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_ARM** (container=enums.41E0)
- **CL_KERNEL_EXEC_INFO_WORKGROUP_BATCH_SIZE_MODIFIER_ARM** (container=enums.41E0)
- **CL_KERNEL_MAX_SUB_GROUP_SIZE_FOR_NDRANGE** (container=enums.2000)
- **CL_KERNEL_MAX_SUB_GROUP_SIZE_FOR_NDRANGE_KHR** (container=enums.2000)
- **CL_KERNEL_MAX_WARP_COUNT_ARM** (container=enums.41E0)
- **CL_KERNEL_SPILL_MEM_SIZE_INTEL** (container=enums.4100)
- **CL_KERNEL_SUB_GROUP_COUNT_FOR_NDRANGE** (container=enums.2000)
- **CL_KERNEL_SUB_GROUP_COUNT_FOR_NDRANGE_KHR** (container=enums.2000)
- **CL_LAYER_API_VERSION** (container=enums.4240)
- **CL_LAYER_API_VERSION_100** (container=Constants.cl_loader_layers)
- **CL_LAYER_NAME** (container=enums.4240)
- **CL_LAYER_PROPERTIES_LIST_END** (container=Constants.cl_loader_layers)
- **CL_LONG_MAX** (container=Constants)
- **CL_LONG_MIN** (container=Constants)
- **CL_LUID_SIZE** (container=Constants.uuid)
- **CL_LUID_SIZE_KHR** (container=Constants.cl_khr_device_uuid)
- **CL_MAXFLOAT** (container=Constants)
- **CL_MEM_ALLOC_BASE_PTR_INTEL** (container=enums.4190)
- **CL_MEM_ALLOC_BUFFER_LOCATION_INTEL** (container=enums.4190)
- **CL_MEM_ALLOC_DEVICE_INTEL** (container=enums.4190)
- **CL_MEM_ALLOC_FLAGS_IMG** (container=enums.40D0)
- **CL_MEM_ALLOC_FLAGS_INTEL** (container=enums.4190)
- **CL_MEM_ALLOC_SIZE_INTEL** (container=enums.4190)
- **CL_MEM_ALLOC_TYPE_INTEL** (container=enums.4190)
- **CL_MEM_ANDROID_NATIVE_BUFFER_HOST_PTR_QCOM** (container=enums.40C0)
- **CL_MEM_CHANNEL_INTEL** (container=enums.4210)
- **CL_MEM_D3D10_RESOURCE_KHR** (container=enums.4010)
- **CL_MEM_D3D11_RESOURCE_KHR** (container=enums.4010)
- **CL_MEM_DEVICE_ADDRESS_EXT** (container=enums.5000)
- **CL_MEM_DEVICE_HANDLE_LIST_END_KHR** (container=MiscNumbers)
- **CL_MEM_DEVICE_HANDLE_LIST_KHR** (container=enums.2000)
- **CL_MEM_DEVICE_ID_INTEL** (container=enums.4210)
- **CL_MEM_DEVICE_PRIVATE_ADDRESS_EXT** (container=enums.5000)
- **CL_MEM_DX9_MEDIA_ADAPTER_TYPE_KHR** (container=enums.2000)
- **CL_MEM_DX9_MEDIA_SURFACE_INFO_KHR** (container=enums.2000)
- **CL_MEM_DX9_RESOURCE_INTEL** (container=enums.4010)
- **CL_MEM_DX9_SHARED_HANDLE_INTEL** (container=enums.4070)
- **CL_MEM_HOST_IOCOHERENT_QCOM** (container=enums.40A0)
- **CL_MEM_HOST_UNCACHED_QCOM** (container=enums.40A0)
- **CL_MEM_HOST_WRITEBACK_QCOM** (container=enums.40A0)
- **CL_MEM_HOST_WRITETHROUGH_QCOM** (container=enums.40A0)
- **CL_MEM_HOST_WRITE_COMBINING_QCOM** (container=enums.40A0)
- **CL_MEM_ION_HOST_PTR_QCOM** (container=enums.40A0)
- **CL_MEM_LOCALLY_UNCACHED_RESOURCE_INTEL** (container=enums.4210)
- **CL_MEM_TYPE_DEVICE_INTEL** (container=enums.4190)
- **CL_MEM_TYPE_HOST_INTEL** (container=enums.4190)
- **CL_MEM_TYPE_SHARED_INTEL** (container=enums.4190)
- **CL_MEM_TYPE_UNKNOWN_INTEL** (container=enums.4190)
- **CL_MEM_USES_SVM_POINTER_ARM** (container=enums.40B0)
- **CL_MEM_VA_API_MEDIA_SURFACE_INTEL** (container=enums.4090)
- **CL_M_1_PI** (container=Constants)
- **CL_M_1_PI_F** (container=Constants)
- **CL_M_2_PI** (container=Constants)
- **CL_M_2_PI_F** (container=Constants)
- **CL_M_2_SQRTPI** (container=Constants)
- **CL_M_2_SQRTPI_F** (container=Constants)
- **CL_M_E** (container=Constants)
- **CL_M_E_F** (container=Constants)
- **CL_M_LN10** (container=Constants)
- **CL_M_LN10_F** (container=Constants)
- **CL_M_LN2** (container=Constants)
- **CL_M_LN2_F** (container=Constants)
- **CL_M_LOG10E** (container=Constants)
- **CL_M_LOG10E_F** (container=Constants)
- **CL_M_LOG2E** (container=Constants)
- **CL_M_LOG2E_F** (container=Constants)
- **CL_M_PI** (container=Constants)
- **CL_M_PI_2** (container=Constants)
- **CL_M_PI_2_F** (container=Constants)
- **CL_M_PI_4** (container=Constants)
- **CL_M_PI_4_F** (container=Constants)
- **CL_M_PI_F** (container=Constants)
- **CL_M_SQRT1_2** (container=Constants)
- **CL_M_SQRT1_2_F** (container=Constants)
- **CL_M_SQRT2** (container=Constants)
- **CL_M_SQRT2_F** (container=Constants)
- **CL_NAME_VERSION_MAX_NAME_SIZE** (container=Constants.Versioning)
- **CL_NAME_VERSION_MAX_NAME_SIZE_KHR** (container=Constants.cl_khr_extended_versioning)
- **CL_NAN** (container=Constants)
- **CL_NV12_INTEL** (container=enums.4100)
- **CL_NV21** (container=enums.40D0)
- **CL_NV21_IMG** (container=enums.40D0)
- **CL_PARTITION_BY_COUNTS_LIST_END_EXT** (container=MiscNumbers)
- **CL_PARTITION_BY_NAMES_LIST_END_EXT** (container=MiscNumbers)
- **CL_PARTITION_BY_NAMES_LIST_END_INTEL** (container=MiscNumbers)
- **CL_PERF_HINT_HIGH_QCOM** (container=enums.40C0)
- **CL_PERF_HINT_LOW_QCOM** (container=enums.40C0)
- **CL_PERF_HINT_NORMAL_QCOM** (container=enums.40C0)
- **CL_PLATFORM_EXTERNAL_MEMORY_IMPORT_HANDLE_TYPES_KHR** (container=enums.2000)
- **CL_PLATFORM_SEMAPHORE_EXPORT_HANDLE_TYPES_KHR** (container=enums.2000)
- **CL_PLATFORM_SEMAPHORE_IMPORT_HANDLE_TYPES_KHR** (container=enums.2000)
- **CL_PLATFORM_SEMAPHORE_TYPES_KHR** (container=enums.2000)
- **CL_PREFERRED_DEVICES_FOR_D3D10_KHR** (container=enums.4010)
- **CL_PREFERRED_DEVICES_FOR_D3D11_KHR** (container=enums.4010)
- **CL_PREFERRED_DEVICES_FOR_DX9_INTEL** (container=enums.4010)
- **CL_PREFERRED_DEVICES_FOR_DX9_MEDIA_ADAPTER_KHR** (container=enums.2000)
- **CL_PREFERRED_DEVICES_FOR_VA_API_INTEL** (container=enums.4090)
- **CL_PRINTF_BUFFERSIZE_ARM** (container=enums.40B0)
- **CL_PRINTF_CALLBACK_ARM** (container=enums.40B0)
- **CL_PROGRAM_BINARY_TYPE_INTERMEDIATE** (container=enums.40E0)
- **CL_PROGRAM_HOST_PIPE_NAMES_INTEL** (container=enums.4210)
- **CL_PROGRAM_NUM_HOST_PIPES_INTEL** (container=enums.4210)
- **CL_PROPERTIES_LIST_END_EXT** (container=MiscNumbers)
- **CL_QUEUE_COMPUTE_UNIT_LIMIT_ARM** (container=enums.41E0)
- **CL_QUEUE_DEFAULT_CAPABILITIES_INTEL** (container=Constants.cl_intel_command_queue_families)
- **CL_QUEUE_DEFERRED_FLUSH_ARM** (container=enums.41E0)
- **CL_QUEUE_FAMILY_INTEL** (container=enums.4180)
- **CL_QUEUE_FAMILY_MAX_NAME_SIZE_INTEL** (container=Constants.cl_intel_command_queue_families)
- **CL_QUEUE_INDEX_INTEL** (container=enums.4180)
- **CL_QUEUE_JOB_SLOT_ARM** (container=enums.41E0)
- **CL_QUEUE_KERNEL_BATCHING_ARM** (container=enums.41E0)
- **CL_SCHAR_MAX** (container=Constants)
- **CL_SCHAR_MIN** (container=Constants)
- **CL_SEMAPHORE_CONTEXT_KHR** (container=enums.2000)
- **CL_SEMAPHORE_DEVICE_HANDLE_LIST_END_KHR** (container=MiscNumbers)
- **CL_SEMAPHORE_DEVICE_HANDLE_LIST_KHR** (container=enums.2000)
- **CL_SEMAPHORE_EXPORT_HANDLE_TYPES_KHR** (container=enums.2000)
- **CL_SEMAPHORE_EXPORT_HANDLE_TYPES_LIST_END_KHR** (container=MiscNumbers)
- **CL_SEMAPHORE_FAST_PATH_IMG** (container=enums.4220)
- **CL_SEMAPHORE_HANDLE_D3D12_FENCE_KHR** (container=enums.2000)
- **CL_SEMAPHORE_HANDLE_OPAQUE_FD_KHR** (container=enums.2000)
- **CL_SEMAPHORE_HANDLE_OPAQUE_WIN32_KHR** (container=enums.2000)
- **CL_SEMAPHORE_HANDLE_OPAQUE_WIN32_KMT_KHR** (container=enums.2000)
- **CL_SEMAPHORE_HANDLE_OPAQUE_WIN32_NAME_KHR** (container=enums.2000)
- **CL_SEMAPHORE_HANDLE_SYNC_FD_KHR** (container=enums.2000)
- **CL_SEMAPHORE_PAYLOAD_KHR** (container=enums.2000)
- **CL_SEMAPHORE_PROPERTIES_KHR** (container=enums.2000)
- **CL_SEMAPHORE_REFERENCE_COUNT_KHR** (container=enums.2000)
- **CL_SHRT_MAX** (container=Constants)
- **CL_SHRT_MIN** (container=Constants)
- **CL_SVM_ALLOC_ACCESS_FLAGS_KHR** (container=enums.2000)
- **CL_SVM_ALLOC_ALIGNMENT_KHR** (container=enums.2000)
- **CL_SVM_ALLOC_ASSOCIATED_DEVICE_HANDLE_KHR** (container=enums.2000)
- **CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_IMG** (container=enums.4220)
- **CL_SVM_ALLOC_EXTERNAL_MEMORY_DMA_BUF_VIRTUAL_ADDRESS_IMG** (container=enums.4220)
- **CL_SVM_INFO_ACCESS_FLAGS_KHR** (container=enums.2000)
- **CL_SVM_INFO_ASSOCIATED_DEVICE_HANDLE_KHR** (container=enums.4190)
- **CL_SVM_INFO_BASE_PTR_KHR** (container=enums.4190)
- **CL_SVM_INFO_CAPABILITIES_KHR** (container=enums.2000)
- **CL_SVM_INFO_PROPERTIES_KHR** (container=enums.2000)
- **CL_SVM_INFO_SIZE_KHR** (container=enums.4190)
- **CL_SVM_INFO_TYPE_INDEX_KHR** (container=enums.2000)
- **CL_UCHAR_MAX** (container=Constants)
- **CL_UINT_MAX** (container=Constants)
- **CL_ULONG_MAX** (container=Constants)
- **CL_USHRT_MAX** (container=Constants)
- **CL_UUID_SIZE** (container=Constants.uuid)
- **CL_UUID_SIZE_KHR** (container=Constants.cl_khr_device_uuid)
- **CL_UYVY_INTEL** (container=enums.4070)
- **CL_VA_API_DISPLAY_INTEL** (container=enums.4090)
- **CL_VERSION_MAJOR_BITS** (container=Constants.Versioning)
- **CL_VERSION_MAJOR_BITS_KHR** (container=Constants.cl_khr_extended_versioning)
- **CL_VERSION_MINOR_BITS** (container=Constants.Versioning)
- **CL_VERSION_MINOR_BITS_KHR** (container=Constants.cl_khr_extended_versioning)
- **CL_VERSION_PATCH_BITS** (container=Constants.Versioning)
- **CL_VERSION_PATCH_BITS_KHR** (container=Constants.cl_khr_extended_versioning)
- **CL_VYUY_INTEL** (container=enums.4070)
- **CL_WGL_HDC_KHR** (container=enums.2000)
- **CL_YUYV_INTEL** (container=enums.4070)
- **CL_YV12** (container=enums.40D0)
- **CL_YV12_IMG** (container=enums.40D0)
- **CL_YVYU_INTEL** (container=enums.4070)

## Group: `ErrorCode` (112 single-members)


## Group: `clCommandExecutionStatus` (4 single-members)


## Group: `cl_accelerator_type_intel` (1 single-members)

| token | container | confidence |
|---|---|---|
| CL_ACCELERATOR_TYPE_MOTION_ESTIMATION_INTEL | cl_accelerator_type_intel | declared |

## Group: `cl_affinity_domain_ext` (6 single-members)

| token | container | confidence |
|---|---|---|
| CL_AFFINITY_DOMAIN_L1_CACHE_EXT | cl_affinity_domain_ext | declared |
| CL_AFFINITY_DOMAIN_L2_CACHE_EXT | cl_affinity_domain_ext | declared |
| CL_AFFINITY_DOMAIN_L3_CACHE_EXT | cl_affinity_domain_ext | declared |
| CL_AFFINITY_DOMAIN_L4_CACHE_EXT | cl_affinity_domain_ext | declared |
| CL_AFFINITY_DOMAIN_NUMA_EXT | cl_affinity_domain_ext | declared |
| CL_AFFINITY_DOMAIN_NEXT_FISSIONABLE_EXT | cl_affinity_domain_ext | declared |

## Group: `cl_arm_device_svm_capabilities.flags` (4 single-members)

| token | container | confidence |
|---|---|---|
| CL_DEVICE_SVM_COARSE_GRAIN_BUFFER_ARM | cl_arm_device_svm_capabilities.flags | declared |
| CL_DEVICE_SVM_FINE_GRAIN_BUFFER_ARM | cl_arm_device_svm_capabilities.flags | declared |
| CL_DEVICE_SVM_FINE_GRAIN_SYSTEM_ARM | cl_arm_device_svm_capabilities.flags | declared |
| CL_DEVICE_SVM_ATOMICS_ARM | cl_arm_device_svm_capabilities.flags | declared |

## Group: `cl_arm_svm_alloc.flags` (2 single-members)

| token | container | confidence |
|---|---|---|
| CL_MEM_SVM_FINE_GRAIN_BUFFER_ARM | cl_arm_svm_alloc.flags | declared |
| CL_MEM_SVM_ATOMICS_ARM | cl_arm_svm_alloc.flags | declared |

## Group: `cl_bool` (5 single-members)

| token | container | confidence |
|---|---|---|
| CL_FALSE | cl_bool | declared |
| CL_TRUE | cl_bool | declared |
| CL_BLOCKING | cl_bool | declared |
| CL_NON_BLOCKING | cl_bool | declared |
| CL_SEMAPHORE_EXPORTABLE_KHR | enums.2000 | high |

## Group: `cl_build_status` (4 single-members)

| token | container | confidence |
|---|---|---|
| CL_BUILD_SUCCESS | cl_build_status | declared |
| CL_BUILD_NONE | cl_build_status | declared |
| CL_BUILD_ERROR | cl_build_status | declared |
| CL_BUILD_IN_PROGRESS | cl_build_status | declared |

## Group: `cl_command_buffer_flags_khr` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_COMMAND_BUFFER_SIMULTANEOUS_USE_KHR | cl_command_buffer_flags_khr | high |
| CL_COMMAND_BUFFER_MUTABLE_KHR | cl_command_buffer_flags_khr | high |
| CL_COMMAND_BUFFER_DEVICE_SIDE_SYNC_KHR | cl_command_buffer_flags_khr | high |

## Group: `cl_command_buffer_state_khr` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_COMMAND_BUFFER_STATE_RECORDING_KHR | cl_command_buffer_state_khr | declared |
| CL_COMMAND_BUFFER_STATE_EXECUTABLE_KHR | cl_command_buffer_state_khr | declared |
| CL_COMMAND_BUFFER_STATE_FINALIZED_KHR | cl_command_buffer_state_khr | declared |

## Group: `cl_command_buffer_update_type_khr` (1 single-members)

| token | container | confidence |
|---|---|---|
| CL_STRUCTURE_TYPE_MUTABLE_DISPATCH_CONFIG_KHR | cl_command_buffer_update_type_khr | declared |

## Group: `cl_command_queue_capabilities_intel` (16 single-members)

| token | container | confidence |
|---|---|---|
| CL_QUEUE_CAPABILITY_CREATE_SINGLE_QUEUE_EVENTS_INTEL | cl_command_queue_capabilities_intel | declared |
| CL_QUEUE_CAPABILITY_CREATE_CROSS_QUEUE_EVENTS_INTEL | cl_command_queue_capabilities_intel | declared |
| CL_QUEUE_CAPABILITY_SINGLE_QUEUE_EVENT_WAIT_LIST_INTEL | cl_command_queue_capabilities_intel | declared |
| CL_QUEUE_CAPABILITY_CROSS_QUEUE_EVENT_WAIT_LIST_INTEL | cl_command_queue_capabilities_intel | declared |
| CL_QUEUE_CAPABILITY_TRANSFER_BUFFER_INTEL | cl_command_queue_capabilities_intel | declared |
| CL_QUEUE_CAPABILITY_TRANSFER_BUFFER_RECT_INTEL | cl_command_queue_capabilities_intel | declared |
| CL_QUEUE_CAPABILITY_MAP_BUFFER_INTEL | cl_command_queue_capabilities_intel | declared |
| CL_QUEUE_CAPABILITY_FILL_BUFFER_INTEL | cl_command_queue_capabilities_intel | declared |
| CL_QUEUE_CAPABILITY_TRANSFER_IMAGE_INTEL | cl_command_queue_capabilities_intel | declared |
| CL_QUEUE_CAPABILITY_MAP_IMAGE_INTEL | cl_command_queue_capabilities_intel | declared |
| CL_QUEUE_CAPABILITY_FILL_IMAGE_INTEL | cl_command_queue_capabilities_intel | declared |
| CL_QUEUE_CAPABILITY_TRANSFER_BUFFER_IMAGE_INTEL | cl_command_queue_capabilities_intel | declared |
| CL_QUEUE_CAPABILITY_TRANSFER_IMAGE_BUFFER_INTEL | cl_command_queue_capabilities_intel | declared |
| CL_QUEUE_CAPABILITY_MARKER_INTEL | cl_command_queue_capabilities_intel | declared |
| CL_QUEUE_CAPABILITY_BARRIER_INTEL | cl_command_queue_capabilities_intel | declared |
| CL_QUEUE_CAPABILITY_KERNEL_INTEL | cl_command_queue_capabilities_intel | declared |

## Group: `cl_command_queue_properties` (6 single-members)

| token | container | confidence |
|---|---|---|
| CL_QUEUE_PROFILING_ENABLE | cl_command_queue_properties | high |
| CL_QUEUE_ON_DEVICE | cl_command_queue_properties | high |
| CL_QUEUE_ON_DEVICE_DEFAULT | cl_command_queue_properties | high |
| CL_QUEUE_NO_SYNC_OPERATIONS_INTEL | cl_command_queue_properties | declared |
| CL_QUEUE_RESERVED_QCOM | cl_command_queue_properties | declared |
| CL_QUEUE_THREAD_LOCAL_EXEC_ENABLE_INTEL | cl_command_queue_properties | declared |

## Group: `cl_command_termination_reason_arm` (4 single-members)

| token | container | confidence |
|---|---|---|
| CL_COMMAND_TERMINATION_COMPLETION_ARM | cl_command_termination_reason_arm | declared |
| CL_COMMAND_TERMINATION_CONTROLLED_SUCCESS_ARM | cl_command_termination_reason_arm | declared |
| CL_COMMAND_TERMINATION_CONTROLLED_FAILURE_ARM | cl_command_termination_reason_arm | declared |
| CL_COMMAND_TERMINATION_ERROR_ARM | cl_command_termination_reason_arm | declared |

## Group: `cl_context_memory_initialize_khr` (2 single-members)

| token | container | confidence |
|---|---|---|
| CL_CONTEXT_MEMORY_INITIALIZE_LOCAL_KHR | cl_context_memory_initialize_khr | declared |
| CL_CONTEXT_MEMORY_INITIALIZE_PRIVATE_KHR | cl_context_memory_initialize_khr | declared |

## Group: `cl_context_safety_properties_img` (2 single-members)

| token | container | confidence |
|---|---|---|
| CL_CONTEXT_WORKGROUP_PROTECTION_IMG | cl_context_safety_properties_img | declared |
| CL_CONTEXT_ENHANCED_EVENT_EXECUTION_STATUS_IMG | cl_context_safety_properties_img | declared |

## Group: `cl_device_affinity_domain` (6 single-members)

| token | container | confidence |
|---|---|---|
| CL_DEVICE_AFFINITY_DOMAIN_NUMA | cl_device_affinity_domain | declared |
| CL_DEVICE_AFFINITY_DOMAIN_L4_CACHE | cl_device_affinity_domain | declared |
| CL_DEVICE_AFFINITY_DOMAIN_L3_CACHE | cl_device_affinity_domain | declared |
| CL_DEVICE_AFFINITY_DOMAIN_L2_CACHE | cl_device_affinity_domain | declared |
| CL_DEVICE_AFFINITY_DOMAIN_L1_CACHE | cl_device_affinity_domain | declared |
| CL_DEVICE_AFFINITY_DOMAIN_NEXT_PARTITIONABLE | cl_device_affinity_domain | declared |

## Group: `cl_device_atomic_capabilities` (7 single-members)

| token | container | confidence |
|---|---|---|
| CL_DEVICE_ATOMIC_ORDER_RELAXED | cl_device_atomic_capabilities | high |
| CL_DEVICE_ATOMIC_ORDER_ACQ_REL | cl_device_atomic_capabilities | high |
| CL_DEVICE_ATOMIC_ORDER_SEQ_CST | cl_device_atomic_capabilities | declared |
| CL_DEVICE_ATOMIC_SCOPE_WORK_ITEM | cl_device_atomic_capabilities | declared |
| CL_DEVICE_ATOMIC_SCOPE_WORK_GROUP | cl_device_atomic_capabilities | high |
| CL_DEVICE_ATOMIC_SCOPE_DEVICE | cl_device_atomic_capabilities | declared |
| CL_DEVICE_ATOMIC_SCOPE_ALL_DEVICES | cl_device_atomic_capabilities | high |

## Group: `cl_device_command_buffer_capabilities_khr` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_COMMAND_BUFFER_CAPABILITY_KERNEL_PRINTF_KHR | cl_device_command_buffer_capabilities_khr | high |
| CL_COMMAND_BUFFER_CAPABILITY_DEVICE_SIDE_ENQUEUE_KHR | cl_device_command_buffer_capabilities_khr | high |
| CL_COMMAND_BUFFER_CAPABILITY_MULTIPLE_QUEUE_KHR | cl_device_command_buffer_capabilities_khr | high |

## Group: `cl_device_controlled_termination_capabilities_arm` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_DEVICE_CONTROLLED_TERMINATION_SUCCESS_ARM | cl_device_controlled_termination_capabilities_arm | declared |
| CL_DEVICE_CONTROLLED_TERMINATION_FAILURE_ARM | cl_device_controlled_termination_capabilities_arm | declared |
| CL_DEVICE_CONTROLLED_TERMINATION_QUERY_ARM | cl_device_controlled_termination_capabilities_arm | declared |

## Group: `cl_device_device_enqueue_capabilities` (2 single-members)

| token | container | confidence |
|---|---|---|
| CL_DEVICE_QUEUE_SUPPORTED | cl_device_device_enqueue_capabilities | high |
| CL_DEVICE_QUEUE_REPLACEABLE_DEFAULT | cl_device_device_enqueue_capabilities | high |

## Group: `cl_device_exec_capabilities` (2 single-members)

| token | container | confidence |
|---|---|---|
| CL_EXEC_KERNEL | cl_device_exec_capabilities | high |
| CL_EXEC_NATIVE_KERNEL | cl_device_exec_capabilities | declared |

## Group: `cl_device_feature_capabilities_intel` (2 single-members)

| token | container | confidence |
|---|---|---|
| CL_DEVICE_FEATURE_FLAG_DP4A_INTEL | cl_device_feature_capabilities_intel | declared |
| CL_DEVICE_FEATURE_FLAG_DPAS_INTEL | cl_device_feature_capabilities_intel | declared |

## Group: `cl_device_fp_atomic_capabilities_ext` (6 single-members)

| token | container | confidence |
|---|---|---|
| CL_DEVICE_GLOBAL_FP_ATOMIC_LOAD_STORE_EXT | cl_device_fp_atomic_capabilities_ext | declared |
| CL_DEVICE_GLOBAL_FP_ATOMIC_ADD_EXT | cl_device_fp_atomic_capabilities_ext | declared |
| CL_DEVICE_GLOBAL_FP_ATOMIC_MIN_MAX_EXT | cl_device_fp_atomic_capabilities_ext | declared |
| CL_DEVICE_LOCAL_FP_ATOMIC_LOAD_STORE_EXT | cl_device_fp_atomic_capabilities_ext | declared |
| CL_DEVICE_LOCAL_FP_ATOMIC_ADD_EXT | cl_device_fp_atomic_capabilities_ext | declared |
| CL_DEVICE_LOCAL_FP_ATOMIC_MIN_MAX_EXT | cl_device_fp_atomic_capabilities_ext | declared |

## Group: `cl_device_fp_config` (8 single-members)

| token | container | confidence |
|---|---|---|
| CL_FP_DENORM | cl_device_fp_config | high |
| CL_FP_INF_NAN | cl_device_fp_config | high |
| CL_FP_ROUND_TO_NEAREST | cl_device_fp_config | high |
| CL_FP_ROUND_TO_ZERO | cl_device_fp_config | high |
| CL_FP_ROUND_TO_INF | cl_device_fp_config | high |
| CL_FP_FMA | cl_device_fp_config | high |
| CL_FP_SOFT_FLOAT | cl_device_fp_config | high |
| CL_FP_CORRECTLY_ROUNDED_DIVIDE_SQRT | cl_device_fp_config | declared |

## Group: `cl_device_info` (376 single-members)

| token | container | confidence |
|---|---|---|
| CL_DEVICE_TYPE | cl_device_info | declared |
| CL_DEVICE_VENDOR_ID | cl_device_info | declared |
| CL_DEVICE_MAX_COMPUTE_UNITS | cl_device_info | declared |
| CL_DEVICE_MAX_WORK_ITEM_DIMENSIONS | cl_device_info | declared |
| CL_DEVICE_MAX_WORK_GROUP_SIZE | cl_device_info | declared |
| CL_DEVICE_MAX_WORK_ITEM_SIZES | cl_device_info | declared |
| CL_DEVICE_MAX_WORK_GROUP_SIZES | cl_device_info | declared |
| CL_DEVICE_PREFERRED_VECTOR_WIDTH_CHAR | cl_device_info | declared |
| CL_DEVICE_PREFERRED_VECTOR_WIDTH_SHORT | cl_device_info | declared |
| CL_DEVICE_PREFERRED_VECTOR_WIDTH_INT | cl_device_info | declared |
| CL_DEVICE_PREFERRED_VECTOR_WIDTH_LONG | cl_device_info | declared |
| CL_DEVICE_PREFERRED_VECTOR_WIDTH_FLOAT | cl_device_info | declared |
| CL_DEVICE_PREFERRED_VECTOR_WIDTH_DOUBLE | cl_device_info | declared |
| CL_DEVICE_MAX_CLOCK_FREQUENCY | cl_device_info | declared |
| CL_DEVICE_ADDRESS_BITS | cl_device_info | declared |
| CL_DEVICE_MAX_READ_IMAGE_ARGS | cl_device_info | declared |
| CL_DEVICE_MAX_WRITE_IMAGE_ARGS | cl_device_info | declared |
| CL_DEVICE_MAX_MEM_ALLOC_SIZE | cl_device_info | declared |
| CL_DEVICE_IMAGE2D_MAX_WIDTH | cl_device_info | declared |
| CL_DEVICE_IMAGE2D_MAX_HEIGHT | cl_device_info | declared |
| CL_DEVICE_IMAGE3D_MAX_WIDTH | cl_device_info | declared |
| CL_DEVICE_IMAGE3D_MAX_HEIGHT | cl_device_info | declared |
| CL_DEVICE_IMAGE3D_MAX_DEPTH | cl_device_info | declared |
| CL_DEVICE_IMAGE_SUPPORT | cl_device_info | declared |
| CL_DEVICE_MAX_PARAMETER_SIZE | cl_device_info | declared |
| CL_DEVICE_MAX_SAMPLERS | cl_device_info | declared |
| CL_DEVICE_MEM_BASE_ADDR_ALIGN | cl_device_info | declared |
| CL_DEVICE_MIN_DATA_TYPE_ALIGN_SIZE | cl_device_info | declared |
| CL_DEVICE_SINGLE_FP_CONFIG | cl_device_info | declared |
| CL_DEVICE_GLOBAL_MEM_CACHE_TYPE | cl_device_info | declared |
| CL_DEVICE_GLOBAL_MEM_CACHELINE_SIZE | cl_device_info | declared |
| CL_DEVICE_GLOBAL_MEM_CACHE_SIZE | cl_device_info | declared |
| CL_DEVICE_GLOBAL_MEM_SIZE | cl_device_info | declared |
| CL_DEVICE_MAX_CONSTANT_BUFFER_SIZE | cl_device_info | declared |
| CL_DEVICE_MAX_CONSTANT_ARGS | cl_device_info | declared |
| CL_DEVICE_LOCAL_MEM_TYPE | cl_device_info | declared |
| CL_DEVICE_LOCAL_MEM_SIZE | cl_device_info | declared |
| CL_DEVICE_ERROR_CORRECTION_SUPPORT | cl_device_info | declared |
| CL_DEVICE_PROFILING_TIMER_RESOLUTION | cl_device_info | declared |
| CL_DEVICE_ENDIAN_LITTLE | cl_device_info | declared |
| CL_DEVICE_AVAILABLE | cl_device_info | declared |
| CL_DEVICE_COMPILER_AVAILABLE | cl_device_info | declared |
| CL_DEVICE_EXECUTION_CAPABILITIES | cl_device_info | declared |
| CL_DEVICE_QUEUE_PROPERTIES | cl_device_info | declared |
| CL_DEVICE_QUEUE_ON_HOST_PROPERTIES | cl_device_info | declared |
| CL_DEVICE_NAME | cl_device_info | declared |
| CL_DEVICE_VENDOR | cl_device_info | declared |
| CL_DRIVER_VERSION | cl_device_info | declared |
| CL_DEVICE_PROFILE | cl_device_info | declared |
| CL_DEVICE_VERSION | cl_device_info | declared |
| CL_DEVICE_EXTENSIONS | cl_device_info | declared |
| CL_DEVICE_PLATFORM | cl_device_info | declared |
| CL_DEVICE_DOUBLE_FP_CONFIG | cl_device_info | declared |
| CL_DEVICE_HALF_FP_CONFIG | cl_device_info | declared |
| CL_DEVICE_PREFERRED_VECTOR_WIDTH_HALF | cl_device_info | declared |
| CL_DEVICE_HOST_UNIFIED_MEMORY | cl_device_info | declared |
| CL_DEVICE_NATIVE_VECTOR_WIDTH_CHAR | cl_device_info | declared |
| CL_DEVICE_NATIVE_VECTOR_WIDTH_SHORT | cl_device_info | declared |
| CL_DEVICE_NATIVE_VECTOR_WIDTH_INT | cl_device_info | declared |
| CL_DEVICE_NATIVE_VECTOR_WIDTH_LONG | cl_device_info | declared |
| CL_DEVICE_NATIVE_VECTOR_WIDTH_FLOAT | cl_device_info | declared |
| CL_DEVICE_NATIVE_VECTOR_WIDTH_DOUBLE | cl_device_info | declared |
| CL_DEVICE_NATIVE_VECTOR_WIDTH_HALF | cl_device_info | declared |
| CL_DEVICE_OPENCL_C_VERSION | cl_device_info | declared |
| CL_DEVICE_LINKER_AVAILABLE | cl_device_info | declared |
| CL_DEVICE_BUILT_IN_KERNELS | cl_device_info | declared |
| CL_DEVICE_IMAGE_MAX_BUFFER_SIZE | cl_device_info | declared |
| CL_DEVICE_IMAGE_MAX_ARRAY_SIZE | cl_device_info | declared |
| CL_DEVICE_PARENT_DEVICE | cl_device_info | declared |
| CL_DEVICE_PARTITION_MAX_SUB_DEVICES | cl_device_info | declared |
| CL_DEVICE_PARTITION_PROPERTIES | cl_device_info | declared |
| CL_DEVICE_PARTITION_AFFINITY_DOMAIN | cl_device_info | declared |
| CL_DEVICE_PARTITION_TYPE | cl_device_info | declared |
| CL_DEVICE_REFERENCE_COUNT | cl_device_info | declared |
| CL_DEVICE_PREFERRED_INTEROP_USER_SYNC | cl_device_info | declared |
| CL_DEVICE_PRINTF_BUFFER_SIZE | cl_device_info | declared |
| CL_DEVICE_IMAGE_PITCH_ALIGNMENT | cl_device_info | declared |
| CL_DEVICE_IMAGE_PITCH_ALIGNMENT_KHR | cl_device_info | declared |
| CL_DEVICE_IMAGE_BASE_ADDRESS_ALIGNMENT | cl_device_info | declared |
| CL_DEVICE_IMAGE_BASE_ADDRESS_ALIGNMENT_KHR | cl_device_info | declared |
| CL_DEVICE_MAX_READ_WRITE_IMAGE_ARGS | cl_device_info | declared |
| CL_DEVICE_MAX_GLOBAL_VARIABLE_SIZE | cl_device_info | declared |
| CL_DEVICE_QUEUE_ON_DEVICE_PROPERTIES | cl_device_info | declared |
| CL_DEVICE_QUEUE_ON_DEVICE_PREFERRED_SIZE | cl_device_info | declared |
| CL_DEVICE_QUEUE_ON_DEVICE_MAX_SIZE | cl_device_info | declared |
| CL_DEVICE_MAX_ON_DEVICE_QUEUES | cl_device_info | declared |
| CL_DEVICE_MAX_ON_DEVICE_EVENTS | cl_device_info | declared |
| CL_DEVICE_SVM_CAPABILITIES | cl_device_info | declared |
| CL_DEVICE_GLOBAL_VARIABLE_PREFERRED_TOTAL_SIZE | cl_device_info | declared |
| CL_DEVICE_MAX_PIPE_ARGS | cl_device_info | declared |
| CL_DEVICE_PIPE_MAX_ACTIVE_RESERVATIONS | cl_device_info | declared |
| CL_DEVICE_PIPE_MAX_PACKET_SIZE | cl_device_info | declared |
| CL_DEVICE_PREFERRED_PLATFORM_ATOMIC_ALIGNMENT | cl_device_info | declared |
| CL_DEVICE_PREFERRED_GLOBAL_ATOMIC_ALIGNMENT | cl_device_info | declared |
| CL_DEVICE_PREFERRED_LOCAL_ATOMIC_ALIGNMENT | cl_device_info | declared |
| CL_DEVICE_IL_VERSION | cl_device_info | declared |
| CL_DEVICE_IL_VERSION_KHR | cl_device_info | declared |
| CL_DEVICE_MAX_NUM_SUB_GROUPS | cl_device_info | declared |
| CL_DEVICE_SUB_GROUP_INDEPENDENT_FORWARD_PROGRESS | cl_device_info | declared |
| CL_DEVICE_NUMERIC_VERSION_KHR | cl_device_info | declared |
| CL_DEVICE_NUMERIC_VERSION | cl_device_info | declared |
| CL_DEVICE_OPENCL_C_NUMERIC_VERSION_KHR | cl_device_info | declared |
| CL_DEVICE_EXTENSIONS_WITH_VERSION_KHR | cl_device_info | declared |
| CL_DEVICE_EXTENSIONS_WITH_VERSION | cl_device_info | declared |
| CL_DEVICE_ILS_WITH_VERSION_KHR | cl_device_info | declared |
| CL_DEVICE_ILS_WITH_VERSION | cl_device_info | declared |
| CL_DEVICE_BUILT_IN_KERNELS_WITH_VERSION_KHR | cl_device_info | declared |
| CL_DEVICE_BUILT_IN_KERNELS_WITH_VERSION | cl_device_info | declared |
| CL_DEVICE_ATOMIC_FENCE_CAPABILITIES | cl_device_info | declared |
| CL_DEVICE_NON_UNIFORM_WORK_GROUP_SUPPORT | cl_device_info | declared |
| CL_DEVICE_OPENCL_C_ALL_VERSIONS | cl_device_info | declared |
| CL_DEVICE_PREFERRED_WORK_GROUP_SIZE_MULTIPLE | cl_device_info | declared |
| CL_DEVICE_WORK_GROUP_COLLECTIVE_FUNCTIONS_SUPPORT | cl_device_info | declared |
| CL_DEVICE_UUID_KHR | cl_device_info | declared |
| CL_DEVICE_UUID | cl_device_info | declared |
| CL_DRIVER_UUID_KHR | cl_device_info | declared |
| CL_DRIVER_UUID | cl_device_info | declared |
| CL_DEVICE_LUID_VALID_KHR | cl_device_info | declared |
| CL_DEVICE_LUID_VALID | cl_device_info | declared |
| CL_DEVICE_LUID_KHR | cl_device_info | declared |
| CL_DEVICE_LUID | cl_device_info | declared |
| CL_DEVICE_NODE_MASK_KHR | cl_device_info | declared |
| CL_DEVICE_NODE_MASK | cl_device_info | declared |
| CL_DEVICE_OPENCL_C_FEATURES | cl_device_info | declared |
| CL_DEVICE_PIPE_SUPPORT | cl_device_info | declared |
| CL_DEVICE_LATEST_CONFORMANCE_VERSION_PASSED | cl_device_info | declared |
| CL_DEVICE_INTEGER_DOT_PRODUCT_CAPABILITIES_KHR | cl_device_info | declared |
| CL_DEVICE_INTEGER_DOT_PRODUCT_CAPABILITIES | cl_device_info | declared |
| CL_DEVICE_INTEGER_DOT_PRODUCT_ACCELERATION_PROPERTIES_8BIT_KHR | cl_device_info | declared |
| CL_DEVICE_INTEGER_DOT_PRODUCT_ACCELERATION_PROPERTIES_8BIT | cl_device_info | declared |
| CL_DEVICE_INTEGER_DOT_PRODUCT_ACCELERATION_PROPERTIES_4x8BIT_PACKED_KHR | cl_device_info | declared |
| CL_DEVICE_INTEGER_DOT_PRODUCT_ACCELERATION_PROPERTIES_4x8BIT_PACKED | cl_device_info | declared |
| CL_DEVICE_KERNEL_CLOCK_CAPABILITIES_KHR | cl_device_info | declared |
| CL_DEVICE_SVM_TYPE_CAPABILITIES_KHR | cl_device_info | declared |
| CL_CONTEXT_REFERENCE_COUNT | cl_device_info | declared |
| CL_CONTEXT_DEVICES | cl_device_info | declared |
| CL_CONTEXT_PROPERTIES | cl_device_info | declared |
| CL_CONTEXT_NUM_DEVICES | cl_device_info | declared |
| CL_CONTEXT_PLATFORM | cl_device_info | declared |
| CL_CONTEXT_INTEROP_USER_SYNC | cl_device_info | declared |
| CL_DEVICE_PARTITION_EQUALLY | cl_device_info | declared |
| CL_DEVICE_PARTITION_BY_COUNTS | cl_device_info | declared |
| CL_QUEUE_CONTEXT | cl_device_info | declared |
| CL_QUEUE_DEVICE | cl_device_info | declared |
| CL_QUEUE_REFERENCE_COUNT | cl_device_info | declared |
| CL_QUEUE_SIZE | cl_device_info | declared |
| CL_QUEUE_DEVICE_DEFAULT | cl_device_info | declared |
| CL_QUEUE_PRIORITY_KHR | cl_device_info | declared |
| CL_QUEUE_THROTTLE_KHR | cl_device_info | declared |
| CL_QUEUE_PROPERTIES_ARRAY | cl_device_info | declared |
| CL_R | cl_device_info | declared |
| CL_A | cl_device_info | declared |
| CL_RG | cl_device_info | declared |
| CL_RA | cl_device_info | declared |
| CL_RGB | cl_device_info | declared |
| CL_RGBA | cl_device_info | declared |
| CL_BGRA | cl_device_info | declared |
| CL_ARGB | cl_device_info | declared |
| CL_INTENSITY | cl_device_info | declared |
| CL_LUMINANCE | cl_device_info | declared |
| CL_Rx | cl_device_info | declared |
| CL_RGx | cl_device_info | declared |
| CL_RGBx | cl_device_info | declared |
| CL_DEPTH | cl_device_info | declared |
| CL_DEPTH_STENCIL | cl_device_info | declared |
| CL_sRGB | cl_device_info | declared |
| CL_sRGBx | cl_device_info | declared |
| CL_sRGBA | cl_device_info | declared |
| CL_sBGRA | cl_device_info | declared |
| CL_ABGR | cl_device_info | declared |
| CL_SNORM_INT8 | cl_device_info | declared |
| CL_SNORM_INT16 | cl_device_info | declared |
| CL_UNORM_INT8 | cl_device_info | declared |
| CL_UNORM_INT16 | cl_device_info | declared |
| CL_UNORM_SHORT_565 | cl_device_info | declared |
| CL_UNORM_SHORT_555 | cl_device_info | declared |
| CL_UNORM_INT_101010 | cl_device_info | declared |
| CL_SIGNED_INT8 | cl_device_info | declared |
| CL_SIGNED_INT16 | cl_device_info | declared |
| CL_SIGNED_INT32 | cl_device_info | declared |
| CL_UNSIGNED_INT8 | cl_device_info | declared |
| CL_UNSIGNED_INT16 | cl_device_info | declared |
| CL_UNSIGNED_INT32 | cl_device_info | declared |
| CL_HALF_FLOAT | cl_device_info | declared |
| CL_FLOAT | cl_device_info | declared |
| CL_UNORM_INT24 | cl_device_info | declared |
| CL_UNORM_INT_101010_2 | cl_device_info | declared |
| CL_UNORM_INT10X6_EXT | cl_device_info | declared |
| CL_UNSIGNED_INT_RAW10_EXT | cl_device_info | declared |
| CL_UNSIGNED_INT_RAW12_EXT | cl_device_info | declared |
| CL_UNORM_INT_2_101010_EXT | cl_device_info | declared |
| CL_UNSIGNED_INT10X6_EXT | cl_device_info | declared |
| CL_UNSIGNED_INT12X4_EXT | cl_device_info | declared |
| CL_UNSIGNED_INT14X2_EXT | cl_device_info | declared |
| CL_UNORM_INT12X4_EXT | cl_device_info | declared |
| CL_UNORM_INT14X2_EXT | cl_device_info | declared |
| CL_MEM_OBJECT_BUFFER | cl_device_info | declared |
| CL_MEM_OBJECT_IMAGE2D | cl_device_info | declared |
| CL_MEM_OBJECT_IMAGE3D | cl_device_info | declared |
| CL_MEM_OBJECT_IMAGE2D_ARRAY | cl_device_info | declared |
| CL_MEM_OBJECT_IMAGE1D | cl_device_info | declared |
| CL_MEM_OBJECT_IMAGE1D_ARRAY | cl_device_info | declared |
| CL_MEM_OBJECT_IMAGE1D_BUFFER | cl_device_info | declared |
| CL_MEM_OBJECT_PIPE | cl_device_info | declared |
| CL_MEM_TYPE | cl_device_info | declared |
| CL_MEM_FLAGS | cl_device_info | declared |
| CL_MEM_SIZE | cl_device_info | declared |
| CL_MEM_HOST_PTR | cl_device_info | declared |
| CL_MEM_MAP_COUNT | cl_device_info | declared |
| CL_MEM_REFERENCE_COUNT | cl_device_info | declared |
| CL_MEM_CONTEXT | cl_device_info | declared |
| CL_MEM_ASSOCIATED_MEMOBJECT | cl_device_info | declared |
| CL_MEM_OFFSET | cl_device_info | declared |
| CL_MEM_USES_SVM_POINTER | cl_device_info | declared |
| CL_MEM_PROPERTIES | cl_device_info | declared |
| CL_IMAGE_FORMAT | cl_device_info | declared |
| CL_IMAGE_ELEMENT_SIZE | cl_device_info | declared |
| CL_IMAGE_ROW_PITCH | cl_device_info | declared |
| CL_IMAGE_SLICE_PITCH | cl_device_info | declared |
| CL_IMAGE_WIDTH | cl_device_info | declared |
| CL_IMAGE_HEIGHT | cl_device_info | declared |
| CL_IMAGE_DEPTH | cl_device_info | declared |
| CL_IMAGE_ARRAY_SIZE | cl_device_info | declared |
| CL_IMAGE_BUFFER | cl_device_info | declared |
| CL_IMAGE_NUM_MIP_LEVELS | cl_device_info | declared |
| CL_IMAGE_NUM_SAMPLES | cl_device_info | declared |
| CL_PIPE_PACKET_SIZE | cl_device_info | declared |
| CL_PIPE_MAX_PACKETS | cl_device_info | declared |
| CL_PIPE_PROPERTIES | cl_device_info | declared |
| CL_ADDRESS_NONE | cl_device_info | declared |
| CL_ADDRESS_CLAMP_TO_EDGE | cl_device_info | declared |
| CL_ADDRESS_CLAMP | cl_device_info | declared |
| CL_ADDRESS_REPEAT | cl_device_info | declared |
| CL_ADDRESS_MIRRORED_REPEAT | cl_device_info | declared |
| CL_FILTER_NEAREST | cl_device_info | declared |
| CL_FILTER_LINEAR | cl_device_info | declared |
| CL_SAMPLER_REFERENCE_COUNT | cl_device_info | declared |
| CL_SAMPLER_CONTEXT | cl_device_info | declared |
| CL_SAMPLER_NORMALIZED_COORDS | cl_device_info | declared |
| CL_SAMPLER_ADDRESSING_MODE | cl_device_info | declared |
| CL_SAMPLER_FILTER_MODE | cl_device_info | declared |
| CL_SAMPLER_MIP_FILTER_MODE | cl_device_info | declared |
| CL_SAMPLER_MIP_FILTER_MODE_KHR | cl_device_info | declared |
| CL_SAMPLER_LOD_MIN | cl_device_info | declared |
| CL_SAMPLER_LOD_MIN_KHR | cl_device_info | declared |
| CL_SAMPLER_LOD_MAX | cl_device_info | declared |
| CL_SAMPLER_LOD_MAX_KHR | cl_device_info | declared |
| CL_SAMPLER_PROPERTIES | cl_device_info | declared |
| CL_PROGRAM_REFERENCE_COUNT | cl_device_info | declared |
| CL_PROGRAM_CONTEXT | cl_device_info | declared |
| CL_PROGRAM_NUM_DEVICES | cl_device_info | declared |
| CL_PROGRAM_DEVICES | cl_device_info | declared |
| CL_PROGRAM_SOURCE | cl_device_info | declared |
| CL_PROGRAM_BINARY_SIZES | cl_device_info | declared |
| CL_PROGRAM_BINARIES | cl_device_info | declared |
| CL_PROGRAM_NUM_KERNELS | cl_device_info | declared |
| CL_PROGRAM_KERNEL_NAMES | cl_device_info | declared |
| CL_PROGRAM_IL | cl_device_info | declared |
| CL_PROGRAM_IL_KHR | cl_device_info | declared |
| CL_PROGRAM_SCOPE_GLOBAL_CTORS_PRESENT | cl_device_info | declared |
| CL_PROGRAM_SCOPE_GLOBAL_DTORS_PRESENT | cl_device_info | declared |
| CL_PROGRAM_BUILD_STATUS | cl_device_info | declared |
| CL_PROGRAM_BUILD_OPTIONS | cl_device_info | declared |
| CL_PROGRAM_BUILD_LOG | cl_device_info | declared |
| CL_PROGRAM_BINARY_TYPE | cl_device_info | declared |
| CL_PROGRAM_BUILD_GLOBAL_VARIABLE_TOTAL_SIZE | cl_device_info | declared |
| CL_KERNEL_FUNCTION_NAME | cl_device_info | declared |
| CL_KERNEL_NUM_ARGS | cl_device_info | declared |
| CL_KERNEL_REFERENCE_COUNT | cl_device_info | declared |
| CL_KERNEL_CONTEXT | cl_device_info | declared |
| CL_KERNEL_PROGRAM | cl_device_info | declared |
| CL_KERNEL_ATTRIBUTES | cl_device_info | declared |
| CL_KERNEL_ARG_ADDRESS_QUALIFIER | cl_device_info | declared |
| CL_KERNEL_ARG_ACCESS_QUALIFIER | cl_device_info | declared |
| CL_KERNEL_ARG_TYPE_NAME | cl_device_info | declared |
| CL_KERNEL_ARG_NAME | cl_device_info | declared |
| CL_KERNEL_ARG_ADDRESS_GLOBAL | cl_device_info | declared |
| CL_KERNEL_ARG_ADDRESS_LOCAL | cl_device_info | declared |
| CL_KERNEL_ARG_ADDRESS_CONSTANT | cl_device_info | declared |
| CL_KERNEL_ARG_ADDRESS_PRIVATE | cl_device_info | declared |
| CL_KERNEL_ARG_ACCESS_READ_ONLY | cl_device_info | declared |
| CL_KERNEL_ARG_ACCESS_WRITE_ONLY | cl_device_info | declared |
| CL_KERNEL_ARG_ACCESS_READ_WRITE | cl_device_info | declared |
| CL_KERNEL_ARG_ACCESS_NONE | cl_device_info | declared |
| CL_KERNEL_WORK_GROUP_SIZE | cl_device_info | declared |
| CL_KERNEL_COMPILE_WORK_GROUP_SIZE | cl_device_info | declared |
| CL_KERNEL_LOCAL_MEM_SIZE | cl_device_info | declared |
| CL_KERNEL_PREFERRED_WORK_GROUP_SIZE_MULTIPLE | cl_device_info | declared |
| CL_KERNEL_PRIVATE_MEM_SIZE | cl_device_info | declared |
| CL_KERNEL_GLOBAL_WORK_SIZE | cl_device_info | declared |
| CL_KERNEL_EXEC_INFO_SVM_PTRS | cl_device_info | declared |
| CL_KERNEL_EXEC_INFO_SVM_FINE_GRAIN_SYSTEM | cl_device_info | declared |
| CL_KERNEL_LOCAL_SIZE_FOR_SUB_GROUP_COUNT | cl_device_info | declared |
| CL_KERNEL_MAX_NUM_SUB_GROUPS | cl_device_info | declared |
| CL_KERNEL_COMPILE_NUM_SUB_GROUPS | cl_device_info | declared |
| CL_KERNEL_EXEC_INFO_SVM_INDIRECT_ACCESS_KHR | cl_device_info | declared |
| CL_EVENT_COMMAND_QUEUE | cl_device_info | declared |
| CL_EVENT_COMMAND_TYPE | cl_device_info | declared |
| CL_EVENT_REFERENCE_COUNT | cl_device_info | declared |
| CL_EVENT_COMMAND_EXECUTION_STATUS | cl_device_info | declared |
| CL_EVENT_CONTEXT | cl_device_info | declared |
| CL_COMMAND_NDRANGE_KERNEL | cl_device_info | declared |
| CL_COMMAND_TASK | cl_device_info | declared |
| CL_COMMAND_NATIVE_KERNEL | cl_device_info | declared |
| CL_COMMAND_READ_BUFFER | cl_device_info | declared |
| CL_COMMAND_WRITE_BUFFER | cl_device_info | declared |
| CL_COMMAND_COPY_BUFFER | cl_device_info | declared |
| CL_COMMAND_READ_IMAGE | cl_device_info | declared |
| CL_COMMAND_WRITE_IMAGE | cl_device_info | declared |
| CL_COMMAND_COPY_IMAGE | cl_device_info | declared |
| CL_COMMAND_COPY_IMAGE_TO_BUFFER | cl_device_info | declared |
| CL_COMMAND_COPY_BUFFER_TO_IMAGE | cl_device_info | declared |
| CL_COMMAND_MAP_BUFFER | cl_device_info | declared |
| CL_COMMAND_MAP_IMAGE | cl_device_info | declared |
| CL_COMMAND_UNMAP_MEM_OBJECT | cl_device_info | declared |
| CL_COMMAND_MARKER | cl_device_info | declared |
| CL_COMMAND_ACQUIRE_GL_OBJECTS | cl_device_info | declared |
| CL_COMMAND_RELEASE_GL_OBJECTS | cl_device_info | declared |
| CL_COMMAND_READ_BUFFER_RECT | cl_device_info | declared |
| CL_COMMAND_WRITE_BUFFER_RECT | cl_device_info | declared |
| CL_COMMAND_COPY_BUFFER_RECT | cl_device_info | declared |
| CL_COMMAND_USER | cl_device_info | declared |
| CL_COMMAND_BARRIER | cl_device_info | declared |
| CL_COMMAND_MIGRATE_MEM_OBJECTS | cl_device_info | declared |
| CL_COMMAND_FILL_BUFFER | cl_device_info | declared |
| CL_COMMAND_FILL_IMAGE | cl_device_info | declared |
| CL_COMMAND_SVM_FREE | cl_device_info | declared |
| CL_COMMAND_SVM_MEMCPY | cl_device_info | declared |
| CL_COMMAND_SVM_MEMFILL | cl_device_info | declared |
| CL_COMMAND_SVM_MAP | cl_device_info | declared |
| CL_COMMAND_SVM_UNMAP | cl_device_info | declared |
| CL_COMMAND_SVM_MIGRATE_MEM | cl_device_info | declared |
| CL_BUFFER_CREATE_TYPE_REGION | cl_device_info | declared |
| CL_PROFILING_COMMAND_QUEUED | cl_device_info | declared |
| CL_PROFILING_COMMAND_SUBMIT | cl_device_info | declared |
| CL_PROFILING_COMMAND_START | cl_device_info | declared |
| CL_PROFILING_COMMAND_END | cl_device_info | declared |
| CL_PROFILING_COMMAND_COMPLETE | cl_device_info | declared |
| CL_IMAGE_REQUIREMENTS_ROW_PITCH_ALIGNMENT_EXT | cl_device_info | declared |
| CL_IMAGE_REQUIREMENTS_SLICE_PITCH_ALIGNMENT_EXT | cl_device_info | declared |
| CL_IMAGE_REQUIREMENTS_BASE_ADDRESS_ALIGNMENT_EXT | cl_device_info | declared |
| CL_COMMAND_BUFFER_FLAGS_KHR | cl_device_info | declared |
| CL_COMMAND_BUFFER_QUEUES_KHR | cl_device_info | declared |
| CL_COMMAND_BUFFER_NUM_QUEUES_KHR | cl_device_info | declared |
| CL_COMMAND_BUFFER_REFERENCE_COUNT_KHR | cl_device_info | declared |
| CL_COMMAND_BUFFER_STATE_KHR | cl_device_info | declared |
| CL_COMMAND_BUFFER_PROPERTIES_ARRAY_KHR | cl_device_info | declared |
| CL_COMMAND_BUFFER_CONTEXT_KHR | cl_device_info | declared |
| CL_DEVICE_COMMAND_BUFFER_SUPPORTED_QUEUE_PROPERTIES_KHR | cl_device_info | declared |
| CL_MUTABLE_COMMAND_COMMAND_QUEUE_KHR | cl_device_info | declared |
| CL_MUTABLE_COMMAND_COMMAND_BUFFER_KHR | cl_device_info | declared |
| CL_MUTABLE_COMMAND_PROPERTIES_ARRAY_KHR | cl_device_info | declared |
| CL_MUTABLE_DISPATCH_KERNEL_KHR | cl_device_info | declared |
| CL_MUTABLE_DISPATCH_DIMENSIONS_KHR | cl_device_info | declared |
| CL_MUTABLE_DISPATCH_GLOBAL_WORK_OFFSET_KHR | cl_device_info | declared |
| CL_MUTABLE_DISPATCH_GLOBAL_WORK_SIZE_KHR | cl_device_info | declared |
| CL_MUTABLE_DISPATCH_LOCAL_WORK_SIZE_KHR | cl_device_info | declared |
| CL_COMMAND_COMMAND_BUFFER_KHR | cl_device_info | declared |
| CL_DEVICE_COMMAND_BUFFER_CAPABILITIES_KHR | cl_device_info | declared |
| CL_DEVICE_COMMAND_BUFFER_REQUIRED_QUEUE_PROPERTIES_KHR | cl_device_info | declared |
| CL_DEVICE_COMMAND_BUFFER_NUM_SYNC_DEVICES_KHR | cl_device_info | declared |
| CL_MUTABLE_COMMAND_COMMAND_TYPE_KHR | cl_device_info | declared |
| CL_MUTABLE_DISPATCH_UPDATABLE_FIELDS_KHR | cl_device_info | declared |
| CL_IMAGE_REQUIREMENTS_SIZE_EXT | cl_device_info | declared |
| CL_IMAGE_REQUIREMENTS_MAX_WIDTH_EXT | cl_device_info | declared |
| CL_IMAGE_REQUIREMENTS_MAX_HEIGHT_EXT | cl_device_info | declared |
| CL_IMAGE_REQUIREMENTS_MAX_DEPTH_EXT | cl_device_info | declared |
| CL_IMAGE_REQUIREMENTS_MAX_ARRAY_SIZE_EXT | cl_device_info | declared |
| CL_COMMAND_BUFFER_MUTABLE_DISPATCH_ASSERTS_KHR | cl_device_info | declared |
| CL_MUTABLE_DISPATCH_ASSERTS_KHR | cl_device_info | declared |
| CL_DEVICE_SPIRV_EXTENDED_INSTRUCTION_SETS_KHR | cl_device_info | declared |
| CL_DEVICE_SPIRV_EXTENDED_INSTRUCTION_SETS | cl_device_info | declared |
| CL_DEVICE_SPIRV_EXTENSIONS_KHR | cl_device_info | declared |
| CL_DEVICE_SPIRV_EXTENSIONS | cl_device_info | declared |
| CL_DEVICE_SPIRV_CAPABILITIES_KHR | cl_device_info | declared |
| CL_DEVICE_SPIRV_CAPABILITIES | cl_device_info | declared |

## Group: `cl_device_integer_dot_product_capabilities` (2 single-members)

| token | container | confidence |
|---|---|---|
| CL_DEVICE_INTEGER_DOT_PRODUCT_INPUT_4x8BIT_PACKED | cl_device_integer_dot_product_capabilities | declared |
| CL_DEVICE_INTEGER_DOT_PRODUCT_INPUT_4x8BIT | cl_device_integer_dot_product_capabilities | declared |

## Group: `cl_device_integer_dot_product_capabilities_khr` (2 single-members)

| token | container | confidence |
|---|---|---|
| CL_DEVICE_INTEGER_DOT_PRODUCT_INPUT_4x8BIT_PACKED_KHR | cl_device_integer_dot_product_capabilities_khr | declared |
| CL_DEVICE_INTEGER_DOT_PRODUCT_INPUT_4x8BIT_KHR | cl_device_integer_dot_product_capabilities_khr | declared |

## Group: `cl_device_kernel_clock_capabilities_khr` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_DEVICE_KERNEL_CLOCK_SCOPE_DEVICE_KHR | cl_device_kernel_clock_capabilities_khr | declared |
| CL_DEVICE_KERNEL_CLOCK_SCOPE_WORK_GROUP_KHR | cl_device_kernel_clock_capabilities_khr | declared |
| CL_DEVICE_KERNEL_CLOCK_SCOPE_SUB_GROUP_KHR | cl_device_kernel_clock_capabilities_khr | declared |

## Group: `cl_device_local_mem_type` (2 single-members)

| token | container | confidence |
|---|---|---|
| CL_LOCAL | cl_device_local_mem_type | declared |
| CL_GLOBAL | cl_device_local_mem_type | declared |

## Group: `cl_device_mem_cache_type` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_NONE | cl_device_mem_cache_type | high |
| CL_READ_ONLY_CACHE | cl_device_mem_cache_type | declared |
| CL_READ_WRITE_CACHE | cl_device_mem_cache_type | declared |

## Group: `cl_device_scheduling_controls_capabilities_arm` (8 single-members)

| token | container | confidence |
|---|---|---|
| CL_DEVICE_SCHEDULING_KERNEL_BATCHING_ARM | cl_device_scheduling_controls_capabilities_arm | declared |
| CL_DEVICE_SCHEDULING_WORKGROUP_BATCH_SIZE_ARM | cl_device_scheduling_controls_capabilities_arm | declared |
| CL_DEVICE_SCHEDULING_WORKGROUP_BATCH_SIZE_MODIFIER_ARM | cl_device_scheduling_controls_capabilities_arm | declared |
| CL_DEVICE_SCHEDULING_DEFERRED_FLUSH_ARM | cl_device_scheduling_controls_capabilities_arm | declared |
| CL_DEVICE_SCHEDULING_REGISTER_ALLOCATION_ARM | cl_device_scheduling_controls_capabilities_arm | declared |
| CL_DEVICE_SCHEDULING_WARP_THROTTLING_ARM | cl_device_scheduling_controls_capabilities_arm | declared |
| CL_DEVICE_SCHEDULING_COMPUTE_UNIT_BATCH_QUEUE_SIZE_ARM | cl_device_scheduling_controls_capabilities_arm | declared |
| CL_DEVICE_SCHEDULING_COMPUTE_UNIT_LIMIT_ARM | cl_device_scheduling_controls_capabilities_arm | declared |

## Group: `cl_device_scheduling_controls_capabilities_img` (7 single-members)

| token | container | confidence |
|---|---|---|
| CL_DEVICE_WORK_GROUP_SCHEDULING_ALGORITHM_LINEAR_ORDER_IMG | cl_device_scheduling_controls_capabilities_img | declared |
| CL_DEVICE_WORK_GROUP_SCHEDULING_ALGORITHM_MORTON_ORDER_IMG | cl_device_scheduling_controls_capabilities_img | declared |
| CL_DEVICE_WORK_GROUP_SCHEDULING_ALGORITHM_TWOD_MORTON_ORDER_IMG | cl_device_scheduling_controls_capabilities_img | declared |
| CL_DEVICE_WORK_GROUP_SCHEDULING_ALGORITHM_THREED_MORTON_ORDER_IMG | cl_device_scheduling_controls_capabilities_img | declared |
| CL_DEVICE_WORK_GROUP_ARBITRATION_ALGORITHM_TASK_DEMAND_IMG | cl_device_scheduling_controls_capabilities_img | declared |
| CL_DEVICE_WORK_GROUP_ARBITRATION_ALGORITHM_ROUND_ROBIN_IMG | cl_device_scheduling_controls_capabilities_img | declared |
| CL_DEVICE_WORK_GROUP_EXECUTE_COUNT_IMG | cl_device_scheduling_controls_capabilities_img | declared |

## Group: `cl_device_svm_capabilities` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_DEVICE_SVM_COARSE_GRAIN_BUFFER | cl_device_svm_capabilities | high |
| CL_DEVICE_SVM_FINE_GRAIN_BUFFER | cl_device_svm_capabilities | declared |
| CL_DEVICE_SVM_FINE_GRAIN_SYSTEM | cl_device_svm_capabilities | declared |

## Group: `cl_device_terminate_capability_khr` (1 single-members)

| token | container | confidence |
|---|---|---|
| CL_DEVICE_TERMINATE_CAPABILITY_CONTEXT_KHR | cl_device_terminate_capability_khr | declared |

## Group: `cl_device_type` (7 single-members)

| token | container | confidence |
|---|---|---|
| CL_DEVICE_TYPE_DEFAULT | cl_device_type | declared |
| CL_DEVICE_TYPE_CPU | cl_device_type | declared |
| CL_DEVICE_TYPE_GPU | cl_device_type | declared |
| CL_DEVICE_TYPE_ACCELERATOR | cl_device_type | declared |
| CL_DEVICE_TYPE_CUSTOM | cl_device_type | declared |
| CL_DEVICE_TYPE_ALL | cl_device_type | declared |
| CL_DEVICE_TYPE_RESERVED0_QCOM | cl_device_type | declared |

## Group: `cl_device_unified_shared_memory_capabilities_intel` (4 single-members)

| token | container | confidence |
|---|---|---|
| CL_UNIFIED_SHARED_MEMORY_ACCESS_INTEL | cl_device_unified_shared_memory_capabilities_intel | declared |
| CL_UNIFIED_SHARED_MEMORY_ATOMIC_ACCESS_INTEL | cl_device_unified_shared_memory_capabilities_intel | declared |
| CL_UNIFIED_SHARED_MEMORY_CONCURRENT_ACCESS_INTEL | cl_device_unified_shared_memory_capabilities_intel | declared |
| CL_UNIFIED_SHARED_MEMORY_CONCURRENT_ATOMIC_ACCESS_INTEL | cl_device_unified_shared_memory_capabilities_intel | declared |

## Group: `cl_diagnostic_verbose_level_intel` (4 single-members)

| token | container | confidence |
|---|---|---|
| CL_CONTEXT_DIAGNOSTICS_LEVEL_ALL_INTEL | cl_diagnostic_verbose_level_intel | declared |
| CL_CONTEXT_DIAGNOSTICS_LEVEL_GOOD_INTEL | cl_diagnostic_verbose_level_intel | declared |
| CL_CONTEXT_DIAGNOSTICS_LEVEL_BAD_INTEL | cl_diagnostic_verbose_level_intel | declared |
| CL_CONTEXT_DIAGNOSTICS_LEVEL_NEUTRAL_INTEL | cl_diagnostic_verbose_level_intel | declared |

## Group: `cl_icdl_info` (4 single-members)

| token | container | confidence |
|---|---|---|
| CL_ICDL_OCL_VERSION | cl_icdl_info | declared |
| CL_ICDL_VERSION | cl_icdl_info | declared |
| CL_ICDL_NAME | cl_icdl_info | declared |
| CL_ICDL_VENDOR | cl_icdl_info | declared |

## Group: `cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_ME_FORWARD_INPUT_MODE_INTEL | cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel | declared |
| CL_ME_BACKWARD_INPUT_MODE_INTEL | cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel | declared |
| CL_ME_BIDIRECTION_INPUT_MODE_INTEL | cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel | declared |

## Group: `cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel.2` (5 single-members)

| token | container | confidence |
|---|---|---|
| CL_ME_BIDIR_WEIGHT_QUARTER_INTEL | cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel.2 | declared |
| CL_ME_BIDIR_WEIGHT_THIRD_INTEL | cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel.2 | declared |
| CL_ME_BIDIR_WEIGHT_HALF_INTEL | cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel.2 | declared |
| CL_ME_BIDIR_WEIGHT_TWO_THIRD_INTEL | cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel.2 | declared |
| CL_ME_BIDIR_WEIGHT_THREE_QUARTER_INTEL | cl_intel_advanced_motion_estimation.cl_motion_detect_desc_intel.2 | declared |

## Group: `cl_intel_advanced_motion_estimation.device_me_version` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_ME_VERSION_LEGACY_INTEL | cl_intel_advanced_motion_estimation.device_me_version | declared |
| CL_ME_VERSION_ADVANCED_VER_1_INTEL | cl_intel_advanced_motion_estimation.device_me_version | declared |
| CL_ME_VERSION_ADVANCED_VER_2_INTEL | cl_intel_advanced_motion_estimation.device_me_version | declared |

## Group: `cl_intel_advanced_motion_estimation.flags` (2 single-members)

| token | container | confidence |
|---|---|---|
| CL_ME_CHROMA_INTRA_PREDICT_ENABLED_INTEL | cl_intel_advanced_motion_estimation.flags | declared |
| CL_ME_LUMA_INTRA_PREDICT_ENABLED_INTEL | cl_intel_advanced_motion_estimation.flags | declared |

## Group: `cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.chroma_block` (4 single-members)

| token | container | confidence |
|---|---|---|
| CL_ME_CHROMA_PREDICTOR_MODE_DC_INTEL | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.chroma_block | declared |
| CL_ME_CHROMA_PREDICTOR_MODE_HORIZONTAL_INTEL | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.chroma_block | declared |
| CL_ME_CHROMA_PREDICTOR_MODE_VERTICAL_INTEL | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.chroma_block | declared |
| CL_ME_CHROMA_PREDICTOR_MODE_PLANE_INTEL | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.chroma_block | declared |

## Group: `cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block` (10 single-members)

| token | container | confidence |
|---|---|---|
| CL_ME_LUMA_PREDICTOR_MODE_VERTICAL_INTEL | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block | declared |
| CL_ME_LUMA_PREDICTOR_MODE_HORIZONTAL_INTEL | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block | declared |
| CL_ME_LUMA_PREDICTOR_MODE_DC_INTEL | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block | declared |
| CL_ME_LUMA_PREDICTOR_MODE_DIAGONAL_DOWN_LEFT_INTEL | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block | declared |
| CL_ME_LUMA_PREDICTOR_MODE_DIAGONAL_DOWN_RIGHT_INTEL | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block | declared |
| CL_ME_LUMA_PREDICTOR_MODE_PLANE_INTEL | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block | declared |
| CL_ME_LUMA_PREDICTOR_MODE_VERTICAL_RIGHT_INTEL | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block | declared |
| CL_ME_LUMA_PREDICTOR_MODE_HORIZONTAL_DOWN_INTEL | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block | declared |
| CL_ME_LUMA_PREDICTOR_MODE_VERTICAL_LEFT_INTEL | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block | declared |
| CL_ME_LUMA_PREDICTOR_MODE_HORIZONTAL_UP_INTEL | cl_intel_advanced_motion_estimation.intra_search_prediction_modes_buffer.luma_block | declared |

## Group: `cl_intel_advanced_motion_estimation.search_cost_penalty` (4 single-members)

| token | container | confidence |
|---|---|---|
| CL_ME_COST_PENALTY_NONE_INTEL | cl_intel_advanced_motion_estimation.search_cost_penalty | declared |
| CL_ME_COST_PENALTY_LOW_INTEL | cl_intel_advanced_motion_estimation.search_cost_penalty | declared |
| CL_ME_COST_PENALTY_NORMAL_INTEL | cl_intel_advanced_motion_estimation.search_cost_penalty | declared |
| CL_ME_COST_PENALTY_HIGH_INTEL | cl_intel_advanced_motion_estimation.search_cost_penalty | declared |

## Group: `cl_intel_advanced_motion_estimation.search_cost_precision` (4 single-members)

| token | container | confidence |
|---|---|---|
| CL_ME_COST_PRECISION_QPEL_INTEL | cl_intel_advanced_motion_estimation.search_cost_precision | declared |
| CL_ME_COST_PRECISION_HPEL_INTEL | cl_intel_advanced_motion_estimation.search_cost_precision | declared |
| CL_ME_COST_PRECISION_PEL_INTEL | cl_intel_advanced_motion_estimation.search_cost_precision | declared |
| CL_ME_COST_PRECISION_DPEL_INTEL | cl_intel_advanced_motion_estimation.search_cost_precision | declared |

## Group: `cl_intel_advanced_motion_estimation.skip_block_type` (2 single-members)

| token | container | confidence |
|---|---|---|
| CL_ME_SKIP_BLOCK_TYPE_16x16_INTEL | cl_intel_advanced_motion_estimation.skip_block_type | declared |
| CL_ME_SKIP_BLOCK_TYPE_8x8_INTEL | cl_intel_advanced_motion_estimation.skip_block_type | declared |

## Group: `cl_intel_device_side_avc_motion_estimation.adjust` (2 single-members)

| token | container | confidence |
|---|---|---|
| CL_AVC_ME_SAD_ADJUST_MODE_NONE_INTEL | cl_intel_device_side_avc_motion_estimation.adjust | declared |
| CL_AVC_ME_SAD_ADJUST_MODE_HAAR_INTEL | cl_intel_device_side_avc_motion_estimation.adjust | declared |

## Group: `cl_intel_device_side_avc_motion_estimation.border` (4 single-members)

| token | container | confidence |
|---|---|---|
| CL_AVC_ME_BORDER_REACHED_LEFT_INTEL | cl_intel_device_side_avc_motion_estimation.border | declared |
| CL_AVC_ME_BORDER_REACHED_RIGHT_INTEL | cl_intel_device_side_avc_motion_estimation.border | declared |
| CL_AVC_ME_BORDER_REACHED_TOP_INTEL | cl_intel_device_side_avc_motion_estimation.border | declared |
| CL_AVC_ME_BORDER_REACHED_BOTTOM_INTEL | cl_intel_device_side_avc_motion_estimation.border | declared |

## Group: `cl_intel_device_side_avc_motion_estimation.cost.precision` (4 single-members)

| token | container | confidence |
|---|---|---|
| CL_AVC_ME_COST_PRECISION_QPEL_INTEL | cl_intel_device_side_avc_motion_estimation.cost.precision | declared |
| CL_AVC_ME_COST_PRECISION_HPEL_INTEL | cl_intel_device_side_avc_motion_estimation.cost.precision | declared |
| CL_AVC_ME_COST_PRECISION_PEL_INTEL | cl_intel_device_side_avc_motion_estimation.cost.precision | declared |
| CL_AVC_ME_COST_PRECISION_DPEL_INTEL | cl_intel_device_side_avc_motion_estimation.cost.precision | declared |

## Group: `cl_intel_device_side_avc_motion_estimation.frame.dir` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_AVC_ME_FRAME_FORWARD_INTEL | cl_intel_device_side_avc_motion_estimation.frame.dir | declared |
| CL_AVC_ME_FRAME_BACKWARD_INTEL | cl_intel_device_side_avc_motion_estimation.frame.dir | declared |
| CL_AVC_ME_FRAME_DUAL_INTEL | cl_intel_device_side_avc_motion_estimation.frame.dir | declared |

## Group: `cl_intel_device_side_avc_motion_estimation.intra` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_AVC_ME_INTRA_16x16_INTEL | cl_intel_device_side_avc_motion_estimation.intra | declared |
| CL_AVC_ME_INTRA_8x8_INTEL | cl_intel_device_side_avc_motion_estimation.intra | declared |
| CL_AVC_ME_INTRA_4x4_INTEL | cl_intel_device_side_avc_motion_estimation.intra | declared |

## Group: `cl_intel_device_side_avc_motion_estimation.intra.luma` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_AVC_ME_INTRA_LUMA_PARTITION_MASK_16x16_INTEL | cl_intel_device_side_avc_motion_estimation.intra.luma | declared |
| CL_AVC_ME_INTRA_LUMA_PARTITION_MASK_8x8_INTEL | cl_intel_device_side_avc_motion_estimation.intra.luma | declared |
| CL_AVC_ME_INTRA_LUMA_PARTITION_MASK_4x4_INTEL | cl_intel_device_side_avc_motion_estimation.intra.luma | declared |

## Group: `cl_intel_device_side_avc_motion_estimation.intra.neighbor` (4 single-members)

| token | container | confidence |
|---|---|---|
| CL_AVC_ME_INTRA_NEIGHBOR_LEFT_MASK_ENABLE_INTEL | cl_intel_device_side_avc_motion_estimation.intra.neighbor | declared |
| CL_AVC_ME_INTRA_NEIGHBOR_UPPER_MASK_ENABLE_INTEL | cl_intel_device_side_avc_motion_estimation.intra.neighbor | declared |
| CL_AVC_ME_INTRA_NEIGHBOR_UPPER_RIGHT_MASK_ENABLE_INTEL | cl_intel_device_side_avc_motion_estimation.intra.neighbor | declared |
| CL_AVC_ME_INTRA_NEIGHBOR_UPPER_LEFT_MASK_ENABLE_INTEL | cl_intel_device_side_avc_motion_estimation.intra.neighbor | declared |

## Group: `cl_intel_device_side_avc_motion_estimation.luma.predictor` (14 single-members)

| token | container | confidence |
|---|---|---|
| CL_AVC_ME_LUMA_PREDICTOR_MODE_VERTICAL_INTEL | cl_intel_device_side_avc_motion_estimation.luma.predictor | declared |
| CL_AVC_ME_LUMA_PREDICTOR_MODE_HORIZONTAL_INTEL | cl_intel_device_side_avc_motion_estimation.luma.predictor | declared |
| CL_AVC_ME_LUMA_PREDICTOR_MODE_DC_INTEL | cl_intel_device_side_avc_motion_estimation.luma.predictor | declared |
| CL_AVC_ME_LUMA_PREDICTOR_MODE_DIAGONAL_DOWN_LEFT_INTEL | cl_intel_device_side_avc_motion_estimation.luma.predictor | declared |
| CL_AVC_ME_LUMA_PREDICTOR_MODE_DIAGONAL_DOWN_RIGHT_INTEL | cl_intel_device_side_avc_motion_estimation.luma.predictor | declared |
| CL_AVC_ME_LUMA_PREDICTOR_MODE_PLANE_INTEL | cl_intel_device_side_avc_motion_estimation.luma.predictor | declared |
| CL_AVC_ME_LUMA_PREDICTOR_MODE_VERTICAL_RIGHT_INTEL | cl_intel_device_side_avc_motion_estimation.luma.predictor | declared |
| CL_AVC_ME_LUMA_PREDICTOR_MODE_HORIZONTAL_DOWN_INTEL | cl_intel_device_side_avc_motion_estimation.luma.predictor | declared |
| CL_AVC_ME_LUMA_PREDICTOR_MODE_VERTICAL_LEFT_INTEL | cl_intel_device_side_avc_motion_estimation.luma.predictor | declared |
| CL_AVC_ME_LUMA_PREDICTOR_MODE_HORIZONTAL_UP_INTEL | cl_intel_device_side_avc_motion_estimation.luma.predictor | declared |
| CL_AVC_ME_CHROMA_PREDICTOR_MODE_DC_INTEL | cl_intel_device_side_avc_motion_estimation.luma.predictor | declared |
| CL_AVC_ME_CHROMA_PREDICTOR_MODE_HORIZONTAL_INTEL | cl_intel_device_side_avc_motion_estimation.luma.predictor | declared |
| CL_AVC_ME_CHROMA_PREDICTOR_MODE_VERTICAL_INTEL | cl_intel_device_side_avc_motion_estimation.luma.predictor | declared |
| CL_AVC_ME_CHROMA_PREDICTOR_MODE_PLANE_INTEL | cl_intel_device_side_avc_motion_estimation.luma.predictor | declared |

## Group: `cl_intel_device_side_avc_motion_estimation.major` (4 single-members)

| token | container | confidence |
|---|---|---|
| CL_AVC_ME_MAJOR_16x16_INTEL | cl_intel_device_side_avc_motion_estimation.major | declared |
| CL_AVC_ME_MAJOR_16x8_INTEL | cl_intel_device_side_avc_motion_estimation.major | declared |
| CL_AVC_ME_MAJOR_8x16_INTEL | cl_intel_device_side_avc_motion_estimation.major | declared |
| CL_AVC_ME_MAJOR_8x8_INTEL | cl_intel_device_side_avc_motion_estimation.major | declared |

## Group: `cl_intel_device_side_avc_motion_estimation.major.dir` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_AVC_ME_MAJOR_FORWARD_INTEL | cl_intel_device_side_avc_motion_estimation.major.dir | declared |
| CL_AVC_ME_MAJOR_BACKWARD_INTEL | cl_intel_device_side_avc_motion_estimation.major.dir | declared |
| CL_AVC_ME_MAJOR_BIDIRECTIONAL_INTEL | cl_intel_device_side_avc_motion_estimation.major.dir | declared |

## Group: `cl_intel_device_side_avc_motion_estimation.minor` (4 single-members)

| token | container | confidence |
|---|---|---|
| CL_AVC_ME_MINOR_8x8_INTEL | cl_intel_device_side_avc_motion_estimation.minor | declared |
| CL_AVC_ME_MINOR_8x4_INTEL | cl_intel_device_side_avc_motion_estimation.minor | declared |
| CL_AVC_ME_MINOR_4x8_INTEL | cl_intel_device_side_avc_motion_estimation.minor | declared |
| CL_AVC_ME_MINOR_4x4_INTEL | cl_intel_device_side_avc_motion_estimation.minor | declared |

## Group: `cl_intel_device_side_avc_motion_estimation.partition` (8 single-members)

| token | container | confidence |
|---|---|---|
| CL_AVC_ME_PARTITION_MASK_ALL_INTEL | cl_intel_device_side_avc_motion_estimation.partition | declared |
| CL_AVC_ME_PARTITION_MASK_16x16_INTEL | cl_intel_device_side_avc_motion_estimation.partition | declared |
| CL_AVC_ME_PARTITION_MASK_16x8_INTEL | cl_intel_device_side_avc_motion_estimation.partition | declared |
| CL_AVC_ME_PARTITION_MASK_8x16_INTEL | cl_intel_device_side_avc_motion_estimation.partition | declared |
| CL_AVC_ME_PARTITION_MASK_8x8_INTEL | cl_intel_device_side_avc_motion_estimation.partition | declared |
| CL_AVC_ME_PARTITION_MASK_8x4_INTEL | cl_intel_device_side_avc_motion_estimation.partition | declared |
| CL_AVC_ME_PARTITION_MASK_4x8_INTEL | cl_intel_device_side_avc_motion_estimation.partition | declared |
| CL_AVC_ME_PARTITION_MASK_4x4_INTEL | cl_intel_device_side_avc_motion_estimation.partition | declared |

## Group: `cl_intel_device_side_avc_motion_estimation.scan.dir` (2 single-members)

| token | container | confidence |
|---|---|---|
| CL_AVC_ME_INTERLACED_SCAN_TOP_FIELD_INTEL | cl_intel_device_side_avc_motion_estimation.scan.dir | declared |
| CL_AVC_ME_INTERLACED_SCAN_BOTTOM_FIELD_INTEL | cl_intel_device_side_avc_motion_estimation.scan.dir | declared |

## Group: `cl_intel_device_side_avc_motion_estimation.skip` (2 single-members)

| token | container | confidence |
|---|---|---|
| CL_AVC_ME_SKIP_BLOCK_PARTITION_16x16_INTEL | cl_intel_device_side_avc_motion_estimation.skip | declared |
| CL_AVC_ME_SKIP_BLOCK_PARTITION_8x8_INTEL | cl_intel_device_side_avc_motion_estimation.skip | declared |

## Group: `cl_intel_device_side_avc_motion_estimation.skip.block.based` (2 single-members)

| token | container | confidence |
|---|---|---|
| CL_AVC_ME_BLOCK_BASED_SKIP_4x4_INTEL | cl_intel_device_side_avc_motion_estimation.skip.block.based | declared |
| CL_AVC_ME_BLOCK_BASED_SKIP_8x8_INTEL | cl_intel_device_side_avc_motion_estimation.skip.block.based | declared |

## Group: `cl_intel_device_side_avc_motion_estimation.skip.dir` (14 single-members)

| token | container | confidence |
|---|---|---|
| CL_AVC_ME_SKIP_BLOCK_16x16_FORWARD_ENABLE_INTEL | cl_intel_device_side_avc_motion_estimation.skip.dir | declared |
| CL_AVC_ME_SKIP_BLOCK_16x16_BACKWARD_ENABLE_INTEL | cl_intel_device_side_avc_motion_estimation.skip.dir | declared |
| CL_AVC_ME_SKIP_BLOCK_16x16_DUAL_ENABLE_INTEL | cl_intel_device_side_avc_motion_estimation.skip.dir | declared |
| CL_AVC_ME_SKIP_BLOCK_8x8_FORWARD_ENABLE_INTEL | cl_intel_device_side_avc_motion_estimation.skip.dir | declared |
| CL_AVC_ME_SKIP_BLOCK_8x8_BACKWARD_ENABLE_INTEL | cl_intel_device_side_avc_motion_estimation.skip.dir | declared |
| CL_AVC_ME_SKIP_BLOCK_8x8_DUAL_ENABLE_INTEL | cl_intel_device_side_avc_motion_estimation.skip.dir | declared |
| CL_AVC_ME_SKIP_BLOCK_8x8_0_FORWARD_ENABLE_INTEL | cl_intel_device_side_avc_motion_estimation.skip.dir | declared |
| CL_AVC_ME_SKIP_BLOCK_8x8_0_BACKWARD_ENABLE_INTEL | cl_intel_device_side_avc_motion_estimation.skip.dir | declared |
| CL_AVC_ME_SKIP_BLOCK_8x8_1_FORWARD_ENABLE_INTEL | cl_intel_device_side_avc_motion_estimation.skip.dir | declared |
| CL_AVC_ME_SKIP_BLOCK_8x8_1_BACKWARD_ENABLE_INTEL | cl_intel_device_side_avc_motion_estimation.skip.dir | declared |
| CL_AVC_ME_SKIP_BLOCK_8x8_2_FORWARD_ENABLE_INTEL | cl_intel_device_side_avc_motion_estimation.skip.dir | declared |
| CL_AVC_ME_SKIP_BLOCK_8x8_2_BACKWARD_ENABLE_INTEL | cl_intel_device_side_avc_motion_estimation.skip.dir | declared |
| CL_AVC_ME_SKIP_BLOCK_8x8_3_FORWARD_ENABLE_INTEL | cl_intel_device_side_avc_motion_estimation.skip.dir | declared |
| CL_AVC_ME_SKIP_BLOCK_8x8_3_BACKWARD_ENABLE_INTEL | cl_intel_device_side_avc_motion_estimation.skip.dir | declared |

## Group: `cl_intel_device_side_avc_motion_estimation.slice` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_AVC_ME_SLICE_TYPE_PRED_INTEL | cl_intel_device_side_avc_motion_estimation.slice | declared |
| CL_AVC_ME_SLICE_TYPE_BPRED_INTEL | cl_intel_device_side_avc_motion_estimation.slice | declared |
| CL_AVC_ME_SLICE_TYPE_INTRA_INTEL | cl_intel_device_side_avc_motion_estimation.slice | declared |

## Group: `cl_intel_device_side_avc_motion_estimation.subpixel` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_AVC_ME_SUBPIXEL_MODE_INTEGER_INTEL | cl_intel_device_side_avc_motion_estimation.subpixel | declared |
| CL_AVC_ME_SUBPIXEL_MODE_HPEL_INTEL | cl_intel_device_side_avc_motion_estimation.subpixel | declared |
| CL_AVC_ME_SUBPIXEL_MODE_QPEL_INTEL | cl_intel_device_side_avc_motion_estimation.subpixel | declared |

## Group: `cl_intel_device_side_avc_motion_estimation.version` (2 single-members)

| token | container | confidence |
|---|---|---|
| CL_AVC_ME_VERSION_0_INTEL | cl_intel_device_side_avc_motion_estimation.version | declared |
| CL_AVC_ME_VERSION_1_INTEL | cl_intel_device_side_avc_motion_estimation.version | declared |

## Group: `cl_intel_device_side_avc_motion_estimation.weight` (5 single-members)

| token | container | confidence |
|---|---|---|
| CL_AVC_ME_BIDIR_WEIGHT_QUARTER_INTEL | cl_intel_device_side_avc_motion_estimation.weight | declared |
| CL_AVC_ME_BIDIR_WEIGHT_THIRD_INTEL | cl_intel_device_side_avc_motion_estimation.weight | declared |
| CL_AVC_ME_BIDIR_WEIGHT_HALF_INTEL | cl_intel_device_side_avc_motion_estimation.weight | declared |
| CL_AVC_ME_BIDIR_WEIGHT_TWO_THIRD_INTEL | cl_intel_device_side_avc_motion_estimation.weight | declared |
| CL_AVC_ME_BIDIR_WEIGHT_THREE_QUARTER_INTEL | cl_intel_device_side_avc_motion_estimation.weight | declared |

## Group: `cl_intel_device_side_avc_motion_estimation.window` (12 single-members)

| token | container | confidence |
|---|---|---|
| CL_AVC_ME_SEARCH_WINDOW_EXHAUSTIVE_INTEL | cl_intel_device_side_avc_motion_estimation.window | declared |
| CL_AVC_ME_SEARCH_WINDOW_SMALL_INTEL | cl_intel_device_side_avc_motion_estimation.window | declared |
| CL_AVC_ME_SEARCH_WINDOW_TINY_INTEL | cl_intel_device_side_avc_motion_estimation.window | declared |
| CL_AVC_ME_SEARCH_WINDOW_EXTRA_TINY_INTEL | cl_intel_device_side_avc_motion_estimation.window | declared |
| CL_AVC_ME_SEARCH_WINDOW_DIAMOND_INTEL | cl_intel_device_side_avc_motion_estimation.window | declared |
| CL_AVC_ME_SEARCH_WINDOW_LARGE_DIAMOND_INTEL | cl_intel_device_side_avc_motion_estimation.window | declared |
| CL_AVC_ME_SEARCH_WINDOW_RESERVED0_INTEL | cl_intel_device_side_avc_motion_estimation.window | declared |
| CL_AVC_ME_SEARCH_WINDOW_RESERVED1_INTEL | cl_intel_device_side_avc_motion_estimation.window | declared |
| CL_AVC_ME_SEARCH_WINDOW_CUSTOM_INTEL | cl_intel_device_side_avc_motion_estimation.window | declared |
| CL_AVC_ME_SEARCH_WINDOW_16x12_RADIUS_INTEL | cl_intel_device_side_avc_motion_estimation.window | declared |
| CL_AVC_ME_SEARCH_WINDOW_4x4_RADIUS_INTEL | cl_intel_device_side_avc_motion_estimation.window | declared |
| CL_AVC_ME_SEARCH_WINDOW_2x2_RADIUS_INTEL | cl_intel_device_side_avc_motion_estimation.window | declared |

## Group: `cl_kernel_arg_type_qualifier` (5 single-members)

| token | container | confidence |
|---|---|---|
| CL_KERNEL_ARG_TYPE_NONE | cl_kernel_arg_type_qualifier | high |
| CL_KERNEL_ARG_TYPE_CONST | cl_kernel_arg_type_qualifier | high |
| CL_KERNEL_ARG_TYPE_RESTRICT | cl_kernel_arg_type_qualifier | high |
| CL_KERNEL_ARG_TYPE_VOLATILE | cl_kernel_arg_type_qualifier | high |
| CL_KERNEL_ARG_TYPE_PIPE | cl_kernel_arg_type_qualifier | declared |

## Group: `cl_khronos_vendor_id` (2 single-members)

| token | container | confidence |
|---|---|---|
| CL_KHRONOS_VENDOR_ID_CODEPLAY | cl_khronos_vendor_id | declared |
| CL_KHRONOS_VENDOR_ID_POCL | cl_khronos_vendor_id | declared |

## Group: `cl_map_flags` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_MAP_READ | cl_map_flags | declared |
| CL_MAP_WRITE | cl_map_flags | declared |
| CL_MAP_WRITE_INVALIDATE_REGION | cl_map_flags | declared |

## Group: `cl_mem_alloc_flags_img` (6 single-members)

| token | container | confidence |
|---|---|---|
| CL_MEM_ALLOC_RELAX_REQUIREMENTS_IMG | cl_mem_alloc_flags_img | declared |
| CL_MEM_ALLOC_GPU_WRITE_COMBINE_IMG | cl_mem_alloc_flags_img | declared |
| CL_MEM_ALLOC_GPU_CACHED_IMG | cl_mem_alloc_flags_img | declared |
| CL_MEM_ALLOC_CPU_LOCAL_IMG | cl_mem_alloc_flags_img | declared |
| CL_MEM_ALLOC_GPU_LOCAL_IMG | cl_mem_alloc_flags_img | declared |
| CL_MEM_ALLOC_GPU_PRIVATE_IMG | cl_mem_alloc_flags_img | declared |

## Group: `cl_mem_alloc_flags_intel` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_MEM_ALLOC_WRITE_COMBINED_INTEL | cl_mem_alloc_flags_intel | declared |
| CL_MEM_ALLOC_INITIAL_PLACEMENT_DEVICE_INTEL | cl_mem_alloc_flags_intel | declared |
| CL_MEM_ALLOC_INITIAL_PLACEMENT_HOST_INTEL | cl_mem_alloc_flags_intel | declared |

## Group: `cl_mem_flags` (30 single-members)

| token | container | confidence |
|---|---|---|
| CL_MEM_READ_WRITE | cl_mem_flags | declared |
| CL_MEM_WRITE_ONLY | cl_mem_flags | declared |
| CL_MEM_READ_ONLY | cl_mem_flags | declared |
| CL_MEM_USE_HOST_PTR | cl_mem_flags | declared |
| CL_MEM_ALLOC_HOST_PTR | cl_mem_flags | declared |
| CL_MEM_COPY_HOST_PTR | cl_mem_flags | declared |
| CL_MEM_IMMUTABLE_EXT | cl_mem_flags | declared |
| CL_MEM_HOST_WRITE_ONLY | cl_mem_flags | declared |
| CL_MEM_HOST_READ_ONLY | cl_mem_flags | declared |
| CL_MEM_HOST_NO_ACCESS | cl_mem_flags | declared |
| CL_MEM_SVM_FINE_GRAIN_BUFFER | cl_mem_flags | declared |
| CL_MEM_KERNEL_READ_AND_WRITE | cl_mem_flags | declared |
| CL_MEM_FORCE_HOST_MEMORY_INTEL | cl_mem_flags | declared |
| CL_MEM_RESERVED21_INTEL | cl_mem_flags | declared |
| CL_MEM_RESERVED22_INTEL | cl_mem_flags | declared |
| CL_MEM_NO_ACCESS_INTEL | cl_mem_flags | declared |
| CL_MEM_ACCESS_FLAGS_UNRESTRICTED_INTEL | cl_mem_flags | declared |
| CL_MEM_USE_UNCACHED_CPU_MEMORY_IMG | cl_mem_flags | declared |
| CL_MEM_USE_CACHED_CPU_MEMORY_IMG | cl_mem_flags | declared |
| CL_MEM_USE_GRALLOC_PTR_IMG | cl_mem_flags | declared |
| CL_MEM_EXT_HOST_PTR_QCOM | cl_mem_flags | declared |
| CL_MEM_RESERVED0_ARM | cl_mem_flags | declared |
| CL_MEM_RESERVED1_ARM | cl_mem_flags | declared |
| CL_MEM_RESERVED2_ARM | cl_mem_flags | declared |
| CL_MEM_RESERVED3_ARM | cl_mem_flags | declared |
| CL_MEM_PROTECTED_ALLOC_ARM | cl_mem_flags | declared |
| CL_MEM_RESERVED0_QCOM | cl_mem_flags | declared |
| CL_MEM_RESERVED1_QCOM | cl_mem_flags | declared |
| CL_MEM_RESERVED2_QCOM | cl_mem_flags | declared |
| CL_MEM_RESERVED3_QCOM | cl_mem_flags | declared |

## Group: `cl_mem_migration_flags` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_MIGRATE_MEM_OBJECT_HOST | cl_mem_migration_flags | declared |
| CL_MIGRATE_MEM_OBJECT_HOST_EXT | cl_mem_migration_flags | declared |
| CL_MIGRATE_MEM_OBJECT_CONTENT_UNDEFINED | cl_mem_migration_flags | declared |

## Group: `cl_mipmap_filter_mode_img` (2 single-members)

| token | container | confidence |
|---|---|---|
| CL_MIPMAP_FILTER_ANY_IMG | cl_mipmap_filter_mode_img | declared |
| CL_MIPMAP_FILTER_BOX_IMG | cl_mipmap_filter_mode_img | declared |

## Group: `cl_motion_estimation_desc_intel.mb_block_type` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_ME_MB_TYPE_16x16_INTEL | cl_motion_estimation_desc_intel.mb_block_type | declared |
| CL_ME_MB_TYPE_8x8_INTEL | cl_motion_estimation_desc_intel.mb_block_type | declared |
| CL_ME_MB_TYPE_4x4_INTEL | cl_motion_estimation_desc_intel.mb_block_type | declared |

## Group: `cl_motion_estimation_desc_intel.sad_adjust_mode` (2 single-members)

| token | container | confidence |
|---|---|---|
| CL_ME_SAD_ADJUST_MODE_NONE_INTEL | cl_motion_estimation_desc_intel.sad_adjust_mode | declared |
| CL_ME_SAD_ADJUST_MODE_HAAR_INTEL | cl_motion_estimation_desc_intel.sad_adjust_mode | declared |

## Group: `cl_motion_estimation_desc_intel.search_path_type` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_ME_SEARCH_PATH_RADIUS_2_2_INTEL | cl_motion_estimation_desc_intel.search_path_type | declared |
| CL_ME_SEARCH_PATH_RADIUS_4_4_INTEL | cl_motion_estimation_desc_intel.search_path_type | declared |
| CL_ME_SEARCH_PATH_RADIUS_16_12_INTEL | cl_motion_estimation_desc_intel.search_path_type | declared |

## Group: `cl_motion_estimation_desc_intel.subpixel_mode` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_ME_SUBPIXEL_MODE_INTEGER_INTEL | cl_motion_estimation_desc_intel.subpixel_mode | declared |
| CL_ME_SUBPIXEL_MODE_HPEL_INTEL | cl_motion_estimation_desc_intel.subpixel_mode | declared |
| CL_ME_SUBPIXEL_MODE_QPEL_INTEL | cl_motion_estimation_desc_intel.subpixel_mode | declared |

## Group: `cl_mutable_dispatch_asserts_khr` (1 single-members)

| token | container | confidence |
|---|---|---|
| CL_MUTABLE_DISPATCH_ASSERT_NO_ADDITIONAL_WORK_GROUPS_KHR | cl_mutable_dispatch_asserts_khr | high |

## Group: `cl_mutable_dispatch_fields_khr` (5 single-members)

| token | container | confidence |
|---|---|---|
| CL_MUTABLE_DISPATCH_GLOBAL_OFFSET_KHR | cl_mutable_dispatch_fields_khr | high |
| CL_MUTABLE_DISPATCH_GLOBAL_SIZE_KHR | cl_mutable_dispatch_fields_khr | high |
| CL_MUTABLE_DISPATCH_LOCAL_SIZE_KHR | cl_mutable_dispatch_fields_khr | high |
| CL_MUTABLE_DISPATCH_ARGUMENTS_KHR | cl_mutable_dispatch_fields_khr | high |
| CL_MUTABLE_DISPATCH_EXEC_INFO_KHR | cl_mutable_dispatch_fields_khr | high |

## Group: `cl_platform_command_buffer_capabilities_khr` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_COMMAND_BUFFER_PLATFORM_UNIVERSAL_SYNC_KHR | cl_platform_command_buffer_capabilities_khr | high |
| CL_COMMAND_BUFFER_PLATFORM_REMAP_QUEUES_KHR | cl_platform_command_buffer_capabilities_khr | high |
| CL_COMMAND_BUFFER_PLATFORM_AUTOMATIC_REMAP_KHR | cl_platform_command_buffer_capabilities_khr | high |

## Group: `cl_platform_info` (14 single-members)

| token | container | confidence |
|---|---|---|
| CL_PLATFORM_PROFILE | cl_platform_info | declared |
| CL_PLATFORM_VERSION | cl_platform_info | declared |
| CL_PLATFORM_NAME | cl_platform_info | declared |
| CL_PLATFORM_VENDOR | cl_platform_info | declared |
| CL_PLATFORM_EXTENSIONS | cl_platform_info | declared |
| CL_PLATFORM_HOST_TIMER_RESOLUTION | cl_platform_info | declared |
| CL_PLATFORM_NUMERIC_VERSION_KHR | cl_platform_info | declared |
| CL_PLATFORM_NUMERIC_VERSION | cl_platform_info | declared |
| CL_PLATFORM_EXTENSIONS_WITH_VERSION_KHR | cl_platform_info | declared |
| CL_PLATFORM_EXTENSIONS_WITH_VERSION | cl_platform_info | declared |
| CL_PLATFORM_COMMAND_BUFFER_CAPABILITIES_KHR | cl_platform_info | declared |
| CL_PLATFORM_SVM_TYPE_CAPABILITIES_KHR | cl_platform_info | declared |
| CL_PLATFORM_ICD_SUFFIX_KHR | cl_platform_info | declared |
| CL_PLATFORM_UNLOADABLE_KHR | cl_platform_info | declared |

## Group: `cl_program_binary_type` (4 single-members)

| token | container | confidence |
|---|---|---|
| CL_PROGRAM_BINARY_TYPE_NONE | cl_program_binary_type | declared |
| CL_PROGRAM_BINARY_TYPE_COMPILED_OBJECT | cl_program_binary_type | high |
| CL_PROGRAM_BINARY_TYPE_LIBRARY | cl_program_binary_type | high |
| CL_PROGRAM_BINARY_TYPE_EXECUTABLE | cl_program_binary_type | high |

## Group: `cl_queue_priority_khr` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_QUEUE_PRIORITY_HIGH_KHR | cl_queue_priority_khr | declared |
| CL_QUEUE_PRIORITY_MED_KHR | cl_queue_priority_khr | declared |
| CL_QUEUE_PRIORITY_LOW_KHR | cl_queue_priority_khr | declared |

## Group: `cl_queue_throttle_khr` (3 single-members)

| token | container | confidence |
|---|---|---|
| CL_QUEUE_THROTTLE_HIGH_KHR | cl_queue_throttle_khr | declared |
| CL_QUEUE_THROTTLE_MED_KHR | cl_queue_throttle_khr | declared |
| CL_QUEUE_THROTTLE_LOW_KHR | cl_queue_throttle_khr | declared |

## Group: `cl_semaphore_type_khr` (2 single-members)

| token | container | confidence |
|---|---|---|
| CL_SEMAPHORE_TYPE_BINARY_KHR | cl_semaphore_type_khr | declared |
| CL_SEMAPHORE_TYPE_KHR | enums.2000 | high |

## Group: `cl_svm_alloc_access_flags_khr` (4 single-members)

| token | container | confidence |
|---|---|---|
| CL_SVM_ALLOC_ACCESS_HOST_NOREAD_KHR | cl_svm_alloc_access_flags_khr | declared |
| CL_SVM_ALLOC_ACCESS_HOST_NOWRITE_KHR | cl_svm_alloc_access_flags_khr | declared |
| CL_SVM_ALLOC_ACCESS_DEVICE_NOREAD_KHR | cl_svm_alloc_access_flags_khr | declared |
| CL_SVM_ALLOC_ACCESS_DEVICE_NOWRITE_KHR | cl_svm_alloc_access_flags_khr | declared |

## Group: `cl_svm_capabilities_khr` (15 single-members)

| token | container | confidence |
|---|---|---|
| CL_SVM_CAPABILITY_SINGLE_ADDRESS_SPACE_KHR | cl_svm_capabilities_khr | declared |
| CL_SVM_CAPABILITY_SYSTEM_ALLOCATED_KHR | cl_svm_capabilities_khr | declared |
| CL_SVM_CAPABILITY_DEVICE_OWNED_KHR | cl_svm_capabilities_khr | declared |
| CL_SVM_CAPABILITY_DEVICE_UNASSOCIATED_KHR | cl_svm_capabilities_khr | declared |
| CL_SVM_CAPABILITY_CONTEXT_ACCESS_KHR | cl_svm_capabilities_khr | declared |
| CL_SVM_CAPABILITY_HOST_OWNED_KHR | cl_svm_capabilities_khr | declared |
| CL_SVM_CAPABILITY_HOST_READ_KHR | cl_svm_capabilities_khr | declared |
| CL_SVM_CAPABILITY_HOST_WRITE_KHR | cl_svm_capabilities_khr | declared |
| CL_SVM_CAPABILITY_HOST_MAP_KHR | cl_svm_capabilities_khr | declared |
| CL_SVM_CAPABILITY_DEVICE_READ_KHR | cl_svm_capabilities_khr | declared |
| CL_SVM_CAPABILITY_DEVICE_WRITE_KHR | cl_svm_capabilities_khr | declared |
| CL_SVM_CAPABILITY_DEVICE_ATOMIC_ACCESS_KHR | cl_svm_capabilities_khr | declared |
| CL_SVM_CAPABILITY_CONCURRENT_ACCESS_KHR | cl_svm_capabilities_khr | declared |
| CL_SVM_CAPABILITY_CONCURRENT_ATOMIC_ACCESS_KHR | cl_svm_capabilities_khr | declared |
| CL_SVM_CAPABILITY_INDIRECT_ACCESS_KHR | cl_svm_capabilities_khr | declared |
