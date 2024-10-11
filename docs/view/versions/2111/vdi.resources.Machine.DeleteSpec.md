---
layout: page
title: Data Object - MachineDeleteSpec
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Machine.DeleteSpec`

Parameter to  
> [Machine_Delete](vdi.resources.Machine.md#delete), [Machine_DeleteMachines](vdi.resources.Machine.md#deleteMachines)

See also  
> [DatastorePathId](vdi.entity.DatastorePathId.md)

Since  
> Horizon View 6.0


## Data Object Description 

The specification for deleting a Machine. For managed VMs, [deleteFromDisk](vdi.resources.Machine.DeleteSpec.md#deleteFromDisk) must be set to true, in order to delete it from disk. For linked-clone VMs, there are three options: a. Delete from disk: set [deleteFromDisk](vdi.resources.Machine.DeleteSpec.md#deleteFromDisk) to true. b. Archive persistent disk in place: set [archivePersistentDisk](vdi.resources.Machine.DeleteSpec.md#archivePersistentDisk) to true, and [archiveDatastorePath](vdi.resources.Machine.DeleteSpec.md#archiveDatastorePath) to null. c. Archive persistent disk to a specific datastore path: set [archivePersistentDisk](vdi.resources.Machine.DeleteSpec.md#archivePersistentDisk) to true, and [archiveDatastorePath](vdi.resources.Machine.DeleteSpec.md#archiveDatastorePath) to non-null. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**deleteFromDisk**|  xsd:boolean|  Determines whether the Machine VM should be deleted from vCenter Server. This is only applicable for managed machines. This must always be true for machines in linked and instant clone desktops. This defaults to true for linked and instant clone machines and false for all other types.   
Note :- If this is true, then machine being deleted must not have any active user session, otherwise delete operation would fail.   


* This property need not be set.

  
**archivePersistentDisk**|  xsd:boolean|  Determines whether to detach the persistent user disk and save it for future use. This can only be specified for linked-clone desktops with [redirectWindowsProfile](vdi.resources.Desktop.PersistentDiskSettings.md#redirectWindowsProfile) enabled, in which case it defaults to true.   


* This property need not be set.

  
**archiveDatastorePath**| [DatastorePathId](vdi.entity.DatastorePathId.md)|  Determines the location where the persistent user disk will be saved for future use. If this is unset and [archivePersistentDisk](vdi.resources.Machine.DeleteSpec.md#archivePersistentDisk) is specified, the persistent disk is archived in place.   


* This property need not be set.

  
**allowDeleteFromMultiDesktops**|  xsd:boolean|  Determines whether the machines from different desktops can be deleted. This defaults to false in which case only machines belonging to single desktop pool can be deleted. If true, machines from different desktops can be deleted.  **_Since_** Horizon 7.5  


  * This property has a default value of false.
* This property need not be set.

  
**forceLogoffSession**|  xsd:boolean|  Determines whether active session on the machine to be logged off before deletion. This is only applicable for managed machines. If true, active session on the machine will be logged off before Machine delete. Otherwise,it will result in an exception.  **_Since_** Horizon 7.7  


  * This property has a default value of false.
* This property need not be set.

  
  
  
   
  
  
