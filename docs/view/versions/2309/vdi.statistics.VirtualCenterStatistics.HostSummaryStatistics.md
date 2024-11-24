---
layout: page
title: Data Object - HostSummaryStatistics
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.statistics.VirtualCenterStatistics.HostSummaryStatistics`

Property of
> [VirtualCenterSummaryStatistics](vdi.statistics.VirtualCenterStatistics.VirtualCenterSummaryStatistics.md#field_detail)

Since
> Horizon 7.8


## Data Object Description

Statistics on a specific host managed by the Virtual Center server.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**name**|  xsd:string|  The name of the Virtual Center host. [^2]
**version**|  xsd:string|  The version of the Virtual Center host. [^1] [^2]
**status**|  xsd:string|  The status of the Virtual Center host. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>CONNECTED</td><td>The host is successfully connected to Virtual Center server.</td></tr><tr><td>DISCONNECTED</td><td>The host is disconnected from Virtual Center server.</td></tr><tr><td>NOT_RESPONDING</td><td>The host is not responding.</td></tr></table>
**numCpuCores**|  xsd:int|  Number of physical CPU cores on the host. [^1] [^2]
**cpuMhz**|  xsd:int|  CPU speed per core. This might be an averaged value if the speed is not uniform across all cores. The total CPU speed of the box is defined as cpuMhz * numCpuCores [^1] [^2]
**overallCpuUsage**|  xsd:int|  Aggregated CPU usage across all cores on the host, in MHz. [^1] [^2]
**memorySizeBytes**|  xsd:long|  The physical memory size, in bytes. [^1] [^2]
**overallMemoryUsageMB**|  xsd:int|  Physical memory usage on the host, in MBs. [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.