---
layout: page
title: Data Object - VirtualCenterSummaryStatistics
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.statistics.VirtualCenterStatistics.VirtualCenterSummaryStatistics`

Returned by
> [VirtualCenterStatistics_getSummaryStatistics](vdi.statistics.VirtualCenterStatistics.md#getSummaryStatistics), [VirtualCenterStatistics_listSummaryStatistics](vdi.statistics.VirtualCenterStatistics.md#listSummaryStatistics)

See also
> [DataStoreSummaryStatistics](vdi.statistics.VirtualCenterStatistics.DataStoreSummaryStatistics.md), [HostSummaryStatistics](vdi.statistics.VirtualCenterStatistics.HostSummaryStatistics.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon 7.8


## Data Object Description

Summary statistics for a Virtual Center server.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  The ID of the virtual center server. [^2]
**name**|  xsd:string|  The name of the Virtual Center server. [^1] [^2]
**instanceUuid**|  xsd:string|  Virtual center instance uuid. [^1] [^2]
**version**|  xsd:string|  The version of the Virtual Center server. [^1] [^2]
**hostSummaryStatistics**| [HostSummaryStatistics[]](vdi.statistics.VirtualCenterStatistics.HostSummaryStatistics.md)|  Statistics information about each host managed by the Virtual Center server. [^1] [^2]
**dataStoreSummaryStatistics**| [DataStoreSummaryStatistics[]](vdi.statistics.VirtualCenterStatistics.DataStoreSummaryStatistics.md)|  Statistics information about each data store managed by the Virtual Center server. [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.