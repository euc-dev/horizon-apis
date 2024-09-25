---
layout: page
title: Data Object - RemoteApplicationStatistics
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.helpdesk.Performance.RemoteApplicationStatistics
Returned by
     [Performance_GetRemoteApplicationPerformanceData](vdi.helpdesk.Performance.md#getRemoteApplicationPerformanceData), [Performance_GetRemoteApplicationStatistics](vdi.helpdesk.Performance.md#getRemoteApplicationStatistics)
Since 
    Horizon 7.3

## Data Object Description 

The performance data for a remote application running on any virtual desktop. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**applicationId**|  xsd:string|  The identity of an application.  **_Since_** Horizon 7.6  


[^2]

  
**processId**|  xsd:long|  The process Id.   


[^2]

  
**name**|  xsd:string|  The name of a remote application.   


[^2]

  
**status**|  xsd:string|  The status of a remote application.   


[^1]
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"RUNNING"| The remote application is working properly.  
"NOT_RESPONDING"| The remote application is not responding.  
"UNKNOWN"| The status of the remote application is not known.  

  
**description**|  xsd:string|  The description of a remote application.   


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

