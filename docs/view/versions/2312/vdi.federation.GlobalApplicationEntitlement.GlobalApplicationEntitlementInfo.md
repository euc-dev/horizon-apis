---
layout: page
title: Data Object - GlobalApplicationEntitlementInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementInfo  
Returned by
     [GlobalApplicationEntitlement_Get](vdi.federation.GlobalApplicationEntitlement.md#get), [GlobalEntitlement_ListCompatibleBackupGAEs](vdi.federation.GlobalApplicationEntitlement.md#listCompatibleBackupGAEs)  
See also
     [ApplicationIconId](vdi.entity.ApplicationIconId.md), [GlobalApplicationEntitlementBase](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementBase.md), [GlobalApplicationEntitlementData](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementData.md), [GlobalApplicationEntitlementExecutionData](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementExecutionData.md), [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)  
Since 
    Horizon View 6.2

## Data Object Description 

Information about Global Entitlements. 

##  Queryable Data Object 

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService"). 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  Identifier for Global Application Entitlement.   


 * This property cannot be updated.

  
**base**| [GlobalApplicationEntitlementBase](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementBase.md)|  Global Application Entitlement base data.   
  
**data**| [GlobalApplicationEntitlementData](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementData.md)|  Data about members of the Global Application Entitlement.   


 * This property cannot be updated.

  
**executionData**| [GlobalApplicationEntitlementExecutionData](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementExecutionData.md)|  Global Application Entitlement execution data.   
  
**icons**| [ApplicationIconId[]](vdi.entity.ApplicationIconId.md)|  Icons associated with the Global Application Entitlement   


 * This property need not be set.
  * This property is an unordered array of unique values.
 * This property cannot be updated.

  
**primaryGAE**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  Indicates the Global Application Entitlement for which this Global Application Entitlement acts as backup.  **_Since_** Horizon 7.11  


 * This property need not be set.
 * This property cannot be updated.

  
**refId**|  xsd:string|  Reference ID used for this Global Application Entitlement.  **_Since_** Horizon 8.1  


 * This property need not be set.
 * This property cannot be updated.

  
  
  
   
  
  

