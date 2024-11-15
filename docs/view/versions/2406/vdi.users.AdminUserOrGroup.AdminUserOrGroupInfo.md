---
layout: page
title: Data Object - AdminUserOrGroupInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.AdminUserOrGroup.AdminUserOrGroupInfo`

Property of
> [AdminUserOrGroupView](vdi.users.AdminUserOrGroup.AdminUserOrGroupView.md#field_detail)

Returned by
> [AdminUserOrGroup_Get](vdi.users.AdminUserOrGroup.md#get), [AdminUserOrGroup_List](vdi.users.AdminUserOrGroup.md#list)

See also
> [AdminUserOrGroupPermissionData](vdi.users.AdminUserOrGroup.AdminUserOrGroupPermissionData.md), [ADUserOrGroupBase](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0


## Data Object Description

The root administrator user or group information.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User or group ID of this entity. [^2]
**base**| [ADUserOrGroupBase](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md)|  Basic active directory data for a user or group. [^2]
**permissionData**| [AdminUserOrGroupPermissionData](vdi.users.AdminUserOrGroup.AdminUserOrGroupPermissionData.md)|  Administrative permission data relevant to this user or group. [^2]


 


[^2]: This property cannot be updated.