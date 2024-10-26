---
layout: page
title: Data Object - PermissionInfo
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.users.Permission.PermissionInfo`

Property of
> [AdminUserOrGroupView](vdi.users.AdminUserOrGroup.AdminUserOrGroupView.md#field_detail)

Returned by
> [Permission_Get](vdi.users.Permission.md#get), [Permission_GetInfos](vdi.users.Permission.md#getInfos), [Permission_List](vdi.users.Permission.md#list)

See also
> [PermissionBase](vdi.users.Permission.PermissionBase.md), [PermissionId](vdi.entity.PermissionId.md), [PermissionNamesData](vdi.users.Permission.PermissionNamesData.md)

Since
> Horizon View 6.0


## Data Object Description

The permission information.
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [PermissionId](vdi.entity.PermissionId.md)|  Permission ID of this entity. [^2]
**base**| [PermissionBase](vdi.users.Permission.PermissionBase.md)|  Base data used for permission creation. [^2]
**namesData**| [PermissionNamesData](vdi.users.Permission.PermissionNamesData.md)|  Names data of User, Role and AccessGroup involved in this permission.  **_Since_** Horizon 7.8 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.