---
layout: page
title: Data Object - GlobalEntitlementInfo
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.federation.GlobalEntitlement.GlobalEntitlementInfo`

Returned by
> [GlobalEntitlement_Get](vdi.federation.GlobalEntitlement.md#get), [GlobalEntitlement_ListCompatibleBackupGEs](vdi.federation.GlobalEntitlement.md#listCompatibleBackupGEs)

See also
> [GlobalEntitlementBase](vdi.federation.GlobalEntitlement.GlobalEntitlementBase.md), [GlobalEntitlementData](vdi.federation.GlobalEntitlement.GlobalEntitlementData.md), [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)

Since
> Horizon View 6.0


## Data Object Description

Information about Global Entitlements.

##  Queryable Data Object

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService").

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  Identifier for Global Entitlement. [^2]
**base**| [GlobalEntitlementBase](vdi.federation.GlobalEntitlement.GlobalEntitlementBase.md)|  Global entitlement base data.
**data**| [GlobalEntitlementData](vdi.federation.GlobalEntitlement.GlobalEntitlementData.md)|  Data about members of Global entitlement. [^1] [^2]
**primaryGE**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  Indicates the Global Entitlement for which this Global Entitlement acts as backup.  **_Since_** Horizon 7.11 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.