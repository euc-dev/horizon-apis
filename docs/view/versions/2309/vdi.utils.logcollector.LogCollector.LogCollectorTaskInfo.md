---
layout: page
title: Data Object - LogCollectorTaskInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.logcollector.LogCollector.LogCollectorTaskInfo`

Returned by
> [LogCollector_Collect](vdi.utils.logcollector.LogCollector.md#collect), [LogCollector_GetTaskInfo](vdi.utils.logcollector.LogCollector.md#getTaskInfo), [LogCollector_GetTaskInfoById](vdi.utils.logcollector.LogCollector.md#getTaskInfoById), [LogCollector_List](vdi.utils.logcollector.LogCollector.md#list), [LogCollector_Purge](vdi.utils.logcollector.LogCollector.md#purge)

See also
> [LogCollectorComponentIdentifier](vdi.utils.logcollector.LogCollector.LogCollectorComponentIdentifier.md), [LogCollectorTaskId](vdi.entity.LogCollectorTaskId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon 7.10


## Data Object Description

Task information for a log collector component.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**logCollectorComponentId**| [LogCollectorComponentIdentifier](vdi.utils.logcollector.LogCollector.LogCollectorComponentIdentifier.md)|  Log component identifier. [^1]
**id**| [LogCollectorTaskId](vdi.entity.LogCollectorTaskId.md)|  Unique identifier of a log collector task. [^1]
**startTime**|  xsd:dateTime|  Start time of the log collection. [^1]
**endTime**|  xsd:dateTime|  End time of the log collection. [^1]
**initiatedBy**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User identity information.
**logCollectorTaskState**|  xsd:string|  Log collector task state. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"IDLE"</td><td>Log Collection task is in IDLE state.</td></tr><tr><td>"COLLECT"</td><td>Log Collection task has started collecting logs bundle.</td></tr><tr><td>"COLLECT_COMPLETE"</td><td>Log collection task has completed collection of logs bundle.</td></tr><tr><td>"PURGE_COMPLETE"</td><td>Log collection task has completed purge operation.</td></tr><tr><td>"PURGE"</td><td>Log collection task is in purge operation.</td></tr><tr><td>"COLLECT_TIMED_OUT"</td><td>Log collection task has timed out and the process has been interrupted.</td></tr><tr><td>"ERROR"</td><td>Log collection task has ended in error.</td></tr><tr><td>"NON_RESPONSIVE"</td><td>In rare occasions, the log collection process becomes non-responsive. A connection server restart is required to remediate it.</td></tr></table>
 


 


[^1]: This property need not be set.