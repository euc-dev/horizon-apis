---
layout: page
title: Service - Machine
hide:
#- navigation
- toc
---







Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Machine`

See also
> [MachineAliasUpdateSpec](vdi.resources.Machine.MachineAliasUpdateSpec.md), [MachineDeleteSpec](vdi.resources.Machine.DeleteSpec.md), [MachineId](vdi.entity.MachineId.md), [MachineInfo](vdi.resources.Machine.MachineInfo.md), [MachineRegisterResult](vdi.resources.Machine.RegisterResult.md), [MachineRegisterSpec](vdi.resources.Machine.RegisterSpec.md), [MachineSummaryView](vdi.resources.Machine.MachineSummaryView.md), [MapEntry](vdi.util.MapEntry.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0





## Service Description

Service interface for Machine. A Machine is a single instance of any one of the following: Virtual Machine (Managed), Physical Machine (Unmanaged)

Methods

Methods defined in this Service
---
Machine_assignUsers, Machine_CancelTasks, Machine_Delete, Machine_DeleteMachines, Machine_EnterMaintenanceMode, Machine_EnterMaintenanceModeMachines, Machine_ExitMaintenanceMode, Machine_ExitMaintenanceModeMachines, Machine_Get, Machine_GetInfos, Machine_GetSummaryView, Machine_GetSummaryViews, Machine_Rebuild, Machine_RebuildMachines, Machine_Recover, Machine_RecoverMachines, Machine_Register, Machine_Reset, Machine_ResetMachines, Machine_Restart, Machine_RestartMachines, Machine_unassignUsers, Machine_Update, Machine_UpdateMachineAliases




Assign the given user(s) to this machine. For single user machines this method resets the assignment, if present. Assignments are only allowed for users, not for groups.


Privileges

Privilege |  Description
---|---
MACHINE_MANAGEMENT|  privilege is required to assign the Machine.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  Unique identifier of the machine to be assigned. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.

**userIds**| [UserOrGroupId[]](vdi.entity.UserOrGroupId.md)|  Unique identifiers of the users for assignment. UserIds of this type must originate from the ADUserOrGroup service.




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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if one or more user could not be assigned.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_MACHINE_UPDATED|  if one or more user is assigned successfully.
VLSI_MACHINE_UPDATE_FAILED|  if no user is assigned.

Show WSDL type definition







Cancel pending tasks on the specified machines related to Linked-Clone rebalance/recompose/refresh operations.

Privileges

Privilege |  Description
---|---
POOL_SVI_IMAGE_MANAGEMENT|  Manage Composer Desktop Pool Image privilege is required on each of the machines to cancel the respective pending tasks.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**ids**| [MachineId[]](vdi.entity.MachineId.md)|  Array of unique identifiers of the machines. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if all operations were not successful, a PartialFailureFault will be thrown indicating cancel task on which machines were successful and which ones failed. The index of results in the PartialFailureFault corresponds to the machine's index in request. The result entry will contain either the original return type (on success) or an exception (on failure).
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_VIEW_COMPOSER_OPERATION_CANCELED|  if Machine was marked for cancelling the pending tasks.
VLSI_VIEW_COMPOSER_OPERATION_CANCEL_FAILED|  if failed to mark the Machine for cancelling the pending tasks.

Show WSDL type definition







Delete the machine.
Note :- If [deleteFromDisk](vdi.resources.Machine.DeleteSpec.md#deleteFromDisk) is true, then machine being deleted must not have any active user session, otherwise this operation would fail. Requires at least one of the listed privileges.

Privileges

Privilege |  Description
---|---
MACHINE_MANAGEMENT|  privilege is required to delete Machine configuration.
POOL_MANAGEMENT|  privilege is required to delete Machine configuration.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  unique identifier of the machine to delete. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.

**spec**| [MachineDeleteSpec](vdi.resources.Machine.DeleteSpec.md)|  attributes needed to delete the Machine.

 [^135]





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
VLSI_MACHINE_DELETED|  if Machine was deleted.
VLSI_MACHINE_DELETE_FAILED|  if the Machine delete failed.

Show WSDL type definition







Delete the machines. This applies only to managed Machines.
Note :- If [deleteFromDisk](vdi.resources.Machine.DeleteSpec.md#deleteFromDisk) is true, then machines being deleted must not have any active user session, otherwise this operation would fail. Requires at least one of the listed privileges.

Privileges

Privilege |  Description
---|---
MACHINE_MANAGEMENT|  privilege is required to delete Machine configuration.
POOL_MANAGEMENT|  privilege is required to delete Machine configuration.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**ids**| [MachineId[]](vdi.entity.MachineId.md)|  Array of unique identifiers of the machines to delete. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.

**spec**| [MachineDeleteSpec](vdi.resources.Machine.DeleteSpec.md)|  attributes needed to delete the Machines.

 [^135]





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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if delete operation fails on one or more Machines.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_MACHINE_DELETED|  if Machine was deleted.
VLSI_MACHINE_DELETE_FAILED|  if the Machine delete failed.

Show WSDL type definition







Mark the machine for maintenance. This operation puts the current machine into maintenance mode. This operation applies only to managed machines which do not belong to Instant Clone Engine desktops.


Privileges

Privilege |  Description
---|---
MACHINE_MANAGEMENT|  privilege is required to perform maintenance.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  Unique identifier of the machine. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




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
VLSI_MACHINE_MAINTENANCE|  if Machine entered maintenance mode successfully.
VLSI_MACHINE_MAINTENANCE_FAILED|  if the Machine failed to enter maintenance mode.

Show WSDL type definition







Mark machines for maintenance. For each machine, this operation puts the current machine into maintenance mode. This operation applies only to managed machines which do not belong to Instant Clone Engine desktops.


Privileges

Privilege |  Description
---|---
MACHINE_MANAGEMENT|  privilege is required to perform maintenance.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**ids**| [MachineId[]](vdi.entity.MachineId.md)|  Array of unique identifier of the machines. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if enter maintenance operation fails on one or more Machines.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_MACHINE_MAINTENANCE|  if Machine entered maintenance mode successfully.
VLSI_MACHINE_MAINTENANCE_FAILED|  if the Machine failed to enter maintenance mode.

Show WSDL type definition







Mark the machine out of maintenance. This operation takes the current machine out of maintenance mode. This operation applies only to managed machines which do not belong to Instant Clone Engine desktops.


Privileges

Privilege |  Description
---|---
MACHINE_MANAGEMENT|  privilege is required to perform maintenance.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  Unique identifier of the machine. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




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
VLSI_MACHINE_MAINTENANCE|  if Machine exited maintenance mode successfully.
VLSI_MACHINE_MAINTENANCE_FAILED|  if the Machine failed to exit maintenance mode.

Show WSDL type definition







Mark machines out of maintenance. For each machine, this operation takes the current machine out of maintenance mode. This operation applies only to managed machines which do not belong to Instant Clone Engine desktops.


Privileges

Privilege |  Description
---|---
MACHINE_MANAGEMENT|  privilege is required to perform maintenance.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**ids**| [MachineId[]](vdi.entity.MachineId.md)|  Array of unique identifier of the machines. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if exit maintenance operation fails on one or more Machines.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_MACHINE_MAINTENANCE|  if Machine exited maintenance mode successfully.
VLSI_MACHINE_MAINTENANCE_FAILED|  if the Machine failed to exit maintenance mode.

Show WSDL type definition







Gets the MachineInfo for the specified machine entry

Privileges

Privilege |  Description
---|---
MACHINE_VIEW|  privilege is required to read Machine configuration.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  Unique identifier for the machine entry. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




Return Value

Type |  Description
---|---
[MachineInfo](vdi.resources.Machine.MachineInfo.md)| The MachineInfo



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets the MachineInfo for the specified machine entries

Privileges

Privilege |  Description
---|---
MACHINE_VIEW|  privilege is required to read Machine configuration.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**ids**| [MachineId[]](vdi.entity.MachineId.md)|  Array of unique identifiers for the machine entries. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




Return Value

Type |  Description
---|---
[MachineInfo[]](vdi.resources.Machine.MachineInfo.md)| The MachineInfo array



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets the MachineSummaryView for the specified machine entry

Privileges

Privilege |  Description
---|---
MACHINE_VIEW|  privilege is required to read Machine configuration.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  Unique identifier for the machine entry. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




Return Value

Type |  Description
---|---
[MachineSummaryView](vdi.resources.Machine.MachineSummaryView.md)| The MachineSummaryView



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets the MachineSummaryViews for the specified machine entries

Privileges

Privilege |  Description
---|---
MACHINE_VIEW|  privilege is required to read Machine configuration.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**ids**| [MachineId[]](vdi.entity.MachineId.md)|  Array of unique identifiers for the machine entries. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




Return Value

Type |  Description
---|---
[MachineSummaryView[]](vdi.resources.Machine.MachineSummaryView.md)| The MachineSummaryView array



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Mark the machine for rebuilding. This operation deletes the current machine and provisions a new machine with the same name. Usually this operation is performed to rebuild a dedicated machine that is in error state or otherwise unusable. This operation applies only to machines belonging to Full Clone desktops.


Privileges

Privilege |  Description
---|---
MACHINE_MANAGEMENT|  privilege is required to rebuild Machine.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  Unique identifier of the machine to rebuild. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




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
VLSI_MACHINE_REBUILD|  if Machine was rebuilt.
VLSI_MACHINE_REBUILD_FAILED|  if the Machine rebuild failed.

Show WSDL type definition







Mark machines for rebuilding. For each machine, this operation deletes the current machine and provisions a new machine with the same name. Usually this operation is performed to rebuild a dedicated machine that is in error state or otherwise unusable. This operation applies only to machines belonging to Full Clone desktops.


Privileges

Privilege |  Description
---|---
MACHINE_MANAGEMENT|  privilege is required to rebuild Machine.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**ids**| [MachineId[]](vdi.entity.MachineId.md)|  Array of unique identifier of the machines to rebuild. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if one or more Machines cannot be rebuilt.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_MACHINE_REBUILD|  if Machine was rebuilt.
VLSI_MACHINE_REBUILD_FAILED|  if the Machine rebuild failed.

Show WSDL type definition







Mark the machine for recovery. This operation recovers machine that is in error state or otherwise unusable. This operation applies only to machines belonging to Instant Clone Engine desktops.
For floating Instant Clone Engine pools, this operation deletes the current machine and provisions a new machine from the latest image.
For dedicated Instant Clone Engine pools, this operation resyncs the current machine to the latest image. During this operation, the OS disk of specified machine will be replaced with the one that was generated based on the source template.
Note :- The machine being recovered must not have any active user session, otherwise this operation would fail. Requires at least one of the listed privileges.

Privileges

Privilege |  Description
---|---
MACHINE_MANAGEMENT|  privilege is required to recover the Machine.
POOL_MANAGEMENT|  privilege is required to recover the Machine.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  Unique identifier of the machine to recover. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




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
VLSI_MACHINE_RECOVERY_REQUESTED|  if Machine was marked for recovery.
VLSI_MACHINE_RECOVERY_REQUEST_FAILED|  if failed to mark the Machine for recovery.

Show WSDL type definition







Mark the machines for recovery. This operation recovers machines that are in error state or otherwise unusable. This operation applies only to machines belonging to Instant Clone Engine desktops.
For floating Instant Clone Engine pools, this operation deletes the current machines and provisions a machines from the latest image.
For dedicated Instant Clone Engine pools, this operation resyncs the current machines to the latest image. During this operation, the OS disk of specified machines will be replaced with the one that was generated based on the source template.
Note :- The machines being recovered must not have any active user session, otherwise this operation would fail. Requires at least one of the listed privileges.

Privileges

Privilege |  Description
---|---
MACHINE_MANAGEMENT|  privilege is required to recover the Machines.
POOL_MANAGEMENT|  privilege is required to recover the Machines.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**ids**| [MachineId[]](vdi.entity.MachineId.md)|  Array of unique identifiers of the machines to recover. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if recover operation fails on one or more Machines.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_MACHINE_RECOVERY_REQUESTED|  if Machine was marked for recovery.
VLSI_MACHINE_RECOVERY_REQUEST_FAILED|  if failed to mark the Machine for recovery.

Show WSDL type definition







Registers a machine.

Privileges

Privilege |  Description
---|---
GLOBAL_MACHINE_REGISTER|  Global machine registration privilege is required to register a machine.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**spec**| [MachineRegisterSpec](vdi.resources.Machine.RegisterSpec.md)|  The specification for the register operation.




Return Value

Type |  Description
---|---
[MachineRegisterResult](vdi.resources.Machine.RegisterResult.md)| The registration result.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if the machine cannot be registered in the specified desktop.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_MACHINE_REGISTERED|  If the machine is successfully registered.
VLSI_MACHINE_REGISTRATION_FAILED|  If the machine could not be registered.

Show WSDL type definition







Reset the machine. This applies only to managed Machine.

Privileges

Privilege |  Description
---|---
MACHINE_REBOOT|  privilege is required to reset Machine.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  Unique identifier of the machine to reset. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




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
VLSI_MACHINE_RESET|  if Machine was reset.
VLSI_MACHINE_RESET_FAILED|  if the Machine reset failed.

Show WSDL type definition







Reset the machines. This applies only to managed Machines.

Privileges

Privilege |  Description
---|---
MACHINE_REBOOT|  privilege is required to reset Machine.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**ids**| [MachineId[]](vdi.entity.MachineId.md)|  Array of unique identifier of the machines to reset. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if one or more Machines cannot be reset.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_MACHINE_RESET|  if Machine was reset.
VLSI_MACHINE_RESET_FAILED|  if the Machine reset failed.

Show WSDL type definition







Restart the machine. This applies only to managed Machine.

Privileges

Privilege |  Description
---|---
MACHINE_REBOOT|  privilege is required to restart Machine.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  Unique identifier of the machine to restart. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




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
VLSI_MACHINE_RESTART|  if Machine was restarted.
VLSI_MACHINE_RESTART_FAILED|  if the Machine restart failed.

Show WSDL type definition







Restart the machines. This applies only to managed Machines.

Privileges

Privilege |  Description
---|---
MACHINE_REBOOT|  privilege is required to restart Machine.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**ids**| [MachineId[]](vdi.entity.MachineId.md)|  Array of unique identifier of the machines to restart. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if one or more Machines cannot be restarted.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_MACHINE_RESTART|  if Machine was restarted.
VLSI_MACHINE_RESTART_FAILED|  if the Machine restart failed.

Show WSDL type definition







Unassign the given user(s) from this machine. Unassignments are only allowed for users, not for groups.


Privileges

Privilege |  Description
---|---
MACHINE_MANAGEMENT|  privilege is required to assign the Machine.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  Unique identifier of the machine to be unassigned. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.

**userIds**| [UserOrGroupId[]](vdi.entity.UserOrGroupId.md)|  Unique identifiers of the users for unassignment. UserIds of this type must originate from the ADUserOrGroup service.




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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if one or more User could not be unassigned.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_MACHINE_UPDATED|  if one or more user is unassigned successfully.
VLSI_MACHINE_UPDATE_FAILED|  if no user is unassigned.

Show WSDL type definition







Updates the machine.
NOTE: This operation will fail if [user](vdi.resources.Machine.MachineBase.md#user) field is updated for machine belonging to pools with "allowMultipleAssignments" enabled. Use [Machine_assignUsers](vdi.resources.Machine.md#assignUsers) or [Machine_unassignUsers](vdi.resources.Machine.md#unassignUsers) for assigning or unassigning users.

Privileges

Privilege |  Description
---|---
MACHINE_MANAGEMENT|  privilege is required to update Machine configuration.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  The ID of the machine to update. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.

**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  The updates to apply

 [^219]





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
VLSI_MACHINE_UPDATED|  for each Machine attribute that was updated.
VLSI_MACHINE_UPDATE_FAILED|  if the Machine update failed.

Show WSDL type definition







Updates the machine aliases of the assigned users. Machine alias will be updated if the assigned user already has the machine alias set, otherwise provided machine alias is set for the user. Machine alias will be removed for the assigned user if [alias](vdi.resources.Machine.MachineAlias.md#alias) is set to null. If no machine alias is provided in the spec for an assigned user, existing machine alias is retained for that user.

Privileges

Privilege |  Description
---|---
MACHINE_MANAGEMENT|  privilege is required to update the machine alias of the assigned user.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**spec**| [MachineAliasUpdateSpec](vdi.resources.Machine.MachineAliasUpdateSpec.md)|  Specification for updating the machine aliases of the assigned users.




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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if aliases contain more than one alias for the same user or if the alias is present for the unassigned user.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_MACHINE_UPDATED|  if one or more user's machine alias is added, removed or updated successfully.
VLSI_MACHINE_UPDATE_FAILED|  if none of the user's machine alias is added, removed or updated.

Show WSDL type definition












 [^1]: This property need not be set. [^2]: This property cannot be updated. [^3]: This property must contain only alphanumerics, spaces, underscores, and dashes. The maximum length is 32 characters. [^4]: This property has a maximum length of 400 characters. [^5]: This property has a default value of false. [^6]: This property has a default value of true. [^7]: If specified, this property is limited to letters, numbers, punctuation, spaces, and tabs. [^8]: This property has a minimum value of 1. [^9]: This property is required if maxSessionsType is set to 'LIMITED'. [^10]: This property has a default value of 1. [^11]: This property must contain only alphanumerics, underscores, and dashes. The maximum length is 64 characters. [^12]: This property has a maximum length of 256 characters. [^13]: This property has a maximum length of 1024 characters. [^14]: This property is an unordered array of unique values. [^15]: This property is required if enableAntiAffinityRules is set to true. [^16]: This property has a maximum value of 20. [^17]: This property has a default value of 'DISABLED'. [^18]: This property is required if multiSessionMode is set to 'ENABLED_DEFAULT_OFF', 'ENABLED_DEFAULT_ON', or 'ENABLED_ENFORCED'. [^19]: This property has a default value of 0. [^20]: This property cannot contain ? characters. [^21]: This property must contain the time in 24 hours format. e.g. 14:30. [^22]: This property must be in the form hh:mm in 24 hours format. [^23]: This property is required if customizationType is set to 'NONE'. [^24]: This property is required if customizationType is set to 'SYS_PREP'. [^25]: This property is required if customizationType is set to 'QUICK_PREP'. [^26]: This property is required if type is set to 'MANUAL'. [^27]: This property is required if type is set to 'RDS'. [^28]: This property has a default value of 'DESKTOP'. [^29]: This property is required if type is set to 'AUTOMATED'. [^30]: This property has a default value of ['PCOIP', 'RDP', 'BLAST']. [^31]: This property is required if operation is set to 'INITIAL_PUBLISH', 'SCHEDULE_PUSH_IMAGE', 'CANCEL_SCHEDULED_PUSH_IMAGE', or 'INFRASTRUCTURE_CHANGE'. [^32]: This property is required if operation is set to 'SCHEDULE_PUSH_IMAGE'. [^33]: For Instant clone desktops this setting can only be set to ALWAYS_POWERED_ON. [^34]: This property has a default value of 'TAKE_NO_POWER_ACTION'. [^35]: This property has a default value of 'NEVER'. [^36]: This property has a default value of 120. [^37]: This property is required if automaticLogoffPolicy is set to 'AFTER'. [^38]: This is applicable for automated desktops with virtual machines names based on pattern naming. This is not applicable for desktops that are using specified naming since dynamic creation and deletion of VMs is not supported. [^39]: For Instant clone desktops this setting can only be set to DELETE. [^40]: This property is required if refreshOsDiskAfterLogoff is set to 'EVERY'. [^41]: This property has a maximum value of 100. [^42]: This property is required if refreshOsDiskAfterLogoff is set to 'AT_SIZE'. [^43]: This property has a default value of 'AFTER'. [^44]: This property is required if emptySessionTimeoutPolicy is set to 'AFTER'. [^45]: This property has a default value of 10. [^46]: This property has a minimum value of 10. [^47]: This property is required if preLaunchSessionTimeoutPolicy is set to 'AFTER'. [^48]: This property has a default value of 'DEFAULT'. [^49]: This property has a default value of 'BLOCK_ACCESS'. [^50]: This property is required if source is set to 'VIRTUAL_CENTER'. [^51]: For Instant clone desktops this setting can only be set to false. [^52]: This property is required if overrideGlobalSetting is set to true. [^53]: This property is required if enabled is set to true. [^54]: This property is required if maxLabelType is set to 'LIMITED'. [^55]: This property has a default value of 4096. [^56]: This property has a minimum value of 512. [^57]: This property is required if redirectDisposableFiles is set to true. [^58]: This property has a default value of Auto. [^59]: This property must be single letters from D to Z or the word Auto. [^60]: This property is required if redirectDisposableFiles is set to true. [^61]: This property has a default value of 96. [^62]: This property has a minimum value of 64. [^63]: This property has a maximum value of 512. [^64]: This property is required if renderer3D is set to 'AUTOMATIC', 'SOFTWARE', or 'HARDWARE'. [^65]: This property has a default value of 2. [^66]: This property has a maximum value of 4. [^67]: This property is required if renderer3D is set to 'AUTOMATIC', 'SOFTWARE', 'HARDWARE', or 'DISABLED'. [^68]: This property has a default value of 'WUXGA'. [^69]: This property is required if renderer3D is set to 'AUTOMATIC', 'SOFTWARE', 'HARDWARE', or 'DISABLED'. [^70]: This property must contain only alphanumerics and dashes. It must contain at least one alpha character. It may also optionally contain a numeric placement token {n} or {n:fixed=#}. If the pattern does not specify the numeric placement token, the maximum length is 14 characters. [^71]: This property has a default value of 'UP_FRONT'. [^72]: This property has a minimum value of 0. [^73]: This property is required if provisioningTime is set to 'ON_DEMAND'. [^74]: This property is required if redirectWindowsProfile is set to true. [^75]: This property is required if useSeparateDatastoresPersistentAndOSDisks is set to true. [^76]: This property has a default value of 2048. [^77]: This property has a minimum value of 128. [^78]: This property has a default value of D. [^79]: This property is required if reclaimVmDiskSpace is set to true. [^80]: This property must contain only alphanumerics and dashes. It must contain at least one alpha character. The maximum length is 15 characters. [^81]: This property is required if userAssignment is set to 'DEDICATED'. [^82]: Fast NFS Clones (VAAI) will be unavailable if the Replica disks are stored separately from the OS disks. [^83]: Datastores with file system type VVOL will also be unavailable if the Replica disks are stored separately from the OS disks. [^84]: This setting is applicable to both View Composer and Instant clone engine sourced desktops. [^85]: For Instant clone desktops, this can be modified only if there are no current operations ( [operation](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md#operation) is NONE). [^86]: This property is required if useSeparateDatastoresReplicaAndOSDisks is set to true. [^87]: For Instant clone desktops, this setting can only be set to false. [^88]: This is applicable only to Virtual Center, View Composer, or Instant Clone Engine sourced manual or automatic desktops. [^89]: If true, VirtualCenter.StorageAcceleratorData#enabled must also be enabled. [^90]: This value cannot be updated for Instant Clone Engine sourced desktops. [^91]: This property has a default value of 'OS_DISKS'. [^92]: This property is required if useViewStorageAccelerator is set to true. [^93]: This property has a default value of 7. [^94]: This property has a maximum value of 999. [^95]: For Instant clone desktops, this setting can only be set to UNBOUNDED. [^96]: This property has a default value of 'CONSERVATIVE'. [^97]: This property has a default value of 'VM'. [^98]: For Instant clone desktops only it can be only a cluster and not a host. [^99]: For Instant clone desktops, this can be modified only if there are no current operations ( [operation](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md#operation) is NONE). [^100]: If the naming method is PATTERN, this value must be less than [minNumberOfMachines](vdi.resources.Desktop.PatternNamingSettings.md#minNumberOfMachines). If the naming method is SPECIFIED and this is a create, this value must be less than the number of specified names. If the naming method is SPECIFIED and this value is updated, it must be less than the total number of existing machines in the desktop. The above checks are not done if this value is 0. [^101]: For Full clone desktops, if Storage DRS cluster is used then it can only have one element. [^102]: This property is required if namingMethod is set to 'PATTERN'. [^103]: This property is required if namingMethod is set to 'SPECIFIED'. [^104]: For Instant clone desktops, this setting can only be set to PATTERN. [^105]: License is not applied to the system. [^106]: Applied license is expired. [^107]: Applied license does not have instant clone feature enabled. [^108]: This parameter is an update map based on [DesktopInfo](vdi.resources.Desktop.DesktopInfo.md 'DesktopInfo'). [^109]: Both instant and linked clones share the same base image and use less storage space than full virtual machines. [^110]: The user profile for both types clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes. [^111]: This property has a default value of 'PCOIP'. [^112]: This property is required if enableGRIDvGPUs is set to true. [^113]: This property has a default value of 'LIMITED'. [^114]: This property is required if operation is set to 'INITIAL_PUBLISH', 'CANCEL_SCHEDULED_MAINTENANCE', or 'INFRASTRUCTURE_CHANGE'. [^115]: This property has a maximum value of 100. [^116]: This property has a maximum value of 150. [^117]: This property is required if useCustomScript is set to false. [^118]: This property is required if maintenanceMode is set to 'RECURRING'. [^119]: This property has a maximum value of 31. [^120]: This property is required if maintenancePeriod is set to 'WEEKLY' or 'MONTHLY'. [^121]: This property has a default value of 'NEVER'. [^122]: This property is required if disconnectedSessionTimeoutPolicy is set to 'AFTER'. [^123]: This property has a minimum value of 10. [^124]: This property has a default value of 'VM'. [^125]: For Instant clone farms only it can be only a cluster and not a host. [^126]: For Instant clone farms, this can be modified only if there are no current operations ( [operation](vdi.resources.Farm.InstantCloneProvisioningStatusData.md#operation) is NONE). [^127]: This must be between 1 and 255 characters. [^128]: This property has a maximum length of 64 characters. [^129]: This property has a default value of 'ANY'. [^130]: This property has a default value of 'NONE'. [^131]: This property has a default value of ['PCOIP', 'BLAST']. [^132]: This property defines valid folder names with a max length of 64 characters and up to 4 subdirectory levels. The subdirectories can be specified using a backslash, e.g. (dir1\dir2\dir3\dir4). Folder names can't start or end with a backslash nor can there be 2 or more backslashes together. Combinations such as (\dir1, dir1\dir2\, dir1\\dir2, dir1\\\dir2) are invalid. The windows reserved keywords (CON, PRN, NUL, AUX, COM1 - COM9, LPT1 - LPT9 etc.) are not allowed in subdirectory names.
 [^133]: This property has a default value of "AFTER." [^134]: This property has a default value of "UNCONFIGURED". [^135]: This parameter need not be set. [^136]: This parameter is an update map based on [RoleInfo](vdi.users.Role.RoleInfo.md "RoleInfo"). [^137]: This parameter is an update map based on [SecondaryCredentialsInfo](vdi.users.SecondaryCredentials.SecondaryCredentialsInfo.md "SecondaryCredentialsInfo"). [^138]: This property is required if hybridLogonConfig is set to "password". [^139]: This property has a maximum value of 65535. [^140]: This property must be a valid IP address or DNS name. [^141]: This property must be a valid DNS name. [^142]: This parameter is an update map based on [ADDomainInfo](vdi.utils.ADDomain.ADDomainInfo.md "ADDomainInfo"). [^143]: This property must not be empty and has a maximum length of 256 characters. [^144]: Image management stream is in AVAILABLE or PARTIALLY_AVAILABLE state. [^145]: There is at least one image management version in AVAILABLE or PARTIALLY_AVAILABLE state for this stream. [^146]: There is at least one image management tag associated with the image management version. [^147]: This parameter is an update map based on [ImageManagementStreamInfo](vdi.utils.imagemanagement.ImageManagementStream.ImageManagementStreamInfo.md "ImageManagementStreamInfo"). [^148]: This property must contain only alphanumerics, underscores and dashes. The maximum length is 64 characters. [^149]: This parameter is an update map based on [ImageManagementTagInfo](vdi.utils.imagemanagement.ImageManagementTag.ImageManagementTagInfo.md "ImageManagementTagInfo"). [^150]: This property must contain only alphanumerics, dot, underscores, and dashes. The maximum length is 64 characters. [^151]: This parameter is an update map based on [ImageManagementVersionInfo](vdi.utils.imagemanagement.ImageManagementVersion.ImageManagementVersionInfo.md "ImageManagementVersionInfo"). [^152]: This property must not be empty and has a maximum length of 256 characters. [^153]: This parameter is an update map based on [InstantCloneEngineDomainAdministratorInfo](vdi.utils.InstantCloneEngineDomainAdministrator.InstantCloneEngineDomainAdministratorInfo.md "InstantCloneEngineDomainAdministratorInfo"). [^154]: This property is required if logCollectorComponentType is set to "CONNECTION_SERVER". [^155]: This property is required if logCollectorComponentType is set to "AGENT_RDS". [^156]: This property is required if logCollectorComponentType is set to "AGENT_RDS". [^157]: This property has a default value of ["DEFAULT"]. [^158]: This property is required if reset is set to false. [^159]: Contains null for which the request is processed successfully. [^160]: [LogCollectorFault](vdi.fault.LogCollectorFault.md) for failed ones. [^161]: Contains array of [LogCollectorTaskInfo](vdi.utils.logcollector.LogCollector.LogCollectorTaskInfo.md) for which the request is processed successfully. [^162]: All available log collector task information is returned if no parameter used. [^163]: Log collector task information for specified user returned if parameter used. [^164]: This property has a default value of 5. [^165]: If the [type](vdi.utils.Validator.ValidationSpec.md#type) is "MACHINE", then the naming pattern for the machines will be validated. [^166]: This parameter is an update map based on [ViewComposerDomainAdministratorInfo](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.ViewComposerDomainAdministratorInfo.md "ViewComposerDomainAdministratorInfo"). [^167]: This data object must be updated as a whole. [^168]: This property is required if source is set to "VIEW_COMPOSER" or "INSTANT_CLONE_ENGINE". [^169]: This property is required if source is set to "FULL_CLONE". [^170]: This value will be considered only in case of Dedicated Linked Pool. [^171]: It will be ignored for other Pools and Farms. [^172]: This property is required if isPersistent is set to true. [^173]: Applicable only in case of Linked Clones and Instant Clones. [^174]: Set to true only in case of DEDICATED LINKED_CLONE Pool. [^175]: It will be ignored in case of Farms and other Pools. [^176]: This property has a default value of 1024. [^177]: This property has a minimum value of 100. [^178]: This property has a maximum value of 32768. [^179]: This property is required if viewComposerType is set to "LOCAL_TO_VC" or "STANDALONE". [^180]: This property has a default value of "GENERAL". [^181]: This property cannot contain forward slashes. [^182]: This parameter is an update map based on [ApplicationInfo](vdi.resources.Application.ApplicationInfo.md "ApplicationInfo"). [^183]: This property has a default value of "NO_CONTROL". [^184]: This property has a default value of "AFTER". [^185]: This property must be single letters from D to Z. [^186]: This parameter is an update map based on [FarmInfo](vdi.resources.Farm.FarmInfo.md "FarmInfo"). [^187]: For Instant clone farms, this can be modified only if there are no current operations ( [operation](vdi.resources.Farm.InstantCloneProvisioningStatusData.md#operation) is NONE). [^188]: This parameter is an update map based on [RoleInfo](vdi.users.Role.RoleInfo.md "RoleInfo"). [^189]: This property has a maximum value of 65535. [^190]: This parameter is an update map based on [ADDomainInfo](vdi.utils.ADDomain.ADDomainInfo.md "ADDomainInfo"). [^191]: This parameter is an update map based on [ImageManagementAssetInfo](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetInfo.md "ImageManagementAssetInfo").
 [^192]: This property is required if configured is set to true. [^193]: For Instant clone desktops, this setting can only be set to false. [^194]: This parameter is an update map based on [MachineInfo](vdi.resources.Machine.MachineInfo.md "MachineInfo"). [^195]: This parameter is an update map based on [PersistentDiskInfo](vdi.resources.PersistentDisk.PersistentDiskInfo.md "PersistentDiskInfo"). [^196]: This property must contain only alphanumerics, underscores, and dashes. It must contain at least one alpha character. The maximum length is 15 characters. [^197]: This property has a default value of 1000. [^198]: This parameter is an update map based on [RDSServerInfo](vdi.resources.RDSServer.RDSServerInfo.md "RDSServerInfo"). [^199]: Admin user has single role which is of type either HELP_DESK_ADMIN or HELP_DESK_ADMIN_READ_ONLY. [^200]: This parameter is an update map based on [PoliciesSettings](vdi.users.Policies.PoliciesSettings.md "PoliciesSettings"). [^201]: This property is required if allowPCoIPHardwareAcceleration is set to "Allow". [^202]: This property is required if logCollectorComponentType is set to "AGENT". [^203]: This property is required if type is set to "APPLICATION". [^204]: This property is required if type is set to "DESKTOP". [^205]: This parameter is an update map based on [URLRedirectionInfo](vdi.infrastructure.URLRedirection.URLRedirectionInfo.md "URLRedirectionInfo"). [^206]: This property has a default value of 20. [^207]: This property has a default value of 50. [^208]: This property has a default value of 12. [^209]: This parameter is an update map based on [VirtualCenterInfo](vdi.infrastructure.VirtualCenter.VirtualCenterInfo.md "VirtualCenterInfo"). [^210]: [user](vdi.resources.Desktop.SpecifiedName.md#user) is provided. [^211]: [enabled](vdi.resources.Desktop.DesktopSettings.md#enabled) is false. [^212]: [supportedSessionType](vdi.resources.Desktop.DesktopSettings.md#supportedSessionType) is not "DESKTOP". [^213]: [globalEntitlement](vdi.resources.Desktop.GlobalEntitlementData.md#globalEntitlement) is set. [^214]: [userAssignment](vdi.resources.Desktop.UserAssignment.md#userAssignment) is "DEDICATED" and [automaticAssignment](vdi.resources.Desktop.UserAssignment.md#automaticAssignment) is false. [^215]: Local entitlements are configured. [^216]: Any of the machines in the pool have users assigned. [^217]: [connectionServerRestrictions](vdi.resources.Desktop.DesktopSettings.md#connectionServerRestrictions) is not set. [^218]: [type](vdi.resources.Desktop.DesktopSpec.md#type) is MANUAL. [^219]: This parameter is an update map based on [MachineInfo](vdi.resources.Machine.MachineInfo.md "MachineInfo"). [^220]: Admin user has single role which is of type either HELP_DESK_ADMIN or HELP_DESK_ADMIN_READ_ONLY. [^221]: [DesktopId](vdi.entity.DesktopId.md). [^222]: [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md). [^223]: [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md). [^224]: [URLRedirectionId](vdi.entity.URLRedirectionId.md). [^225]: [ServerSpec](vdi.utils.Certificate.ServerSpec.md). [^226]: [SAMLAuthenticatorServerData](vdi.infrastructure.SAMLAuthenticator.ServerData.md). [^227]: This property is a set of entries with unique "key" members. [^228]: This parameter is an update map based on [GlobalApplicationEntitlementInfo](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementInfo.md "GlobalApplicationEntitlementInfo"). [^229]: This parameter is an update map based on [GlobalEntitlementInfo](vdi.federation.GlobalEntitlement.GlobalEntitlementInfo.md "GlobalEntitlementInfo"). [^230]: This parameter is an update map based on [PodInfo](vdi.federation.Pod.PodInfo.md "PodInfo"). [^231]: This parameter is an update map based on [PodFederationInfo](vdi.federation.PodFederation.PodFederationInfo.md "PodFederationInfo"). [^232]: This parameter is an update map based on [SiteInfo](vdi.federation.Site.SiteInfo.md "SiteInfo"). [^233]: This property has a default value of "CONNECTION_SERVER_DOMAIN". [^234]: When all of the secure gateways (HTTP(S)/PCOIP/BLAST) are enabled, this field denotes the maximum load of connections allowed for the connection server. Once the number of connections to this connection server reaches this value, the subsequent connections from the horizon client will be blocked by secure gateway. [^235]: The application is missing in all the machines of the desktop. [^236]: Desktop do not have any provisioned machines. [^237]: One or more server(s) is either in WARNING or ERROR (not exceeding the predefined threshold) state. [^238]: The RDSServers in this Farm present a mix of both known and unknown load preferences. [^239]: For dedicated assignment desktop, it is the number of assigned machine count. [^240]: For floating assignment desktop, it is the summation of the connected and disconnected sessions. [^241]: For dedicated assignments, it is the total number of assigned machine count. [^242]: For floating assignments, it will be sum of all the connected and disconnected sessions. [^243]: This property is required if thumbprintAccepted is set to false. [^244]: This property is required if thumbprintAccepted is set to false. [^245]: This parameter is an update map based on [CEIPInfo](vdi.infrastructure.CEIP.CEIPInfo.md "CEIPInfo"). [^246]: This parameter is an update map based on [CertificateSSOConnectorInfo](vdi.infrastructure.CertificateSSOConnector.CertificateSSOConnectorInfo.md "CertificateSSOConnectorInfo"). [^247]: This property has a maximum value of 59. [^248]: This property is required if hostRedirection is set to true. [^249]: This parameter is an update map based on [ConnectionServerInfo](vdi.infrastructure.ConnectionServer.ConnectionServerInfo.md "ConnectionServerInfo"). [^250]: This property is required if radiusEnabled is set to true. [^251]: This property is required if samlSupport is set to "ENABLED" or "REQUIRED". [^252]: This property is required if samlSupport is set to "MULTI_ENABLED" or "MULTI_REQUIRED". [^253]: This property has a maximum value of 1440. [^254]: This property has a default value of 21. [^255]: This property has a minimum value of 14. [^256]: This property is required if workspaceOneModeEnabled is set to true. [^257]: This property has a default value of "SUCCESS". [^258]: This property is required if eventDatabaseSet is set to true. [^259]: This property must start with a letter, may only contain letters, numbers, and the characters @, $, #, and _, and may not be longer than 6 characters. [^260]: This property has a maximum value of 3. [^261]: This property has a default value of 2000. [^262]: This property has a maximum value of 7. [^263]: This parameter is an update map based on [EventDatabaseInfo](vdi.infrastructure.EventDatabase.EventDatabaseInfo.md "EventDatabaseInfo"). [^264]: One of [version](vdi.infrastructure.GlobalSettings.ClientData.md#version), [blockSpecificVersions](vdi.infrastructure.GlobalSettings.ClientData.md#blockSpecificVersions), [warnSpecificVersions](vdi.infrastructure.GlobalSettings.ClientData.md#warnSpecificVersions) is mandatory. [^265]: Only one of [version](vdi.infrastructure.GlobalSettings.ClientData.md#version) or [blockSpecificVersions](vdi.infrastructure.GlobalSettings.ClientData.md#blockSpecificVersions) can be set. [^266]: This property cannot be used for [type](vdi.infrastructure.GlobalSettings.ClientData.md#type) "WINSTORE", "HTMLACCESS". [^267]: This property has a maximum length of 128 characters. [^268]: This property accepts all characters including new line with a maximum length of 1024 characters. [^269]: This property has a default value of 60. [^270]: This property has a default value of "TIMEOUT_AFTER". [^271]: This property has a default value of 600. [^272]: This property has a minimum value of 5. [^273]: This property is required if clientMaxSessionTimePolicy is set to "TIMEOUT_AFTER". [^274]: This property has a default value of 15. [^275]: This property is required if clientIdleSessionTimeoutPolicy is set to "TIMEOUT_AFTER". [^276]: This property has a default value of 1200. [^277]: This property is required if desktopSSOTimeoutPolicy is set to "DISABLE_AFTER". [^278]: This property has a default value of "ALWAYS_ENABLED". [^279]: This property is required if applicationSSOTimeoutPolicy is set to "DISABLE_AFTER". [^280]: This property has a maximum value of 4320. [^281]: This property is required if displayWarningBeforeForcedLogoff is set to true. [^282]: If set true, UI clients should show a "Remember me" check box option on the login page. [^283]: If set false, UI clients should not show the "Remember me" check box option on the login page. [^284]: This property has a default value of 30. [^285]: This property has a maximum value of 30. [^286]: This property has a default value of Your virtual session is going to be logged off. Please save your work. [^287]: This property has a default value of Your session has expired. Please re-connect to the portal and restart the session. [^288]: This property has a default value of Attention. [^289]: This property is required if displayPreLoginAdminBanner is set to true. [^290]: This parameter is an update map based on [GlobalSettingsInfo](vdi.infrastructure.GlobalSettings.GlobalSettingsInfo.md "GlobalSettingsInfo"). [^291]: This parameter is an update map based on [GSSAPIAuthenticatorInfo](vdi.infrastructure.GSSAPIAuthenticator.GSSAPIAuthenticatorInfo.md "GSSAPIAuthenticatorInfo"). [^292]: This parameter is an update map based on [NetworkProxyConfigurationDetail](vdi.infrastructure.NetworkProxyConfiguration.NetworkProxyConfigurationDetail.md "NetworkProxyConfigurationDetail"). [^293]: This property is required if networkAutoProxy is set to false. [^294]: This property has a maximum length of 50 characters. [^295]: This property has a maximum length of 20 characters. [^296]: This parameter is an update map based on [RADIUSAuthenticatorInfo](vdi.infrastructure.RADIUSAuthenticator.RADIUSAuthenticatorInfo.md "RADIUSAuthenticatorInfo"). [^297]: This property has a maximum length of 32 characters. [^298]: This parameter is an update map based on [SAMLAuthenticatorInfo](vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorInfo.md "SAMLAuthenticatorInfo"). [^299]: This property has a default value of "DYNAMIC". [^300]: This property is required if authenticatorType is set to "DYNAMIC". [^301]: This property is required if authenticatorType is set to "STATIC". [^302]: This parameter is an update map based on [SecurityServerInfo](vdi.infrastructure.SecurityServer.SecurityServerInfo.md "SecurityServerInfo"). [^303]: This parameter is an update map based on [SyslogInfo](vdi.infrastructure.Syslog.SyslogInfo.md "SyslogInfo"). [^304]: When all of the secure gateways (HTTP(S)/PCOIP/BLAST) are enabled, this field denotes the maximum load of connections allowed for the connection server. Once the number of connections to this connection server reaches this value, the subsequent connections from the horizon client will be blocked by secure gateway. [^305]: When none of the secure gateways(HTTP(S)/PCOIP/BLAST) are enabled, sessionThreshold value will not be set. [^306]: This property has a default value of "BOTH". [^307]: This property has a default value of On proceeding, you agree that you fully comply with the laws of this organisation. [^308]: This property is required if triggerMode is set to "ENABLE_ALWAYS" or "REQUIRE_ALWAYS". [^309]: For those pods running on older version(before 7.12.0), the values for [numHostedSessions](vdi.health.Monitoring.PodSessionCounter.md#numHostedSessions) and [numBrokeredSessions](vdi.health.Monitoring.PodSessionCounter.md#numBrokeredSessions) will not be set. [^310]: When there is at least one Pod running on older version(before 7.12.0), numBrokeredSessions for all the pods will not be set. [^311]: [ApplicationId](vdi.entity.ApplicationId.md). [^312]: When none of the secure gateways(HTTP(S)/PCOIP/BLAST) are enabled, sessionThreshold value will not be set.
