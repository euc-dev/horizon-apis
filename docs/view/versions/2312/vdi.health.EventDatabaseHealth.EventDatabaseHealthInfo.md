---
layout: page
title: Data Object - EventDatabaseHealthInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.EventDatabaseHealth.EventDatabaseHealthInfo  
Returned by
     [EventDatabaseHealth_Get](vdi.health.EventDatabaseHealth.md#get)  
See also
     [EventDatabaseHealthData](vdi.health.EventDatabaseHealth.EventDatabaseHealthData.md), [EventStatistics](vdi.health.EventDatabaseHealth.EventStatistics.md)  
Since 
    Horizon View 6.0

## Data Object Description 

The health of a database connection. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**configured**|  xsd:boolean|  Indicates whether an event database is configured.   
  
**data**| [EventDatabaseHealthData](vdi.health.EventDatabaseHealth.EventDatabaseHealthData.md)|  Information about the health of the event database   


 * This property need not be set.
  * This property is required if configured is set to true.

  
**eventStatistics**| [EventStatistics](vdi.health.EventDatabaseHealth.EventStatistics.md)|  Event statistics.  **_Since_** Horizon 7.9  


 * This property need not be set.
 * This property cannot be updated.

  
  
  
   
  
  

