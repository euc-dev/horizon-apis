---
layout: page
title: Data Object - AuditEventSummaryView
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.AuditEvent.AuditEventSummaryView  
See also
     [ApplicationId](vdi.entity.ApplicationId.md), [DesktopId](vdi.entity.DesktopId.md), [MachineId](vdi.entity.MachineId.md), [PersistentDiskId](vdi.entity.PersistentDiskId.md), [SessionId](vdi.entity.SessionId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)  
Since 
    Horizon 7.13

## Data Object Description 

The AuditEventSummaryView Object. 

##  Queryable Data Object 

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService"). 

Query definitions can specify the following member types: 

  * [eventId](vdi.infrastructure.AuditEvent.AuditEventSummaryView.md#eventId) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 
  * [eventType](vdi.infrastructure.AuditEvent.AuditEventSummaryView.md#eventType) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md), [QueryFilterContains](vdi.query.QueryFilter.Contains.md), or [QueryFilterStartsWith](vdi.query.QueryFilter.StartsWith.md) filter only) 
  * [severity](vdi.infrastructure.AuditEvent.AuditEventSummaryView.md#severity) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 
  * [time](vdi.infrastructure.AuditEvent.AuditEventSummaryView.md#time) ([QueryFilterBetween](vdi.query.QueryFilter.Between.md) filter only) 
  * [module](vdi.infrastructure.AuditEvent.AuditEventSummaryView.md#module) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 
  * [message](vdi.infrastructure.AuditEvent.AuditEventSummaryView.md#message) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md), [QueryFilterContains](vdi.query.QueryFilter.Contains.md), or [QueryFilterStartsWith](vdi.query.QueryFilter.StartsWith.md) filter only) 
  * [machineDnsName](vdi.infrastructure.AuditEvent.AuditEventSummaryView.md#machineDnsName) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md), [QueryFilterContains](vdi.query.QueryFilter.Contains.md), or [QueryFilterStartsWith](vdi.query.QueryFilter.StartsWith.md) filter only) 
  * [userId](vdi.infrastructure.AuditEvent.AuditEventSummaryView.md#userId) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 
  * [desktopId](vdi.infrastructure.AuditEvent.AuditEventSummaryView.md#desktopId) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 
  * [applicationId](vdi.infrastructure.AuditEvent.AuditEventSummaryView.md#applicationId) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 
  * [machineId](vdi.infrastructure.AuditEvent.AuditEventSummaryView.md#machineId) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 
  * [persistentDiskRefId](vdi.infrastructure.AuditEvent.AuditEventSummaryView.md#persistentDiskRefId) ([QueryFilterEquals](vdi.query.QueryFilter.Equals.md) filter only) 

The following caveats apply: 
  * This will consider the audit events summary from Event table only, and will not return events from historical database tables.
  * The first filter may be any of the above or an [QueryFilterAnd](vdi.query.QueryFilter.And.md) or [QueryFilterOr](vdi.query.QueryFilter.Or.md) filter specifying any combination of the above.
  * If [sortBy](vdi.query.QueryDefinition.md#sortBy) is not specified, resulting events will be sorted by [time](vdi.infrastructure.AuditEvent.AuditEventSummaryView.md#time).
  * [maxPageSize](vdi.query.QueryDefinition.md#maxPageSize) cannot exceed 1000.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**eventId**|  xsd:int|  ID of the event in Event Database.   
  
**eventType**|  xsd:string|  Event name that corresponds to an item in the message catalog. For example: BROKER_USERLOGGEDIN, AGENT_CONNECTED etc.   
  
**severity**|  xsd:string|  Severity type of the event.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"INFO"| INFO type.  
"WARNING"| WARNING type.  
"ERROR"| ERROR type.  
"AUDIT_SUCCESS"| AUDIT SUCCESS type.  
"AUDIT_FAIL"| AUDIT FAILURE type.  

  
**module**|  xsd:string|  Horizon View component that has logged this event.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"Admin"| Admin component.  
"Broker"| Broker component.  
"Client"| Client component.  
"Agent"| Agent component.  
"Vlsi"| Vlsi component.  
"Framework"| Framework component.  
"Tunnel"| Tunnel component.  
"Endpoint"| Endpoint component.  
"TransferServer"| TransferServer component.  
"Rest"| Rest component.  

  
**time**|  xsd:dateTime|  Time at which the event occurred, measured from the epoch (January 1, 1970).   
  
**machineDnsName**|  xsd:string|  FQDN of the machine in the Pod that has logged this event.   


 * This property need not be set.

  
**userId**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User involved in this event. Will be unset if there is no user association for this event.   


 * This property need not be set.

  
**desktopId**| [DesktopId](vdi.entity.DesktopId.md)|  Desktop pool associated with this event. Will be unset if there is no desktop association for this event.   


 * This property need not be set.

  
**applicationId**| [ApplicationId](vdi.entity.ApplicationId.md)|  Application associated with this event. Will be unset if there is no Application association for this event.   


 * This property need not be set.

  
**machineId**| [MachineId](vdi.entity.MachineId.md)|  Machine associated with this event. Will be unset if there is no machine association for this event.   


 * This property need not be set.

  
**sessionId**| [SessionId](vdi.entity.SessionId.md)|  Session associated with this event. Will be unset if there is no Session association for this event.   


 * This property need not be set.

  
**message**|  xsd:string|  Event message. Language of this message will be dependent on the locale. Locale can be set at request or session level. Request level locale can be provided by adding X-VIEW-LOCALE request header and session level locale can be set by invoking [AuthenticationManager_SetLocale](vdi.AuthenticationManager.md#setLocale) method after login. Request level locale will be given priority over session level locale. If not set explicitly, locale will default to English language.   
  
**userDisplayName**|  xsd:string|  Display name of the user associated with this event. Will be unset if there is no User association for this event.   


 * This property need not be set.

  
**persistentDiskId**| [PersistentDiskId](vdi.entity.PersistentDiskId.md)| **Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._ Persistent disk associated with this event. Will be unset if there is no Persistent disk association for this event.   


 * This property need not be set.

  
**persistentDiskRefId**|  xsd:string|  Persistent disk associated with this event. Will be unset if there is no Persistent disk association for this event.  **_Since_** Horizon 8.10  


 * This property need not be set.

  
**userSid**|  xsd:string|  Sid of the user associated with this event. Will be unset if there is no User association for this event.   


 * This property need not be set.

  
  

  

