---
layout: page
title: Data Object - GECounter
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.Monitoring.GECounter  
Returned by
     [Monitoring_GetGECounter](vdi.health.Monitoring.md#getGECounter)  
Since 
    Horizon View 6.0

## Data Object Description 

The Global entitlement counter. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**localCapacity**|  xsd:int|  Total of number of machines in each local desktop(s) belonging to the global entitlement.   


 * This property cannot be updated.

  
**localOccupancy**|  xsd:int|  Represents the occupied local desktop(s) belonging to the global entitlement. 

  * For dedicated assignments, it is the total number of assigned machine count. 
  * For floating assignments, it will be sum of all the connected and disconnected sessions. 

  


 * This property cannot be updated.

  
**localConnectedSessions**|  xsd:int|  Represents the number of connected sessions in local desktop(s) belonging to the global entitlement.   


 * This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

