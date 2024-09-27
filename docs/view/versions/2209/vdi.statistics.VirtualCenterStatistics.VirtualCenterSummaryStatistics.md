---
layout: page
title: Data Object - VirtualCenterSummaryStatistics
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.statistics.VirtualCenterStatistics.VirtualCenterSummaryStatistics  
Returned by
     [VirtualCenterStatistics_getSummaryStatistics](vdi.statistics.VirtualCenterStatistics.md#getSummaryStatistics), [VirtualCenterStatistics_listSummaryStatistics](vdi.statistics.VirtualCenterStatistics.md#listSummaryStatistics)  
See also
     [DataStoreSummaryStatistics](vdi.statistics.VirtualCenterStatistics.DataStoreSummaryStatistics.md), [HostSummaryStatistics](vdi.statistics.VirtualCenterStatistics.HostSummaryStatistics.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)  
Since 
    Horizon 7.8

## Data Object Description 

Summary statistics for a Virtual Center server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  The ID of the virtual center server.   


* This property cannot be updated.

  
**name**|  xsd:string|  The name of the Virtual Center server.   


* This property need not be set.
* This property cannot be updated.

  
**instanceUuid**|  xsd:string|  Virtual center instance uuid.   


* This property need not be set.
* This property cannot be updated.

  
**version**|  xsd:string|  The version of the Virtual Center server.   


* This property need not be set.
* This property cannot be updated.

  
**hostSummaryStatistics**| [HostSummaryStatistics[]](vdi.statistics.VirtualCenterStatistics.HostSummaryStatistics.md)|  Statistics information about each host managed by the Virtual Center server.   


* This property need not be set.
* This property cannot be updated.

  
**dataStoreSummaryStatistics**| [DataStoreSummaryStatistics[]](vdi.statistics.VirtualCenterStatistics.DataStoreSummaryStatistics.md)|  Statistics information about each data store managed by the Virtual Center server.   


* This property need not be set.
* This property cannot be updated.

  
  
  
 
  
  

