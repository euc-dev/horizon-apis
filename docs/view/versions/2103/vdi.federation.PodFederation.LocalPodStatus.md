---
layout: page
title: Data Object - PodFederationLocalPodStatus
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.federation.PodFederation.LocalPodStatus`

Property of
> [PodFederationInfo](vdi.federation.PodFederation.PodFederationInfo.md#field_detail)

See also
> [PodFederationLocalConnectionServerStatus](vdi.federation.PodFederation.LocalConnectionServerStatus.md)

Since
> Horizon View 6.0


## Data Object Description

Multi-DataCenter View status for the local Pod.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**status**|  xsd:string|  The Multi-DataCenter View status for the local Pod.
* This property will be one of:
|  Value |  Description
---|---
"ENABLED"| Multi-DataCenter View is enabled.
"DISABLED"| Multi-DataCenter View is disabled.
"PENDING"| Multi-DataCenter View is undergoing an operation related to initialization, uninitialization, joining, or unjoining.
"ENABLE_ERROR"| This status indicates the current Connection Server has failed to reach the ENABLED status in a timely manner. Other Connection Servers in the same Pod were successfully ENABLED. This status may also indicate the current Connection Server was recently installed.
"DISABLE_ERROR"| This status indicates the current Connection Server has failed to reach the DISABLED status in a timely manner. Other Connection Servers in the same Pod were successfully DISABLED.
**localConnectionServerStatuses**| [PodFederationLocalConnectionServerStatus[]](vdi.federation.PodFederation.LocalConnectionServerStatus.md)|  Individual Connection Server Multi-DataCenter View statuses for this pod. Null if insufficient permission to read Connection Server settings. [^1]


 
