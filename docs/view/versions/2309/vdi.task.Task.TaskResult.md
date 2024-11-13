---
layout: page
title: Data Object - TaskResult
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.task.Task.TaskResult`

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
**resultCode**|  xsd:string|  The result code of the task. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>SUCCESS</td><td>Task is completed successfully</td></tr><tr><td>WARN</td><td>Task is finished but has warning.</td></tr><tr><td>ERROR</td><td>Task is finished but it has error</td></tr></table>
**message**|  xsd:string|  The result message [^2]
**messageId**|  xsd:string|  The result message ID. [^2]
**messageValues**| [MapEntry[]](vdi.util.MapEntry.md)|  The result message values. [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.