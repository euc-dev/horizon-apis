---
layout: page
title: Service - PersistentDisk
hide:
 #- navigation
 - toc
---

  
| | | Local Methods  
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.PersistentDisk
See also
     [MachineId](vdi.entity.MachineId.md), [MapEntry](vdi.util.MapEntry.md), [PersistentDiskAttachSpec](vdi.resources.PersistentDisk.AttachSpec.md), [PersistentDiskDeleteSpec](vdi.resources.PersistentDisk.DeleteSpec.md), [PersistentDiskDetachSpec](vdi.resources.PersistentDisk.DetachSpec.md), [PersistentDiskId](vdi.entity.PersistentDiskId.md), [PersistentDiskIncompatibleReasons](vdi.resources.PersistentDisk.PersistentDiskIncompatibleReasons.md), [PersistentDiskInfo](vdi.resources.PersistentDisk.PersistentDiskInfo.md), [PersistentDiskRecreateMachineInfo](vdi.resources.PersistentDisk.PersistentDiskRecreateMachineInfo.md), [PersistentDiskRecreateMachineSpec](vdi.resources.PersistentDisk.RecreateMachineSpec.md), [PersistentDiskReplaceSpec](vdi.resources.PersistentDisk.ReplaceSpec.md), [PersistentDiskSpec](vdi.resources.PersistentDisk.PersistentDiskSpec.md)
Since 
    Horizon View 6.0

  


## Service Description

**Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Service for managing persistent disks. View Composer preserves the user information on the persistent disk when the OS data is updated, refreshed, or rebalanced. A View Composer persistent disk contains user settings and other user-generated data. 

Methods

Methods defined in this Service   
---  
PersistentDisk_Attach, PersistentDisk_Create, PersistentDisk_Delete, PersistentDisk_Detach, PersistentDisk_Get, PersistentDisk_PreviewRecreateMachines, PersistentDisk_RecreateMachine, PersistentDisk_RecreateMachines, PersistentDisk_Replace, PersistentDisk_Update  
  



**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Attaches the specified persistent disk to a machine. 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PersistentDisk](vdi.resources.PersistentDisk.md) used to make the method call.   
**id**| [PersistentDiskId](vdi.entity.PersistentDiskId.md)|  The ID of the persistent disk to attach.   
  
**spec**| [PersistentDiskAttachSpec](vdi.resources.PersistentDisk.AttachSpec.md)|  The specification of how to attach the disk.   
  
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_PERSISTENT_DISK_ATTACHED|  If the persistent disk attachment was successfully requested.   
VLSI_PERSISTENT_DISK_ATTACH_FAILED|  If the persistent disk attachment failed to be requested.   
  
Show WSDL type definition

  
  
  



**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Creates a persistent disk from a Virtual Center persistent disk. 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PersistentDisk](vdi.resources.PersistentDisk.md) used to make the method call.   
**spec**| [PersistentDiskSpec](vdi.resources.PersistentDisk.PersistentDiskSpec.md)|  The specification for creating the persistent disk.   
  
  


Return Value 

Type |  Description   
---|---  
[PersistentDiskId](vdi.entity.PersistentDiskId.md)| The ID of the newly created persistent disk.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_PERSISTENT_DISK_CREATED|  If the persistent disk was successfully created.   
VLSI_PERSISTENT_DISK_CREATE_FAILED|  If the persistent disk could not be created.   
  
Show WSDL type definition

  
  
  



**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Deletes the specified persistent disk. 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PersistentDisk](vdi.resources.PersistentDisk.md) used to make the method call.   
**id**| [PersistentDiskId](vdi.entity.PersistentDiskId.md)|  The ID of the persistent disk to delete.   
  
**spec**| [PersistentDiskDeleteSpec](vdi.resources.PersistentDisk.DeleteSpec.md)|  The specification for deleting the persistent disk.   


  * This parameter need not be set.

  
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_PERSISTENT_DISK_DELETED|  If the persistent disk was successfully deleted.   
VLSI_PERSISTENT_DISK_DELETE_FAILED|  If the persistent disk could not be deleted.   
  
Show WSDL type definition

  
  
  



**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Detaches a persistent disk from a machine. The [usage](vdi.resources.PersistentDisk.PersistentDiskGeneralData.md#usage) of that disk must be SECONDARY. 

Privileges 

Privilege |  Description   
---|---  
MACHINE_MANAGEMENT|  Machine management privilege is required to detach a primary persistent disk.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PersistentDisk](vdi.resources.PersistentDisk.md) used to make the method call.   
**id**| [PersistentDiskId](vdi.entity.PersistentDiskId.md)|  The ID of the persistent disk to detach.   
  
**spec**| [PersistentDiskDetachSpec](vdi.resources.PersistentDisk.DetachSpec.md)|  The specification of how to detach the disk.   
  
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_PERSISTENT_DISK_DETACHED|  If the persistent disk detachment was successfully requested.   
VLSI_PERSISTENT_DISK_DETACH_FAILED|  If the persistent disk detachment failed to be requested.   
  
Show WSDL type definition

  
  
  



**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Retrieves information about a persistent disk. 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PersistentDisk](vdi.resources.PersistentDisk.md) used to make the method call.   
**id**| [PersistentDiskId](vdi.entity.PersistentDiskId.md)|  The ID of the persistent disk to retrieve.   
  
  


Return Value 

Type |  Description   
---|---  
[PersistentDiskInfo](vdi.resources.PersistentDisk.PersistentDiskInfo.md)| Information about the specified persistent disk.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Returns the incompatibility reasons for Persistent Disks 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PersistentDisk](vdi.resources.PersistentDisk.md) used to make the method call.   
**specs**| [PersistentDiskRecreateMachineSpec[]](vdi.resources.PersistentDisk.RecreateMachineSpec.md)|  The specifications for previewing recreate a machine with persistent disk.   
  
  


Return Value 

Type |  Description   
---|---  
[PersistentDiskIncompatibleReasons[]](vdi.resources.PersistentDisk.PersistentDiskIncompatibleReasons.md)| returns array of PersistentIncomaptibleReasons  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Recreates a machine with the specified persistent disk. 

Privileges 

Privilege |  Description   
---|---  
POOL_MANAGEMENT|  Desktop management privilege with the corresponding access group permission is required on the desktop associated with the persistent disk to recreate a machine from a persistent disk.   
MACHINE_MANAGEMENT|  Machine management privilege is required to recreate a machine from a persistent disk.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PersistentDisk](vdi.resources.PersistentDisk.md) used to make the method call.   
**id**| [PersistentDiskId](vdi.entity.PersistentDiskId.md)|  The ID of the persistent disk to associate with the new machine.   
  
**spec**| [PersistentDiskRecreateMachineSpec](vdi.resources.PersistentDisk.RecreateMachineSpec.md)|  The specification of how to recreate the machine.   


  * This parameter need not be set.

  
  


Return Value 

Type |  Description   
---|---  
[MachineId](vdi.entity.MachineId.md)| The ID of the newly created machine.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_PERSISTENT_DISK_RECREATE_MACHINE|  If the machine recreation was successfully requested.   
VLSI_PERSISTENT_DISK_RECREATE_MACHINE_FAILED|  If the machine recreation failed to be requested.   
  
Show WSDL type definition

  
  
  



**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Recreates machines with the specified persistent disks. 

Privileges 

Privilege |  Description   
---|---  
POOL_MANAGEMENT|  Desktop management privilege with the corresponding access group permission is required on the desktop associated with the persistent disk to recreate a machine from a persistent disk.   
MACHINE_MANAGEMENT|  Machine management privilege is required to recreate a machine from a persistent disk.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PersistentDisk](vdi.resources.PersistentDisk.md) used to make the method call.   
**specs**| [PersistentDiskRecreateMachineSpec[]](vdi.resources.PersistentDisk.RecreateMachineSpec.md)|    
  
  


Return Value 

Type |  Description   
---|---  
[PersistentDiskRecreateMachineInfo[]](vdi.resources.PersistentDisk.PersistentDiskRecreateMachineInfo.md)| returns array of [PersistentDiskRecreateMachineInfo](vdi.resources.PersistentDisk.PersistentDiskRecreateMachineInfo.md)  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_PERSISTENT_DISK_RECREATE_MACHINE|  If the machine recreation was successfully requested.   
VLSI_PERSISTENT_DISK_RECREATE_MACHINE_FAILED|  If the machine recreation failed to be requested.   
  
Show WSDL type definition

  
  
  



**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Replaces the primary persistent disk on a machine. 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PersistentDisk](vdi.resources.PersistentDisk.md) used to make the method call.   
**id**| [PersistentDiskId](vdi.entity.PersistentDiskId.md)|  The ID of the persistent disk to replace.   
  
**spec**| [PersistentDiskReplaceSpec](vdi.resources.PersistentDisk.ReplaceSpec.md)|  The specification of how to replace the existing disk.   
  
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_PERSISTENT_DISK_REPLACED|  If the persistent disk replacement was successfully requested.   
VLSI_PERSISTENT_DISK_REPLACE_FAILED|  If the persistent disk replacement failed to be requested.   
  
Show WSDL type definition

  
  
  



**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Updates a persistent disk. A persistent disk can only be updated if it is unattached. 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PersistentDisk](vdi.resources.PersistentDisk.md) used to make the method call.   
**id**| [PersistentDiskId](vdi.entity.PersistentDiskId.md)|  The ID of the persistent disk to update.   
  
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  Key value pairs describing attributes to be updated.   


  * This parameter is an update map based on [PersistentDiskInfo](vdi.resources.PersistentDisk.PersistentDiskInfo.md "PersistentDiskInfo"). 

  
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the persistent disk is in a state other than unattached.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_PERSISTENT_DISK_UPDATED|  If the persistent disk was successfully updated.   
VLSI_PERSISTENT_DISK_UPDATE_FAILED|  If the persistent disk could not be updated.   
  
Show WSDL type definition

  
  
  
  
Top of page| | | Local Methods  
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

