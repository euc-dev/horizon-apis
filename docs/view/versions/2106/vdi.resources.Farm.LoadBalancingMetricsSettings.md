---
layout: page
title: Data Object - RDSHLoadBalancingMetricsSettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Farm.LoadBalancingMetricsSettings  
Property of
     [RDSHLoadBalancingSettings](vdi.resources.Farm.LoadBalancingSettings.md#field_detail)  
Since 
    Horizon 7.8

## Data Object Description 

Load Balancing metrics 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**includeSessionCount**|  xsd:boolean|  Whether to include session count for load balancing. If #useCustomScript is false, by default session count will be used. It is true by default.   


  * This property has a default value of true.
* This property need not be set.

  
**cpuThreshold**|  xsd:int|  Represents threshold of CPU usage, in percentage. If the value is 0, then this metric will not be considered for load balancing.   


  * This property has a default value of 0.
* This property need not be set.
  * This property has a minimum value of 0. 
  * This property has a maximum value of 100. 

  
**memThreshold**|  xsd:int|  Represents threshold of memory usage, in percentage. If the value is 0, then this metric will not be considered for load balancing.   


  * This property has a default value of 0.
* This property need not be set.
  * This property has a minimum value of 0. 
  * This property has a maximum value of 100. 

  
**diskQueueLengthThreshold**|  xsd:int|  Represents the threshold of average number of both read and write requests that were queued for the selected disk during the sample interval. If the value is 0, then this metric will not be considered for load balancing.   


  * This property has a default value of 0.
* This property need not be set.
  * This property has a minimum value of 0. 

  
**diskReadLatencyThreshold**|  xsd:int|  Represents the threshold of average time, in milliseconds, of a read of data from the disk. If the value is 0, then this metric will not be considered for load balancing.   


  * This property has a default value of 0.
* This property need not be set.
  * This property has a minimum value of 0. 

  
**diskWriteLatencyThreshold**|  xsd:int|  Represents the threshold of average time, in milliseconds, of a write of data to the disk. If the value is 0, then this metric will not be considered for load balancing.   


  * This property has a default value of 0.
* This property need not be set.
  * This property has a minimum value of 0. 

  
  
  

  
  

