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
**status**|  xsd:string|  The Multi-DataCenter View status for this Connection Server. Individual connection server statuses should converge to the containing Pod's status over time.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"ENABLED"</td><td>Multi-DataCenter View is enabled.</td></tr><tr><td>"DISABLED"</td><td>Multi-DataCenter View is disabled.</td></tr><tr><td>"PENDING"</td><td>Multi-DataCenter View is undergoing an operation related to initialization, uninitialization, joining, or unjoining.</td></tr><tr><td>"ENABLE_ERROR"</td><td>This status indicates the current Connection Server has failed to reach the ENABLED status in a timely manner. Other Connection Servers in the same Pod were successfully ENABLED. This status may also indicate the current Connection Server was recently installed.</td></tr><tr><td>"DISABLE_ERROR"</td><td>This status indicates the current Connection Server has failed to reach the DISABLED status in a timely manner. Other Connection Servers in the same Pod were successfully DISABLED.</td></tr></table>
**localConnectionServerStatuses**| [PodFederationLocalConnectionServerStatus[]](vdi.federation.PodFederation.LocalConnectionServerStatus.md)|  Individual Connection Server Multi-DataCenter View statuses for this pod. Null if insufficient permission to read Connection Server settings. [^1]


 


[^1]: This property need not be set.