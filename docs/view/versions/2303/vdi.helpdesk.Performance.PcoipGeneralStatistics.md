---
layout: page
title: Data Object - PcoipGeneralStatistics
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.helpdesk.Performance.PcoipGeneralStatistics`

Property of
> [PcoipPerformanceData](vdi.helpdesk.Performance.PcoipPerformanceData.md#field_detail)

Since
> Horizon 7.2


## Data Object Description

The general statistics about PCoIP session.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**durationSeconds**|  xsd:long|  Total number of seconds that the PCoIP session has been open. [^1] [^2]
**bytesReceived**|  xsd:long|  Total number of bytes of PCoIP data that have been received since the PCoIP session started. [^1] [^2]
**bytesSent**|  xsd:long|  Total number of bytes of PCoIP data that have been transmitted since the PCoIP session started. [^1] [^2]
**packetsReceived**|  xsd:long|  Total number of packets that have been received successfully since the PCoIP session started. Not all packets are the same size. [^1] [^2]
**packetsSent**|  xsd:long|  Total number of packets that have been transmitted since the PCoIP session started. Not all packets are the same size. [^1] [^2]
**rxPacketsLost**|  xsd:long|  Total number of received packets that have been lost since the PCoIP session started. [^1] [^2]
**txPacketsLost**|  xsd:long|  Total number of transmitted packets that have been lost since the PCoIP session started. [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.