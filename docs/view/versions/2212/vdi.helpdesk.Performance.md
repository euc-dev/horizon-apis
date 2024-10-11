---
layout: page
title: Service - Performance
hide:
 #- navigation
 - toc
---

  
  
  



Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.helpdesk.Performance`

See also  
> [DisplayProtocolPerformanceData](vdi.helpdesk.Performance.DisplayProtocolPerformanceData.md), [HistoricalPerformanceData](vdi.helpdesk.Performance.HistoricalPerformanceData.md), [PerformanceInfo](vdi.helpdesk.Performance.PerformanceInfo.md), [ProcessFilter](vdi.helpdesk.Performance.ProcessFilter.md), [ProcessPerformanceData](vdi.helpdesk.Performance.ProcessPerformanceData.md), [RemoteApplicationStatistics](vdi.helpdesk.Performance.RemoteApplicationStatistics.md), [SessionId](vdi.entity.SessionId.md)

Since  
> Horizon 7.2


  


## Service Description

The service for fetching performance information. 

Methods

Methods defined in this Service   
---  
Performance_Get, Performance_GetDisplayProtocolPerformanceData, Performance_GetHistoricalPerformanceData, Performance_GetProcessPerformanceData, Performance_GetRemoteApplicationPerformanceData, Performance_GetRemoteApplicationStatistics  
  



**Deprecated.**_New code should use #getProcessPerformanceData(SessionId) or #getDisplayProtocolPerformanceData(SessionId) if you just want to retrieve the latest performance data._

Retrieves performance data from the given time point to current time. When firstly calling this method, the timestamp should be set to 0, the agent will return one or more performance data with a timestamp indicating the time when the last performance data was obtained. From that time, the agent will collect the performance data periodically(1 second) and keep them in memory. When getting another request, the agent will check the parameter timestamp, it will return all the performance data from the timestamp to current time. If the timestamp is not set, the agent will return all the performance data it has collected. The agent will stop the collection if there are no requests received after a long period(default is 2 minutes). 

Privileges 

Privilege |  Description   
---|---  
MACHINE_VIEW|  Machine read with the corresponding access group permission is sufficient to get a session's performance information.   
POOL_VIEW|  Desktop read with the corresponding access group permission is sufficient to get a session's performance information.   
FEDERATED_SESSIONS_VIEW|  Global session read is sufficient to get a session's performance information.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Performance](vdi.helpdesk.Performance.md) used to make the method call.   
**id**| [SessionId](vdi.entity.SessionId.md)|  SessionID to get the performance data for.   
  
**timestamp**|  xsd:long|  The time point after which performance data should be obtained.   


  * This parameter need not be set.

  
  


Return Value 

Type |  Description   
---|---  
[PerformanceInfo](vdi.helpdesk.Performance.PerformanceInfo.md)| performance data collected since the given time stamp.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Retrieves performance data of the current session display protocol (PCoIP or BLAST). 

Privileges 

Privilege |  Description   
---|---  
MACHINE_VIEW|  Machine read with the corresponding access group permission is sufficient to get a session's protocol performance information.   
POOL_VIEW|  Desktop read with the corresponding access group permission is sufficient to get a session's protocol performance information.   
FEDERATED_SESSIONS_VIEW|  Global session read is sufficient to get a session's protocol performance information.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Performance](vdi.helpdesk.Performance.md) used to make the method call.   
**id**| [SessionId](vdi.entity.SessionId.md)|  SessionID to get the protocol performance data for.   
  
  


Return Value 

Type |  Description   
---|---  
[DisplayProtocolPerformanceData](vdi.helpdesk.Performance.DisplayProtocolPerformanceData.md)| Protocol performance data collected.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Retrieves historical performance data of the specific session in latest 15 minutes. The sampling period is 5 seconds. So it returns 180 samples in this response. 

Privileges 

Privilege |  Description   
---|---  
MACHINE_VIEW|  Machine read with the corresponding access group permission is sufficient to get a session's performance information.   
POOL_VIEW|  Desktop read with the corresponding access group permission is sufficient to get a session's performance information.   
FEDERATED_SESSIONS_VIEW|  Global session read is sufficient to get a session's performance information.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Performance](vdi.helpdesk.Performance.md) used to make the method call.   
**id**| [SessionId](vdi.entity.SessionId.md)|  SessionID to get the performance data for.   
  
  


Return Value 

Type |  Description   
---|---  
[HistoricalPerformanceData[]](vdi.helpdesk.Performance.HistoricalPerformanceData.md)| Historical performance data collected in latest 15 minutes.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Retrieves the process performance data. 

Privileges 

Privilege |  Description   
---|---  
MACHINE_VIEW|  Machine read with the corresponding access group permission is sufficient to get a session's process performance information.   
POOL_VIEW|  Desktop read with the corresponding access group permission is sufficient to get a session's process performance information.   
FEDERATED_SESSIONS_VIEW|  Global session read is sufficient to get a session's process performance information.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Performance](vdi.helpdesk.Performance.md) used to make the method call.   
**id**| [SessionId](vdi.entity.SessionId.md)|  SessionID to get the process performance data for.   
  
**processFilter**| [ProcessFilter](vdi.helpdesk.Performance.ProcessFilter.md)|  A filter to filter the processes in remote virtual machine.  **_Since_** Horizon 7.6  


  * This parameter need not be set.

  
  


Return Value 

Type |  Description   
---|---  
[ProcessPerformanceData[]](vdi.helpdesk.Performance.ProcessPerformanceData.md)| Process performance data collected. Will return all processes on the remote virtual machine if processFilter is not set.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



**Deprecated.**_use #getRemoteApplicationStatistics(SessionId) instead._

Retrieves the remote applications statistics. 

Privileges 

Privilege |  Description   
---|---  
MACHINE_VIEW|  Machine read with the corresponding access group permission is sufficient to get a session's remote application statistics.   
POOL_VIEW|  Desktop read with the corresponding access group permission is sufficient to get a session's remote application statistics.   
FEDERATED_SESSIONS_VIEW|  Global session read is sufficient to get a session's remote application statistics.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Performance](vdi.helpdesk.Performance.md) used to make the method call.   
**id**| [SessionId](vdi.entity.SessionId.md)|  SessionID to get the remote application statistics for.   
  
  


Return Value 

Type |  Description   
---|---  
[RemoteApplicationStatistics[]](vdi.helpdesk.Performance.RemoteApplicationStatistics.md)| Remote application statistics.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Retrieves the remote applications statistics. 

Privileges 

Privilege |  Description   
---|---  
MACHINE_VIEW|  Machine read with the corresponding access group permission is sufficient to get a session's remote application statistics.   
POOL_VIEW|  Desktop read with the corresponding access group permission is sufficient to get a session's remote application statistics.   
FEDERATED_SESSIONS_VIEW|  Global session read is sufficient to get a session's remote application statistics.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Performance](vdi.helpdesk.Performance.md) used to make the method call.   
**id**| [SessionId](vdi.entity.SessionId.md)|  SessionID to get the remote application statistics for.   
  
  


Return Value 

Type |  Description   
---|---  
[RemoteApplicationStatistics[]](vdi.helpdesk.Performance.RemoteApplicationStatistics.md)| Remote application statistics.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  
