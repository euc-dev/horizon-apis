---
layout: page
title: Service - ADUserOrGroup
hide:
#  - navigation
  - toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.users.ADUserOrGroup`

See also
> [ADGroupInfo](vdi.users.ADUserOrGroup.ADGroupInfo.md), [ADUserCredentialSpec](vdi.users.ADUserOrGroup.ADUserCredentialSpec.md), [ADUserOrGroupInfo](vdi.users.ADUserOrGroup.ADUserOrGroupInfo.md), [ADUserOrGroupSummaryView](vdi.users.ADUserOrGroup.ADUserOrGroupSummaryView.md), [ADUserOrGroupView](vdi.users.ADUserOrGroup.ADUserOrGroupView.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0





## Service Description

Data originated from Active Directory for a user or group.

**Methods**

Methods defined in this Service:
ADUserOrGroup_Get, ADUserOrGroup_GetEntitlementGroups, ADUserOrGroup_GetInfos, ADUserOrGroup_GetSummaryView, ADUserOrGroup_GetSummaryViews, ADUserOrGroup_GetView, ADUserOrGroup_GetViews, ADUserOrGroup_Refresh, ADUserOrGroup_RefreshUsersOrGroups, ADUserOrGroup_ValidateCredentials




Get an AD user or group info by ID.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ADUserOrGroup](vdi.users.ADUserOrGroup.md) used to make the method call.
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  UserOrGroupId of entity to get.




**Return Value**

Type | Description
:---|:---
[ADUserOrGroupInfo](vdi.users.ADUserOrGroup.ADUserOrGroupInfo.md)| requested user or group info.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Get ADGroupInfo that can be entitled for a given user by ID.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ADUserOrGroup](vdi.users.ADUserOrGroup.md) used to make the method call.
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  UserOrGroupId of entity to get.




**Return Value**

Type | Description
:---|:---
[ADGroupInfo[]](vdi.users.ADUserOrGroup.ADGroupInfo.md)| Array of ADGroupInfo that can be entitled for the user.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Get AD user or group infos by ids.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ADUserOrGroup](vdi.users.ADUserOrGroup.md) used to make the method call.
**ids**| [UserOrGroupId[]](vdi.entity.UserOrGroupId.md)|  UserOrGroupIds of entities to get.




**Return Value**

Type | Description
:---|:---
[ADUserOrGroupInfo[]](vdi.users.ADUserOrGroup.ADUserOrGroupInfo.md)| requested user or group infos.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Get an AD user or group summary view by ID.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ADUserOrGroup](vdi.users.ADUserOrGroup.md) used to make the method call.
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  UserOrGroupId of entity to get.




**Return Value**

Type | Description
:---|:---
[ADUserOrGroupSummaryView](vdi.users.ADUserOrGroup.ADUserOrGroupSummaryView.md)| requested user or group summary view.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Get AD user or group summary views by ids.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ADUserOrGroup](vdi.users.ADUserOrGroup.md) used to make the method call.
**ids**| [UserOrGroupId[]](vdi.entity.UserOrGroupId.md)|  UserOrGroupIds of entities to get.




**Return Value**

Type | Description
:---|:---
[ADUserOrGroupSummaryView[]](vdi.users.ADUserOrGroup.ADUserOrGroupSummaryView.md)| requested user or group summary views.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Get an AD user or group full view by ID.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ADUserOrGroup](vdi.users.ADUserOrGroup.md) used to make the method call.
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  UserOrGroupId of entity to get.




**Return Value**

Type | Description
:---|:---
[ADUserOrGroupView](vdi.users.ADUserOrGroup.ADUserOrGroupView.md)| requested user or group full view.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Get AD user or group full views by ids.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ADUserOrGroup](vdi.users.ADUserOrGroup.md) used to make the method call.
**ids**| [UserOrGroupId[]](vdi.entity.UserOrGroupId.md)|  UserOrGroupIds of entities to get.




**Return Value**

Type | Description
:---|:---
[ADUserOrGroupView[]](vdi.users.ADUserOrGroup.ADUserOrGroupView.md)| requested user or group full views.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Refresh and return the given user or group with current general information from Active Directory (including name, phone, email, user name, and default Windows domain) for any entitled or admin user or group stored in LDAP FSPs. This information is cached by the broker, both locally and globally if Multi-DataCenter View is enabled. The latter will only be refreshed if permissions exist to modify global data. If the given user or group's domain is one-way trusted, the refresh for that user may occur asynchronously when that user next logs in. In those cases, the returned value will be null.

**Privileges**

Privilege | Description
:---|:---
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to update the user or group in global LDAP in addition to local LDAP.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ADUserOrGroup](vdi.users.ADUserOrGroup.md) used to make the method call.
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  UserOrGroupId of entities to refresh.




**Return Value**

Type | Description
:---|:---
[ADUserOrGroupSummaryView](vdi.users.ADUserOrGroup.ADUserOrGroupSummaryView.md)| The refreshed summary view of the user or group.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Refreshes the given users and/or groups with current general information from Active Directory (including name, phone, email, user name, and default Windows domain) for any entitled or admin user or group stored in LDAP FSPs. This information is cached by the broker, both locally and globally if Multi-DataCenter View is enabled. The latter will only be refreshed if permissions exist to modify global data.
If the given user or group's domain is one-way trusted, the refresh for that user may occur asynchronously when that user next logs in. In those cases, the returned value will be null.
If this method is invoked with null argument, it refreshes the FSP entries from local LDAP. In this case, refresh for the user will occur asynchronously when the user next logs in. So, the returned value will be null.

**Privileges**

Privilege | Description
:---|:---
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to update the user or group in global LDAP in addition to local LDAP.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ADUserOrGroup](vdi.users.ADUserOrGroup.md) used to make the method call.
**ids**| [UserOrGroupId[]](vdi.entity.UserOrGroupId.md)|  UserOrGroupIds of entities to refresh. [^135]





**Return Value**

Type | Description
:---|:---
[ADUserOrGroupSummaryView[]](vdi.users.ADUserOrGroup.ADUserOrGroupSummaryView.md)| Refreshed summary views of given users/groups.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Validate supplied credentials.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ADUserOrGroup](vdi.users.ADUserOrGroup.md) used to make the method call.
**adUserCredentialSpec**| [ADUserCredentialSpec](vdi.users.ADUserOrGroup.ADUserCredentialSpec.md)|




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

Show WSDL type definition












 


[^135]: This parameter need not be set.