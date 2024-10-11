---
layout: page
title: Data Object - DisplayProtocolPerformanceData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.helpdesk.Performance.DisplayProtocolPerformanceData`

Property of  
> [PerformanceInfo](vdi.helpdesk.Performance.PerformanceInfo.md#field_detail)

Returned by  
> [Performance_GetDisplayProtocolPerformanceData](vdi.helpdesk.Performance.md#getDisplayProtocolPerformanceData)

See also  
> [BlastPerformanceData](vdi.helpdesk.Performance.BlastPerformanceData.md), [PcoipPerformanceData](vdi.helpdesk.Performance.PcoipPerformanceData.md)

Since  
> Horizon 7.2


## Data Object Description 

The performance for the current display protocol. It includes PCOIP or BLAST performance data. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**blastPerformanceData**| [BlastPerformanceData](vdi.helpdesk.Performance.BlastPerformanceData.md)|  The performance data when session is using BLAST protocol.   


* This property need not be set.
* This property cannot be updated.

  
**pcoipPerformanceData**| [PcoipPerformanceData](vdi.helpdesk.Performance.PcoipPerformanceData.md)|  The performance data when session is using PCoIP protocol.   


* This property need not be set.
* This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
