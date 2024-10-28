---
layout: page
title: Data Object - ApplicationDiscoveryData
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.resources.Application.ApplicationDiscoveryData`

Returned by
> [Desktop_DiscoverInstalledApplications](vdi.resources.Desktop.md#discoverInstalledApplications), [Farm_DiscoverInstalledApplications](vdi.resources.Farm.md#discoverInstalledApplications)

See also
> [ApplicationExecutionData](vdi.resources.Application.ApplicationExecutionData.md)

Since
> Horizon View 6.0


## Data Object Description

Application discovery data obtained from Broker.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**executionData**| [ApplicationExecutionData](vdi.resources.Application.ApplicationExecutionData.md)|  Application execution data, fetched during app. discovery.
**name**|  xsd:string|  Application name information, as sent by RDSServer during app. discovery. [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.