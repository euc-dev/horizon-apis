---
layout: page
title: Data Object - HelpdeskActivityView
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.infrastructure.AuditEvent.HelpdeskActivityView`

See also
> [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon 7.13


## Data Object Description

The HelpdeskActivityView Object.

##  Queryable Data Object

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService").

Query definitions can specify the following member types:

* [eventId](vdi.infrastructure.AuditEvent.HelpdeskActivityView.md#eventId) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only)
* [time](vdi.infrastructure.AuditEvent.HelpdeskActivityView.md#time) ([QueryFilterBetween](vdi.query.QueryFilter.Between.md) filter only)
* [message](vdi.infrastructure.AuditEvent.HelpdeskActivityView.md#message) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md), [QueryFilterContains](vdi.query.QueryFilter.Contains.md), or [QueryFilterStartsWith](vdi.query.QueryFilter.StartsWith.md) filter only)
* [userId](vdi.infrastructure.AuditEvent.HelpdeskActivityView.md#userId) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only)
* [eventType](vdi.infrastructure.AuditEvent.HelpdeskActivityView.md#eventType) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md), [QueryFilterContains](vdi.query.QueryFilter.Contains.md), or [QueryFilterStartsWith](vdi.query.QueryFilter.StartsWith.md) filter only)

The following caveats apply:
* This will consider the events for helpdesk from Event, Event_Data table only, and will not return events from historical database tables.
* The first filter may be any of the above or an [QueryFilterAnd](vdi.query.QueryFilter.And.md) or [QueryFilterOr](vdi.query.QueryFilter.Or.md) filter specifying any combination of the above.
* If [sortBy](vdi.query.QueryDefinition.md#sortBy) is not specified, resulting events will be sorted by [time](vdi.infrastructure.AuditEvent.HelpdeskActivityView.md#time).
* [maxPageSize](vdi.query.QueryDefinition.md#maxPageSize) cannot exceed 1000.



Query Privileges

Privilege |  Description
---|---
MACHINE_VIEW|  Machine read permission is sufficient to get HelpdeskActivityView.
POOL_VIEW|  Pool read permission is sufficient to get HelpdeskActivityView.
FEDERATED_SESSIONS_VIEW|  Global session read permission is sufficient to get HelpdeskActivityView.



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**eventId**|  xsd:int|  ID of the event in Event Database.
**time**|  xsd:dateTime|  Time at which the event occurred, measured from the epoch (January 1, 1970).
**message**|  xsd:string|  Event message. Language of this message will be dependent on the locale. Locale can be set at request or session level. Request level locale can be provided by adding X-VIEW-LOCALE request header and session level locale can be set by invoking [AuthenticationManager_SetLocale](vdi.AuthenticationManager.md#setLocale) method after login. Request level locale will be given priority over session level locale. If not set explicitly, locale will default to English language.
**userDisplayName**|  xsd:string|  Display name of the user associated with this event. Will be unset if there is no User association for this event. [^1]
**desktopDisplayName**|  xsd:string|  Display name of the Desktop associated with this event. Will be unset if there is no Desktop association for this event. [^1]
**applicationDisplayName**|  xsd:string|  Display name of the Application associated with this event. Will be unset if there is no Application association for this event. [^1]
**machineName**|  xsd:string|  Name of the Machine associated with this event. Will be unset if there is no Machine association for this event. [^1]
**farmDisplayName**|  xsd:string|  Display name of the Farm associated with this event. Will be unset if there is no Farm association for this event. [^1]
**thinappDisplayName**|  xsd:string|  Display name of the Thinapp associated with this event. Will be unset if there is no Thinapp association for this event. [^1]
**processName**|  xsd:string|  Name of the remote process associated with this event. Will be unset if there is no process association for this event. [^1]
**userId**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User involved in this event. Will be unset if there is no user association for this event. [^1]
**eventType**|  xsd:string|  Event name that corresponds to an item in the message catalog. For example: BROKER_USERLOGGEDIN, AGENT_CONNECTED etc.


 


[^1]: This property need not be set.