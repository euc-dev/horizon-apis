---
layout: page
title: Data Object - PcoipImagingStatistics
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.helpdesk.Performance.PcoipImagingStatistics`

Property of
> [PcoipPerformanceData](vdi.helpdesk.Performance.PcoipPerformanceData.md#field_detail)

Since
> Horizon 7.2


## Data Object Description

The imaging statistics about PCoIP session.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**bytesReceived**|  xsd:long|  Total number of bytes of imaging data that have been received since the PCoIP session started. [^1] [^2]
**bytesSent**|  xsd:long|  Total number of bytes of imaging data that have been transmitted since the PCoIP session started. [^1] [^2]
**rxBandwidth**|  xsd:long|  Bandwidth for incoming imaging packets averaged over the sampling period. The unit is kbit/sec. [^1] [^2]
**txBandwidth**|  xsd:long|  Bandwidth for outgoing imaging packets averaged over the sampling period. The unit is kbit/sec. [^1] [^2]
**encodedFrames**|  xsd:long|  Number of imaging frames that were encoded over a one-second sampling period. [^1] [^2]
**activeMinimumQuality**|  xsd:long|  Lowest encoded quality value on a scale from 0 to 100. This statistic is updated once per second. This counter does not correspond to the GPO setting for minimum quality. [^1] [^2]
**decoderCapability**|  xsd:long|  Estimated processing capability of the imaging decoder in kilobits per second. This statistic is updated once per second. [^1] [^2]
**megapixel**|  xsd:long|  Number of megapixel that were rendered over a one-second sampling period. [^1] [^2]
**svgaDevTapFrames**|  xsd:long|  Number of frames that were processed in SVGA devtap over one-second sampling. [^1] [^2]
**negativeAcknowledgements**|  xsd:long|  Number of negative acknowledgements for incoming packets; [^1] [^2]
**apex2800Offload**|  xsd:long|  The number of times Apex2800 offloading is utilized over a one-second sampling period. [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.