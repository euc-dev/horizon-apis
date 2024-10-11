---
layout: page
title: Data Object - TaskResult
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.task.Task.TaskResult`

Property of  
> [TaskInfo](vdi.task.Task.TaskInfo.md#field_detail)

See also  
> [MapEntry](vdi.util.MapEntry.md)

Since  
> Horizon View 6.0


## Data Object Description 

Information about a Task result. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**resultCode**|  xsd:string|  The result code of the task.   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"SUCCESS"| Task is completed successfully  
"WARN"| Task is finished but has warning.  
"ERROR"| Task is finished but the it has error  

  
**message**|  xsd:string|  The result message   


* This property cannot be updated.

  
**messageId**|  xsd:string|  The result message ID.   


* This property cannot be updated.

  
**messageValues**| [MapEntry[]](vdi.util.MapEntry.md)|  The result message values.   


* This property need not be set.
* This property cannot be updated.

  
  
  
   
  
  
