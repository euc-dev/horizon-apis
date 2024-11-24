---
layout: page
title: Data Object - PcoipNetworkStatistics
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.helpdesk.Performance.PcoipNetworkStatistics`

Property of
> [PcoipPerformanceData](vdi.helpdesk.Performance.PcoipPerformanceData.md#field_detail)

Since
> Horizon 7.2


## Data Object Description

The network statistics about PCoIP session.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**roundTripLatency**|  xsd:long|  Round trip latency in milliseconds between the PCoIP server and the PCoIP client. [^1] [^2]
**rxBandwidth**|  xsd:long|  Overall bandwidth for incoming PCoIP packets averaged over the sampling period, in kilobits per second. [^1] [^2]
**rxBandwidthPeak**|  xsd:long|  Peak bandwidth in kilobits per second for incoming PCoIP packets over a one-second sampling period. [^1] [^2]
**rxPacketLoss**|  xsd:long|  Percentage of incoming packets lost during a sampling period. [^1] [^2]
**txBandwidth**|  xsd:long|  Overall bandwidth for outgoing PCoIP packets averaged over the sampling period, in kilobits per second. [^1] [^2]
**txBandwidthActiveLimit**|  xsd:long|  Estimated available network bandwidth in kilobits per second. This statistic is updated once per second. [^1] [^2]
**txBandwidthLimit**|  xsd:long|  Transmission bandwidth limit in kilobits per second for outgoing packets. <br>The limit is the minimum of the following values.  GPO bandwidth limit for the PCoIP client  GPO bandwidth limit for the PCoIP server  Bandwidth limit for the local network connection  Negotiated bandwidth limit for the Zero Client firmware based on encryption limits [^1] [^2]
**txPacketLoss**|  xsd:long|  Percentage of transmitted packets lost during a sampling period. [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.