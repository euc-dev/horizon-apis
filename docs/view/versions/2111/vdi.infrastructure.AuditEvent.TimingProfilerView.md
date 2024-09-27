---
layout: page
title: Data Object - TimingProfilerView
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.AuditEvent.TimingProfilerView  
See also
     [SessionId](vdi.entity.SessionId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)  
Since 
    Horizon 8.2

## Data Object Description 

The TimingProfilerView Object. 

##  Queryable Data Object 

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService"). 

Query definitions can specify the following member types: 

  * [time](vdi.infrastructure.AuditEvent.TimingProfilerView.md#time) ([QueryFilterBetween](vdi.query.QueryFilter.Between.md) filter only) 
  * [eventType](vdi.infrastructure.AuditEvent.TimingProfilerView.md#eventType) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md), [QueryFilterContains](vdi.query.QueryFilter.Contains.md), or [QueryFilterStartsWith](vdi.query.QueryFilter.StartsWith.md) filter only) 
  * [userId](vdi.infrastructure.AuditEvent.TimingProfilerView.md#userId) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 
  * [sessionId](vdi.infrastructure.AuditEvent.TimingProfilerView.md#sessionId) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 

The following caveats apply: 
  * This will consider the Timing Profiler events from Timing_Profiler table.
  * The first filter may be any of the above or an [QueryFilterAnd](vdi.query.QueryFilter.And.md) or [QueryFilterOr](vdi.query.QueryFilter.Or.md) filter specifying any combination of the above.
  * If [sortBy](vdi.query.QueryDefinition.md#sortBy) is not specified, resulting events will be sorted by [time](vdi.infrastructure.AuditEvent.TimingProfilerView.md#time).
  * [maxPageSize](vdi.query.QueryDefinition.md#maxPageSize) cannot exceed 1000.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**eventId**|  xsd:int|  ID of the Timing Profiler event in Event Database.   
  
**time**|  xsd:dateTime|  Time at which the event occurred, measured from the epoch (January 1, 1970).   
  
**userId**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User involved in this event. Will be unset if there is no user association for this event.   


* This property need not be set.

  
**eventType**|  xsd:string|  Type of the Timing Profiler event. For example: TIMING_PROFILER_DESKTOP_RECONNECT, TIMING_PROFILER_GET_LAUNCH_ITEMS etc.   
  
**sessionId**| [SessionId](vdi.entity.SessionId.md)|  Session associated with this event. Will be unset if there is no Session association for this event.   


* This property need not be set.

  
**logonTiming**|  xsd:string|  Logon timing profiler tree. Will be unset if there is no timing profiler tree association for this event.   


* This property need not be set.

  
**properties**|  xsd:string|  Json containing various attributes associated with this timing profiler event.   


* This property need not be set.

  
  
  
   
  
  

