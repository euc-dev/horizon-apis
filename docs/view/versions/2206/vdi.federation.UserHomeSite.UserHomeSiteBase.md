---
layout: page
title: Data Object - UserHomeSiteBase
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.federation.UserHomeSite.UserHomeSiteBase
Property of
     [UserHomeSiteInfo](vdi.federation.UserHomeSite.UserHomeSiteInfo.md#field_detail), [UserHomeSitesSpec](vdi.federation.UserHomeSite.UserHomeSitesSpec.md#field_detail)
Parameter to
     [UserHomeSite_Create](vdi.federation.UserHomeSite.md#create)
See also
     [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md), [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md), [SiteId](vdi.entity.SiteId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)
Since 
    Horizon View 6.0

## Data Object Description 

User home site base information. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**userOrGroup**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  The user or group for whom this is the home site.   


[^2]

  
**site**| [SiteId](vdi.entity.SiteId.md)|  Home Site Id   


[^2]

  
**globalEntitlement**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  If set, the specified site is the overriding home site for this GlobalEntitlement. If both globalEntitlement and globalApplicationEntitlement are unset, the specified site is the global configured home site.   


[^1]
[^2]

  
**globalApplicationEntitlement**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  If set, the specified site is the overriding home site for this GlobalApplicationEntitlement. If both globalEntitlement and globalApplicationEntitlement are unset, the specified site is the global configured home site.  **_Since_** Horizon View 6.2  


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
