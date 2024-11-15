---
layout: page
title: Data Object - PcoipPerformanceData
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.helpdesk.Performance.PcoipPerformanceData`

Property of
> [DisplayProtocolPerformanceData](vdi.helpdesk.Performance.DisplayProtocolPerformanceData.md#field_detail)

See also
> [PcoipAudioStatistics](vdi.helpdesk.Performance.PcoipAudioStatistics.md), [PcoipGeneralStatistics](vdi.helpdesk.Performance.PcoipGeneralStatistics.md), [PcoipImagingStatistics](vdi.helpdesk.Performance.PcoipImagingStatistics.md), [PcoipNetworkStatistics](vdi.helpdesk.Performance.PcoipNetworkStatistics.md), [PcoipUSBStatistics](vdi.helpdesk.Performance.PcoipUSBStatistics.md)

Since
> Horizon 7.2


## Data Object Description

The PCoIP protocol performance metrics.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**pcoipGeneralStatistics**| [PcoipGeneralStatistics](vdi.helpdesk.Performance.PcoipGeneralStatistics.md)|  The general statistics about PCoIP session. [^1] [^2]
**pcoipNetworkStatistics**| [PcoipNetworkStatistics](vdi.helpdesk.Performance.PcoipNetworkStatistics.md)|  The network statistics about PCoIP session. [^1] [^2]
**pcoipUsbStatistics**| [PcoipUSBStatistics](vdi.helpdesk.Performance.PcoipUSBStatistics.md)|  The USB statistics about PCoIP session. [^1] [^2]
**pcoipAudioStatistics**| [PcoipAudioStatistics](vdi.helpdesk.Performance.PcoipAudioStatistics.md)|  The audio statistics about PCoIP session. [^1] [^2]
**pcoipImagingStatistics**| [PcoipImagingStatistics](vdi.helpdesk.Performance.PcoipImagingStatistics.md)|  The imaging statistics about PCoIP session. [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.