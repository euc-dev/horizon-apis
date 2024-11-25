---
layout: page
title: Data Object - TaskInfo
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.task.Task.TaskInfo`

Returned by
> [PodFederation_Initialize](vdi.federation.PodFederation.md#initialize), [PodFederation_Join](vdi.federation.PodFederation.md#join), [PodFederation_Uninitialize](vdi.federation.PodFederation.md#uninitialize), [PodFederation_Unjoin](vdi.federation.PodFederation.md#unjoin), [Task_Get](vdi.task.Task.md#get)

See also
> [TaskId](vdi.entity.TaskId.md), [TaskResult](vdi.task.Task.TaskResult.md)

Since
> Horizon View 6.0


## Data Object Description

Info on a task.

##  Queryable Data Object

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService").

Query **Privileges**

Privilege | Description
:---|:---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to query information about a task.



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [TaskId](vdi.entity.TaskId.md)|  The ID of the task. [^2]
**taskCategory**|  xsd:string|  The category of the task. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>POD_FEDERATION_CATEGORY</td><td>Category for PodFederation related tasks</td></tr></table>
**taskType**|  xsd:string|  The type of the task. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>POD_FEDERATION_INITIALIZING</td><td>A task performing PodFederation initialize operation</td></tr><tr><td>POD_FEDERATION_UNINITIALIZING</td><td>A task performing PodFederation uninitialize operation</td></tr><tr><td>POD_FEDERATION_JOINING</td><td>A task performing PodFederation join operation</td></tr><tr><td>POD_FEDERATION_UNJOINING</td><td>A task performing PodFederation unjoin operation</td></tr></table>
**cancellable**|  xsd:boolean|  Whether the task can be cancelled or not. [^2]
**state**|  xsd:string|  The state of the task. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>RUNNING</td><td>The task is currently running.</td></tr><tr><td>WAITING</td><td>The task is currently waiting to execute.</td></tr><tr><td>COMPLETED</td><td>The task execution has completed.</td></tr><tr><td>FAILED</td><td>The task execution has failed.</td></tr><tr><td>PAUSED</td><td>The task execution has been paused.</td></tr><tr><td>CANCELLED</td><td>The task execution has been cancelled.</td></tr></table>
**percentageComplete**|  xsd:int|  How complete the task is as a percentage. [^1] [^2]
**result**| [TaskResult](vdi.task.Task.TaskResult.md)|  The result of a task, only available when task is completed. [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.