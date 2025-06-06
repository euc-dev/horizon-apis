---
layout: page
title: Data Object - GlobalApplicationEntitlementExecutionData
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementExecutionData`

Property of
> [GlobalApplicationEntitlementInfo](vdi.federation.GlobalApplicationEntitlement.GlobalApplicationEntitlementInfo.md#field_detail)

Since
> Horizon View 6.2


## Data Object Description

Global Application Entitlement execution data These attributes are automatically populated when the first Application is assigned to the GlobalApplicationEntitlement and automatically cleared when the last Application is unassigned.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**executablePath**|  xsd:string|  Path to Application executable. [^1]
**publisher**|  xsd:string|  Application publisher [^1]
**version**|  xsd:string|  Application version [^1]


 


[^1]: This property need not be set.