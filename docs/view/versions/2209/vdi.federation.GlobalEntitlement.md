---
layout: page
title: Service - GlobalEntitlement
hide:
#- navigation
- toc
---







Java Class
> `com.vmware.vdi.vlsi.binding.vdi.federation.GlobalEntitlement`

See also
> [DesktopId](vdi.entity.DesktopId.md), [GlobalEntitlementBase](vdi.federation.GlobalEntitlement.GlobalEntitlementBase.md), [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md), [GlobalEntitlementInfo](vdi.federation.GlobalEntitlement.GlobalEntitlementInfo.md), [GlobalEntitlementSummaryView](vdi.federation.GlobalEntitlement.GlobalEntitlementSummaryView.md), [MapEntry](vdi.util.MapEntry.md)

Since
> Horizon View 6.0





## Service Description

The Global Entitlement service interface.

Methods

Methods defined in this Service
---
GlobalEntitlement_AddDesktopsToGE, GlobalEntitlement_Create, GlobalEntitlement_Delete, GlobalEntitlement_Get, GlobalEntitlement_GetSummaryView, GlobalEntitlement_GetSummaryViews, GlobalEntitlement_ListCompatibleBackupGEs, GlobalEntitlement_RemoveDesktopsFromGE, GlobalEntitlement_Update




Add list of desktops to the Global Entitlement.

Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to update the [globalEntitlementData](vdi.resources.Desktop.DesktopInfo.md#globalEntitlementData) members of a desktop.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalEntitlement](vdi.federation.GlobalEntitlement.md) used to make the method call.
**id**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  unique identifier for Global Entitlement
**desktops**| [DesktopId[]](vdi.entity.DesktopId.md)|  Desktops to be added to the Global Entitlement




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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if all operations were not successful, a PartialFailureFault will be thrown indicating which desktops were successfully added and which ones failed. The index of results in the PartialFailureFault corresponds to the desktop's index in request. The result entry will contain either the original return type (on success) or an exception (on failure).
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_DESKTOP_UPDATE_ATTEMPT|  For every Desktop, if an attempt to update the desktop was made successfully
VLSI_DESKTOP_UPDATED|  For every Desktop, if a desktop is successfully updated.
VLSI_DESKTOP_UPDATE_FAILED|  For every Desktop that could not be updated.

Show WSDL type definition







Creates a Global Entitlement. Global entitlements are used to route users to their resources across multiple pods. These are persisted in a global ldap instance that is replicated across all pods in a linked mode view set.


Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to create a global entitlement.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalEntitlement](vdi.federation.GlobalEntitlement.md) used to make the method call.
**base**| [GlobalEntitlementBase](vdi.federation.GlobalEntitlement.GlobalEntitlementBase.md)|  attributes required to create a Global Entitlement




Return Value

Type |  Description
---|---
[GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)| unique identifier for Global Entitlement



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if this pod is not part of a Pod Federation
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_GE_ADDED|  If the global entitlement was successfully created.
VLSI_GE_ADD_FAILED|  If the global entitlement could not be created.

Show WSDL type definition







Deletes a Global Entitlement.

Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to delete a global entitlement.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalEntitlement](vdi.federation.GlobalEntitlement.md) used to make the method call.
**id**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  unique identifier for Global Entitlement to be deleted




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
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if Global Entitlement is active and has resources associated with it in any pod.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the Pod Federation has not been initialized.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_GE_DELETED|  If the global entitlement was successfully deleted.
VLSI_GE_DELETE_FAILED|  If the global entitlement could not be deleted.

Show WSDL type definition







Returns Global Entitlement corresponding to a specific Global Entitlement id.

Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read a global entitlement.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalEntitlement](vdi.federation.GlobalEntitlement.md) used to make the method call.
**id**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  unique identifier for Global Entitlement




Return Value

Type |  Description
---|---
[GlobalEntitlementInfo](vdi.federation.GlobalEntitlement.GlobalEntitlementInfo.md)| Global entitlement info



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if this pod is not part of a Pod Federation
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Returns Global Entitlement summary corresponding to a specific Global Entitlement id.

Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read a global entitlement.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalEntitlement](vdi.federation.GlobalEntitlement.md) used to make the method call.
**id**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  unique identifier for Global Entitlement




Return Value

Type |  Description
---|---
[GlobalEntitlementSummaryView](vdi.federation.GlobalEntitlement.GlobalEntitlementSummaryView.md)| Global entitlement summary view



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if this pod is not part of a Pod Federation
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Returns Global Entitlement summaries corresponding to the specific Global Entitlement ids.

Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read a global entitlements.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalEntitlement](vdi.federation.GlobalEntitlement.md) used to make the method call.
**ids**| [GlobalEntitlementId[]](vdi.entity.GlobalEntitlementId.md)|  unique identifiers for Global Entitlements




Return Value

Type |  Description
---|---
[GlobalEntitlementSummaryView[]](vdi.federation.GlobalEntitlement.GlobalEntitlementSummaryView.md)| Global entitlement summary views



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if this pod is not part of a Pod Federation
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Lists the Global Entitlements that can be associated as backup Global Entitlement.

Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read a global entitlement.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalEntitlement](vdi.federation.GlobalEntitlement.md) used to make the method call.
**id**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  unique identifier for Global Entitlement




Return Value

Type |  Description
---|---
[GlobalEntitlementInfo[]](vdi.federation.GlobalEntitlement.GlobalEntitlementInfo.md)|



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Remove the specified desktops from the Global Entitlement.

Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to update the [globalEntitlementData](vdi.resources.Desktop.DesktopInfo.md#globalEntitlementData) members of a desktop.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalEntitlement](vdi.federation.GlobalEntitlement.md) used to make the method call.
**id**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  unique identifier for Global Entitlement
**desktops**| [DesktopId[]](vdi.entity.DesktopId.md)|  Desktops to be removed from the Global Entitlement




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
VLSI_DESKTOP_UPDATE_ATTEMPT|  For every Desktop, if an attempt to update the desktop was made successfully.
VLSI_DESKTOP_UPDATED|  For every Desktop, if a desktop is successfully updated.
VLSI_DESKTOP_UPDATE_FAILED|  For every Desktop that could not be updated.

Show WSDL type definition







Updates Global Entitlement with the set of attributes in the map.


Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to update a global entitlement.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalEntitlement](vdi.federation.GlobalEntitlement.md) used to make the method call.
**id**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  unique identifier for Global Entitlement to be updated
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  key value pairs describing attributes to be updated [^229]





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
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if the update map contains invalid or non-permitted fields
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the Pod Federation has not been initialized.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_GE_CHANGED|  If the global entitlement was successfully updated.
VLSI_GE_CHANGE_FAILED|  If the global entitlement could not be updated.

Show WSDL type definition












 
