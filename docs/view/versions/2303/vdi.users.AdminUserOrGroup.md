---
layout: page
title: Service - AdminUserOrGroup
hide:
#  - navigation
  - toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.AdminUserOrGroup`

See also
> [AdminUserOrGroupInfo](vdi.users.AdminUserOrGroup.AdminUserOrGroupInfo.md), [AdminUserOrGroupLoginView](vdi.users.AdminUserOrGroup.AdminUserOrGroupLoginView.md), [AdminUserOrGroupView](vdi.users.AdminUserOrGroup.AdminUserOrGroupView.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0





## Service Description

Information about an administrator user or a group.

**Methods**

Methods defined in this Service:
AdminUserOrGroup_Get, AdminUserOrGroup_GetLoginView, AdminUserOrGroup_GetLoginViewById, AdminUserOrGroup_GetView, AdminUserOrGroup_List, AdminUserOrGroup_ListViews




Get an administrator user or group by ID.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_PERMISSION_VIEW|  Permission read access privilege is required to get admin user information.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [AdminUserOrGroup](vdi.users.AdminUserOrGroup.md) used to make the method call.
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  UserOrGroupId of entity to get.




**Return Value**

Type | Description
:---|:---
[AdminUserOrGroupInfo](vdi.users.AdminUserOrGroup.AdminUserOrGroupInfo.md)| requested user or group entity.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets login view of current loggedin user.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [AdminUserOrGroup](vdi.users.AdminUserOrGroup.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[AdminUserOrGroupLoginView](vdi.users.AdminUserOrGroup.AdminUserOrGroupLoginView.md)| login view of current loggedin user.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets login view by ID.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_PERMISSION_VIEW|  Permission read access privilege is required to get admin user information.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [AdminUserOrGroup](vdi.users.AdminUserOrGroup.md) used to make the method call.
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  UserOrGroupId of the user.




**Return Value**

Type | Description
:---|:---
[AdminUserOrGroupLoginView](vdi.users.AdminUserOrGroup.AdminUserOrGroupLoginView.md)| requested user login view.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Get an administrator user or group full view by ID. If this method is invoked without any argument, it will return the information related to current loggedin user.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_PERMISSION_VIEW|  Permission read access privilege is required to get admin user information.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [AdminUserOrGroup](vdi.users.AdminUserOrGroup.md) used to make the method call.
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  UserOrGroupId of entity to get. [^135]





**Return Value**

Type | Description
:---|:---
[AdminUserOrGroupView](vdi.users.AdminUserOrGroup.AdminUserOrGroupView.md)| requested user or group full view.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







List all users or groups used by the broker as administrators.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_PERMISSION_VIEW|  Permission read access privilege is required to get any admin user information.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [AdminUserOrGroup](vdi.users.AdminUserOrGroup.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[AdminUserOrGroupInfo[]](vdi.users.AdminUserOrGroup.AdminUserOrGroupInfo.md)| All admin user or group infos



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







List all users or group full views used by the broker as administrators.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_PERMISSION_VIEW|  Permission read access privilege is required to get any admin user information.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [AdminUserOrGroup](vdi.users.AdminUserOrGroup.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[AdminUserOrGroupView[]](vdi.users.AdminUserOrGroup.AdminUserOrGroupView.md)| All admin user or group full views



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 


[^135]: This parameter need not be set.