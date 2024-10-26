---
layout: page
title: Fault - LogCollectorFault
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.fault.LogCollectorFault`

Thrown by
> [LogCollector_List](vdi.utils.logcollector.LogCollector.md#list)

Extends
> [ViewServerFault](vdi.fault.ViewServerFault.md)

See also
> [EntityId](vdi.EntityId.md), [LogCollectorTaskId](vdi.entity.LogCollectorTaskId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon 7.10


## Fault Description

Fault for log collector method invocations.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**logCollectorFaultCode**|  xsd:string|
* This property will be one of:
|  Value |  Description
---|---
"COLLECT_OPERATION_TIMED_OUT"| Log collection operation has timed out.
"LOG_COLLECT_PROCESS_NON_RESPONSIVE"| Log collection process has become non responsive.
"LOW_DISK_SPACE"| Not enough disk space available to proceed with logs collection operation.
"INTERNAL_SERVER_ERROR"| An internal server error has occurred.
"LOG_COLLECTOR_TASK_ID_NOT_FOUND"| Log collection task identifier not found.
"USER_NOT_OWNS_LOG_COLLECTOR_TASK_ID"| Log collection task identifier is not owned by the user.
"SERVER_BUSY_REJECTS_COLLECT_REQUEST"| Request for log collection is rejected with busy error.
"PURGE_ELIGIBLE_LOG_COLLECTOR_TASK_NOT_FOUND"| Purge operation not performed as none are eligible.
"SERVER_CLEAN_REJECTS_PURGE_REQUEST"| Purge operation not performed as none.
"LOG_COLLECTOR_COMPONENT_ID_NOT_FOUND"| Log component identifier not found.
"LOG_COLLECTOR_COMPONENT_TYPE_INVALID"| Log component type is invalid or unknown.
"LOG_BUNDLE_DOWNLOAD_URL_NOT_FOUND"| Log component download URL not found.
"LOG_COLLECTOR_USER_ID_NOT_FOUND"| User identifier not found.
"LOG_COLLECTOR_FILTER_TYPE_INVALID"| Log collection filter type in invalid.
**logCollectorTaskId**| [LogCollectorTaskId](vdi.entity.LogCollectorTaskId.md)| [^1]
**userId**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)| [^1]
**logCollectorTaskState**|  xsd:string| [^1]<br>* This property will be one of:<br><table><thead><tr><th>Value</th><th>Description</th></tr></thead><tbody><tr><td>"IDLE"</td><td>Log Collection task is in IDLE state.</td></tr><tr><td>"COLLECT"</td><td>Log Collection task has started collecting logs bundle.</td></tr><tr><td>"COLLECT_COMPLETE"</td><td>Log collection task has completed collection of logs bundle.</td></tr><tr><td>"PURGE_COMPLETE"</td><td>Log collection task has completed purge operation.</td></tr><tr><td>"PURGE"</td><td>Log collection task is in purge operation.</td></tr><tr><td>"COLLECT_TIMED_OUT"</td><td>Log collection task has timed out and the process has been interrupted.</td></tr><tr><td>"ERROR"</td><td>Log collection task has ended in error.</td></tr><tr><td>"NON_RESPONSIVE"</td><td>In rare occasions, the log collection process becomes non-responsive. A connection server restart is required to remediate it.</td></tr></tbody></table>
**logComponentIdentifier**| [EntityId](vdi.EntityId.md)| [^1]
Properties inherited from [ViewServerFault](vdi.fault.ViewServerFault.md)
[errorMessage](vdi.fault.ViewServerFault.md#errorMessage)
Properties inherited from [MethodFault](vmodl.MethodFault.md)
None


 
