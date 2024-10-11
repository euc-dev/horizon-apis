---
layout: page
title: Data Object - BlastPerformanceData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.helpdesk.Performance.BlastPerformanceData`

Property of  
> [DisplayProtocolPerformanceData](vdi.helpdesk.Performance.DisplayProtocolPerformanceData.md#field_detail)

See also  
> [BlastAudioStatistics](vdi.helpdesk.Performance.BlastAudioStatistics.md), [BlastCDRStatistics](vdi.helpdesk.Performance.BlastCDRStatistics.md), [BlastImagingStatistics](vdi.helpdesk.Performance.BlastImagingStatistics.md), [BlastSessionStatistics](vdi.helpdesk.Performance.BlastSessionStatistics.md)

Since  
> Horizon 7.2


## Data Object Description 

The BLAST protocol performance metrics. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**estimatedThroughput**|  xsd:long| **Deprecated.**_use #BlastSessionStatistics.bytesTransmitted instead of this estimatedThroughput._ Estimated throughput of BLAST data that have been received since the session started. The unit is kilobits.   


 * This property need not be set.
 * This property cannot be updated.

  
**estimatedFPS**|  xsd:long| **Deprecated.**_use #blastImagingStatistics.framesPerSecond instead of this estimatedFPS._ Estimated number of frames per second.   


 * This property need not be set.
 * This property cannot be updated.

  
**estimatedRTT**|  xsd:long| **Deprecated.**_use #BlastSessionStatistics.roundTripTime instead of this estimatedRTT._ Estimated round trip time in milliseconds between the server and the client.   


 * This property need not be set.
 * This property cannot be updated.

  
**estimatedBandwidth**|  xsd:long| **Deprecated.**_use #BlastSessionStatistics.bandwidthUplink instead of this estimatedRTT._ Estimated overall bandwidth averaged over the sampling period, in kilobits per second.   


 * This property need not be set.
 * This property cannot be updated.

  
**blastSessionStatistics**| [BlastSessionStatistics](vdi.helpdesk.Performance.BlastSessionStatistics.md)|  The session statistics about Blast protocol.  **_Since_** Horizon 7.3  


 * This property need not be set.
 * This property cannot be updated.

  
**blastImagingStatistics**| [BlastImagingStatistics](vdi.helpdesk.Performance.BlastImagingStatistics.md)|  The image statistics about Blast protocol.  **_Since_** Horizon 7.3  


 * This property need not be set.
 * This property cannot be updated.

  
**blastAudioStatistics**| [BlastAudioStatistics](vdi.helpdesk.Performance.BlastAudioStatistics.md)|  The audio statistics about Blast protocol.  **_Since_** Horizon 7.3  


 * This property need not be set.
 * This property cannot be updated.

  
**blastCDRStatistics**| [BlastCDRStatistics](vdi.helpdesk.Performance.BlastCDRStatistics.md)|  The CDR statistics about Blast protocol.  **_Since_** Horizon 7.3  


 * This property need not be set.
 * This property cannot be updated.

  
  

  
