---
layout: page
title: Data Object - GlobalApplicationEntitlementInfo
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementInfo`

Returned by
> [GlobalApplicationEntitlement_Get](vdi.federation.GlobalApplicationEntitlement.md#get), [GlobalEntitlement_ListCompatibleBackupGAEs](vdi.federation.GlobalApplicationEntitlement.md#listCompatibleBackupGAEs)

See also
> [ApplicationIconId](vdi.entity.ApplicationIconId.md), [GlobalApplicationEntitlementBase](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementBase.md), [GlobalApplicationEntitlementData](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementData.md), [GlobalApplicationEntitlementExecutionData](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementExecutionData.md), [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)

Since
> Horizon View 6.2


## Data Object Description

Information about Global Entitlements.

##  Queryable Data Object

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService").

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  Identifier for Global Application Entitlement. [^2]
**base**| [GlobalApplicationEntitlementBase](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementBase.md)|  Global Application Entitlement base data.
**data**| [GlobalApplicationEntitlementData](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementData.md)|  Data about members of the Global Application Entitlement. [^2]
**executionData**| [GlobalApplicationEntitlementExecutionData](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementExecutionData.md)|  Global Application Entitlement execution data.
**icons**| [ApplicationIconId[]](vdi.entity.ApplicationIconId.md)|  Icons associated with the Global Application Entitlement [^1] [^14] [^2]
**primaryGAE**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  Indicates the Global Application Entitlement for which this Global Application Entitlement acts as backup.  **_Since_** Horizon 7.11 [^1] [^2]
**refId**|  xsd:string|  Reference ID used for this Global Application Entitlement.  **_Since_** Horizon 8.1 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^14]: This property is an unordered array of unique values.