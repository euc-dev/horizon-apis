---
layout: page
title: Data Object - UserEntitlementBase
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.UserEntitlement.UserEntitlementBase`

Property of
> [UserEntitlementInfo](vdi.users.UserEntitlement.UserEntitlementInfo.md#field_detail)

Parameter to
> [UserEntitlement_Create](vdi.users.UserEntitlement.md#create), [UserEntitlement_CreateUserEntitlements](vdi.users.UserEntitlement.md#createUserEntitlements)

See also
> [EntityId](vdi.EntityId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0


## Data Object Description

Base data used for user entitlement creation.
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**userOrGroup**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  The user or group for this user entitlement. [^2]
**resource**| [EntityId](vdi.EntityId.md)|  The resource id for this user entitlement. The valid types of resource ids are: [^311] [^221] [^222] [^223] [^224] [^2]


 


[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.
[^221]: [DesktopId](vdi.entity.DesktopId.md).
[^222]: [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md).
[^223]: [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md).
[^224]: [URLRedirectionId](vdi.entity.URLRedirectionId.md).
[^311]: [ApplicationId](vdi.entity.ApplicationId.md).