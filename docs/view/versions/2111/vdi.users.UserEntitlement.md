---
layout: page
title: Service - UserEntitlement
hide:
#  - navigation
  - toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.users.UserEntitlement`

See also
> [UserEntitlementBase](vdi.users.UserEntitlement.UserEntitlementBase.md), [UserEntitlementId](vdi.entity.UserEntitlementId.md), [UserEntitlementInfo](vdi.users.UserEntitlement.UserEntitlementInfo.md)

Since
> Horizon View 6.0





## Service Description

Information about a user entitlement. This represents a simple association between a single user/group and a resource that they can be assigned to.
Examples of associated resources are Desktops, Applications, GlobalEntitlements,GlobalApplicationEntitlements,or URLRedirection Settings.
Individual users/groups and resources may be associated with multiple user entitlements.
List operation is not supported - a list of entitlements can be obtained from the [EntitledUserOrGroup](vdi.users.EntitledUserOrGroup.md) service by specific resource reference.

**Methods**

Methods defined in this Service:
UserEntitlement_Create, UserEntitlement_CreateUserEntitlements, UserEntitlement_Delete, UserEntitlement_DeleteUserEntitlements, UserEntitlement_Get, UserEntitlement_GetInfos




Add a user entitlement that connects a user/group and a resource. delete/create should be used instead of update.

**Privileges**

Privilege | Description
:---|:---
POOL_ENTITLE|  If the specified resource is a desktop or application, an entitlement privilege on that resource and its access group is required to create a user entitlement.
FEDERATED_LDAP_MANAGE|  If the specified resource is a global entitlement or global application entitlement, Global LDAP management is required to create a user entitlement.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UserEntitlement](vdi.users.UserEntitlement.md) used to make the method call.
**base**| [UserEntitlementBase](vdi.users.UserEntitlement.UserEntitlementBase.md)|  attributes needed to add a user entitlement




**Return Value**

Type | Description
:---|:---
[UserEntitlementId](vdi.entity.UserEntitlementId.md)| The created user entitlement id



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
VLSI_DESKTOP_USER_ENTITLEMENT_ADDED|  If the specified resource is a desktop, sent when successfully creating a user entitlement.
VLSI_DESKTOP_USER_ENTITLEMENT_ADD_FAILED|  If the specified resource is a desktop, sent when a user entitlement failed to be created.
VLSI_APPLICATION_USER_ENTITLEMENT_ADDED|  If the specified resource is an application, sent when successfully creating a user entitlement.
VLSI_APPLICATION_USER_ENTITLEMENT_ADD_FAILED|  If the specified resource is an application, sent when a user entitlement failed to be created.
VLSI_GE_USER_ENTITLEMENT_ADDED|  If the specified resource is a global entitlement, sent when successfully creating a user entitlement.
VLSI_GE_USER_ENTITLEMENT_ADD_FAILED|  If the specified resource is a global entitlement, sent when a user entitlement failed to be created.

Show WSDL type definition







Add multiple user entitlements.
If all resources are the same desktop or application, either all specified user entitlements will exist upon return, or, on error, no new entitlements will be added.


**Privileges**

Privilege | Description
:---|:---
POOL_ENTITLE|  If a specified resource is a desktop or application, an entitlement privilege on that resource and its access group is required to create that user entitlement.
FEDERATED_LDAP_MANAGE|  If a specified resource is a global entitlement or global application entitlement, Global LDAP management is required to create that user entitlement.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UserEntitlement](vdi.users.UserEntitlement.md) used to make the method call.
**bases**| [UserEntitlementBase[]](vdi.users.UserEntitlement.UserEntitlementBase.md)|  array of user entitlement bases to create




**Return Value**

Type | Description
:---|:---
[UserEntitlementId[]](vdi.entity.UserEntitlementId.md)| The created user entitlement ids



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidRequest](vdi.fault.InvalidRequest.md)| When unauthenticated access users are entitled to Application Pools sourced from Desktops, entitlement fails with Invalid Request exception.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| On error, if all resources are not the same desktop or application, a PartialFailureFault will be thrown indicating which bases were successfully created and which failed. If all resources are the same desktop or application, this exception will contain at least one EntityAlreadyExists and no other exception types (all specified entitlements are now present, but some were already present). The index of results in the PartialFailureFault correspond to the index of the original base. The result entry will contain either be the normal return type (on success) or an exception (on failure).
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_DESKTOP_USER_ENTITLEMENT_ADDED|  If the specified resource is a desktop, sent for each successfully created user entitlement.
VLSI_DESKTOP_USER_ENTITLEMENT_ADD_FAILED|  If the specified resource is a desktop, sent for each user entitlement that failed to be created.
VLSI_APPLICATION_USER_ENTITLEMENT_ADDED|  If the specified resource is an application, sent for each successfully created user entitlement.
VLSI_APPLICATION_USER_ENTITLEMENT_ADD_FAILED|  If the specified resource is an application, sent for each user entitlement that failed to be created
VLSI_GE_USER_ENTITLEMENT_ADDED|  If the specified resource is a global entitlement, sent for each successfully created user entitlement.
VLSI_GE_USER_ENTITLEMENT_ADD_FAILED|  If the specified resource is a global entitlement, sent for each user entitlement that failed to be created.

Show WSDL type definition







Delete a given user entitlement. delete/create should be used instead of update.

**Privileges**

Privilege | Description
:---|:---
POOL_ENTITLE|  If the specified resource is a desktop or application, an entitlement privilege on that resource and its access group is required to delete the user entitlement.
FEDERATED_LDAP_MANAGE|  If the user entitlement's resource is a global entitlement or global application entitlement, Global LDAP management is required to delete the user entitlement.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UserEntitlement](vdi.users.UserEntitlement.md) used to make the method call.
**id**| [UserEntitlementId](vdi.entity.UserEntitlementId.md)|  UserEntitlementId of entity to delete.




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
VLSI_DESKTOP_USER_ENTITLEMENT_DELETED|  If the specified resource is a desktop, sent when successfully deleting a user entitlement.
VLSI_DESKTOP_USER_ENTITLEMENT_DELETE__FAILED|  If the specified resource is a desktop, sent when a user entitlement failed to be deleted.
VLSI_APPLICATION_USER_ENTITLEMENT_DELETED|  If the specified resource is an application, sent when successfully deleting a user entitlement.
VLSI_APPLICATION_USER_ENTITLEMENT_DELETE_FAILED|  If the specified resource is an application, sent when a user entitlement failed to be deleted.
VLSI_GE_USER_ENTITLEMENT_DELETED|  If the specified resource is a global entitlement, sent when successfully deleting a user entitlement.
VLSI_GE_USER_ENTITLEMENT_DELETE_FAILED|  If the specified resource is a global entitlement, sent when a user entitlement failed to be deleted.

Show WSDL type definition







Delete multiple user entitlements.
If all resources are the same desktop or application, either all user entitlements will be deleted, or, on error, none will.


**Privileges**

Privilege | Description
:---|:---
POOL_ENTITLE|  If any specified resource is a desktop or application, an entitlement privilege on that resource and its access group is required to delete that user entitlement.
FEDERATED_LDAP_MANAGE|  If a user entitlement's resource is a global entitlement or global application entitlement, Global LDAP management is required to delete that user entitlement.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UserEntitlement](vdi.users.UserEntitlement.md) used to make the method call.
**ids**| [UserEntitlementId[]](vdi.entity.UserEntitlementId.md)|  UserEntitlementIds of entities to delete.




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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| On error, if all resources are not the same desktop or application, a PartialFailureFault will be thrown indicating which bases were successfully deleted and which failed. If all resources are the same desktop or application, this exception will contain at least one EntityNotFound and no other exception types (all specified entitlements are now not present, but some were already not present). The index of results in the PartialFailureFault correspond to the index of the original base. The result entry will contain a fault on failure.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_DESKTOP_USER_ENTITLEMENT_DELETED|  If the specified resource is a desktop, sent for each successfully deleted user entitlement.
VLSI_DESKTOP_USER_ENTITLEMENT_DELETE_FAILED|  If the specified resource is a desktop, sent for each user entitlement that failed to be deleted.
VLSI_APPLICATION_USER_ENTITLEMENT_DELETED|  If the specified resource is an application, sent for each successfully deleted user entitlement.
VLSI_APPLICATION_USER_ENTITLEMENT_DELETE_FAILED|  If the specified resource is an application, sent for each user entitlement that failed to be deleted
VLSI_GE_USER_ENTITLEMENT_DELETED|  If the specified resource is a global entitlement, sent for each successfully deleted user entitlement.
VLSI_GE_USER_ENTITLEMENT_DELETE_FAILED|  If the specified resource is a global entitlement, sent for each user entitlement that failed to be deleted.

Show WSDL type definition







Get a user entitlement by Id.

**Privileges**

Privilege | Description
:---|:---
POOL_VIEW|  IF the user entitlement's resource is a desktop or application, a read privilege is required on that resource and its access group to read that user entitlement.
FEDERATED_LDAP_VIEW|  If the user entitlement's resource is a global entitlement or global application entitlement, Global LDAP read is required to read that user entitlement.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UserEntitlement](vdi.users.UserEntitlement.md) used to make the method call.
**id**| [UserEntitlementId](vdi.entity.UserEntitlementId.md)|  UserEntitlementId of entity to get.




**Return Value**

Type | Description
:---|:---
[UserEntitlementInfo](vdi.users.UserEntitlement.UserEntitlementInfo.md)| The user entitlement info



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Get multiple user entitlement by Id.

**Privileges**

Privilege | Description
:---|:---
POOL_VIEW|  If any user entitlement's resource is a desktop or application, a read privilege on that resource and its access group is required to read the user entitlements.
FEDERATED_LDAP_VIEW|  If any user entitlement's resource is a global entitlement or global application entitlement, Global LDAP read is required to read the user entitlements.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UserEntitlement](vdi.users.UserEntitlement.md) used to make the method call.
**ids**| [UserEntitlementId[]](vdi.entity.UserEntitlementId.md)|  UserEntitlementIds of entities to get.




**Return Value**

Type | Description
:---|:---
[UserEntitlementInfo[]](vdi.users.UserEntitlement.UserEntitlementInfo.md)| The user entitlement infos



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
