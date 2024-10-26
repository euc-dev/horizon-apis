---
layout: page
title: Data Object - PodAssignmentData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.federation.PodAssignment.PodAssignmentData`

Property of
> [PodAssignmentInfo](vdi.federation.PodAssignment.PodAssignmentInfo.md#field_detail)

See also
> [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md), [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md), [PodId](vdi.entity.PodId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0


## Data Object Description

Data about the pod assignment.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  The user id associated with this pod assignment. This will never be a group id. [^2]
**pod**| [PodId](vdi.entity.PodId.md)|  The pod id associated with this pod assignment. [^2]
**globalEntitlement**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  The global entitlement id associated with this pod assignment. Only one of [globalEntitlement](vdi.federation.PodAssignment.PodAssignmentData.md#globalEntitlement) and [globalApplicationEntitlement](vdi.federation.PodAssignment.PodAssignmentData.md#globalApplicationEntitlement) may be set. [^1] [^2]
**globalApplicationEntitlement**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  The global application entitlement id associated with this pod assignment. Only one of [globalEntitlement](vdi.federation.PodAssignment.PodAssignmentData.md#globalEntitlement) and [globalApplicationEntitlement](vdi.federation.PodAssignment.PodAssignmentData.md#globalApplicationEntitlement) may be set.  **_Since_** Horizon View 6.2 [^1] [^2]


 
