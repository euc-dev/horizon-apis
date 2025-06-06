---
layout: page
title: Data Object - ApplicationSummaryData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Application.ApplicationSummaryData`

Property of
> [ApplicationSummaryView](vdi.resources.Application.ApplicationSummaryView.md#field_detail)

See also
> [DesktopId](vdi.entity.DesktopId.md), [FarmId](vdi.entity.FarmId.md), [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)

Since
> Horizon 7.2


## Data Object Description

Application Summary Data

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**name**|  xsd:string|  Application name.
**displayName**|  xsd:string|  Application display name. [^1]
**description**|  xsd:string|  Application description. [^1]
**enabled**|  xsd:boolean|  Indicates if Application is enabled. [^1]
**version**|  xsd:string|  Application version. [^1]
**publisher**|  xsd:string|  Application publisher. [^1]
**farm**| [FarmId](vdi.entity.FarmId.md)|  Farm to which this Application is associated with. Either this or [desktop](vdi.resources.Application.ApplicationSummaryData.md#desktop) should be set. [^1]
**desktop**| [DesktopId](vdi.entity.DesktopId.md)|  Desktop to which this Application is associated with. Either this or [farm](vdi.resources.Application.ApplicationSummaryData.md#farm) should be set.  **_Since_** Horizon 7.9 [^1]
**globalApplicationEntitlement**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  Global Application Entitlement for this Application. This member will be null if not set or caller does not have global read permissions. [^1]


 


[^1]: This property need not be set.