---
layout: page
title: Data Object - RoleInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.Role.RoleInfo`

Property of
> [AdminUserOrGroupView](vdi.users.AdminUserOrGroup.AdminUserOrGroupView.md#field_detail)

Returned by
> [Role_Get](vdi.users.Role.md#get), [Role_List](vdi.users.Role.md#list)

See also
> [RoleBase](vdi.users.Role.RoleBase.md), [RoleData](vdi.users.Role.RoleData.md), [RoleId](vdi.entity.RoleId.md)

Since
> Horizon View 6.0


## Data Object Description

The root role information.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [RoleId](vdi.entity.RoleId.md)|  Role ID of this entity. [^2]
**base**| [RoleBase](vdi.users.Role.RoleBase.md)|  Base data used for role creation.
**data**| [RoleData](vdi.users.Role.RoleData.md)|  Readonly data about this role. [^2]
**refId**|  xsd:string|  Reference ID for this role.  **_Since_** Horizon 8.6 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.