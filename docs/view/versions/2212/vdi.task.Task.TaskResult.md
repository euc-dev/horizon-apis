---
layout: page
title: Data Object - TaskResult
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.task.Task.TaskResult
Property of
     [TaskInfo](vdi.task.Task.TaskInfo.md#field_detail)
See also
     [MapEntry](vdi.util.MapEntry.md)
Since 
    Horizon View 6.0

## Data Object Description 

Information about a Task result. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**resultCode**|  xsd:string|  The result code of the task.   


[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"SUCCESS"| Task is completed successfully  
"WARN"| Task is finished but has warning.  
"ERROR"| Task is finished but the it has error  

  
**message**|  xsd:string|  The result message   


[^2]

  
**messageId**|  xsd:string|  The result message ID.   


[^2]

  
**messageValues**| [MapEntry[]](vdi.util.MapEntry.md)|  The result message values.   


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
