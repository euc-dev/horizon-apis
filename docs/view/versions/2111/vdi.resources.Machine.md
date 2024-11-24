---
layout: page
title: Service - Machine
hide:
#- navigation
- toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.resources.Machine`

See also
> [MachineAliasUpdateSpec](vdi.resources.Machine.MachineAliasUpdateSpec.md), [MachineDeleteSpec](vdi.resources.Machine.DeleteSpec.md), [MachineId](vdi.entity.MachineId.md), [MachineInfo](vdi.resources.Machine.MachineInfo.md), [MachineRegisterResult](vdi.resources.Machine.RegisterResult.md), [MachineRegisterSpec](vdi.resources.Machine.RegisterSpec.md), [MachineStateCounts](vdi.resources.Machine.MachineStateCounts.md), [MachineSummaryView](vdi.resources.Machine.MachineSummaryView.md), [MapEntry](vdi.util.MapEntry.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0





## Service Description

Service interface for Machine. A Machine is a single instance of any one of the following: Virtual Machine (Managed), Physical Machine (Unmanaged)

**Methods**

Methods defined in this Service:
Machine_assignUsers, Machine_CancelTasks, Machine_Delete, Machine_DeleteMachines, Machine_EnterMaintenanceMode, Machine_EnterMaintenanceModeMachines, Machine_ExitMaintenanceMode, Machine_ExitMaintenanceModeMachines, Machine_Get, Machine_GetInfos, Machine_GetStateCounts, Machine_GetSummaryView, Machine_GetSummaryViews, Machine_Rebuild, Machine_RebuildMachines, Machine_Recover, Machine_RecoverMachines, Machine_Register, Machine_Reset, Machine_ResetMachines, Machine_Restart, Machine_RestartMachines, Machine_unassignUsers, Machine_Update, Machine_UpdateMachineAliases




Assign the given user(s) to this machine. For single user machines this method resets the assignment, if present. Assignments are only allowed for users, not for groups.


**Privileges**

Privilege | Description
:---|:---
MACHINE_USER_MANAGEMENT|  privilege is required to assign the Machine.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  Unique identifier of the machine to be assigned. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.
**userIds**| [UserOrGroupId[]](vdi.entity.UserOrGroupId.md)|  Unique identifiers of the users for assignment. UserIds of this type must originate from the ADUserOrGroup service.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if one or more user could not be assigned.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_MACHINE_UPDATED|  if one or more user is assigned successfully.
VLSI_MACHINE_UPDATE_FAILED|  if no user is assigned.

Show WSDL type definition







Cancel pending tasks on the specified machines related to Linked-Clone rebalance/recompose/refresh operations.

**Privileges**

Privilege | Description
:---|:---
POOL_SVI_IMAGE_MANAGEMENT|  Manage Composer Desktop Pool Image privilege is required on each of the machines to cancel the respective pending tasks.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**ids**| [MachineId[]](vdi.entity.MachineId.md)|  Array of unique identifiers of the machines. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if all operations were not successful, a PartialFailureFault will be thrown indicating cancel task on which machines were successful and which ones failed. The index of results in the PartialFailureFault corresponds to the machine's index in request. The result entry will contain either the original return type (on success) or an exception (on failure).
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_VIEW_COMPOSER_OPERATION_CANCELED|  if Machine was marked for cancelling the pending tasks.
VLSI_VIEW_COMPOSER_OPERATION_CANCEL_FAILED|  if failed to mark the Machine for cancelling the pending tasks.

Show WSDL type definition







Delete the machine.
Note :- If [deleteFromDisk](vdi.resources.Machine.DeleteSpec.md#deleteFromDisk) is true, then machine being deleted must not have any active user session, otherwise this operation would fail. Requires at least one of the listed privileges.

**Privileges**

Privilege | Description
:---|:---
MACHINE_MANAGEMENT|  privilege is required to delete Machine configuration.
POOL_MANAGEMENT|  privilege is required to delete Machine configuration.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  unique identifier of the machine to delete. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.
**spec**| [MachineDeleteSpec](vdi.resources.Machine.DeleteSpec.md)|  attributes needed to delete the Machine. [^135]





**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_MACHINE_DELETED|  if Machine was deleted.
VLSI_MACHINE_DELETE_FAILED|  if the Machine delete failed.

Show WSDL type definition







Delete the machines. This applies only to managed Machines.
Note :- If [deleteFromDisk](vdi.resources.Machine.DeleteSpec.md#deleteFromDisk) is true, then machines being deleted must not have any active user session, otherwise this operation would fail. Requires at least one of the listed privileges.

**Privileges**

Privilege | Description
:---|:---
MACHINE_MANAGEMENT|  privilege is required to delete Machine configuration.
POOL_MANAGEMENT|  privilege is required to delete Machine configuration.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**ids**| [MachineId[]](vdi.entity.MachineId.md)|  Array of unique identifiers of the machines to delete. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.
**spec**| [MachineDeleteSpec](vdi.resources.Machine.DeleteSpec.md)|  attributes needed to delete the Machines. [^135]





**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if delete operation fails on one or more Machines.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_MACHINE_DELETED|  if Machine was deleted.
VLSI_MACHINE_DELETE_FAILED|  if the Machine delete failed.

Show WSDL type definition







Mark the machine for maintenance. This operation puts the current machine into maintenance mode. This operation applies only to managed machines which do not belong to Instant Clone Engine desktops.


**Privileges**

Privilege | Description
:---|:---
MACHINE_MAINTENANCE|  privilege is required to perform maintenance.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  Unique identifier of the machine. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_MACHINE_MAINTENANCE|  if Machine entered maintenance mode successfully.
VLSI_MACHINE_MAINTENANCE_FAILED|  if the Machine failed to enter maintenance mode.

Show WSDL type definition







Mark machines for maintenance. For each machine, this operation puts the current machine into maintenance mode. This operation applies only to managed machines which do not belong to Instant Clone Engine desktops.


**Privileges**

Privilege | Description
:---|:---
MACHINE_MAINTENANCE|  privilege is required to perform maintenance.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**ids**| [MachineId[]](vdi.entity.MachineId.md)|  Array of unique identifier of the machines. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if enter maintenance operation fails on one or more Machines.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_MACHINE_MAINTENANCE|  if Machine entered maintenance mode successfully.
VLSI_MACHINE_MAINTENANCE_FAILED|  if the Machine failed to enter maintenance mode.

Show WSDL type definition







Mark the machine out of maintenance. This operation takes the current machine out of maintenance mode. This operation applies only to managed machines which do not belong to Instant Clone Engine desktops.


**Privileges**

Privilege | Description
:---|:---
MACHINE_MAINTENANCE|  privilege is required to perform maintenance.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  Unique identifier of the machine. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_MACHINE_MAINTENANCE|  if Machine exited maintenance mode successfully.
VLSI_MACHINE_MAINTENANCE_FAILED|  if the Machine failed to exit maintenance mode.

Show WSDL type definition







Mark machines out of maintenance. For each machine, this operation takes the current machine out of maintenance mode. This operation applies only to managed machines which do not belong to Instant Clone Engine desktops.


**Privileges**

Privilege | Description
:---|:---
MACHINE_MAINTENANCE|  privilege is required to perform maintenance.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**ids**| [MachineId[]](vdi.entity.MachineId.md)|  Array of unique identifier of the machines. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if exit maintenance operation fails on one or more Machines.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_MACHINE_MAINTENANCE|  if Machine exited maintenance mode successfully.
VLSI_MACHINE_MAINTENANCE_FAILED|  if the Machine failed to exit maintenance mode.

Show WSDL type definition







Gets the MachineInfo for the specified machine entry

**Privileges**

Privilege | Description
:---|:---
MACHINE_VIEW|  privilege is required to read Machine configuration.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  Unique identifier for the machine entry. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




**Return Value**

Type | Description
:---|:---
[MachineInfo](vdi.resources.Machine.MachineInfo.md)| The MachineInfo



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets the MachineInfo for the specified machine entries

**Privileges**

Privilege | Description
:---|:---
MACHINE_VIEW|  privilege is required to read Machine configuration.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**ids**| [MachineId[]](vdi.entity.MachineId.md)|  Array of unique identifiers for the machine entries. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




**Return Value**

Type | Description
:---|:---
[MachineInfo[]](vdi.resources.Machine.MachineInfo.md)| The MachineInfo array



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Returns the counters for various machine states.

**Privileges**

Privilege | Description
:---|:---
MACHINE_VIEW|  privilege is required to get Machine state counts.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[MachineStateCounts](vdi.resources.Machine.MachineStateCounts.md)| The MachineStateCounts



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets the MachineSummaryView for the specified machine entry

**Privileges**

Privilege | Description
:---|:---
MACHINE_VIEW|  privilege is required to read Machine configuration.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  Unique identifier for the machine entry. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




**Return Value**

Type | Description
:---|:---
[MachineSummaryView](vdi.resources.Machine.MachineSummaryView.md)| The MachineSummaryView



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets the MachineSummaryViews for the specified machine entries

**Privileges**

Privilege | Description
:---|:---
MACHINE_VIEW|  privilege is required to read Machine configuration.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**ids**| [MachineId[]](vdi.entity.MachineId.md)|  Array of unique identifiers for the machine entries. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




**Return Value**

Type | Description
:---|:---
[MachineSummaryView[]](vdi.resources.Machine.MachineSummaryView.md)| The MachineSummaryView array



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Mark the machine for rebuilding. This operation deletes the current machine and provisions a new machine with the same name. Usually this operation is performed to rebuild a dedicated machine that is in error state or otherwise unusable. This operation applies only to machines belonging to Full Clone desktops.


**Privileges**

Privilege | Description
:---|:---
MACHINE_MANAGEMENT|  privilege is required to rebuild Machine.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  Unique identifier of the machine to rebuild. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_MACHINE_REBUILD|  if Machine was rebuilt.
VLSI_MACHINE_REBUILD_FAILED|  if the Machine rebuild failed.

Show WSDL type definition







Mark machines for rebuilding. For each machine, this operation deletes the current machine and provisions a new machine with the same name. Usually this operation is performed to rebuild a dedicated machine that is in error state or otherwise unusable. This operation applies only to machines belonging to Full Clone desktops.


**Privileges**

Privilege | Description
:---|:---
MACHINE_MANAGEMENT|  privilege is required to rebuild Machine.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**ids**| [MachineId[]](vdi.entity.MachineId.md)|  Array of unique identifier of the machines to rebuild. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if one or more Machines cannot be rebuilt.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_MACHINE_REBUILD|  if Machine was rebuilt.
VLSI_MACHINE_REBUILD_FAILED|  if the Machine rebuild failed.

Show WSDL type definition







Mark the machine for recovery. This operation recovers machine that is in error state or otherwise unusable. This operation applies only to machines belonging to Instant Clone Engine desktops.
For floating Instant Clone Engine pools, this operation deletes the current machine and provisions a new machine from the latest image.
For dedicated Instant Clone Engine pools, this operation resyncs the current machine to the latest image. During this operation, the OS disk of specified machine will be replaced with the one that was generated based on the source template.
Note :- The machine being recovered must not have any active user session, otherwise this operation would fail. Requires at least one of the listed privileges.

**Privileges**

Privilege | Description
:---|:---
MACHINE_MANAGEMENT|  privilege is required to recover the Machine.
POOL_MANAGEMENT|  privilege is required to recover the Machine.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  Unique identifier of the machine to recover. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_MACHINE_RECOVERY_REQUESTED|  if Machine was marked for recovery.
VLSI_MACHINE_RECOVERY_REQUEST_FAILED|  if failed to mark the Machine for recovery.

Show WSDL type definition







Mark the machines for recovery. This operation recovers machines that are in error state or otherwise unusable. This operation applies only to machines belonging to Instant Clone Engine desktops.
For floating Instant Clone Engine pools, this operation deletes the current machines and provisions a machines from the latest image.
For dedicated Instant Clone Engine pools, this operation resyncs the current machines to the latest image. During this operation, the OS disk of specified machines will be replaced with the one that was generated based on the source template.
Note :- The machines being recovered must not have any active user session, otherwise this operation would fail. Requires at least one of the listed privileges.

**Privileges**

Privilege | Description
:---|:---
MACHINE_MANAGEMENT|  privilege is required to recover the Machines.
POOL_MANAGEMENT|  privilege is required to recover the Machines.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**ids**| [MachineId[]](vdi.entity.MachineId.md)|  Array of unique identifiers of the machines to recover. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if recover operation fails on one or more Machines.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_MACHINE_RECOVERY_REQUESTED|  if Machine was marked for recovery.
VLSI_MACHINE_RECOVERY_REQUEST_FAILED|  if failed to mark the Machine for recovery.

Show WSDL type definition







Registers a machine.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_MACHINE_REGISTER|  Global machine registration privilege is required to register a machine.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**spec**| [MachineRegisterSpec](vdi.resources.Machine.RegisterSpec.md)|  The specification for the register operation.




**Return Value**

Type | Description
:---|:---
[MachineRegisterResult](vdi.resources.Machine.RegisterResult.md)| The registration result.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if the machine cannot be registered in the specified desktop.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_MACHINE_REGISTERED|  If the machine is successfully registered.
VLSI_MACHINE_REGISTRATION_FAILED|  If the machine could not be registered.

Show WSDL type definition







Reset the machine. This applies only to managed Machine.

**Privileges**

Privilege | Description
:---|:---
MACHINE_REBOOT|  privilege is required to reset Machine.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  Unique identifier of the machine to reset. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_MACHINE_RESET|  if Machine was reset.
VLSI_MACHINE_RESET_FAILED|  if the Machine reset failed.

Show WSDL type definition







Reset the machines. This applies only to managed Machines.

**Privileges**

Privilege | Description
:---|:---
MACHINE_REBOOT|  privilege is required to reset Machine.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**ids**| [MachineId[]](vdi.entity.MachineId.md)|  Array of unique identifier of the machines to reset. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if one or more Machines cannot be reset.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_MACHINE_RESET|  if Machine was reset.
VLSI_MACHINE_RESET_FAILED|  if the Machine reset failed.

Show WSDL type definition







Restart the machine. This applies only to managed Machine.

**Privileges**

Privilege | Description
:---|:---
MACHINE_REBOOT|  privilege is required to restart Machine.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  Unique identifier of the machine to restart. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_MACHINE_RESTART|  if Machine was restarted.
VLSI_MACHINE_RESTART_FAILED|  if the Machine restart failed.

Show WSDL type definition







Restart the machines. This applies only to managed Machines.

**Privileges**

Privilege | Description
:---|:---
MACHINE_REBOOT|  privilege is required to restart Machine.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**ids**| [MachineId[]](vdi.entity.MachineId.md)|  Array of unique identifier of the machines to restart. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if one or more Machines cannot be restarted.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_MACHINE_RESTART|  if Machine was restarted.
VLSI_MACHINE_RESTART_FAILED|  if the Machine restart failed.

Show WSDL type definition







Unassign the given user(s) from this machine. Unassignments are only allowed for users, not for groups.


**Privileges**

Privilege | Description
:---|:---
MACHINE_USER_MANAGEMENT|  privilege is required to assign the Machine.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  Unique identifier of the machine to be unassigned. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.
**userIds**| [UserOrGroupId[]](vdi.entity.UserOrGroupId.md)|  Unique identifiers of the users for unassignment. UserIds of this type must originate from the ADUserOrGroup service.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if one or more User could not be unassigned.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_MACHINE_UPDATED|  if one or more user is unassigned successfully.
VLSI_MACHINE_UPDATE_FAILED|  if no user is unassigned.

Show WSDL type definition







Updates the machine.
NOTE: This operation will fail if [user](vdi.resources.Machine.MachineBase.md#user) field is updated for machine belonging to pools with "allowMultipleAssignments" enabled. Use [Machine_assignUsers](vdi.resources.Machine.md#assignUsers) or [Machine_unassignUsers](vdi.resources.Machine.md#unassignUsers) for assigning or unassigning users.

**Privileges**

Privilege | Description
:---|:---
MACHINE_MAINTENANCE|  privilege is required to update machine maintenance state
MACHINE_USER_MANAGEMENT|  privilege is required to update user assignment



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  The ID of the machine to update. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  The updates to apply [^219]





**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_MACHINE_UPDATED|  for each Machine attribute that was updated.
VLSI_MACHINE_UPDATE_FAILED|  if the Machine update failed.

Show WSDL type definition







Updates the machine aliases of the assigned users. Machine alias will be updated if the assigned user already has the machine alias set, otherwise provided machine alias is set for the user. Machine alias will be removed for the assigned user if [alias](vdi.resources.Machine.MachineAlias.md#alias) is set to null. If no machine alias is provided in the spec for an assigned user, existing machine alias is retained for that user.

**Privileges**

Privilege | Description
:---|:---
MACHINE_USER_MANAGEMENT|  privilege is required to update the machine alias of the assigned user.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Machine](vdi.resources.Machine.md) used to make the method call.
**spec**| [MachineAliasUpdateSpec](vdi.resources.Machine.MachineAliasUpdateSpec.md)|  Specification for updating the machine aliases of the assigned users.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if aliases contain more than one alias for the same user or if the alias is present for the unassigned user.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_MACHINE_UPDATED|  if one or more user's machine alias is added, removed or updated successfully.
VLSI_MACHINE_UPDATE_FAILED|  if none of the user's machine alias is added, removed or updated.

Show WSDL type definition












 


[^135]: This parameter need not be set.
[^219]: This parameter is an update map based on [MachineInfo](vdi.resources.Machine.MachineInfo.md "MachineInfo").