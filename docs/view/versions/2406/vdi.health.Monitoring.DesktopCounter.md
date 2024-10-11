---
layout: page
title: Data Object - DesktopCounter
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.health.Monitoring.DesktopCounter`

Returned by  
> [Monitoring_GetDesktopCounters](vdi.health.Monitoring.md#getDesktopCounters)

See also  
> [DesktopId](vdi.entity.DesktopId.md)

Since  
> Horizon 7.11


## Data Object Description 

The desktop counter. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [DesktopId](vdi.entity.DesktopId.md)|  Desktop ID.   


 * This property cannot be updated.

  
**numMachines**|  xsd:int|  Maximum number of machines in the desktop.   


 * This property cannot be updated.

  
**occupancy**|  xsd:int|  Represents the occupancy count for the desktop. 

  * For dedicated assignment desktop, it is the number of assigned machine count.
  * For floating assignment desktop, it is the summation of the connected and disconnected sessions.

  


 * This property cannot be updated.

  
**connectedSessions**|  xsd:int|  Represents the number of connected sessions of the desktop.   


 * This property cannot be updated.

  
  

  
