---
layout: page
title: Data Object - PersistentDiskSpec
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.PersistentDisk.PersistentDiskSpec`

Parameter to  
> [PersistentDisk_Create](vdi.resources.PersistentDisk.md#create)

See also  
> [AccessGroupId](vdi.entity.AccessGroupId.md), [DesktopId](vdi.entity.DesktopId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md), [VirtualDiskId](vdi.entity.VirtualDiskId.md)

Since  
> Horizon View 6.0


## Data Object Description 

**Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

The specification for creating a persistent disk from a Virtual Center virtual disk. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**virtualDisk**| [VirtualDiskId](vdi.entity.VirtualDiskId.md)|  The ID of the virtual disk.   
  
**accessGroup**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  The access group for the newly imported virtual disk.   
  
**desktop**| [DesktopId](vdi.entity.DesktopId.md)|  The desktop to associate this persistent disk with.   


 * This property need not be set.

  
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  The user who owns the persistent disk.   


 * This property need not be set.

  
  

  
