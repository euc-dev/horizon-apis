---
layout: page
title: Data Object - PcoipAudioStatistics
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.helpdesk.Performance.PcoipAudioStatistics`

Property of
> [PcoipPerformanceData](vdi.helpdesk.Performance.PcoipPerformanceData.md#field_detail)

Since
> Horizon 7.2


## Data Object Description

The audio statistics about PCoIP session.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**bytesReceived**|  xsd:long|  Total number of bytes of audio data that have been received since the PCoIP session started. [^1] [^2]
**bytesSent**|  xsd:long|  Total number of bytes of audio data that have been sent since the PCoIP session started. [^1] [^2]
**rxBandwidth**|  xsd:long|  Bandwidth for ingoing audio packets averaged over the sampling period, in kilobits per second. [^1] [^2]
**txBandwidth**|  xsd:long|  Bandwidth for outgoing audio packets averaged over the sampling period, in kilobits per second. [^1] [^2]
**txBandwidthLimit**|  xsd:long|  Transmission bandwidth limit in kilobits per second for outgoing audio packets. The limit is defined by a GPO setting. [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.