---
layout: page
title: Data Object - RDSServerSettings
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.resources.RDSServer.RDSServerSettings`

Property of
> [RDSServerInfo](vdi.resources.RDSServer.RDSServerInfo.md#field_detail), [RDSServerSummaryView](vdi.resources.RDSServer.RDSServerSummaryView.md#field_detail)

See also
> [RDSServerAgentMaxSessionsData](vdi.resources.RDSServer.AgentMaxSessionsData.md), [RDSServerSessionSettings](vdi.resources.RDSServer.RDSServerSessionSettings.md)

Since
> Horizon View 6.0


## Data Object Description

RDS Server settings

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**sessionSettings**| [RDSServerSessionSettings](vdi.resources.RDSServer.RDSServerSessionSettings.md)|  RDSServer session settings
**agentMaxSessionsData**| [RDSServerAgentMaxSessionsData](vdi.resources.RDSServer.AgentMaxSessionsData.md)|  Max number of sessions as seen by the agent [^2]
**enabled**|  xsd:boolean|  Indicates if RDS server is enabled [^6]


 


[^2]: This property cannot be updated.
[^6]: This property has a default value of true.