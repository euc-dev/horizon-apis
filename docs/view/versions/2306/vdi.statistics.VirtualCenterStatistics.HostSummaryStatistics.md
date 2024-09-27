---
layout: page
title: Data Object - HostSummaryStatistics
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.statistics.VirtualCenterStatistics.HostSummaryStatistics  
Property of
     [VirtualCenterSummaryStatistics](vdi.statistics.VirtualCenterStatistics.VirtualCenterSummaryStatistics.md#field_detail)  
Since 
    Horizon 7.8

## Data Object Description 

Statistics on a specific host managed by the Virtual Center server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  The name of the Virtual Center host.   


* This property cannot be updated.

  
**version**|  xsd:string|  The version of the Virtual Center host.   


* This property need not be set.
* This property cannot be updated.

  
**status**|  xsd:string|  The status of the Virtual Center host.   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"CONNECTED"| The host is successfully connected to Virtual Center server.  
"DISCONNECTED"| The host is disconnected from Virtual Center server.  
"NOT_RESPONDING"| The host is not responding.  

  
**numCpuCores**|  xsd:int|  Number of physical CPU cores on the host.   


* This property need not be set.
* This property cannot be updated.

  
**cpuMhz**|  xsd:int|  CPU speed per core. This might be an averaged value if the speed is not uniform across all cores. The total CPU speed of the box is defined as cpuMhz * numCpuCores   


* This property need not be set.
* This property cannot be updated.

  
**overallCpuUsage**|  xsd:int|  Aggregated CPU usage across all cores on the host, in MHz.   


* This property need not be set.
* This property cannot be updated.

  
**memorySizeBytes**|  xsd:long|  The physical memory size, in bytes.   


* This property need not be set.
* This property cannot be updated.

  
**overallMemoryUsageMB**|  xsd:int|  Physical memory usage on the host, in MBs.   


* This property need not be set.
* This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

