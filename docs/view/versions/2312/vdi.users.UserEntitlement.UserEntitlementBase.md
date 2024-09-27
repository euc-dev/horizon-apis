---
layout: page
title: Data Object - UserEntitlementBase
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.UserEntitlement.UserEntitlementBase  
Property of
     [UserEntitlementInfo](vdi.users.UserEntitlement.UserEntitlementInfo.md#field_detail)  
Parameter to
     [UserEntitlement_Create](vdi.users.UserEntitlement.md#create), [UserEntitlement_CreateUserEntitlements](vdi.users.UserEntitlement.md#createUserEntitlements)  
See also
     [EntityId](vdi.EntityId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Base data used for user entitlement creation. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**userOrGroup**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  The user or group for this user entitlement.   


 * This property cannot be updated.

  
**resource**| [EntityId](vdi.EntityId.md)|  The resource id for this user entitlement. The valid types of resource ids are: 

  * [ApplicationId](vdi.entity.ApplicationId.md)
  * [DesktopId](vdi.entity.DesktopId.md)
  * [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)
  * [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)
  * [URLRedirectionId](vdi.entity.URLRedirectionId.md)

  


 * This property cannot be updated.

  
  
  
   
  
  

