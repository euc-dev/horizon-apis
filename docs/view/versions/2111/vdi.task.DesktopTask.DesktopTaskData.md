---
layout: page
title: Data Object - DesktopTaskData
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.task.DesktopTask.DesktopTaskData`

Property of
> [DesktopTaskInfo](vdi.task.DesktopTask.DesktopTaskInfo.md#field_detail)

Since
> Horizon 7.4


## Data Object Description

Desktop task object

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**taskType**|  xsd:string| <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>REFRESH</td><td>A refresh operation.</td></tr><tr><td>RESYNC</td><td>A resync operation.</td></tr><tr><td>REBALANCE</td><td>A rebalance operation.</td></tr><tr><td>ATTACH</td><td>A persistent disk attach operation.</td></tr><tr><td>DETACH</td><td>A persistent disk detach operation.</td></tr><tr><td>REPLACE</td><td>A persistent disk replace operation.</td></tr><tr><td>CHECKPOINT</td><td>A checkpoint operation.</td></tr><tr><td>PUSH_IMAGE</td><td>A push image operation (Instant Clone Engine only).</td></tr></table>
**description**|  xsd:string|  Description of desktop task [^1]
**scheduleTime**|  xsd:dateTime|  Time at which desktop task is scheduled to start [^1]
**remaining**|  xsd:int|  Total VMs on which task is scheduled or running [^1]
**errors**|  xsd:int|  Number of VMs whose task is in fault state [^1]
**halted**|  xsd:int|  Number of VMs whose task is in holding state [^1]
**cancelled**|  xsd:int|  Number of VMs whose task is in cancelled state [^1]


 


[^1]: This property need not be set.