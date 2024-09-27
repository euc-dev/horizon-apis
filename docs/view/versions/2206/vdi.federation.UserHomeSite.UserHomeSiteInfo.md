---
layout: page
title: Data Object - UserHomeSiteInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.federation.UserHomeSite.UserHomeSiteInfo  
Returned by
     [UserHomeSite_Get](vdi.federation.UserHomeSite.md#get), [UserHomeSite_GetInfos](vdi.federation.UserHomeSite.md#getInfos), [UserHomeSite_List](vdi.federation.UserHomeSite.md#list), [UserHomeSite_Resolve](vdi.federation.UserHomeSite.md#resolve), [UserHomeSite_ResolveForGAE](vdi.federation.UserHomeSite.md#resolveForGAE)  
See also
     [UserHomeSiteBase](vdi.federation.UserHomeSite.UserHomeSiteBase.md), [UserHomeSiteId](vdi.entity.UserHomeSiteId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

The User home site info class. 

##  Queryable Data Object 

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService"). 

The query for user home sites. 

Query Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_VIEW|  Global LDAP read access is required to query for UserHomeSites.   
  


## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [UserHomeSiteId](vdi.entity.UserHomeSiteId.md)|  Id of the user home site configuration   


* This property cannot be updated.

  
**base**| [UserHomeSiteBase](vdi.federation.UserHomeSite.UserHomeSiteBase.md)|  Base data for user home site configuration.   
  
**refId**|  xsd:string|  Reference ID used for this user home site.  **_Since_** Horizon 8.1  


* This property need not be set.
* This property cannot be updated.

  
  
  
 
  
  

