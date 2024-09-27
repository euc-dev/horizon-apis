---
layout: page
title: Data Object - DesktopPCoIPDisplaySettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.PCoIPDisplaySettings  
Property of
     [DesktopDisplayProtocolSettings](vdi.resources.Desktop.DisplayProtocolSettings.md#field_detail)  
Since 
    Horizon View 6.0

## Data Object Description 

PCoIP or BLAST protocol settings. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**renderer3D**|  xsd:string|  3D rendering is supported on Windows 7 or later guests running on VMs with virtual hardware version 8 or later. The default protocol must be PCoIP and users must not be allowed to choose their own protocol to enable 3D rendering. For instant clone source desktop 3D rendering always mapped to MANAGE_BY_VSPHERE_CLIENT   


  * This property has a default value of "DISABLED".
  * This property will be one of:  
|  Value |  Description   
---|---  
"MANAGE_BY_VSPHERE_CLIENT"| 3D rendering managed by vSphere Client.  
"AUTOMATIC"| 3D rendering is automatic.  
"SOFTWARE"| 3D rendering is software dependent. The software renderer is supported (at minimum) on virtual hardware version 8 in a vSphere 5.0 environment.  
"HARDWARE"| 3D rendering is hardware dependent. The hardware-based renderer is supported (at minimum) on virtual hardware version 9 in a vSphere 5.1 environment.  
"DISABLED"| 3D rendering is disabled.  

  
**enableGRIDvGPUs**|  xsd:boolean|  When 3D rendering is managed by the vSphere Client, this enables support for NVIDIA GRID vGPUs. This must be false if 3D rendering is not managed by the vSphere Client. If this is true, the host or cluster associated with the desktop must support NVIDIA GRID and vGPU types required by the desktop's VirtualMachines, VmTemplate, or BaseImageSnapshot. If this is false, the desktop's VirtualMachines, VmTemplate, or BaseImageSnapshot must not support NVIDIA GRID vGPUs. Since suspending VMs with passthrough devices such as vGPUs is not possible, [powerPolicy](vdi.resources.Desktop.LogoffSettings.md#powerPolicy) cannot be set to SUSPEND if this is enabled.  **_Since_** Horizon View 6.1  


  * This property has a default value of false.
 * This property cannot be updated.

  
**vGPUGridProfile**|  xsd:string|  NVIDIA GRID vGPUs might have multiple profiles and any one of the available profiles can be applied to newly created instant clone desktop. The profile specified in this field will be used in the newly created instant clone desktop.  **_Since_** Horizon 7.1  


 * This property need not be set.
 * This property cannot be updated.

  
**vRamSizeMB**|  xsd:int|  VRAM size for View managed 3D rendering. More VRAM can improve 3D performance. Size is in MB. On ESXi 5.0 hosts, the renderer allows a maximum VRAM size of 128MB. On ESXi 5.1 and later hosts, the maximum VRAM size is 512MB. For Instant Clones, this value is inherited from snapshot of Master VM.   


  * This property has a default value of 96.
 * This property need not be set.
  * This property has a minimum value of 64. 
  * This property has a maximum value of 512. 
  * This property is required if renderer3D is set to "AUTOMATIC", "SOFTWARE", or "HARDWARE".

  
**vRamSizeKB**|  xsd:long|  VRAM size in KB for Instant Clone desktops. This field is populated after reading VRAM size from snapshot of MasterVM in the backend. It is applicable only when 3D is disabled.  **_Since_** Horizon 7.2  


 * This property need not be set.
 * This property cannot be updated.

  
**maxNumberOfMonitors**|  xsd:int|  When 3D is disabled, the 'Max number of monitors' and 'Max resolution of any one monitor' settings determine the amount of vRAM assigned to machines in this desktop. The greater these values are, the more memory will be consumed on the associated ESX hosts. Existing virtual machines must be powered off and subsequently powered on for the change to take effect. A restart will not cause the changes to take effect. If 3D is enabled and managed by View, the maximum number of monitors must be 1 or 2. For Instant Clones, this value is inherited from snapshot of Master VM.   


  * This property has a default value of 2.
 * This property need not be set.
  * This property has a minimum value of 1. 
  * This property has a maximum value of 4. 
  * This property is required if renderer3D is set to "AUTOMATIC", "SOFTWARE", "HARDWARE", or "DISABLED".

  
**maxResolutionOfAnyOneMonitor**|  xsd:string|  If 3D rendering is enabled and managed by View, this must be set to the default value. When 3D rendering is disabled, the 'Max number of monitors' and 'Max resolution of any one monitor' settings determine the amount of vRAM assigned to machines in this desktop. The greater these values are, the more memory will be consumed on the associated ESX hosts. This setting is only relevant on managed machines. Existing virtual machines must be powered off and subsequently powered on for the change to take effect. A restart will not cause the changes to take effect. For Instant Clones, this value is inherited from snapshot of Master VM   


  * This property has a default value of "WUXGA".
 * This property need not be set.
  * This property is required if renderer3D is set to "AUTOMATIC", "SOFTWARE", "HARDWARE", or "DISABLED".
  * This property will be one of:  
|  Value |  Description   
---|---  
"WUXGA"| 1920x1200  
"WSXGA_PLUS"| 1680x1050  
"WQXGA"| 2560x1600  
"UHD"| 3840x2160  
"UHD_5K"| 5120x2880  
"UHD_8K"| 7680x4320  

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

