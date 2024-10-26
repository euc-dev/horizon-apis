---
layout: page
title: Data Object - EventData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.EventDatabase.EventData`

Property of
> [EventSummaryView](vdi.infrastructure.EventDatabase.EventSummaryView.md#field_detail)

See also
> [ApplicationId](vdi.entity.ApplicationId.md), [DesktopId](vdi.entity.DesktopId.md), [FarmId](vdi.entity.FarmId.md), [MachineId](vdi.entity.MachineId.md), [PersistentDiskId](vdi.entity.PersistentDiskId.md), [RDSServerId](vdi.entity.RDSServerId.md), [SessionId](vdi.entity.SessionId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon 7.3


## Data Object Description

The Event data Object. This contains all the attributes related to a particular event.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**eventType**|  xsd:string|  Event name that corresponds to an item in the message catalog. For example: BROKER_USERLOGGEDIN, AGENT_CONNECTED etc.
**severity**|  xsd:string|  Severity type of the event.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"INFO"</td><td>INFO type.</td></tr><tr><td>"WARNING"</td><td>WARNING type.</td></tr><tr><td>"ERROR"</td><td>ERROR type.</td></tr><tr><td>"AUDIT_SUCCESS"</td><td>AUDIT SUCCESS type.</td></tr><tr><td>"AUDIT_FAIL"</td><td>AUDIT FAILURE type.</td></tr></table>
**time**|  xsd:dateTime|  Time at which the event occurred, measured from the epoch (January 1, 1970).
**module**|  xsd:string|  Horizon View component that has logged this event.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"Admin"</td><td>Admin component.</td></tr><tr><td>"Broker"</td><td>Broker component.</td></tr><tr><td>"Client"</td><td>Client component.</td></tr><tr><td>"Agent"</td><td>Agent component.</td></tr><tr><td>"Vlsi"</td><td>Vlsi component.</td></tr><tr><td>"Framework"</td><td>Framework component.</td></tr><tr><td>"Tunnel"</td><td>Tunnel component.</td></tr><tr><td>"Endpoint"</td><td>Endpoint component.</td></tr><tr><td>"TransferServer"</td><td>TransferServer component.</td></tr><tr><td>"Rest"</td><td>Rest component.</td></tr></table>
**message**|  xsd:string|  Event message. Language of this message will be dependent on the locale of the currently logged-in user. Locale can be set by invoking [AuthenticationManager_SetLocale](vdi.AuthenticationManager.md#setLocale) method after login. If not set explicitly, locale will default to English language.
**node**|  xsd:string|  FQDN of the machine in the Pod that has logged this event. [^1]
**userId**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User involved in this event. Will be unset if there is no user association for this event. [^1]
**desktopId**| [DesktopId](vdi.entity.DesktopId.md)|  Desktop pool associated with this event. Will be unset if there is no desktop association for this event. [^1]
**applicationId**| [ApplicationId](vdi.entity.ApplicationId.md)|  Application associated with this event. Will be unset if there is no Application association for this event. [^1]
**machineId**| [MachineId](vdi.entity.MachineId.md)|  Machine associated with this event. Will be unset if there is no machine association for this event. [^1]
**rdsServerId**| [RDSServerId](vdi.entity.RDSServerId.md)|  RDS Server associated with this event. Will be unset if there is no RDS server association for this event. [^1]
**farmId**| [FarmId](vdi.entity.FarmId.md)|  Farm associated with this event. Will be unset if there is no Farm association for this event. [^1]
**sessionId**| [SessionId](vdi.entity.SessionId.md)|  Session associated with this event. Will be unset if there is no Session association for this event. [^1]
**logonTiming**|  xsd:string|  Logon timing profiler tree. Will be unset if there is no timing profiler tree association for this event. [^1]
**persistentDiskId**| [PersistentDiskId](vdi.entity.PersistentDiskId.md)|  Persistent disk associated with this event. Will be unset if there is no Persistent disk association for this event.  **_Since_** Horizon 7.9 [^1]


 
