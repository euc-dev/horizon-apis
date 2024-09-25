---
layout: page
title: Data Object - DesktopTaskData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.task.DesktopTask.DesktopTaskData
Property of
     [DesktopTaskInfo](vdi.task.DesktopTask.DesktopTaskInfo.md#field_detail)
Since 
    Horizon 7.4

## Data Object Description 

Desktop task object 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**taskType**|  xsd:string|    


  * This property will be one of:  
|  Value |  Description   
---|---  
"REFRESH"| A refresh operation.  
"RESYNC"| A resync operation.  
"REBALANCE"| A rebalance operation.  
"ATTACH"| A persistent disk attach operation.  
"DETACH"| A persistent disk detach operation.  
"REPLACE"| A persistent disk replace operation.  
"CHECKPOINT"| A checkpoint operation.  
"PUSH_IMAGE"| A push image operation (Instant Clone Engine only).  

  
**description**|  xsd:string|  Description of desktop task   


[^1]

  
**scheduleTime**|  xsd:dateTime|  Time at which desktop task is scheduled to start   


[^1]

  
**remaining**|  xsd:int|  Total VMs on which task is scheduled or running   


[^1]

  
**errors**|  xsd:int|  Number of VMs whose task is in fault state   


[^1]

  
**halted**|  xsd:int|  Number of VMs whose task is in holding state   


[^1]

  
**cancelled**|  xsd:int|  Number of VMs whose task is in cancelled state   


[^1]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
