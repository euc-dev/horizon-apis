---
layout: page
title: Data Object - BlastImagingStatistics
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.helpdesk.Performance.BlastImagingStatistics`

Property of
> [BlastPerformanceData](vdi.helpdesk.Performance.BlastPerformanceData.md#field_detail)

Since
> Horizon 7.3


## Data Object Description

The imaging related statistics for Blast protocol.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**framesPerSecond**|  xsd:long|  Number of image frames per second. [^1] [^2]
**bytesReceived**|  xsd:long|  The number of bytes of imaging data that have been received. [^1] [^2]
**bytesTransmitted**|  xsd:long|  The number of bytes of imaging data that have been transmitted. [^1] [^2]
**encoderType**|  xsd:string|  The codec value for BlastPerformanceData  **_Since_** Horizon 8.7 [^1]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.