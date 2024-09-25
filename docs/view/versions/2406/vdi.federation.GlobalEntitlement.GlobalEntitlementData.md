---
layout: page
title: Data Object - GlobalEntitlementData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.federation.GlobalEntitlement.GlobalEntitlementData
Property of
     [GlobalEntitlementInfo](vdi.federation.GlobalEntitlement.GlobalEntitlementInfo.md#field_detail)
See also
     [PodId](vdi.entity.PodId.md)
Since 
    Horizon View 6.0

## Data Object Description 

Data about members of Global Entitlement 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**localDesktopCount**|  xsd:int|  Count of desktops local to this pod that are associated with this Global Entitlement.   


[^2]

  
**remoteDesktopCount**|  xsd:int|  Count of desktops on remote pods that are associated with this Global Entitlement.   


[^2]

  
**userCount**|  xsd:int|  Count of users that are associated with this Global Entitlement. This value will be populated only in #get(GlobalEntitlementId).   


[^2]

  
**userGroupCount**|  xsd:int|  Count of users and groups that are associated with this Global Entitlement.   


[^2]

  
**userGroupSiteOverrideCount**|  xsd:int|  Count of all User Home Site overrides associated with this Global Entitlement (for either users or groups). This value will be populated only in #get(GlobalEntitlementId).   


[^2]

  
**memberPods**| [PodId[]](vdi.entity.PodId.md)|  Pods that have desktops associated with this Global Entitlement.   


[^1]
[^2]

  
  

  

