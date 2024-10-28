---
layout: page
title: Service - Desktop
hide:
#- navigation
- toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop`

See also
> [ApplicationDiscoveryData](vdi.resources.Application.ApplicationDiscoveryData.md), [DesktopDeleteSpec](vdi.resources.Desktop.DesktopDeleteSpec.md), [DesktopDetailView](vdi.resources.Desktop.DesktopDetailView.md), [DesktopId](vdi.entity.DesktopId.md), [DesktopImageManagementPushImageSpec](vdi.resources.Desktop.ImageManagementPushImageSpec.md), [DesktopInfo](vdi.resources.Desktop.DesktopInfo.md), [DesktopManualVirtualMachineData](vdi.resources.Desktop.ManualVirtualMachineData.md), [DesktopManualVirtualMachineDefinition](vdi.resources.Desktop.ManualVirtualMachineDefinition.md), [DesktopMissingApplicationInstallationData](vdi.resources.Desktop.MissingApplicationInstallationData.md), [DesktopPushImageSpec](vdi.resources.Desktop.PushImageSpec.md), [DesktopRebalanceSpec](vdi.resources.Desktop.RebalanceSpec.md), [DesktopRecomposeSpec](vdi.resources.Desktop.RecomposeSpec.md), [DesktopRefreshSpec](vdi.resources.Desktop.RefreshSpec.md), [DesktopSpec](vdi.resources.Desktop.DesktopSpec.md), [DesktopSpecifiedName](vdi.resources.Desktop.SpecifiedName.md), [DesktopSummaryView](vdi.resources.Desktop.DesktopSummaryView.md), [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md), [MachineId](vdi.entity.MachineId.md), [MapEntry](vdi.util.MapEntry.md)

Since
> Horizon View 6.0





## Service Description

Service interface for Desktop. A Desktop is a collection of Machines managed by View.

Methods

Methods defined in this Service
---
Desktop_AddMachinesToManualDesktop, Desktop_AddMachinesToSpecifiedNamingDesktop, Desktop_AddMachineToManualDesktop, Desktop_AddMachineToSpecifiedNamingDesktop, Desktop_ApplyImage, Desktop_CancelScheduledPushImage, Desktop_Create, Desktop_Delete, Desktop_DiscoverInstalledApplications, Desktop_Get, Desktop_GetByNamingPattern, Desktop_GetDetailView, Desktop_GetSummaryView, Desktop_GetSummaryViews, Desktop_ImageManagementSchedulePushImage, Desktop_ListGECompatibleDesktops, Desktop_PromotePendingImage, Desktop_Rebalance, Desktop_Recompose, Desktop_Refresh, Desktop_RemoveMachineFromManualDesktop, Desktop_RemoveMachinesFromManualDesktop, Desktop_SchedulePushImage, Desktop_Update, Desktop_ValidateInstalledApplications, Desktop_ValidateVmNamesInfo




Adds the machines in the specified manual-type desktop.

Privileges

Privilege |  Description
---|---
POOL_MANAGEMENT|  Desktop management with the corresponding access group permission is required to add machines.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  unique identifier for a desktop entry
**machines**| [MachineId[]](vdi.entity.MachineId.md)|  array of machineIds to add. MachineIds of this type must originate from the [VirtualMachine](vdi.utils.virtualcenter.VirtualMachine.md) or [RegisteredPhysicalMachine](vdi.resources.RegisteredPhysicalMachine.md) services, but not the [Machine](vdi.resources.Machine.md) service.




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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if all operations were not successful, a PartialFailureFault will be thrown indicating which machines were successfully added and which ones failed. The index of results in the PartialFailureFault correspond to the index of the original machine. The result entry will contain either the original return type (on success) or an exception (on failure).
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_DESKTOP_MACHINE_ADDED|  This will be sent if a machine was successfully added to the desktop.
VLSI_DESKTOP_MACHINE_ADD_FAILED|  This will be sent if a machine could not be added to the desktop.

Show WSDL type definition







Adds the machines with the given specified names to the desktop. The desktop must have been created to use specified naming of machines.

Privileges

Privilege |  Description
---|---
POOL_MANAGEMENT|  Desktop management with the corresponding access group permission is required to add machines.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  unique identifier for a desktop entry
**specifiedNames**| [DesktopSpecifiedName[]](vdi.resources.Desktop.SpecifiedName.md)|  array of SpecifiedNames to add




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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if all operations were not successful, a PartialFailureFault will be thrown indicating which specified naming machines were successfully added and which ones failed. The index of results in the PartialFailureFault correspond to the index of the original specified name. The result entry will contain either be the original return type (on success) or an exception (on failure).
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_DESKTOP_MACHINE_ADDED|  This will be sent if a machine was successfully added to the desktop.
VLSI_DESKTOP_MACHINE_ADD_FAILED|  This will be sent if a machine could not be added to the desktop.

Show WSDL type definition







Adds the machine in the specified manual-type desktop.

Privileges

Privilege |  Description
---|---
POOL_MANAGEMENT|  Desktop management with the corresponding access group permission is required to add a machine.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  unique identifier for a desktop entry
**machine**| [MachineId](vdi.entity.MachineId.md)|  machineId to add. MachineIds of this type must originate from the [VirtualMachine](vdi.utils.virtualcenter.VirtualMachine.md) or [RegisteredPhysicalMachine](vdi.resources.RegisteredPhysicalMachine.md) services, but not the [Machine](vdi.resources.Machine.md) service.




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
VLSI_DESKTOP_MACHINE_ADDED|  This will be sent if a machine was successfully added to the desktop.
VLSI_DESKTOP_MACHINE_ADD_FAILED|  This will be sent if a machine could not be added to the desktop.

Show WSDL type definition







Adds the machine with the given specified name to the desktop. The desktop must have been created to use specified naming of machines.

Privileges

Privilege |  Description
---|---
POOL_MANAGEMENT|  Desktop management with the corresponding access group permission is required to add a machine.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  unique identifier for a desktop entry
**specifiedName**| [DesktopSpecifiedName](vdi.resources.Desktop.SpecifiedName.md)|  SpecifiedName to add




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
VLSI_DESKTOP_MACHINE_ADDED|  This will be sent if a machine was successfully added to the desktop.
VLSI_DESKTOP_MACHINE_ADD_FAILED|  This will be sent if a machine could not be added to the desktop.

Show WSDL type definition







Requests an update of the Image in the specified desktop. This applies either the pending image (in ready held state) or the current image to selected VMs in the pool.

Privileges

Privilege |  Description
---|---
POOL_SVI_IMAGE_MANAGEMENT|  Manage maintenance operations on Automated Desktops & Farms with the corresponding access group permission is required to pushImage.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  unique identifier for a desktop entry.

**machines**| [MachineId[]](vdi.entity.MachineId.md)|  The list of machines of which the image is to be applied.
**pendingImage**|  xsd:boolean|  Set to true if the pending image is to be applied. Else current image is applied




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
VLSI_DESKTOP_PUSH_IMAGE_SCHEDULED|  This will be sent if the new image is successfully marked for update.
VLSI_DESKTOP_PUSH_IMAGE_SCHEDULE_FAILED|  This will be sent if the new image failed to be marked for update.

Show WSDL type definition







Requests a cancellation of the current scheduled push image operation on the specified Instant Clone Engine sourced desktop.
[operation](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md#operation) must be SCHEDULE_PUSH_IMAGE and this must be called prior to the time set in [startTime](vdi.resources.Desktop.PushImageSettings.md#startTime). This operation is applicable only to Instant clone engine sourced desktops.

Privileges

Privilege |  Description
---|---
POOL_SVI_IMAGE_MANAGEMENT|  Manage maintenance operations on Automated Desktops & Farms with the corresponding access group permission is required to cancel pushImage.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  unique identifier for a desktop entry.




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
VLSI_DESKTOP_PUSH_IMAGE_CANCELLED|  This will be sent if the push image operation was successfully cancelled.
VLSI_DESKTOP_PUSH_IMAGE_CANCEL_FAILED|  This will be sent if the push image operation failed to be cancelled.

Show WSDL type definition







Create a new desktop.

Privileges

Privilege |  Description
---|---
POOL_MANAGEMENT|  Desktop management with the corresponding access group permission is required to create a desktop.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**spec**| [DesktopSpec](vdi.resources.Desktop.DesktopSpec.md)|  attributes needed to create a desktop




Return Value

Type |  Description
---|---
[DesktopId](vdi.entity.DesktopId.md)| unique identifier for the desktop



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidLicense](vdi.fault.InvalidLicense.md)| Thrown in one of the following cases during Instant Clone Desktop creation: <br> [^105] [^106] [^107]
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
ADMIN_DESKTOP_ADDED|  If the desktop was successfully created.
ADMIN_POOL_ADD_FAILED|  If the desktop could not be created.

Show WSDL type definition







Requests that the specified desktop be deleted. This sets the [deleting](vdi.resources.Desktop.DesktopSettings.md#deleting) flag of the desktop. The desktop will still be present until its machines and their disks are asynchronously dealt with according to the provided DesktopDeleteSpec.

Privileges

Privilege |  Description
---|---
POOL_MANAGEMENT|  Desktop management with the corresponding access group permission is required to delete a desktop.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  unique identifier for a desktop entry
**spec**| [DesktopDeleteSpec](vdi.resources.Desktop.DesktopDeleteSpec.md)|  attributes needed to delete a desktop. If unset, default values will be used. [^135]





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
ADMIN_REMOVE_DESKTOP_SUCCEEDED|  If a request to begin desktop deletion was successful.
ADMIN_REMOVE_DESKTOP_FAILED|  If the request to delete the desktop could not be made.

Show WSDL type definition







Query AppTap for the list of installed applications on the given Desktop.

Privileges

Privilege |  Description
---|---
POOL_VIEW|  privilege is required to discover installed Applications.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  The entityId of the Desktop on which to discover installed applications




Return Value

Type |  Description
---|---
[ApplicationDiscoveryData[]](vdi.resources.Application.ApplicationDiscoveryData.md)| The list of installed applications



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets the DesktopInfo for a specific desktop entry.

Privileges

Privilege |  Description
---|---
POOL_VIEW|  Desktop read privilege with the corresponding access group permission is required to read a desktop.
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read the [globalEntitlementData](vdi.resources.Desktop.DesktopInfo.md#globalEntitlementData) members of a desktop. This will otherwise be unset.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  unique identifier for a desktop entry




Return Value

Type |  Description
---|---
[DesktopInfo](vdi.resources.Desktop.DesktopInfo.md)| The DesktopInfo



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Get a desktop by naming pattern.

Privileges

Privilege |  Description
---|---
POOL_VIEW|  privilege is required to get the desktop information.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**namingPattern**|  xsd:string|  Unique virtual machine naming pattern for a desktop entry.




Return Value

Type |  Description
---|---
[DesktopInfo](vdi.resources.Desktop.DesktopInfo.md)| The DesktopInfo



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets the DesktopDetailView for a specific desktop entry.

Privileges

Privilege |  Description
---|---
POOL_VIEW|  Desktop read privilege with the corresponding access group permission is required to read a desktop.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  unique identifier for a desktop entry




Return Value

Type |  Description
---|---
[DesktopDetailView](vdi.resources.Desktop.DesktopDetailView.md)| The DesktopDetailView



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets the DesktopSummaryView for a specific desktop entry.

Privileges

Privilege |  Description
---|---
POOL_VIEW|  Desktop read privilege with the corresponding access group permission is required to read a desktop.
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read the [desktopSummaryData](vdi.resources.Desktop.DesktopSummaryView.md#desktopSummaryData).[globalEntitlement](vdi.resources.Desktop.DesktopSummaryData.md#globalEntitlement) member of a desktop. This will otherwise be unset.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  unique identifier for a desktop entry




Return Value

Type |  Description
---|---
[DesktopSummaryView](vdi.resources.Desktop.DesktopSummaryView.md)| The DesktopSummaryView



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets the DesktopSummaryView for selected desktop entries.

Privileges

Privilege |  Description
---|---
POOL_VIEW|  Desktop read privilege with the corresponding access group permission is required to read desktops.
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read the [desktopSummaryData](vdi.resources.Desktop.DesktopSummaryView.md#desktopSummaryData).[globalEntitlement](vdi.resources.Desktop.DesktopSummaryData.md#globalEntitlement) member of a desktop. This will otherwise be unset.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**ids**| [DesktopId[]](vdi.entity.DesktopId.md)|  array of unique identifiers for a desktop entry




Return Value

Type |  Description
---|---
[DesktopSummaryView[]](vdi.resources.Desktop.DesktopSummaryView.md)| The DesktopSummaryViews



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Requests an update of the Image in an Instant Clone desktop created using Image catalog. This marks the old image to be replaced by new image, which is performed asynchronously. Once the new image is successfully updated, all eligible machines in desktop would also be marked for update with new image, this operation is also performed asynchronously. [operation](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md#operation) must be NONE.
Same operation can also be used to reschedule an existing scheduled push image operation, if [operation](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md#operation) is SCHEDULE_PUSH_IMAGE and schedule has not triggered yet. In case of reschedule other than [startTime](vdi.resources.Desktop.PushImageSettings.md#startTime) all the parameters in [DesktopImageManagementPushImageSpec](vdi.resources.Desktop.ImageManagementPushImageSpec.md) should be identical to previous [Desktop_ImageManagementSchedulePushImage](vdi.resources.Desktop.md#imageManagementSchedulePushImage) call.


Privileges

Privilege |  Description
---|---
POOL_SVI_IMAGE_MANAGEMENT|  Manage maintenance operations on Automated Desktops & Farms with the corresponding access group permission is required to pushImage.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  unique identifier for a desktop entry.
**spec**| [DesktopImageManagementPushImageSpec](vdi.resources.Desktop.ImageManagementPushImageSpec.md)|  The specification for the pushImage operation if desktop is created using image catalog.




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
VLSI_DESKTOP_PUSH_IMAGE_SCHEDULED|  This will be sent if the new image is successfully marked for update.
VLSI_DESKTOP_PUSH_IMAGE_SCHEDULE_FAILED|  This will be sent if the new image failed to be marked for update.
VLSI_MACHINE_PUSH_IMAGE_FAILED|  This will be sent if a machine failed to be marked for update.

Show WSDL type definition







List of desktops that can be associated with the specified Global Entitlement.

Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read a Global Entitlement
POOL_VIEW|  Desktop read privilege with the corresponding access group permission is required to read a desktop and farm information



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**globalEntitlement**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  unique identifier for Global Entitlement. GlobalEntitlementIds of this type must originate from GlobalEntitlement service




Return Value

Type |  Description
---|---
[DesktopSummaryView[]](vdi.resources.Desktop.DesktopSummaryView.md)|



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Requests an update of the Image in the specified desktop. This API can be called only if there is a pending image in a ready held state. This image is then applied to all the vms in the pool.

Privileges

Privilege |  Description
---|---
POOL_SVI_IMAGE_MANAGEMENT|  Manage maintenance operations on Automated Desktops & Farms with the corresponding access group permission is required to pushImage.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  unique identifier for a desktop entry.




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
VLSI_DESKTOP_PUSH_IMAGE_SCHEDULED|  This will be sent if the new image is successfully marked for update.
VLSI_DESKTOP_PUSH_IMAGE_SCHEDULE_FAILED|  This will be sent if the new image failed to be marked for update.

Show WSDL type definition







**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Requests a rebalance of machines in the specified desktop. This marks the machines for rebalance, which is performed asynchronously.
This operation is applicable only to View Composer sourced desktops.

Privileges

Privilege |  Description
---|---
POOL_SVI_IMAGE_MANAGEMENT|  Manage maintenance operations on Automated Desktops & Farms privilege with the corresponding access group permission is required to rebalance.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  unique identifier for a desktop entry.
**spec**| [DesktopRebalanceSpec](vdi.resources.Desktop.RebalanceSpec.md)|  The specification for the rebalance operation.




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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if all operations were not successful, a PartialFailureFault will be thrown indicating which machines were successfully marked for recompose and which ones failed. The index of results in the PartialFailureFault correspond to the index of the original machine. The result entry will contain either be the original return type (on success) or an exception (on failure).
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_DESKTOP_REBALANCED|  This will be sent if all machines were successfully marked for rebalance.
VLSI_MACHINE_REBALANCED|  This will be sent if a machine was successfully marked for rebalance.
VLSI_DESKTOP_REBALANCE_FAILED|  This will be sent if any machine failed to be marked for rebalance.
VLSI_MACHINE_REBALANCE_FAILED|  This will be sent if a machine failed to be marked for rebalance.

Show WSDL type definition







**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Requests a recompose of machines in the specified desktop. This marks the machines for recompose, which is performed asynchronously.
This operation is applicable only to View Composer sourced desktops.

Privileges

Privilege |  Description
---|---
POOL_SVI_IMAGE_MANAGEMENT|  Manage maintenance operations on Automated Desktops & Farms privilege with the corresponding access group permission is required to recompose.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  unique identifier for a desktop entry.
**spec**| [DesktopRecomposeSpec](vdi.resources.Desktop.RecomposeSpec.md)|  The specification for the recompose operation.




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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if all operations were not successful, a PartialFailureFault will be thrown indicating which machines were successfully marked for recompose and which ones failed. The index of results in the PartialFailureFault correspond to the index of the original machine. The result entry will contain either be the original return type (on success) or an exception (on failure).
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_DESKTOP_RECOMPOSED|  This will be sent if all machines were successfully marked for recompose.
VLSI_MACHINE_RECOMPOSED|  This will be sent if a machine was successfully marked for recompose.
VLSI_DESKTOP_RECOMPOSE_FAILED|  This will be sent if any machine failed to be marked for recompose.
VLSI_MACHINE_RECOMPOSE_FAILED|  This will be sent if a machine failed to be marked for recompose.

Show WSDL type definition







**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Requests a refresh of machines in the specified desktop. This marks the machines for refresh, which is performed asynchronously.
This operation is applicable only to View Composer sourced desktops.

Privileges

Privilege |  Description
---|---
POOL_SVI_IMAGE_MANAGEMENT|  Manage maintenance operations on Automated Desktops & Farms privilege with the corresponding access group permission is required to refresh.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  unique identifier for a desktop entry.
**spec**| [DesktopRefreshSpec](vdi.resources.Desktop.RefreshSpec.md)|  The specification for the refresh operation.




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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if all operations were not successful, a PartialFailureFault will be thrown indicating which machines were successfully marked for refresh and which ones failed. The index of results in the PartialFailureFault correspond to the index of the original machine. The result entry will contain either be the original return type (on success) or an exception (on failure).
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_DESKTOP_REFRESHED|  This will be sent if all machines were successfully marked for refresh.
VLSI_MACHINE_REFRESHED|  This will be sent if a machine was successfully marked for refresh.
VLSI_DESKTOP_REFRESH_FAILED|  This will be sent if any machine failed to be marked for refresh.
VLSI_MACHINE_REFRESH_FAILED|  This will be sent if a machine failed to be marked for refresh.

Show WSDL type definition







Removes the machine in the specified manual-type desktop. Requires at least one of the listed privileges.

Privileges

Privilege |  Description
---|---
POOL_MANAGEMENT|  Desktop management with the corresponding access group permission is required to remove a machine.
MACHINE_MANAGEMENT|  Machine management with the corresponding access group permission is required to remove machines.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  unique identifier for a desktop entry
**machine**| [MachineId](vdi.entity.MachineId.md)|  machineId to remove. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service, but not the [VirtualMachine](vdi.utils.virtualcenter.VirtualMachine.md) or [RegisteredPhysicalMachine](vdi.resources.RegisteredPhysicalMachine.md) services.




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
VLSI_DESKTOP_MACHINE_REMOVED|  This will be sent if a machine was successfully removed from the desktop.
VLSI_DESKTOP_MACHINE_REMOVE_FAILED|  This will be sent if a machine could not be removed from the desktop.

Show WSDL type definition







Removes the machines in the specified manual-type desktop. Requires at least one of the listed privileges.

Privileges

Privilege |  Description
---|---
POOL_MANAGEMENT|  Desktop management with the corresponding access group permission is required to remove machines.
MACHINE_MANAGEMENT|  Machine management with the corresponding access group permission is required to remove machines.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  unique identifier for a desktop entry
**machines**| [MachineId[]](vdi.entity.MachineId.md)|  array of machineIds to remove. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service, but not the [VirtualMachine](vdi.utils.virtualcenter.VirtualMachine.md) or [RegisteredPhysicalMachine](vdi.resources.RegisteredPhysicalMachine.md) services.




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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if all operations were not successful, a PartialFailureFault will be thrown indicating which machines were successfully removed and which ones failed. The index of results in the PartialFailureFault correspond to the index of the original machine. The result entry will contain either be the original return type (on success) or an exception (on failure).
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_DESKTOP_MACHINE_REMOVED|  This will be sent if a machine was successfully removed from the desktop.
VLSI_DESKTOP_MACHINE_REMOVE_FAILED|  This will be sent if a machine could not be removed from the desktop.

Show WSDL type definition







Requests an update of the Image in the specified desktop. This marks the old image to be replaced by new image, which is performed asynchronously. Once the new image is successfully updated, all eligible machines in desktop would also be marked for update with new image, this operation is also performed asynchronously. [operation](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md#operation) must be NONE.
Same operation can also be used to reschedule an existing scheduled push image operation, if [operation](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md#operation) is SCHEDULE_PUSH_IMAGE and schedule has not triggered yet. In case of reschedule other than [startTime](vdi.resources.Desktop.PushImageSettings.md#startTime) all the parameters in [DesktopPushImageSpec](vdi.resources.Desktop.PushImageSpec.md) should be identical to previous [Desktop_SchedulePushImage](vdi.resources.Desktop.md#schedulePushImage) call.
This operation is applicable only to Instant clone engine sourced desktops.

Privileges

Privilege |  Description
---|---
POOL_SVI_IMAGE_MANAGEMENT|  Manage maintenance operations on Automated Desktops & Farms with the corresponding access group permission is required to pushImage.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  unique identifier for a desktop entry.
**spec**| [DesktopPushImageSpec](vdi.resources.Desktop.PushImageSpec.md)|  The specification for the pushImage operation.




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
VLSI_DESKTOP_PUSH_IMAGE_SCHEDULED|  This will be sent if the new image is successfully marked for update.
VLSI_DESKTOP_PUSH_IMAGE_SCHEDULE_FAILED|  This will be sent if the new image failed to be marked for update.
VLSI_MACHINE_PUSH_IMAGE_FAILED|  This will be sent if a machine failed to be marked for update.

Show WSDL type definition







Update desktop with the set of attributes in the map.

Privileges

Privilege |  Description
---|---
POOL_MANAGEMENT|  Desktop management with the corresponding access group permission is required to update a desktop.
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to update the [globalEntitlementData](vdi.resources.Desktop.DesktopInfo.md#globalEntitlementData) members of a desktop.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  unique identifier for a desktop entry
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  key value pairs describing attributes to be updated [^108]





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
VLSI_DESKTOP_UPDATE_ATTEMPT|  This will be sent if an attempt to update the desktop was made successfully.
VLSI_DESKTOP_UPDATED|  If all members were successfully updated, this will be sent for each updated member in the update map.
VLSI_DESKTOP_UPDATE_FAILED|  If any member of the desktop could not be updated.

Show WSDL type definition







Validate that each application in the given list is installed on the machines belonging to the specified Pool.

Privileges

Privilege |  Description
---|---
POOL_VIEW|  privilege is required to validate installed Applications.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  The entityId of the Desktop on which to validate installed applications

**applicationExePaths**|  xsd:string[]|  Array of applicationExePaths for the applications to be validated




Return Value

Type |  Description
---|---
[DesktopMissingApplicationInstallationData[]](vdi.resources.Desktop.MissingApplicationInstallationData.md)| The list of MissingApplicationInstallationData *NOT INSTALLED* on the machines belonging to the Desktop.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Validates manually specified virtual machines. Ensures machine and user names are valid and aren't duplicated in the given desktop.

Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Desktop](vdi.resources.Desktop.md) used to make the method call.
**manualVirtualMachineDefinition**| [DesktopManualVirtualMachineDefinition](vdi.resources.Desktop.ManualVirtualMachineDefinition.md)|




Return Value

Type |  Description
---|---
[DesktopManualVirtualMachineData[]](vdi.resources.Desktop.ManualVirtualMachineData.md)| The ManualVirtualMachineData



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 


[^105]: License is not applied to the system.
[^106]: Applied license is expired.
[^107]: Applied license does not have instant clone feature enabled.
[^108]: This parameter is an update map based on [DesktopInfo](vdi.resources.Desktop.DesktopInfo.md 'DesktopInfo').
[^135]: This parameter need not be set.