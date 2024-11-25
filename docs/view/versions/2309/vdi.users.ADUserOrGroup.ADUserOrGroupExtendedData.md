---
layout: page
title: Data Object - ADUserOrGroupExtendedData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.ADUserOrGroup.ADUserOrGroupExtendedData`

Property of
> [ADUserOrGroupInfo](vdi.users.ADUserOrGroup.ADUserOrGroupInfo.md#field_detail), [ADUserOrGroupView](vdi.users.ADUserOrGroup.ADUserOrGroupView.md#field_detail)

See also
> [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0


## Data Object Description

Computed data about this user or group.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**groupMemberships**| [UserOrGroupId[]](vdi.entity.UserOrGroupId.md)|  The groups this user or group belongs to, or null if none. [^1] [^2]
**userCount**|  xsd:int|  Number of users in this group within this domain, or 0 if not a group. [^2]
**subgroupCount**|  xsd:int|  Number of subgroups in this group within this domain, or 0 if not a group. [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.