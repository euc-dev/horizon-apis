---
layout: page
title: Data Object - AWSCoreWorkspaceSchedule
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.AWSCoreWorkspaceSchedule`

Property of
> [AWSCoreWorkspacePowerPolicySettings](vdi.resources.Desktop.AWSCoreWorkspacePowerPolicySettings.md#field_detail)

Since
> Horizon 8.13


## Data Object Description

Specification for an AWS Core power management settings.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**name**|  xsd:string|  Name of the schedule
**timezone**|  xsd:string|  Time-zone of the schedule.
**daysOfTheWeek**|  xsd:string[]|  Days of the week
**resumeTime**|  xsd:string|  Workspace resume time<br>* This property must contain the time in 24 hours format. e.g. 14:30
**suspendTime**|  xsd:string|  Workspace suspend time<br>* This property must contain the time in 24 hours format. e.g. 14:30


 
