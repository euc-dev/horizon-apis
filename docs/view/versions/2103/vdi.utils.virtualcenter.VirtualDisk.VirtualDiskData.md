---
layout: page
title: Data Object - VirtualDiskData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.VirtualDisk.VirtualDiskData`

Property of
> [VirtualDiskInfo](vdi.utils.virtualcenter.VirtualDisk.VirtualDiskInfo.md#field_detail)

See also
> [DatastoreId](vdi.entity.DatastoreId.md)

Since
> Horizon View 6.0


## Data Object Description

VirtualDiskData is a set of VirtualDisk attributes retrieved from the VC.
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**name**|  xsd:string|  Name of VirtualDisk [^2]
**path**|  xsd:string|  Full path of VirtualDisk [^2]
**datastore**| [DatastoreId](vdi.entity.DatastoreId.md)|  Datastore entityId that the VirtualDisk belongs to [^2]
**attached**|  xsd:boolean|  Indicates if the VirtualDisk is attached to a linked-clone VM. [^2]
**compatible**|  xsd:boolean|  Set true if disk is compatible for persistent disk else set to false  **_Since_** Horizon 7.8 [^2]
**incompatibleReason**|  xsd:string|  Incompatible reason for the persistent disk  **_Since_** Horizon 7.8 [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"REPLICA_DISK"</td><td>Replica Disks are not compatible to be used as Persistent disk</td></tr><tr><td>"INTERNAL_DISK"</td><td>Internal disk are not compatible to be used as Persistent disk</td></tr><tr><td>"DISPOSABLE_DISK"</td><td>Disposable disk are not compatible to be used as Persistent disk</td></tr><tr><td>"DISK_ALREADY_IN_USE"</td><td>Disk already imported as persistent disk</td></tr><tr><td>"INSTANT_CLONE_INTERNAL_DISK"</td><td>Instant clone internal disk is not compatible to be a Persistent disk</td></tr></table>


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.