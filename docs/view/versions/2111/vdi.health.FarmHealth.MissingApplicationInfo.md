---
layout: page
title: Data Object - FarmHealthMissingApplicationInfo
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.health.FarmHealth.MissingApplicationInfo`

Property of
> [FarmHealthRDSServerHealthInfo](vdi.health.FarmHealth.RDSServerHealthInfo.md#field_detail)

See also
> [ApplicationId](vdi.entity.ApplicationId.md)

Since
> Horizon View 6.0


## Data Object Description

Missing Application Info representing Applications. Application health is collected only for those Applications that are enabled.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [ApplicationId](vdi.entity.ApplicationId.md)|  Application Entity Id [^2]
**name**|  xsd:string|  Application name [^2]
**executablePath**|  xsd:string|  Path to Application executable [^2]


 


[^2]: This property cannot be updated.