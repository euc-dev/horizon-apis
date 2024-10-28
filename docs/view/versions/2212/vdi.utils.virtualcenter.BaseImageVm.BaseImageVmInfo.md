---
layout: page
title: Data Object - BaseImageVmInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.BaseImageVm.BaseImageVmInfo`

Returned by
> [BaseImageVm_Get](vdi.utils.virtualcenter.BaseImageVm.md#get), [BaseImageVm_List](vdi.utils.virtualcenter.BaseImageVm.md#list), [BaseImageVm_ListByDatacenter](vdi.utils.virtualcenter.BaseImageVm.md#listByDatacenter)

See also
> [BaseImageVmId](vdi.entity.BaseImageVmId.md), [BaseImageVmIncompatibleReasons](vdi.utils.virtualcenter.BaseImageVm.BaseImageVmIncompatibleReasons.md), [DatacenterId](vdi.entity.DatacenterId.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon View 6.0


## Data Object Description

VMInfo is a set of VM attributes for parent VMs retrieved from the VC.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [BaseImageVmId](vdi.entity.BaseImageVmId.md)|  VM id [^2]
**name**|  xsd:string|  VM name [^2]
**path**|  xsd:string|  VM path [^2]
**operatingSystem**|  xsd:string|  Operating system enumeration as known to View. [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"Unknown"</td><td></td></tr><tr><td>"Windows XP"</td><td>Windows XP</td></tr><tr><td>"Windows Vista"</td><td>Windows Vista</td></tr><tr><td>"Windows 7"</td><td>Windows 7</td></tr><tr><td>"Windows 8"</td><td>Windows 8</td></tr><tr><td>"Windows 10"</td><td>Windows 10</td></tr><tr><td>"Windows 11"</td><td>Windows 11</td></tr><tr><td>"Windows Server 2003"</td><td>Windows Server 2003</td></tr><tr><td>"Windows Server 2008"</td><td>Windows Server 2008</td></tr><tr><td>"Windows Server 2008R2"</td><td>Windows Server 2008R2</td></tr><tr><td>"Windows Server 2012"</td><td>Windows Server 2012</td></tr><tr><td>"Windows Server 2012R2"</td><td>Windows Server 2012R2</td></tr><tr><td>"Windows Server 10"</td><td>null</td></tr><tr><td>"Windows Server 2016"</td><td>null</td></tr><tr><td>"Windows Server 2016 or above"</td><td>Windows Server 2016 or above</td></tr><tr><td>"Linux (other)"</td><td>Linux (other)</td></tr><tr><td>"Linux Server (other)"</td><td>Linux server (other)</td></tr><tr><td>"Linux (Ubuntu)"</td><td>Linux (Ubuntu)</td></tr><tr><td>"Linux (Red Hat Enterprise Linux)"</td><td>Linux (Red Hat Enterprise)</td></tr><tr><td>"Linux (SUSE Linux Enterprise Server)"</td><td>Linux (Suse)</td></tr><tr><td>"Linux (CentOS)"</td><td>Linux (CentOS)</td></tr></table>
**operatingSystemDisplayName**|  xsd:string|  Operating system display name from Virtual Center. [^1] [^2]
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  VirtualCenter id for this VM [^2]
**datacenter**| [DatacenterId](vdi.entity.DatacenterId.md)|  Datacenter id for this VM [^1] [^2]
**incompatibleReasons**| [BaseImageVmIncompatibleReasons](vdi.utils.virtualcenter.BaseImageVm.BaseImageVmIncompatibleReasons.md)|  Reasons that may preclude this BaseImageVm from having its snapshots used in linked clone desktop or farm creation. [^2]
**networkType**|  xsd:string|  Type of network base image vm belongs to.  **_Since_** Horizon 7.9 [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"Network"</td><td>Standard network</td></tr><tr><td>"OpaqueNetwork"</td><td>Opaque network</td></tr><tr><td>"DistributedVirtualPortgroup"</td><td>DVS port group</td></tr></table>
**refId**|  xsd:string|  Reference ID used for this base image VM.  **_Since_** Horizon 8.1 [^1] [^2]
**numNics**|  xsd:int|  Number of network interface cards in this base image VM.  **_Since_** Horizon 8.8 [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.