---
layout: page
title: Data Object - PodFederationLocalConnectionServerStatus
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.federation.PodFederation.LocalConnectionServerStatus`

Property of
> [PodFederationLocalPodStatus](vdi.federation.PodFederation.LocalPodStatus.md#field_detail)

See also
> [ConnectionServerId](vdi.entity.ConnectionServerId.md), [MapEntry](vdi.util.MapEntry.md)

Since
> Horizon View 6.0


## Data Object Description

Multi-DataCenter View status for a Connection Server.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [ConnectionServerId](vdi.entity.ConnectionServerId.md)|  Entity id of the connection server to which this status pertains.
**name**|  xsd:string|  Name of the connection server  **_Since_** Horizon 7.8
**status**|  xsd:string|  The Multi-DataCenter View status for this Connection Server. Individual connection server statuses should converge to the containing Pod's status over time.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"ENABLED"</td><td>Multi-DataCenter View is enabled.</td></tr><tr><td>"DISABLED"</td><td>Multi-DataCenter View is disabled.</td></tr><tr><td>"PENDING"</td><td>Multi-DataCenter View is undergoing an operation related to initialization, uninitialization, joining, or unjoining.</td></tr><tr><td>"ENABLE_ERROR"</td><td>This status indicates the current Connection Server has failed to reach the ENABLED status in a timely manner. Other Connection Servers in the same Pod were successfully ENABLED. This status may also indicate the current Connection Server was recently installed.</td></tr><tr><td>"DISABLE_ERROR"</td><td>This status indicates the current Connection Server has failed to reach the DISABLED status in a timely manner. Other Connection Servers in the same Pod were successfully DISABLED.</td></tr></table>
**pendingPercentage**|  xsd:int|  Value between 0 and 100 representing completion percentage when Connection Server status is pending. Null in other status states. [^1]
**errorMessage**|  xsd:string|  The Multi-DataCenter View error message for this Connection Server, if any is populated, or a success message. [^1]
**errorMessageId**|  xsd:string|  Message ID of the error message. [^1]
**errorMessageValues**| [MapEntry[]](vdi.util.MapEntry.md)|  The error message values. [^1] [^227]


 


[^1]: This property need not be set.
[^227]: This property is a set of entries with unique "key" members.