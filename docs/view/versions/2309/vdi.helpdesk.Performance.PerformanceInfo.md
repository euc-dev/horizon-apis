---
layout: page
title: Data Object - PerformanceInfo
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.helpdesk.Performance.PerformanceInfo`

Returned by
> [Performance_Get](vdi.helpdesk.Performance.md#get)

See also
> [DisplayProtocolPerformanceData](vdi.helpdesk.Performance.DisplayProtocolPerformanceData.md), [PerformanceData](vdi.helpdesk.Performance.PerformanceData.md), [ProcessPerformanceData](vdi.helpdesk.Performance.ProcessPerformanceData.md)

Since
> Horizon 7.2


## Data Object Description

Data used for representation of performance information.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**timestamp**|  xsd:long|  The time stamp when the last PerformanceData was obtained. [^2]
**overallPerformance**| [PerformanceData[]](vdi.helpdesk.Performance.PerformanceData.md)|  Overall performance data for a machine. [^2]
**processesPerformance**| [ProcessPerformanceData[]](vdi.helpdesk.Performance.ProcessPerformanceData.md)|  Performance data for processes in a machine. [^1] [^2]
**displayProtocolPerformance**| [DisplayProtocolPerformanceData[]](vdi.helpdesk.Performance.DisplayProtocolPerformanceData.md)|  Performance data for the current session display protocol. [^1] [^2]
 


 
