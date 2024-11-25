---
layout: page
title: Data Object - SessionGatewayStatistics
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.statistics.SessionStatistics.SessionGatewayStatistics`

Property of
> [LocalSessionStatistics](vdi.statistics.SessionStatistics.LocalSessionStatistics.md#field_detail)

Since
> Horizon 7.7


## Data Object Description

Statistics for gateway location of sessions.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**numInternalGateways**|  xsd:int|  The number of sessions whose gateway location is internal. [^2]
**numExternalGateways**|  xsd:int|  The number of sessions whose gateway location is external. [^2]
**numUnknownGateways**|  xsd:int|  The number of sessions whose gateway location is unknown.If the agent of a session is not upgraded to required version, the gateway location is unknown, this number is for this type of sessions. [^2]
 


 


[^2]: This property cannot be updated.