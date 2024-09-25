---
layout: page
title: Data Object - PersistentDiskIncompatibleReasons
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.PersistentDisk.PersistentDiskIncompatibleReasons
Returned by
     [PersistentDisk_PreviewRecreateMachines](vdi.resources.PersistentDisk.md#previewRecreateMachines)
See also
     [PersistentDiskId](vdi.entity.PersistentDiskId.md)
Since 
    Horizon 7.8

## Data Object Description 

**Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

List all incompatible reasons for persistent disk 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [PersistentDiskId](vdi.entity.PersistentDiskId.md)|  The ID of the persistent disk.   
  
**compatible**|  xsd:boolean|  True if the machine can be recreated with PersistentDisk. If the value is false, incompatible reasons are available at [incompatibleReasons](vdi.resources.PersistentDisk.PersistentDiskIncompatibleReasons.md#incompatibleReasons)   


[^2]

  
**incompatibleReasons**|  xsd:string[]|  Incompatible reasons for recreating machine with the persistent disk.   


[^1]
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"MAX_POOL_SIZE_VIOLATION"| Desktop Pool has reached maximum pool size.  
Type: Error - Machine can not be recreated with this incompatibility  
"NON_VSPHERE_DESKTOP"| vSphere mode of Disk is not compatible with Desktop pool.  
Type: Error - Machine can not be recreated with this incompatibility  
"DISK_WITH_INCOMPATIBLE_DATASTORES"| Data disk and pool should both either be on VSAN datastores or Non-VSAN datastores.  
Type: Error - Machine can not be recreated with this incompatibility  
"DUPLICATE_DISKS"| Two or more of the selected persistent disks are associated with the same desktop pool and user.  
Type: Error - Machine can not be recreated with this incompatibility  
"MACHINE_NAME_EXISTS_IN_DESKTOP"| Machine name exists in desktop.  
Type: Warning - Machine can still be recreated with this incompatibility  
"DISK_USER_NOT_ENTITLED_TO_DESKTOP"| Assigned user to the disk is not entitled to the Desktop Pool.  
Type: Warning - Machine can still be recreated with this incompatibility  
"DISK_USER_ASSIGNED_TO_EXISTING_MACHINE"| Assigned user of the disk is having an Assignment on a machine of the same desktop pool.  
Type: Error - Machine can not be recreated with this incompatibility  
"DESKTOP_SEMI_AUTO_POOL"| Desktop created with specified naming method. Type: Warning - Machine can still be recreated with this incompatibility.  

  
  

  

