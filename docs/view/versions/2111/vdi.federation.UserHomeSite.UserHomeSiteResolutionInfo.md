---
layout: page
title: Data Object - UserHomeSiteResolutionInfo
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.federation.UserHomeSite.UserHomeSiteResolutionInfo`

Returned by
> [UserHomeSite_ResolveHomeSites](vdi.federation.UserHomeSite.md#resolveHomeSites)

See also
> [EntityId](vdi.EntityId.md), [UserHomeSiteResolutionData](vdi.federation.UserHomeSite.UserHomeSiteResolutionData.md)

Since
> Horizon 7.8


## Data Object Description

The User home site resolution info class.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**globalEntitlement**| [EntityId](vdi.EntityId.md)|  The resource id this home site resolution is for. The valid types of resource ids are: [^222] [^223] [^2]
**globalEntitlementName**|  xsd:string|  Name of the Global Entitlement or Global Application Entitlement. [^2]
**resolvedData**| [UserHomeSiteResolutionData[]](vdi.federation.UserHomeSite.UserHomeSiteResolutionData.md)|  User home site resolution data for the Global Entitlement or Global Application Entitlement. [^2]


 


[^2]: This property cannot be updated.
[^222]: [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md).
[^223]: [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md).