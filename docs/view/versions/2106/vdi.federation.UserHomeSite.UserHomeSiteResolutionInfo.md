---
layout: page
title: Data Object - UserHomeSiteResolutionInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.federation.UserHomeSite.UserHomeSiteResolutionInfo`

Returned by  
> [UserHomeSite_ResolveHomeSites](vdi.federation.UserHomeSite.md#resolveHomeSites)

See also  
> [EntityId](vdi.EntityId.md), [UserHomeSiteResolutionData](vdi.federation.UserHomeSite.UserHomeSiteResolutionData.md)

Since  
> Horizon 7.8


## Data Object Description 

The User home site resolution info class. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**globalEntitlement**| [EntityId](vdi.EntityId.md)|  The resource id this home site resolution is for. The valid types of resource ids are: 

  * [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)
  * [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)

  


* This property cannot be updated.

  
**globalEntitlementName**|  xsd:string|  Name of the Global Entitlement or Global Application Entitlement.   


* This property cannot be updated.

  
**resolvedData**| [UserHomeSiteResolutionData[]](vdi.federation.UserHomeSite.UserHomeSiteResolutionData.md)|  User home site resolution data for the Global Entitlement or Global Application Entitlement.   


* This property cannot be updated.

  
  
  

  
  
