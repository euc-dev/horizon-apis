---
layout: page
title: Data Object - SessionGlobalReferenceData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.Session.SessionGlobalReferenceData`

Property of
> [SessionGlobalSummaryView](vdi.users.Session.SessionGlobalSummaryView.md#field_detail)

See also
> [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md), [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md), [PodId](vdi.entity.PodId.md), [SessionLocalReferenceData](vdi.users.Session.SessionLocalReferenceData.md), [SiteId](vdi.entity.SiteId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0


## Data Object Description

References to other objects in a global session.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User for this session.
**brokerUser**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User Id for the broker user associated with the session. [^1]
**globalEntitlement**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  Global entitlement Id for this session. Either globalEntitlement or globalApplicationEntitlements will be set but not both. [^1]
**globalApplicationEntitlement**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)| **Deprecated.**_use[globalApplicationEntitlements](vdi.users.Session.SessionGlobalReferenceData.md#globalApplicationEntitlements) instead _ Global application entitlement Id for this session  **_Since_** Horizon View 6.2 [^1]
**globalApplicationEntitlements**| [GlobalApplicationEntitlementId[]](vdi.entity.GlobalApplicationEntitlementId.md)|  The Global Application Entitlements that have been used to launch applications in this session. Either globalEntitlement or globalApplicationEntitlements will be set but not both.  **_Since_** Horizon 7.2 [^1]
**site**| [SiteId](vdi.entity.SiteId.md)|  Site Id of Pod where session landed.
**brokeringPod**| [PodId](vdi.entity.PodId.md)|  Pod Id of Pod where session was brokered. [^1]
**pod**| [PodId](vdi.entity.PodId.md)|  Pod Id of Pod where session was established. [^1]
**localReferenceData**| [SessionLocalReferenceData](vdi.users.Session.SessionLocalReferenceData.md)|  References to the local pod's object if this global session residing on the local pod. Unset if this session does not reside on the local pod. [^1]


 


[^1]: This property need not be set.