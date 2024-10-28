---
layout: page
title: Data Object - PermissionBase
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.Permission.PermissionBase`

Property of
> [PermissionInfo](vdi.users.Permission.PermissionInfo.md#field_detail)

Parameter to
> [Permission_Create](vdi.users.Permission.md#create), [Permission_CreatePermissions](vdi.users.Permission.md#createPermissions)

See also
> [AccessGroupId](vdi.entity.AccessGroupId.md), [RoleId](vdi.entity.RoleId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0


## Data Object Description

Base data used for permission creation.
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**userOrGroup**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  The user or group for this permission. [^2]
**role**| [RoleId](vdi.entity.RoleId.md)|  The role for this permission. [^2]
**accessGroup**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  The access group for this permission. If the role is not applicable to access groups, specify the root access group. [^2]


 


[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.