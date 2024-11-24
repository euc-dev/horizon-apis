---
layout: page
title: Service - Permission
hide:
#- navigation
- toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.Permission`

See also
> [PermissionBase](vdi.users.Permission.PermissionBase.md), [PermissionId](vdi.entity.PermissionId.md), [PermissionInfo](vdi.users.Permission.PermissionInfo.md)

Since
> Horizon View 6.0





## Service Description

Information about a permission. This represents a simple association between a single admin user, a single role (which may encompass multiple privileges), and a single access group. Admin users/groups, roles, and access groups may each be associated with multiple permissions.

**Methods**

Methods defined in this Service:
Permission_Create, Permission_CreatePermissions, Permission_Delete, Permission_DeletePermissions, Permission_Get, Permission_GetInfos, Permission_List




Add a permission that connects a user/group, role, and access group. delete/create should be used instead of update.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_PERMISSION_MANAGEMENT|  Permission management privilege is required to create a permission.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Permission](vdi.users.Permission.md) used to make the method call.
**base**| [PermissionBase](vdi.users.Permission.PermissionBase.md)|  attributes needed to add a permission




**Return Value**

Type | Description
:---|:---
[PermissionId](vdi.entity.PermissionId.md)| unique identifier



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
ADMIN_PERMISSION_ADDED|  Sent when a permission is successfully created.
ADMIN_PERMISSION_ADD_FAILED|  Sent when a permission fails to be created.

Show WSDL type definition







Create multiple admin permissions. If all creations were not successful, a PartialFailureFault will be thrown indicating which bases were successfully created and which failed. The index of results in the PartialFailureFault correspond to the index of the original base. The result entry will contain either be the original return type (on success) or an exception (on failure).

**Privileges**

Privilege | Description
:---|:---
GLOBAL_PERMISSION_MANAGEMENT|  Permission management privilege is required to create any permissions.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Permission](vdi.users.Permission.md) used to make the method call.
**bases**| [PermissionBase[]](vdi.users.Permission.PermissionBase.md)|  PermissionBases of entities to create.




**Return Value**

Type | Description
:---|:---
[PermissionId[]](vdi.entity.PermissionId.md)| The created permission ids



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if all operations were not successful, a PartialFailureFault will be thrown indicating which permissions were successfully created and which ones failed. The index of results in the PartialFailureFault correspond to the index of the original permission. The result entry will contain either the original return type (on success) or an exception (on failure).
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
ADMIN_PERMISSION_ADDED|  Sent for each permission that is successfully created.
ADMIN_PERMISSION_ADD_FAILED|  Sent for each permission that fails to be created.

Show WSDL type definition







Delete a given permission. delete/create should be used instead of update.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_PERMISSION_MANAGEMENT|  Permission management privilege is required to delete any permissions.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Permission](vdi.users.Permission.md) used to make the method call.
**id**| [PermissionId](vdi.entity.PermissionId.md)|  PermissionId of entity to delete.




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
ADMIN_PERMISSION_REMOVED|  Sent when a permission is successfully deleted.
ADMIN_PERMISSION_REMOVE_FAILED|  Sent when a permission fails to be deleted.

Show WSDL type definition







Delete multiple admin permissions. If all deletions were not successful, a PartialFailureFault will be thrown indicating which bases were successfully deleted and which failed. The index of results in the PartialFailureFault correspond to the index of the original base. The result entry will contain a fault if the deletion failed.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_PERMISSION_MANAGEMENT|  Permission management privilege is required to delete any permissions.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Permission](vdi.users.Permission.md) used to make the method call.
**ids**| [PermissionId[]](vdi.entity.PermissionId.md)|  PermissionIds of entities to delete.




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
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if all operations were not successful, a PartialFailureFault will be thrown indicating which permissions were successfully deleted and which ones failed. The index of results in the PartialFailureFault correspond to the index of the original permission. The result entry will contain either the original return type (on success) or an exception (on failure).
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
ADMIN_PERMISSION_REMOVED|  Sent for each permission that is successfully deleted.
ADMIN_PERMISSION_REMOVE_FAILED|  Sent for each permission that fails to be deleted.

Show WSDL type definition







Get a permission by Id.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_PERMISSION_VIEW|  Permission read access privilege is required to read any permissions.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Permission](vdi.users.Permission.md) used to make the method call.
**id**| [PermissionId](vdi.entity.PermissionId.md)|  PermissionId of entity to get.




**Return Value**

Type | Description
:---|:---
[PermissionInfo](vdi.users.Permission.PermissionInfo.md)| requested permission entity.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Get multiple permission by Id.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_PERMISSION_VIEW|  Permission read access privilege is required to read any permissions.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Permission](vdi.users.Permission.md) used to make the method call.
**ids**| [PermissionId[]](vdi.entity.PermissionId.md)|  PermissionIds of entities to get.




**Return Value**

Type | Description
:---|:---
[PermissionInfo[]](vdi.users.Permission.PermissionInfo.md)| requested permission entities.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







List all permissions.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_PERMISSION_VIEW|  Permission read access privilege is required to read any permissions.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Permission](vdi.users.Permission.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[PermissionInfo[]](vdi.users.Permission.PermissionInfo.md)| An array of permissions.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
