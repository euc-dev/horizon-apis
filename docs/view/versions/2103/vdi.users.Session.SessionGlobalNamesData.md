---
layout: page
title: Data Object - SessionGlobalNamesData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.Session.SessionGlobalNamesData`

Property of
> [SessionGlobalSummaryView](vdi.users.Session.SessionGlobalSummaryView.md#field_detail)

See also
> [SessionNamesData](vdi.users.Session.SessionNamesData.md)

Since
> Horizon View 6.0


## Data Object Description

Names of objects that reside in a global session.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**baseNames**| [SessionNamesData](vdi.users.Session.SessionNamesData.md)|  Names of objects for a basic session.
**entitlementName**|  xsd:string|  Global Entitlement for this session. [^1]
**applicationEntitlementNames**|  xsd:string[]|  Global Application Entitlements for this session.  **_Since_** Horizon 7.2 [^1]
**siteName**|  xsd:string|  Site for this session. [^1]
**brokeringPodName**|  xsd:string|  Brokering Pod for this session. [^1]
**podName**|  xsd:string|  Pod for this session. [^1]


 


[^1]: This property need not be set.