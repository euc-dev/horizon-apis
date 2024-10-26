---
layout: page
title: Data Object - GlobalEntitlementSummaryView
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.federation.GlobalEntitlement.GlobalEntitlementSummaryView`

Returned by
> [GlobalEntitlement_GetSummaryView](vdi.federation.GlobalEntitlement.md#getSummaryView), [GlobalEntitlement_GetSummaryViews](vdi.federation.GlobalEntitlement.md#getSummaryViews)

See also
> [GlobalEntitlementBase](vdi.federation.GlobalEntitlement.GlobalEntitlementBase.md), [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)

Since
> Horizon View 6.0


## Data Object Description

Summary information about Global Entitlements.

##  Queryable Data Object

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService").

Query Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_VIEW|  Global LDAP read access is required to query for GlobalEntitlementSummaryView.



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  Identifier for Global Entitlement. [^2]
**base**| [GlobalEntitlementBase](vdi.federation.GlobalEntitlement.GlobalEntitlementBase.md)|  Global entitlement base data. [^2]


 


[^2]: This property cannot be updated.