---
layout: page
title: Data Object - ProblemMachineCount
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Machine.ProblemMachineCount`

Property of
> [StateCount](vdi.resources.Machine.StateCount.md#field_detail)

Since
> Horizon 8.4


## Data Object Description

Number of the machines which are in problem states. Such machine's [basicState](vdi.resources.Machine.MachineBase.md#basicState) is one of the following : AGENT_ERR_DISABLED, AGENT_UNREACHABLE, AGENT_ERR_INVALID_IP, AGENT_ERR_NEED_REBOOT, AGENT_ERR_PROTOCOL_FAILURE, AGENT_ERR_DOMAIN_FAILURE, AGENT_CONFIG_ERROR, PROVISIONING_ERROR, ERROR, UNASSIGNED_USER_CONNECTED, UNASSIGNED_USER_DISCONNECTED, UNKNOWN.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**agentDisabled**|  xsd:int|  Number of machines which are in AGENT_ERR_DISABLED [basicState](vdi.resources.Machine.MachineBase.md#basicState) [^2]
**agentUnreachable**|  xsd:int|  Number of machines which are in AGENT_UNREACHABLE [basicState](vdi.resources.Machine.MachineBase.md#basicState) [^2]
**invalidIp**|  xsd:int|  Number of machines which are in AGENT_ERR_INVALID_IP [basicState](vdi.resources.Machine.MachineBase.md#basicState) [^2]
**needReboot**|  xsd:int|  Number of machines which are in AGENT_ERR_NEED_REBOOT [basicState](vdi.resources.Machine.MachineBase.md#basicState) [^2]
**protocolFailure**|  xsd:int|  Number of machines which are in AGENT_ERR_PROTOCOL_FAILURE [basicState](vdi.resources.Machine.MachineBase.md#basicState) [^2]
**domainFailure**|  xsd:int|  Number of machines which are in AGENT_ERR_DOMAIN_FAILURE [basicState](vdi.resources.Machine.MachineBase.md#basicState) [^2]
**configError**|  xsd:int|  Number of machines which are in AGENT_CONFIG_ERROR [basicState](vdi.resources.Machine.MachineBase.md#basicState) [^2]
**unassignedUserConnected**|  xsd:int|  Number of machines which are in UNASSIGNED_USER_CONNECTED [basicState](vdi.resources.Machine.MachineBase.md#basicState). [^2]
**unassignedUserDisconnected**|  xsd:int|  Number of machines which are in UNASSIGNED_USER_DISCONNECTED [basicState](vdi.resources.Machine.MachineBase.md#basicState). [^2]
**provisioningError**|  xsd:int|  Number of machines which are in PROVISIONING_ERROR [basicState](vdi.resources.Machine.MachineBase.md#basicState). Applicable only for VC managed virtual machines. [^2]
**error**|  xsd:int|  Number of machines which are in ERROR [basicState](vdi.resources.Machine.MachineBase.md#basicState). Applicable only for VC managed virtual machines. [^2]
**unknown**|  xsd:int|  Number of machines which are in UNKNOWN [basicState](vdi.resources.Machine.MachineBase.md#basicState). [^2]
**alreadyUsed**|  xsd:int|  Number of machines which are in ALREADY_USED [basicState](vdi.resources.Machine.MachineBase.md#basicState). Applicable only for VC managed virtual machines. [^2]
 


 


[^2]: This property cannot be updated.