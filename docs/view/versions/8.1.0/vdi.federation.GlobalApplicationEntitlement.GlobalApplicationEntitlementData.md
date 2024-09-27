---
layout: page
title: Data Object - GlobalApplicationEntitlementData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementData  
Property of
     [GlobalApplicationEntitlementInfo](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementInfo.md#field_detail)  
See also
     [PodId](vdi.entity.PodId.md)  
Since 
    Horizon View 6.2

## Data Object Description 

Data about members of Global Application Entitlement 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**localApplicationCount**|  xsd:int|  Count of Applications local to this pod that are associated with this Global Application Entitlement.   


* This property cannot be updated.

  
**remoteApplicationCount**|  xsd:int|  Count of Applications on remote pods that are associated with this Global Application Entitlement.   


* This property cannot be updated.

  
**userCount**|  xsd:int|  Count of users that are associated with this Global Application Entitlement. This value will be populated only in #get(GlobalApplicationEntitlementId).   


* This property cannot be updated.

  
**userGroupCount**|  xsd:int|  Count of users and groups that are associated with this Global Application Entitlement.   


* This property cannot be updated.

  
**userGroupSiteOverrideCount**|  xsd:int|  Count of all User Home Site overrides associated with this Global Application Entitlement (for either users or groups). This value will be populated only in #get(GlobalApplicationEntitlementId).   


* This property cannot be updated.

  
**memberPods**| [PodId[]](vdi.entity.PodId.md)|  Pods that have Applications associated with this Global Application Entitlement.   


* This property need not be set.
* This property cannot be updated.

  
  
  
  
  
  

