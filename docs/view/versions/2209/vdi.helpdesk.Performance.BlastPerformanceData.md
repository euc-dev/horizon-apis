---
layout: page
title: Data Object - BlastPerformanceData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.helpdesk.Performance.BlastPerformanceData`

Property of
> [DisplayProtocolPerformanceData](vdi.helpdesk.Performance.DisplayProtocolPerformanceData.md#field_detail)

See also
> [BlastAudioStatistics](vdi.helpdesk.Performance.BlastAudioStatistics.md), [BlastCDRStatistics](vdi.helpdesk.Performance.BlastCDRStatistics.md), [BlastImagingStatistics](vdi.helpdesk.Performance.BlastImagingStatistics.md), [BlastSessionStatistics](vdi.helpdesk.Performance.BlastSessionStatistics.md)

Since
> Horizon 7.2


## Data Object Description

The BLAST protocol performance metrics.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**estimatedThroughput**|  xsd:long| **Deprecated.**_use #BlastSessionStatistics.bytesTransmitted instead of this estimatedThroughput._ Estimated throughput of BLAST data that have been received since the session started. The unit is kilobits. [^1] [^2]
**estimatedFPS**|  xsd:long| **Deprecated.**_use #blastImagingStatistics.framesPerSecond instead of this estimatedFPS._ Estimated number of frames per second. [^1] [^2]
**estimatedRTT**|  xsd:long| **Deprecated.**_use #BlastSessionStatistics.roundTripTime instead of this estimatedRTT._ Estimated round trip time in milliseconds between the server and the client. [^1] [^2]
**estimatedBandwidth**|  xsd:long| **Deprecated.**_use #BlastSessionStatistics.bandwidthUplink instead of this estimatedRTT._ Estimated overall bandwidth averaged over the sampling period, in kilobits per second. [^1] [^2]
**blastSessionStatistics**| [BlastSessionStatistics](vdi.helpdesk.Performance.BlastSessionStatistics.md)|  The session statistics about Blast protocol.  **_Since_** Horizon 7.3 [^1] [^2]
**blastImagingStatistics**| [BlastImagingStatistics](vdi.helpdesk.Performance.BlastImagingStatistics.md)|  The image statistics about Blast protocol.  **_Since_** Horizon 7.3 [^1] [^2]
**blastAudioStatistics**| [BlastAudioStatistics](vdi.helpdesk.Performance.BlastAudioStatistics.md)|  The audio statistics about Blast protocol.  **_Since_** Horizon 7.3 [^1] [^2]
**blastCDRStatistics**| [BlastCDRStatistics](vdi.helpdesk.Performance.BlastCDRStatistics.md)|  The CDR statistics about Blast protocol.  **_Since_** Horizon 7.3 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.