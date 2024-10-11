---
layout: page
title: Data Object - SessionGlobalReferenceData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.users.Session.SessionGlobalReferenceData`

Property of  
> [SessionGlobalSummaryView](vdi.users.Session.SessionGlobalSummaryView.md#field_detail)

See also  
> [GlobalAccessGroupId](vdi.entity.GlobalAccessGroupId.md), [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md), [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md), [PodId](vdi.entity.PodId.md), [SessionLocalReferenceData](vdi.users.Session.SessionLocalReferenceData.md), [SiteId](vdi.entity.SiteId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since  
> Horizon View 6.0


## Data Object Description 

References to other objects in a global session. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User for this session.   
  
**brokerUser**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User Id for the broker user associated with the session.   


 * This property need not be set.

  
**globalEntitlement**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  Global entitlement Id for this session. Either globalEntitlement or globalApplicationEntitlements will be set but not both.   


 * This property need not be set.

  
**globalApplicationEntitlement**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)| **Deprecated.**_use[globalApplicationEntitlements](vdi.users.Session.SessionGlobalReferenceData.md#globalApplicationEntitlements) instead _ Global application entitlement Id for this session  **_Since_** Horizon View 6.2  


 * This property need not be set.

  
**globalApplicationEntitlements**| [GlobalApplicationEntitlementId[]](vdi.entity.GlobalApplicationEntitlementId.md)|  The Global Application Entitlements that have been used to launch applications in this session. Either globalEntitlement or globalApplicationEntitlements will be set but not both.  **_Since_** Horizon 7.2  


 * This property need not be set.

  
**globalAccessGroups**| [GlobalAccessGroupId[]](vdi.entity.GlobalAccessGroupId.md)|  Global access group(s) associated with this session. For a global desktop entitlement session, this is the global desktop entitlement's global access group. In case of global application entitlement session, this is global access groups of all the global application entitlements that have been used to launch applications in this session.  **_Since_** Horizon 8.2  


 * This property need not be set.

  
**site**| [SiteId](vdi.entity.SiteId.md)|  Site Id of Pod where session landed.   
  
**brokeringPod**| [PodId](vdi.entity.PodId.md)|  Pod Id of Pod where session was brokered.   


 * This property need not be set.

  
**pod**| [PodId](vdi.entity.PodId.md)|  Pod Id of Pod where session was established.   


 * This property need not be set.

  
**localReferenceData**| [SessionLocalReferenceData](vdi.users.Session.SessionLocalReferenceData.md)|  References to the local pod's object if this global session residing on the local pod. Unset if this session does not reside on the local pod.   


 * This property need not be set.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
