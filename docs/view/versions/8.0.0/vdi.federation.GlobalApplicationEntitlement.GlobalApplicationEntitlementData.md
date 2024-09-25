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


[^2]

  
**remoteApplicationCount**|  xsd:int|  Count of Applications on remote pods that are associated with this Global Application Entitlement.   


[^2]

  
**userCount**|  xsd:int|  Count of users that are associated with this Global Application Entitlement.   


[^2]

  
**userGroupCount**|  xsd:int|  Count of user groups that are associated with this Global Application Entitlement.   


[^2]

  
**userGroupSiteOverrideCount**|  xsd:int|  Count of all User Home Site overrides associated with this Global Application Entitlement (for either users or groups).   


[^2]

  
**memberPods**| [PodId[]](vdi.entity.PodId.md)|  Pods that have Applications associated with this Global Application Entitlement.   


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
