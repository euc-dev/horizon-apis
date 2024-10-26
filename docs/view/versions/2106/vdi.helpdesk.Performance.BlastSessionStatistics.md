---
layout: page
title: Data Object - BlastSessionStatistics
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.helpdesk.Performance.BlastSessionStatistics`

Property of
> [BlastPerformanceData](vdi.helpdesk.Performance.BlastPerformanceData.md#field_detail)

Since
> Horizon 7.3


## Data Object Description

The session related statistics for Blast protocol.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**roundTripTime**|  xsd:long|  The round trip time in milliseconds between the server and the client. [^1] [^2]
**bandwidthUplink**|  xsd:long|  Uplink bandwidth averaged over the sampling period, in kilobits per second. [^1] [^2]
**packetLossUplink**|  xsd:long|  Network packet loss for uplink. [^1] [^2]
**bytesTransmitted**|  xsd:long|  Transmitted bytes on the connection. [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.