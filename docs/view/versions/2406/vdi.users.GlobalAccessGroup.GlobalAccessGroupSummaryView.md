---
layout: page
title: Data Object - GlobalAccessGroupSummaryView
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.users.GlobalAccessGroup.GlobalAccessGroupSummaryView`

Property of
> [GlobalAdminUserOrGroupPrivilegesInfo](vdi.users.AdminUserOrGroup.GlobalAdminUserOrGroupPrivilegesInfo.md#field_detail)

See also
> [GlobalAccessGroupId](vdi.entity.GlobalAccessGroupId.md)

Since
> Horizon 8.2


## Data Object Description

Global Access Group Summary View.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**name**|  xsd:string|  The global access group name. [^2] [^3]
**id**| [GlobalAccessGroupId](vdi.entity.GlobalAccessGroupId.md)|  The global access group id. [^2]


 


[^2]: This property cannot be updated.
[^3]: This property must contain only alphanumerics, spaces, underscores, and dashes. The maximum length is 32 characters.