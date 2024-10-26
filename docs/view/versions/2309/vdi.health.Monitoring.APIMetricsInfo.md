---
layout: page
title: Data Object - APIMetricsInfo
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.health.Monitoring.APIMetricsInfo`

Returned by
> [Monitoring_GetAPIMetrics](vdi.health.Monitoring.md#getAPIMetrics)

See also
> [APIMetrics](vdi.health.Monitoring.APIMetrics.md), [ConnectionServerId](vdi.entity.ConnectionServerId.md)

Since
> Horizon 7.13


## Data Object Description

Represents the API metrics for the connection server. API metrics include the API name and the number of times the API is invoked since the server started.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [ConnectionServerId](vdi.entity.ConnectionServerId.md)|  Connection Server Id. [^2]
**hostName**|  xsd:string|  Fully qualified host name [^2]
**apiMetrics**| [APIMetrics[]](vdi.health.Monitoring.APIMetrics.md)|  Information on the frequency of the APIs. [^2]
 


 


[^2]: This property cannot be updated.