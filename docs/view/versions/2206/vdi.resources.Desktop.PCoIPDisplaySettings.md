---
layout: page
title: Data Object - DesktopPCoIPDisplaySettings
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.PCoIPDisplaySettings`

Property of
> [DesktopDisplayProtocolSettings](vdi.resources.Desktop.DisplayProtocolSettings.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

PCoIP or BLAST protocol settings.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**renderer3D**|  xsd:string|  3D rendering is supported on Windows 7 or later guests running on VMs with virtual hardware version 8 or later. The default protocol must be PCoIP and users must not be allowed to choose their own protocol to enable 3D rendering. For instant clone source desktop 3D rendering always mapped to MANAGE_BY_VSPHERE_CLIENT [^17] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>MANAGE_BY_VSPHERE_CLIENT</td><td>3D rendering managed by vSphere Client.</td></tr><tr><td>AUTOMATIC</td><td>3D rendering is automatic.</td></tr><tr><td>SOFTWARE</td><td>3D rendering is software dependent. The software renderer is supported (at minimum) on virtual hardware version 8 in a vSphere 5.0 environment.</td></tr><tr><td>HARDWARE</td><td>3D rendering is hardware dependent. The hardware-based renderer is supported (at minimum) on virtual hardware version 9 in a vSphere 5.1 environment.</td></tr><tr><td>DISABLED</td><td>3D rendering is disabled.</td></tr></table>
**enableGRIDvGPUs**|  xsd:boolean|  When 3D rendering is managed by the vSphere Client, this enables support for NVIDIA GRID vGPUs. This must be false if 3D rendering is not managed by the vSphere Client. If this is true, the host or cluster associated with the desktop must support NVIDIA GRID and vGPU types required by the desktop's VirtualMachines, VmTemplate, or BaseImageSnapshot. If this is false, the desktop's VirtualMachines, VmTemplate, or BaseImageSnapshot must not support NVIDIA GRID vGPUs. Since suspending VMs with passthrough devices such as vGPUs is not possible, [powerPolicy](vdi.resources.Desktop.LogoffSettings.md#powerPolicy) cannot be set to SUSPEND if this is enabled.  **_Since_** Horizon View 6.1 [^5] [^2]
**vGPUGridProfile**|  xsd:string|  NVIDIA GRID vGPUs might have multiple profiles and any one of the available profiles can be applied to newly created instant clone desktop. The profile specified in this field will be used in the newly created instant clone desktop.  **_Since_** Horizon 7.1 [^1] [^2]
**vRamSizeMB**|  xsd:int|  VRAM size for View managed 3D rendering. More VRAM can improve 3D performance. Size is in MB. On ESXi 5.0 hosts, the renderer allows a maximum VRAM size of 128MB. On ESXi 5.1 and later hosts, the maximum VRAM size is 512MB. For Instant Clones, this value is inherited from snapshot of Master VM. [^61] [^1] [^62] [^63] [^64]
**vRamSizeKB**|  xsd:long|  VRAM size in KB for Instant Clone desktops. This field is populated after reading VRAM size from snapshot of MasterVM in the backend. It is applicable only when 3D is disabled.  **_Since_** Horizon 7.2 [^1] [^2]
**maxNumberOfMonitors**|  xsd:int|  When 3D is disabled, the 'Max number of monitors' and 'Max resolution of any one monitor' settings determine the amount of vRAM assigned to machines in this desktop. The greater these values are, the more memory will be consumed on the associated ESX hosts. Existing virtual machines must be powered off and subsequently powered on for the change to take effect. A restart will not cause the changes to take effect. If 3D is enabled and managed by View, the maximum number of monitors must be 1 or 2. For Instant Clones, this value is inherited from snapshot of Master VM. [^65] [^1] [^8] [^66] [^69]
**maxResolutionOfAnyOneMonitor**|  xsd:string|  If 3D rendering is enabled and managed by View, this must be set to the default value. When 3D rendering is disabled, the 'Max number of monitors' and 'Max resolution of any one monitor' settings determine the amount of vRAM assigned to machines in this desktop. The greater these values are, the more memory will be consumed on the associated ESX hosts. This setting is only relevant on managed machines. Existing virtual machines must be powered off and subsequently powered on for the change to take effect. A restart will not cause the changes to take effect. For Instant Clones, this value is inherited from snapshot of Master VM [^68] [^1] [^69] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>WUXGA</td><td>1920x1200</td></tr><tr><td>WSXGA_PLUS</td><td>1680x1050</td></tr><tr><td>WQXGA</td><td>2560x1600</td></tr><tr><td>UHD</td><td>3840x2160</td></tr><tr><td>UHD_5K</td><td>5120x2880</td></tr><tr><td>UHD_8K</td><td>7680x4320</td></tr></table>


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^5]: This property has a default value of false.
[^8]: This property has a minimum value of 1.
[^17]: This property has a default value of 'DISABLED'.
[^61]: This property has a default value of 96.
[^62]: This property has a minimum value of 64.
[^63]: This property has a maximum value of 512.
[^64]: This property is required if renderer3D is set to 'AUTOMATIC', 'SOFTWARE', or 'HARDWARE'.
[^65]: This property has a default value of 2.
[^66]: This property has a maximum value of 4.
[^68]: This property has a default value of 'WUXGA'.
[^69]: This property is required if renderer3D is set to 'AUTOMATIC', 'SOFTWARE', 'HARDWARE', or 'DISABLED'.