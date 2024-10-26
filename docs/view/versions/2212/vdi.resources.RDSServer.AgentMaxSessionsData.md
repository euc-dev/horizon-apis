---
layout: page
title: Data Object - RDSServerAgentMaxSessionsData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.RDSServer.AgentMaxSessionsData`

Property of
> [RDSServerSettings](vdi.resources.RDSServer.RDSServerSettings.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Agent max number of sessions

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**maxSessionsType**|  xsd:string|  RDSServer max sessions type as reported by the agent [^113] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>UNLIMITED</td><td>RDSServer has unlimited number of sessions</td></tr><tr><td>LIMITED</td><td>RDSServer has a limited number of sessions</td></tr></table>
**maxSessionsSeenByAgent**|  xsd:int|  Maximum number of sessions on an RDS server as seen by the agent. [^1] [^2] [^8] [^9]


 
