---
layout: page
title: Data Object - ProcessPerformanceData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.helpdesk.Performance.ProcessPerformanceData`

Property of
> [PerformanceInfo](vdi.helpdesk.Performance.PerformanceInfo.md#field_detail)

Returned by
> [Performance_GetProcessPerformanceData](vdi.helpdesk.Performance.md#getProcessPerformanceData)

Since
> Horizon 7.2


## Data Object Description

The performance data for a process.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**cpu**|  xsd:double|  The cpu utilization. [^1] [^2]
**memory**|  xsd:double|  The memory utilization. [^1] [^2]
**disk**|  xsd:double|  The disk utilization. [^1] [^2]
**name**|  xsd:string|  The name of the process. [^2]
**processId**|  xsd:long|  The process id. [^2]
**createTime**|  xsd:long|  The process creation time. [^2]
**userName**|  xsd:string|  The owner of the process. [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.