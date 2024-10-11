---
layout: page
title: Data Object - UserHomeSiteBase
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.federation.UserHomeSite.UserHomeSiteBase`

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

Properties

Name |  Type |  Description   
---|---|---  
**userOrGroup**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  The user or group for whom this is the home site.   


 * This property cannot be updated.

  
**site**| [SiteId](vdi.entity.SiteId.md)|  Home Site Id   


 * This property cannot be updated.

  
**globalEntitlement**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  If set, the specified site is the overriding home site for this GlobalEntitlement. If both globalEntitlement and globalApplicationEntitlement are unset, the specified site is the global configured home site.   


 * This property need not be set.
 * This property cannot be updated.

  
**globalApplicationEntitlement**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  If set, the specified site is the overriding home site for this GlobalApplicationEntitlement. If both globalEntitlement and globalApplicationEntitlement are unset, the specified site is the global configured home site.  **_Since_** Horizon View 6.2  


 * This property need not be set.
 * This property cannot be updated.

  
**useHomesiteForRedirection**|  xsd:boolean|  Determine whether the homesite can be used for redirection.  **_Since_** Horizon 8.13  


  * This property has a default value of false.
 * This property need not be set.

  
  

  
