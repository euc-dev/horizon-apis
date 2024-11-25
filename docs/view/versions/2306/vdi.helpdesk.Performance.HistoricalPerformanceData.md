---
layout: page
title: Data Object - HistoricalPerformanceData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.helpdesk.Performance.HistoricalPerformanceData`

Property of
> [SessionHistoricalPerformanceData](vdi.helpdesk.Performance.SessionHistoricalPerformanceData.md#field_detail)

Returned by
> [Performance_GetHistoricalPerformanceData](vdi.helpdesk.Performance.md#getHistoricalPerformanceData)

Since
> Horizon 7.2


## Data Object Description

The historical performance data for overall machine.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**timestamp**|  xsd:long|  The timestamp for data collection time  **_Since_** Horizon 7.8 [^1] [^2]
**overallCpu**|  xsd:double|  The overall cpu utilization. [^1] [^2]
**overallMemory**|  xsd:double|  The overall memory utilization. [^1] [^2]
**cpu**|  xsd:double|  The cpu utilization. [^1] [^2]
**memory**|  xsd:double|  The memory utilization. [^1] [^2]
**latency**|  xsd:long|  The PCoIP/Blast protocol round trip latency. [^1] [^2]
**diskIops**|  xsd:long|  The disk average IOPS  **_Since_** Horizon 7.4 [^1] [^2]
**diskReadIops**|  xsd:long|  The disk read IO requests completed over a period of one second  **_Since_** Horizon 7.5 [^1] [^2]
**diskWriteIops**|  xsd:long|  The disk write IO requests completed over a period of one second  **_Since_** Horizon 7.5 [^1] [^2]
**diskLatency**|  xsd:long|  The disk average latency (ms)  **_Since_** Horizon 7.4 [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.