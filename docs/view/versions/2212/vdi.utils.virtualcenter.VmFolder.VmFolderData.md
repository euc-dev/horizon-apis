---
layout: page
title: Data Object - VmFolderData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.VmFolder.VmFolderData`

Property of
> [VmFolderInfo](vdi.utils.virtualcenter.VmFolder.VmFolderInfo.md#field_detail)

See also
> [DatacenterId](vdi.entity.DatacenterId.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md), [VmFolderIncompatibleReasons](vdi.utils.virtualcenter.VmFolder.VmFolderIncompatibleReasons.md)

Since
> Horizon View 6.0


## Data Object Description

VmFolderData is a set of attributes for a folder retrieved from the VC.
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**name**|  xsd:string|  VM folder display name [^2]
**path**|  xsd:string|  VM folder path [^2]
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  VirtualCenter id for this VM folder. [^2]
**datacenter**| [DatacenterId](vdi.entity.DatacenterId.md)|  Datacenter id for this VM folder. [^1] [^2]
**type**|  xsd:string|  The type of this VM folder node. Some types may not be suitable for desktop creation. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"DATACENTER"</td><td>A datacenter that serves as a folder suitable for use in desktop creation.</td></tr><tr><td>"FOLDER"</td><td>A regular folder suitable for use in desktop creation.</td></tr><tr><td>"OTHER"</td><td>Some other resource type that cannot be used in desktop creation.</td></tr></table>
**incompatibleReasons**| [VmFolderIncompatibleReasons](vdi.utils.virtualcenter.VmFolder.VmFolderIncompatibleReasons.md)|  Reasons that may preclude this VM folder from being used in desktop creation. [^2]


 
