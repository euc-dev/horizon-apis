---
layout: page
title: Data Object - UserEntitlementInfo
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.users.UserEntitlement.UserEntitlementInfo`

Returned by
> [UserEntitlement_Get](vdi.users.UserEntitlement.md#get), [UserEntitlement_GetInfos](vdi.users.UserEntitlement.md#getInfos)

See also
> [UserEntitlementBase](vdi.users.UserEntitlement.UserEntitlementBase.md), [UserEntitlementId](vdi.entity.UserEntitlementId.md)

Since
> Horizon View 6.0


## Data Object Description

The root user entitlement information.
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [UserEntitlementId](vdi.entity.UserEntitlementId.md)|  User Entitlement ID of this entity. [^2]
**base**| [UserEntitlementBase](vdi.users.UserEntitlement.UserEntitlementBase.md)|  Base data used for user entitlement creation. [^2]


 


[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.