---
layout: page
title: Data Object - UnderConstructionCount
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.RDSServer.UnderConstructionCount`

Property of
> [RDSServerStateCount](vdi.resources.RDSServer.RDSServerStateCount.md#field_detail)

Since
> Horizon 8.4


## Data Object Description

Number of the RDS server machines which are in under construction states. Such machine's [status](vdi.resources.RDSServer.RDSServerStateView.md#status) is one of the following : PROVISIONING,CUSTOMIZING,MAINTENANCE,DELETING,WAIT_FOR_AGENT,AGENT_ERR_STARTUP_IN_PROGRESS, AGENT_DRAIN_MODE,AGENT_DRAIN_UNTIL_RESTART,DISABLED,DISABLE_IN_PROGRESS,VALIDATING,AGENT_ERR_WAIT_FOR_HYBRID_JOIN

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**provisioning**|  xsd:int|  Number of RDS server machines which are in PROVISIONING [status](vdi.resources.RDSServer.RDSServerStateView.md#status) [^2]
**customizing**|  xsd:int|  Number of RDS server machines which are in CUSTOMIZING [status](vdi.resources.RDSServer.RDSServerStateView.md#status) [^2]
**maintenance**|  xsd:int|  Number of RDS server machines which are in MAINTENANCE [status](vdi.resources.RDSServer.RDSServerStateView.md#status) [^2]
**deleting**|  xsd:int|  Number of RDS server machines which are in DELETING [status](vdi.resources.RDSServer.RDSServerStateView.md#status) [^2]
**drainModeEnabled**|  xsd:int|  Number of RDS server machines which are in AGENT_DRAIN_MODE [status](vdi.resources.RDSServer.RDSServerStateView.md#status) [^2]
**drainModeRestart**|  xsd:int|  Number of RDS server machines which are in AGENT_DRAIN_UNTIL_RESTART [status](vdi.resources.RDSServer.RDSServerStateView.md#status) [^2]
**disabled**|  xsd:int|  Number of RDS server machines which are in DISABLED [status](vdi.resources.RDSServer.RDSServerStateView.md#status) [^2]
**disableProgress**|  xsd:int|  Number of RDS server machines which are in DISABLE_IN_PROGRESS [status](vdi.resources.RDSServer.RDSServerStateView.md#status) [^2]
**waitForAgent**|  xsd:int|  Number of RDS server machines which are in WAIT_FOR_AGENT [status](vdi.resources.RDSServer.RDSServerStateView.md#status) [^2]
**startupProgress**|  xsd:int|  Number of RDS server machines which are in AGENT_ERR_STARTUP_IN_PROGRESS [status](vdi.resources.RDSServer.RDSServerStateView.md#status) [^2]
**validating**|  xsd:int|  Number of RDS server machines which are in VALIDATING [status](vdi.resources.RDSServer.RDSServerStateView.md#status) [^2]
**waitForHybridDomainJoin**|  xsd:int|  Number of RDS server machines which are in AGENT_ERR_WAIT_FOR_HYBRID_JOIN [status](vdi.resources.RDSServer.RDSServerStateView.md#status) **_Since_** Horizon 8.13 [^2]


 


[^2]: This property cannot be updated.