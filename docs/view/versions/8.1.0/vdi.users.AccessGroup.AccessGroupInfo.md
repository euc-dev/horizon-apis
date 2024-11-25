---
layout: page
title: Data Object - AccessGroupInfo
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.AccessGroup.AccessGroupInfo`

Property of
> [AccessGroupInfo](vdi.users.AccessGroup.AccessGroupInfo.md#field_detail), [AdminUserOrGroupView](vdi.users.AdminUserOrGroup.AdminUserOrGroupView.md#field_detail)

Returned by
> [AccessGroup_Get](vdi.users.AccessGroup.md#get), [AccessGroup_List](vdi.users.AccessGroup.md#list)

See also
> [AccessGroupBase](vdi.users.AccessGroup.AccessGroupBase.md), [AccessGroupData](vdi.users.AccessGroup.AccessGroupData.md), [AccessGroupId](vdi.entity.AccessGroupId.md),

Since
> Horizon View 6.0


## Data Object Description

The full access group information.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  Access group id of this entity. [^2]
**base**| [AccessGroupBase](vdi.users.AccessGroup.AccessGroupBase.md)|  Base data used for access group creation. [^2]
**data**| [AccessGroupData](vdi.users.AccessGroup.AccessGroupData.md)|  Readonly data about this access group. [^2]
**children**| [AccessGroupInfo[]](vdi.users.AccessGroup.AccessGroupInfo.md)|  An array of AccessGroupInfo for this access group children. [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.