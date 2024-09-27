---
layout: page
title: Data Object - TaskInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.task.Task.TaskInfo  
Returned by
     [PodFederation_Initialize](vdi.federation.PodFederation.md#initialize), [PodFederation_Join](vdi.federation.PodFederation.md#join), [PodFederation_Uninitialize](vdi.federation.PodFederation.md#uninitialize), [PodFederation_Unjoin](vdi.federation.PodFederation.md#unjoin), [Task_Get](vdi.task.Task.md#get)  
See also
     [TaskId](vdi.entity.TaskId.md), [TaskResult](vdi.task.Task.TaskResult.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Info on a task. 

##  Queryable Data Object 

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService"). 

Query Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_VIEW|  Global LDAP read is required to query information about a task.   
  


## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [TaskId](vdi.entity.TaskId.md)|  The ID of the task.   


 * This property cannot be updated.

  
**taskCategory**|  xsd:string|  The category of the task.   


 * This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"POD_FEDERATION_CATEGORY"| Category for PodFederation related tasks  

  
**taskType**|  xsd:string|  The type of the task.   


 * This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"POD_FEDERATION_INITIALIZING"| A task performing PodFederation initialize operation  
"POD_FEDERATION_UNINITIALIZING"| A task performing PodFederation uninitialize operation  
"POD_FEDERATION_JOINING"| A task performing PodFederation join operation  
"POD_FEDERATION_UNJOINING"| A task performing PodFederation unjoin operation  

  
**cancellable**|  xsd:boolean|  Whether the task can be cancelled or not.   


 * This property cannot be updated.

  
**state**|  xsd:string|  The state of the task.   


 * This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"RUNNING"| The task is currently running.  
"WAITING"| The task is currently waiting to execute.  
"COMPLETED"| The task execution has completed.  
"FAILED"| The task execution has failed.  
"PAUSED"| The task execution has been paused.  
"CANCELLED"| The task execution has been cancelled.  

  
**percentageComplete**|  xsd:int|  How complete the task is as a percentage.   


 * This property need not be set.
 * This property cannot be updated.

  
**result**| [TaskResult](vdi.task.Task.TaskResult.md)|  The result of a task, only available when task is completed.   


 * This property need not be set.
 * This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

