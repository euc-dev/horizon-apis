---
layout: page
title: Data Object - UserHomeSiteBase
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.federation.UserHomeSite.UserHomeSiteBase`

Property of
> [UserHomeSiteInfo](vdi.federation.UserHomeSite.UserHomeSiteInfo.md#field_detail), [UserHomeSitesSpec](vdi.federation.UserHomeSite.UserHomeSitesSpec.md#field_detail)

Parameter to
> [UserHomeSite_Create](vdi.federation.UserHomeSite.md#create)

See also
> [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md), [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md), [SiteId](vdi.entity.SiteId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0


## Data Object Description

User home site base information.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**userOrGroup**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  The user or group for whom this is the home site. [^2]
**site**| [SiteId](vdi.entity.SiteId.md)|  Home Site Id [^2]
**globalEntitlement**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  If set, the specified site is the overriding home site for this GlobalEntitlement. If both globalEntitlement and globalApplicationEntitlement are unset, the specified site is the global configured home site. [^1] [^2]
**globalApplicationEntitlement**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  If set, the specified site is the overriding home site for this GlobalApplicationEntitlement. If both globalEntitlement and globalApplicationEntitlement are unset, the specified site is the global configured home site.  **_Since_** Horizon View 6.2 [^1] [^2]
**useHomesiteForRedirection**|  xsd:boolean|  Determine whether the homesite can be used for redirection.  **_Since_** Horizon 8.13 [^5] [^1]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^5]: This property has a default value of false.