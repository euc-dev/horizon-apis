---
layout: page
title: Data Object - SessionHistoricalPerformanceData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.helpdesk.Performance.SessionHistoricalPerformanceData`

See also  
> [HistoricalPerformanceData](vdi.helpdesk.Performance.HistoricalPerformanceData.md), [SessionId](vdi.entity.SessionId.md)

Since  
> Horizon 8.1


## Data Object Description 

The historical performance data for overall machine. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**sessionId**| [SessionId](vdi.entity.SessionId.md)|  Session Id   
  
**historicalPerformanceData**| [HistoricalPerformanceData[]](vdi.helpdesk.Performance.HistoricalPerformanceData.md)|  The historical performance data for overall machine. The value will be null if error occurs while retrieving the data.   


* This property need not be set.

  
**errorMsg**|  xsd:string|  The error encoutered if any in fetching session info for each session. This value will be populated only if an error has occured and will be null otherwise.  **_Since_** Horizon 8.2  


* This property need not be set.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
