---
layout: page
title: Data Object - DesktopCounter
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.health.Monitoring.DesktopCounter`

Returned by
> [Monitoring_GetDesktopCounters](vdi.health.Monitoring.md#getDesktopCounters)

See also
> [DesktopId](vdi.entity.DesktopId.md)

Since
> Horizon 7.11


## Data Object Description

The desktop counter.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [DesktopId](vdi.entity.DesktopId.md)|  Desktop ID. [^2]
**numMachines**|  xsd:int|  Maximum number of machines in the desktop. [^2]
**occupancy**|  xsd:int|  Represents the occupancy count for the desktop. [^239] [^240] [^2]
**connectedSessions**|  xsd:int|  Represents the number of connected sessions of the desktop. [^2]


 


[^2]: This property cannot be updated.
[^239]: For dedicated assignment desktop, it is the number of assigned machine count.
[^240]: For floating assignment desktop, it is the summation of the connected and disconnected sessions.