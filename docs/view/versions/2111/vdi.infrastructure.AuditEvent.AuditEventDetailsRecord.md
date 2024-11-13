---
layout: page
title: Data Object - AuditEventDetailsRecord
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.infrastructure.AuditEvent.AuditEventDetailsRecord`

Returned by
> [AuditEventDetails](vdi.infrastructure.AuditEvent.md#auditEventDetails)

See also
> [RDSServerId](vdi.entity.RDSServerId.md)


## Data Object Description

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**eventId**|  xsd:int|  ID of the event in Event Database.
**desktopName**|  xsd:string|  Name of the Desktop associated with this event. This refers to the unique name used to identify the Desktop. Will be unset if there is no Desktop association for this event. [^1]
**desktopDisplayName**|  xsd:string|  Display name of the Desktop associated with this event. Will be unset if there is no Desktop association for this event. [^1]
**applicationName**|  xsd:string|  Name of the Application associated with this event. This refers to the unique name used to identify the Application. Will be unset if there is no Application association for this event. [^1]
**applicationDisplayName**|  xsd:string|  Display name of the Application associated with this event. Will be unset if there is no Application association for this event. [^1]
**machineName**|  xsd:string|  Name of the Machine associated with this event. Will be unset if there is no Machine association for this event. [^1]
**machineGuid**|  xsd:string|  Guid of the Machine associated with this event. Will be unset if there is no Machine association for this event. [^1]
**farmName**|  xsd:string|  Name of the Farm associated with this event. Will be unset if there is no Farm association for this event. [^1]
**farmDisplayName**|  xsd:string|  Display name of the Farm associated with this event. Will be unset if there is no Farm association for this event. [^1]
**endUserDisplayName**|  xsd:string|  Display name of the end user associated with this event. Will be unset if there is no End User association for this event. [^1]
**thinappDisplayName**|  xsd:string|  Display name of the Thinapp associated with this event. Will be unset if there is no Thinapp association for this event. [^1]
**processId**|  xsd:int|  Id of the remote process associated with this event. Will be unset if there is no process association for this event. [^1]
**processName**|  xsd:string|  Name of the remote process associated with this event. Will be unset if there is no process association for this event. [^1]
**remoteApplicationDescription**|  xsd:string|  Description of the remote application associated with this event. Will be unset if there is no application association for this event. [^1]
**remoteApplicationId**|  xsd:string|  Id of the remote application associated with this event. Will be unset if there is no application association for this event. [^1]
**persistentDiskName**|  xsd:string|  Name of the Persistent disk associated with this event. Will be unset if there is no Persistent disk association for this event. [^1]
**rdsServerId**| [RDSServerId](vdi.entity.RDSServerId.md)|  RDS Server associated with this event. Will be unset if there is no RDS server association for this event. [^1]


 


[^1]: This property need not be set.