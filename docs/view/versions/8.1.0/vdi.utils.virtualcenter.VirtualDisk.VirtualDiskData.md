---
layout: page
title: Data Object - VirtualDiskData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.VirtualDisk.VirtualDiskData
Property of
     [VirtualDiskInfo](vdi.utils.virtualcenter.VirtualDisk.VirtualDiskInfo.md#field_detail)
See also
     [DatastoreId](vdi.entity.DatastoreId.md)
Since 
    Horizon View 6.0

## Data Object Description 

VirtualDiskData is a set of VirtualDisk attributes retrieved from the VC. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  Name of VirtualDisk   


[^2]

  
**path**|  xsd:string|  Full path of VirtualDisk   


[^2]

  
**datastore**| [DatastoreId](vdi.entity.DatastoreId.md)|  Datastore entityId that the VirtualDisk belongs to   


[^2]

  
**attached**|  xsd:boolean|  Indicates if the VirtualDisk is attached to a linked-clone VM.   


[^2]

  
**compatible**|  xsd:boolean|  Set true if disk is compatible for persistent disk else set to false  **_Since_** Horizon 7.8  


[^2]

  
**incompatibleReason**|  xsd:string|  Incompatible reason for the persistent disk  **_Since_** Horizon 7.8  


[^1]
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"REPLICA_DISK"| Replica Disks are not compatible to be used as Persistent disk  
"INTERNAL_DISK"| Internal disk are not compatible to be used as Persistent disk  
"DISPOSABLE_DISK"| Disposable disk are not compatible to be used as Persistent disk  
"DISK_ALREADY_IN_USE"| Disk already imported as persistent disk  
"INSTANT_CLONE_INTERNAL_DISK"| Instant clone internal disk is not compatible to be a Persistent disk  

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
