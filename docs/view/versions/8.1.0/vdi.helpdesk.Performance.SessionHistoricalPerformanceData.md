---
layout: page
title: Data Object - SessionHistoricalPerformanceData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.helpdesk.Performance.SessionHistoricalPerformanceData`

See also
> [HistoricalPerformanceData](vdi.helpdesk.Performance.HistoricalPerformanceData.md), [SessionId](vdi.entity.SessionId.md)

Since
> Horizon 8.1


## Data Object Description

The historical performance data for overall machine.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**sessionId**| [SessionId](vdi.entity.SessionId.md)|  Session Id
**historicalPerformanceData**| [HistoricalPerformanceData[]](vdi.helpdesk.Performance.HistoricalPerformanceData.md)|  The historical performance data for overall machine. The value will be null if error occurs while retrieving the data. [^1]


 


[^1]: This property need not be set.