---
layout: page
title: Data Object - APIMetrics
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.Monitoring.APIMetrics`

Property of
> [APIMetricsInfo](vdi.health.Monitoring.APIMetricsInfo.md#field_detail)

See also
> [MethodMetrics](vdi.health.Monitoring.MethodMetrics.md)

Since
> Horizon 7.13


## Data Object Description

Information about how often the API has been invoked since server started.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**serviceName**|  xsd:string|  Name of the Service. [^2]
**methodMetrics**| [MethodMetrics[]](vdi.health.Monitoring.MethodMetrics.md)|  Method metrics. [^2]
 


 


[^2]: This property cannot be updated.