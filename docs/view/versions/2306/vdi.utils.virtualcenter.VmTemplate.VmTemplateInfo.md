---
layout: page
title: Data Object - VmTemplateInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.VmTemplate.VmTemplateInfo`

Returned by
> [VmTemplate_List](vdi.utils.virtualcenter.VmTemplate.md#list), [VmTemplate_ListByDatacenter](vdi.utils.virtualcenter.VmTemplate.md#listByDatacenter)

See also
> [DatacenterId](vdi.entity.DatacenterId.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md), [VmTemplateId](vdi.entity.VmTemplateId.md), [VmTemplateIncompatibleReasons](vdi.utils.virtualcenter.VmTemplate.VmTemplateIncompatibleReasons.md)

Since
> Horizon View 6.0


## Data Object Description

VMTemplateInfo is a set of template attributes retrieved from the VC.
 [^167]



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [VmTemplateId](vdi.entity.VmTemplateId.md)|  VM template Id [^2]
**name**|  xsd:string|  VM template name [^2]
**path**|  xsd:string|  VM template path [^2]
**operatingSystem**|  xsd:string|  Operating system enumeration as known to View. [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"Unknown"</td><td></td></tr><tr><td>"Windows XP"</td><td>Windows XP</td></tr><tr><td>"Windows Vista"</td><td>Windows Vista</td></tr><tr><td>"Windows 7"</td><td>Windows 7</td></tr><tr><td>"Windows 8"</td><td>Windows 8</td></tr><tr><td>"Windows 10"</td><td>Windows 10</td></tr><tr><td>"Windows 11"</td><td>Windows 11</td></tr><tr><td>"Windows Server 2003"</td><td>Windows Server 2003</td></tr><tr><td>"Windows Server 2008"</td><td>Windows Server 2008</td></tr><tr><td>"Windows Server 2008R2"</td><td>Windows Server 2008R2</td></tr><tr><td>"Windows Server 2012"</td><td>Windows Server 2012</td></tr><tr><td>"Windows Server 2012R2"</td><td>Windows Server 2012R2</td></tr><tr><td>"Windows Server 10"</td><td>null</td></tr><tr><td>"Windows Server 2016"</td><td>null</td></tr><tr><td>"Windows Server 2016 or above"</td><td>Windows Server 2016 or above</td></tr><tr><td>"Linux (other)"</td><td>Linux (other)</td></tr><tr><td>"Linux Server (other)"</td><td>Linux server (other)</td></tr><tr><td>"Linux (Ubuntu)"</td><td>Linux (Ubuntu)</td></tr><tr><td>"Linux (Red Hat Enterprise Linux)"</td><td>Linux (Red Hat Enterprise)</td></tr><tr><td>"Linux (SUSE Linux Enterprise Server)"</td><td>Linux (Suse)</td></tr><tr><td>"Linux (CentOS)"</td><td>Linux (CentOS)</td></tr></table>
**operatingSystemDisplayName**|  xsd:string|  Operating system display name from Virtual Center. [^1] [^2]
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  VirtualCenter id for this template [^2]
**datacenter**| [DatacenterId](vdi.entity.DatacenterId.md)|  Datacenter id for this template [^1] [^2]
**hardwareVersion**|  xsd:int|  Template hardware version. [^1] [^2]
**vGPUType**|  xsd:string|  NVIDIA GRID vGPU type configured on this template, if any.  **_Since_** Horizon View 6.1 [^1] [^2]
**incompatibleReasons**| [VmTemplateIncompatibleReasons](vdi.utils.virtualcenter.VmTemplate.VmTemplateIncompatibleReasons.md)|  Reasons that may preclude this VmTemplate from being used in full clone desktop creation. [^2]
**memoryMB**|  xsd:int|  Memory size of the template, in MB.  **_Since_** Horizon 7.4 [^1] [^2]
**diskSizeInBytes**|  xsd:long|  Sum of capacities of all the virtual disks in the template, in bytes.  **_Since_** Horizon 7.4 [^1] [^2]
**refId**|  xsd:string|  Reference ID used for this vm template.  **_Since_** Horizon 8.1 [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.