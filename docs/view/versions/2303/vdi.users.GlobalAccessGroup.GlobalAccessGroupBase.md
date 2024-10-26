---
layout: page
title: Data Object - GlobalAccessGroupBase
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.users.GlobalAccessGroup.GlobalAccessGroupBase`

Property of
> [GlobalAccessGroupInfo](vdi.users.GlobalAccessGroup.GlobalAccessGroupInfo.md#field_detail)

Parameter to
> [GlobalAccessGroup_Create](vdi.users.GlobalAccessGroup.md#create)

See also
> [GlobalAccessGroupId](vdi.entity.GlobalAccessGroupId.md)

Since
> Horizon 8.2


## Data Object Description

Base data used for global access group creation.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**name**|  xsd:string|  The global access group name. [^2] [^3]
**description**|  xsd:string|  The global access group description. [^1] [^2] [^4]
**parent**| [GlobalAccessGroupId](vdi.entity.GlobalAccessGroupId.md)|  The GlobalAccessGroupId of the access group's parent. This is unset if this is the root access group. [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^3]: This property must contain only alphanumerics, spaces, underscores, and dashes. The maximum length is 32 characters.
[^4]: This property has a maximum length of 400 characters.