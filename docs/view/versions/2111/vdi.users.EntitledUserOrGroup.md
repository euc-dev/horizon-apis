---
layout: page
title: Service - EntitledUserOrGroup
hide:
#  - navigation
  - toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.users.EntitledUserOrGroup`

See also
> [EntitledUserOrGroupGlobalSummaryView](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupGlobalSummaryView.md), [EntitledUserOrGroupInfo](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupInfo.md), [EntitledUserOrGroupLocalSummaryView](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupLocalSummaryView.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0





## Service Description

Information about a User or a Group with resource entitlements.

**Methods**

Methods defined in this Service:
EntitledUserOrGroup_Get, EntitledUserOrGroup_GetGlobalSummaryView, EntitledUserOrGroup_GetGlobalSummaryViews, EntitledUserOrGroup_GetInfos, EntitledUserOrGroup_GetLocalSummaryView, EntitledUserOrGroup_GetLocalSummaryViews




Get an entitled user or group info by ID.

**Privileges**

Privilege | Description
:---|:---
POOL_VIEW|  Desktop or application read privileges in the corresponding access group are required to include results for those desktops or applications.
MACHINE_VIEW|  Machine read privileges in the corresponding access group are required to include results for those machines.
FEDERATED_SESSIONS_VIEW|  Federated session read privilege or one of the above on the corresponding folder is required to include session information for a machine.
FEDERATED_LDAP_VIEW|  Global LDAP read is required to access the [globalData](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupInfo.md#globalData) members.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [EntitledUserOrGroup](vdi.users.EntitledUserOrGroup.md) used to make the method call.
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  UserOrGroupId of entity to get.




**Return Value**

Type | Description
:---|:---
[EntitledUserOrGroupInfo](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupInfo.md)| requested user or group info.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Get an entitled user or group global summary view by ID.

**Privileges**

Privilege | Description
:---|:---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read a [EntitledUserOrGroupGlobalSummaryView](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupGlobalSummaryView.md).



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [EntitledUserOrGroup](vdi.users.EntitledUserOrGroup.md) used to make the method call.
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  UserOrGroupId of entity to get.




**Return Value**

Type | Description
:---|:---
[EntitledUserOrGroupGlobalSummaryView](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupGlobalSummaryView.md)| requested user or group global summary view.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the Pod Federation has not been initialized.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Get entitled user or group summary global views by ids.

**Privileges**

Privilege | Description
:---|:---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read multiple [EntitledUserOrGroupGlobalSummaryView](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupGlobalSummaryView.md).



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [EntitledUserOrGroup](vdi.users.EntitledUserOrGroup.md) used to make the method call.
**ids**| [UserOrGroupId[]](vdi.entity.UserOrGroupId.md)|  UserOrGroupIds of entities to get.




**Return Value**

Type | Description
:---|:---
[EntitledUserOrGroupGlobalSummaryView[]](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupGlobalSummaryView.md)| requested user or group global summary views.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the Pod Federation has not been initialized.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Get entitled user or group infos by ids.

**Privileges**

Privilege | Description
:---|:---
POOL_VIEW|  Desktop or application read privileges in the corresponding access group are required to include results for those desktops or applications.
MACHINE_VIEW|  Machine read privileges in the corresponding access group are required to include results for those machines.
FEDERATED_SESSIONS_VIEW|  Federated session read privilege or one of the above on the corresponding folder is required to include session information for a machine.
FEDERATED_LDAP_VIEW|  Global LDAP read is required to access the [globalData](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupInfo.md#globalData) members.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [EntitledUserOrGroup](vdi.users.EntitledUserOrGroup.md) used to make the method call.
**ids**| [UserOrGroupId[]](vdi.entity.UserOrGroupId.md)|  UserOrGroupIds of entities to get.




**Return Value**

Type | Description
:---|:---
[EntitledUserOrGroupInfo[]](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupInfo.md)| requested user or group infos.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Get an entitled user or group local summary view by ID.

**Privileges**

Privilege | Description
:---|:---
POOL_VIEW|  Desktop or application read privileges in the corresponding access group are required to include results for those desktops or applications.
MACHINE_VIEW|  Machine read privileges in the corresponding access group are required to include results for those machines.
FEDERATED_SESSIONS_VIEW|  Federated session read privilege or one of the above on the corresponding folder is required to include session information for a machine.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [EntitledUserOrGroup](vdi.users.EntitledUserOrGroup.md) used to make the method call.
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  UserOrGroupId of entity to get.




**Return Value**

Type | Description
:---|:---
[EntitledUserOrGroupLocalSummaryView](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupLocalSummaryView.md)| requested user or group local summary view.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Get entitled user or group local summary views by ids.

**Privileges**

Privilege | Description
:---|:---
POOL_VIEW|  Desktop or application read privileges in the corresponding access group are required to include results for those desktops or applications.
MACHINE_VIEW|  Machine read privileges in the corresponding access group are required to include results for those machines.
FEDERATED_SESSIONS_VIEW|  Federated session read privilege or one of the above on the corresponding folder is required to include session information for a machine.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [EntitledUserOrGroup](vdi.users.EntitledUserOrGroup.md) used to make the method call.
**ids**| [UserOrGroupId[]](vdi.entity.UserOrGroupId.md)|  UserOrGroupIds of entities to get.




**Return Value**

Type | Description
:---|:---
[EntitledUserOrGroupLocalSummaryView[]](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupLocalSummaryView.md)| requested user or group local summary views.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
