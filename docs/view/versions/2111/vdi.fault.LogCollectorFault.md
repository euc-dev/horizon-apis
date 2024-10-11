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
> [LogCollector_GetLogLevels](vdi.utils.logcollector.LogCollector.md#getLogLevels), [LogCollector_List](vdi.utils.logcollector.LogCollector.md#list), [LogCollector_SetLogLevels](vdi.utils.logcollector.LogCollector.md#setLogLevels)

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
"LOG_LEVEL_INVALID_PARAMETER"| Invalid parameter passed for log level operations.  
"LOG_LEVEL_INVALID_DATA"| Invalid response received for log level operations.  
"NO_RESPONSE"| No response received for log level operations.  

  
**logCollectorTaskId**| [LogCollectorTaskId](vdi.entity.LogCollectorTaskId.md)|    


* This property need not be set.

  
**userId**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|    


* This property need not be set.

  
**logCollectorTaskState**|  xsd:string|    


* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"IDLE"| Log Collection task is in IDLE state.  
"COLLECT"| Log Collection task has started collecting logs bundle.  
"COLLECT_COMPLETE"| Log collection task has completed collection of logs bundle.  
"PURGE_COMPLETE"| Log collection task has completed purge operation.  
"PURGE"| Log collection task is in purge operation.  
"COLLECT_TIMED_OUT"| Log collection task has timed out and the process has been interrupted.  
"ERROR"| Log collection task has ended in error.  
"NON_RESPONSIVE"| In rare occasions, the log collection process becomes non-responsive. A connection server restart is required to remediate it.  

  
**logComponentIdentifier**| [EntityId](vdi.EntityId.md)|    


* This property need not be set.

  
Properties inherited from [ViewServerFault](vdi.fault.ViewServerFault.md)  
[errorMessage](vdi.fault.ViewServerFault.md#errorMessage)  
Properties inherited from [MethodFault](vmodl.MethodFault.md)  
None  
  
  
   
  
  
