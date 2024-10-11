---
layout: page
title: Data Object - PcoipNetworkStatistics
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.helpdesk.Performance.PcoipNetworkStatistics`

Property of  
> [PcoipPerformanceData](vdi.helpdesk.Performance.PcoipPerformanceData.md#field_detail)

Since  
> Horizon 7.2


## Data Object Description 

The network statistics about PCoIP session. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**roundTripLatency**|  xsd:long|  Round trip latency in milliseconds between the PCoIP server and the PCoIP client.   


* This property need not be set.
* This property cannot be updated.

  
**rxBandwidth**|  xsd:long|  Overall bandwidth for incoming PCoIP packets averaged over the sampling period, in kilobits per second.   


* This property need not be set.
* This property cannot be updated.

  
**rxBandwidthPeak**|  xsd:long|  Peak bandwidth in kilobits per second for incoming PCoIP packets over a one-second sampling period.   


* This property need not be set.
* This property cannot be updated.

  
**rxPacketLoss**|  xsd:long|  Percentage of incoming packets lost during a sampling period.   


* This property need not be set.
* This property cannot be updated.

  
**txBandwidth**|  xsd:long|  Overall bandwidth for outgoing PCoIP packets averaged over the sampling period, in kilobits per second.   


* This property need not be set.
* This property cannot be updated.

  
**txBandwidthActiveLimit**|  xsd:long|  Estimated available network bandwidth in kilobits per second. This statistic is updated once per second.   


* This property need not be set.
* This property cannot be updated.

  
**txBandwidthLimit**|  xsd:long|  Transmission bandwidth limit in kilobits per second for outgoing packets. 

The limit is the minimum of the following values.  GPO bandwidth limit for the PCoIP client  GPO bandwidth limit for the PCoIP server  Bandwidth limit for the local network connection  Negotiated bandwidth limit for the Zero Client firmware based on encryption limits  
  


* This property need not be set.
* This property cannot be updated.

  
**txPacketLoss**|  xsd:long|  Percentage of transmitted packets lost during a sampling period.   


* This property need not be set.
* This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
