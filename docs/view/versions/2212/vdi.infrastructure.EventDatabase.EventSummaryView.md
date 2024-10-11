---
layout: page
title: Data Object - EventSummaryView
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.EventDatabase.EventSummaryView`

See also  
> [EventData](vdi.infrastructure.EventDatabase.EventData.md), [EventNamesData](vdi.infrastructure.EventDatabase.EventNamesData.md)

Since  
> Horizon 7.3


## Data Object Description 

**Deprecated.**_This query view is being deprecated. Please consider using[AuditEventSummaryView](vdi.infrastructure.AuditEvent.AuditEventSummaryView.md) and eventsId) instead. _

The EventSummaryView Object. 

##  Queryable Data Object 

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService"). 

Query definitions can specify the following member types: 

  * [eventId](vdi.infrastructure.EventDatabase.EventSummaryView.md#eventId) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 
  * [data](vdi.infrastructure.EventDatabase.EventSummaryView.md#data).[eventType](vdi.infrastructure.EventDatabase.EventData.md#eventType) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md), [QueryFilterContains](vdi.query.QueryFilter.Contains.md), or [QueryFilterStartsWith](vdi.query.QueryFilter.StartsWith.md) filter only) 
  * [data](vdi.infrastructure.EventDatabase.EventSummaryView.md#data).[severity](vdi.infrastructure.EventDatabase.EventData.md#severity) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 
  * [data](vdi.infrastructure.EventDatabase.EventSummaryView.md#data).[time](vdi.infrastructure.EventDatabase.EventData.md#time) ([QueryFilterBetween](vdi.query.QueryFilter.Between.md) filter only) 
  * [data](vdi.infrastructure.EventDatabase.EventSummaryView.md#data).[module](vdi.infrastructure.EventDatabase.EventData.md#module) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 
  * [data](vdi.infrastructure.EventDatabase.EventSummaryView.md#data).[message](vdi.infrastructure.EventDatabase.EventData.md#message) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md), [QueryFilterContains](vdi.query.QueryFilter.Contains.md), or [QueryFilterStartsWith](vdi.query.QueryFilter.StartsWith.md) filter only) 
  * [data](vdi.infrastructure.EventDatabase.EventSummaryView.md#data).[node](vdi.infrastructure.EventDatabase.EventData.md#node) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md), [QueryFilterContains](vdi.query.QueryFilter.Contains.md), or [QueryFilterStartsWith](vdi.query.QueryFilter.StartsWith.md) filter only) 
  * [data](vdi.infrastructure.EventDatabase.EventSummaryView.md#data).[userId](vdi.infrastructure.EventDatabase.EventData.md#userId) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 
  * [data](vdi.infrastructure.EventDatabase.EventSummaryView.md#data).[desktopId](vdi.infrastructure.EventDatabase.EventData.md#desktopId) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 
  * [data](vdi.infrastructure.EventDatabase.EventSummaryView.md#data).[applicationId](vdi.infrastructure.EventDatabase.EventData.md#applicationId) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 
  * [data](vdi.infrastructure.EventDatabase.EventSummaryView.md#data).[machineId](vdi.infrastructure.EventDatabase.EventData.md#machineId) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 
  * [data](vdi.infrastructure.EventDatabase.EventSummaryView.md#data).[rdsServerId](vdi.infrastructure.EventDatabase.EventData.md#rdsServerId) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 
  * [data](vdi.infrastructure.EventDatabase.EventSummaryView.md#data).[farmId](vdi.infrastructure.EventDatabase.EventData.md#farmId) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 
  * [data](vdi.infrastructure.EventDatabase.EventSummaryView.md#data).[sessionId](vdi.infrastructure.EventDatabase.EventData.md#sessionId) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 

The following caveats apply: 
  * This will consider the events from Event, Event_Data database tables only, and will not return events from historical database tables.
  * The first filter may be any of the above or an [QueryFilterAnd](vdi.query.QueryFilter.And.md) or [QueryFilterOr](vdi.query.QueryFilter.Or.md) filter specifying any combination of the above.
  * If [sortBy](vdi.query.QueryDefinition.md#sortBy) is not specified, resulting events will be sorted by [time](vdi.infrastructure.EventDatabase.EventData.md#time).
  * [maxPageSize](vdi.query.QueryDefinition.md#maxPageSize) cannot exceed 1000.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**eventId**|  xsd:int|  ID of the event in Event Database.   
  
**data**| [EventData](vdi.infrastructure.EventDatabase.EventData.md)|  EventData Object that contains the attributes related to this event.   
  
**namesData**| [EventNamesData](vdi.infrastructure.EventDatabase.EventNamesData.md)|  EventNamesData object that contains the naming attributes related to this event.   
  
  
  
  
  
  
