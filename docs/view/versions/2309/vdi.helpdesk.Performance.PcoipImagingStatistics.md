---
layout: page
title: Data Object - PcoipImagingStatistics
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.helpdesk.Performance.PcoipImagingStatistics`

Property of  
> [PcoipPerformanceData](vdi.helpdesk.Performance.PcoipPerformanceData.md#field_detail)

Since  
> Horizon 7.2


## Data Object Description 

The imaging statistics about PCoIP session. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**bytesReceived**|  xsd:long|  Total number of bytes of imaging data that have been received since the PCoIP session started.   


 * This property need not be set.
 * This property cannot be updated.

  
**bytesSent**|  xsd:long|  Total number of bytes of imaging data that have been transmitted since the PCoIP session started.   


 * This property need not be set.
 * This property cannot be updated.

  
**rxBandwidth**|  xsd:long|  Bandwidth for incoming imaging packets averaged over the sampling period. The unit is kbit/sec.   


 * This property need not be set.
 * This property cannot be updated.

  
**txBandwidth**|  xsd:long|  Bandwidth for outgoing imaging packets averaged over the sampling period. The unit is kbit/sec.   


 * This property need not be set.
 * This property cannot be updated.

  
**encodedFrames**|  xsd:long|  Number of imaging frames that were encoded over a one-second sampling period.   


 * This property need not be set.
 * This property cannot be updated.

  
**activeMinimumQuality**|  xsd:long|  Lowest encoded quality value on a scale from 0 to 100. This statistic is updated once per second. This counter does not correspond to the GPO setting for minimum quality.   


 * This property need not be set.
 * This property cannot be updated.

  
**decoderCapability**|  xsd:long|  Estimated processing capability of the imaging decoder in kilobits per second. This statistic is updated once per second.   


 * This property need not be set.
 * This property cannot be updated.

  
**megapixel**|  xsd:long|  Number of megapixel that were rendered over a one-second sampling period.   


 * This property need not be set.
 * This property cannot be updated.

  
**svgaDevTapFrames**|  xsd:long|  Number of frames that were processed in SVGA devtap over one-second sampling.   


 * This property need not be set.
 * This property cannot be updated.

  
**negativeAcknowledgements**|  xsd:long|  Number of negative acknowledgements for incoming packets;   


 * This property need not be set.
 * This property cannot be updated.

  
**apex2800Offload**|  xsd:long|  The number of times Apex2800 offloading is utilized over a one-second sampling period.   


 * This property need not be set.
 * This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
