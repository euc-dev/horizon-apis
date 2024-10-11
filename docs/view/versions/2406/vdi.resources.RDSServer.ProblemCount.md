---
layout: page
title: Data Object - ProblemCount
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.RDSServer.ProblemCount`

Property of  
> [RDSServerStateCount](vdi.resources.RDSServer.RDSServerStateCount.md#field_detail)

Since  
> Horizon 8.4


## Data Object Description 

Number of the RDS server machines which are in problem states. Such machine's [status](vdi.resources.RDSServer.RDSServerStateView.md#status) is one of the following : AGENT_ERR_DISABLED, AGENT_UNREACHABLE, AGENT_ERR_INVALID_IP, AGENT_ERR_NEED_REBOOT, AGENT_ERR_PROTOCOL_FAILURE, AGENT_ERR_DOMAIN_FAILURE, AGENT_CONFIG_ERROR, PROVISIONING_ERROR, ERROR, ALREADY_USED, UNKNOWN. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**agentDisabled**|  xsd:int|  Number of RDS server machines which are in AGENT_ERR_DISABLED [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
**agentUnreachable**|  xsd:int|  Number of RDS server machines which are in AGENT_UNREACHABLE [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
**invalidIp**|  xsd:int|  Number of RDS server machines which are in AGENT_ERR_INVALID_IP [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
**needReboot**|  xsd:int|  Number of RDS server machines which are in AGENT_ERR_NEED_REBOOT [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
**protocolFailure**|  xsd:int|  Number of RDS server machines which are in AGENT_ERR_PROTOCOL_FAILURE [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
**domainFailure**|  xsd:int|  Number of RDS server machines which are in AGENT_ERR_DOMAIN_FAILURE [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
**configError**|  xsd:int|  Number of RDS server machines which are in AGENT_CONFIG_ERROR [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
**provisioningError**|  xsd:int|  Number of RDS server machines which are in PROVISIONING_ERROR [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
**error**|  xsd:int|  Number of RDS server machines which are in ERROR [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
**unknown**|  xsd:int|  Number of RDS server machines which are in UNKNOWN [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
**alreadyUsed**|  xsd:int|  Number of RDS server machines which are in ALREADY_USED [status](vdi.resources.RDSServer.RDSServerStateView.md#status)   


 * This property cannot be updated.

  
**blockedAgentVersion**|  xsd:int|  Number of RDS server machines which are in BLOCKED_AGENT_VERSION [status](vdi.resources.RDSServer.RDSServerStateView.md#status) **_Since_** Horizon 8.10  


 * This property cannot be updated.

  
  

  
