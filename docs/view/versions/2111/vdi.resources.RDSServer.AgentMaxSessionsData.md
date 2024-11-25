---
layout: page
title: Data Object - RDSServerAgentMaxSessionsData
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.resources.RDSServer.AgentMaxSessionsData`

Property of
> [RDSServerSettings](vdi.resources.RDSServer.RDSServerSettings.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Agent max number of sessions

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**maxSessionsType**|  xsd:string|  RDSServer max sessions type as reported by the agent [^113] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>UNLIMITED</td><td>RDSServer has unlimited number of sessions</td></tr><tr><td>LIMITED</td><td>RDSServer has a limited number of sessions</td></tr></table>
**maxSessionsSeenByAgent**|  xsd:int|  Maximum number of sessions on an RDS server as seen by the agent. [^1] [^2] [^8] [^9]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^8]: This property has a minimum value of 1.
[^9]: This property is required if maxSessionsType is set to 'LIMITED'.
[^113]: This property has a default value of 'LIMITED'.