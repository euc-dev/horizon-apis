---
layout: page
title: Data Object - AccessGroupData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.AccessGroup.AccessGroupData`

Property of
> [AccessGroupInfo](vdi.users.AccessGroup.AccessGroupInfo.md#field_detail)

See also
> [PermissionId](vdi.entity.PermissionId.md)

Since
> Horizon View 6.0


## Data Object Description

Readonly data about this access group.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**permissions**| [PermissionId[]](vdi.entity.PermissionId.md)|  Administrative permissions (user/group and role) for this access group. [^1]
**isDeletable**|  xsd:boolean|  If true, the access group can be deleted, else not. For root access group, the value will always be false.  **_Since_** Horizon 7.8 [^5] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^5]: This property has a default value of false.