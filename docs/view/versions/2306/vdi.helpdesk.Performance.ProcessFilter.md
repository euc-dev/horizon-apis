---
layout: page
title: Data Object - ProcessFilter
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.helpdesk.Performance.ProcessFilter
Parameter to
     [Performance_GetProcessPerformanceData](vdi.helpdesk.Performance.md#getProcessPerformanceData)
Since 
    Horizon 7.6

## Data Object Description 

The filter for processes 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**processSessionFilter**|  xsd:string|  Filter process by process session info   


[^1]
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"CURRENT_USER_SESSION"| The processes which run in the current user session  
"SYSTEM_AND_CURRENT_USER_SESSION"| The union of the system processes and current user session processes.  

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
