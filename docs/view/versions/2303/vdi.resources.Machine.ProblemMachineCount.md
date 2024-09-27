---
layout: page
title: Data Object - ProblemMachineCount
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Machine.ProblemMachineCount  
Property of
     [StateCount](vdi.resources.Machine.StateCount.md#field_detail)  
Since 
    Horizon 8.4

## Data Object Description 

Number of the machines which are in problem states. Such machine's [basicState](vdi.resources.Machine.MachineBase.md#basicState) is one of the following : AGENT_ERR_DISABLED, AGENT_UNREACHABLE, AGENT_ERR_INVALID_IP, AGENT_ERR_NEED_REBOOT, AGENT_ERR_PROTOCOL_FAILURE, AGENT_ERR_DOMAIN_FAILURE, AGENT_CONFIG_ERROR, PROVISIONING_ERROR, ERROR, UNASSIGNED_USER_CONNECTED, UNASSIGNED_USER_DISCONNECTED, UNKNOWN. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**agentDisabled**|  xsd:int|  Number of machines which are in AGENT_ERR_DISABLED [basicState](vdi.resources.Machine.MachineBase.md#basicState)   


* This property cannot be updated.

  
**agentUnreachable**|  xsd:int|  Number of machines which are in AGENT_UNREACHABLE [basicState](vdi.resources.Machine.MachineBase.md#basicState)   


* This property cannot be updated.

  
**invalidIp**|  xsd:int|  Number of machines which are in AGENT_ERR_INVALID_IP [basicState](vdi.resources.Machine.MachineBase.md#basicState)   


* This property cannot be updated.

  
**needReboot**|  xsd:int|  Number of machines which are in AGENT_ERR_NEED_REBOOT [basicState](vdi.resources.Machine.MachineBase.md#basicState)   


* This property cannot be updated.

  
**protocolFailure**|  xsd:int|  Number of machines which are in AGENT_ERR_PROTOCOL_FAILURE [basicState](vdi.resources.Machine.MachineBase.md#basicState)   


* This property cannot be updated.

  
**domainFailure**|  xsd:int|  Number of machines which are in AGENT_ERR_DOMAIN_FAILURE [basicState](vdi.resources.Machine.MachineBase.md#basicState)   


* This property cannot be updated.

  
**configError**|  xsd:int|  Number of machines which are in AGENT_CONFIG_ERROR [basicState](vdi.resources.Machine.MachineBase.md#basicState)   


* This property cannot be updated.

  
**unassignedUserConnected**|  xsd:int|  Number of machines which are in UNASSIGNED_USER_CONNECTED [basicState](vdi.resources.Machine.MachineBase.md#basicState).   


* This property cannot be updated.

  
**unassignedUserDisconnected**|  xsd:int|  Number of machines which are in UNASSIGNED_USER_DISCONNECTED [basicState](vdi.resources.Machine.MachineBase.md#basicState).   


* This property cannot be updated.

  
**provisioningError**|  xsd:int|  Number of machines which are in PROVISIONING_ERROR [basicState](vdi.resources.Machine.MachineBase.md#basicState). Applicable only for VC managed virtual machines.   


* This property cannot be updated.

  
**error**|  xsd:int|  Number of machines which are in ERROR [basicState](vdi.resources.Machine.MachineBase.md#basicState). Applicable only for VC managed virtual machines.   


* This property cannot be updated.

  
**unknown**|  xsd:int|  Number of machines which are in UNKNOWN [basicState](vdi.resources.Machine.MachineBase.md#basicState).   


* This property cannot be updated.

  
**alreadyUsed**|  xsd:int|  Number of machines which are in ALREADY_USED [basicState](vdi.resources.Machine.MachineBase.md#basicState). Applicable only for VC managed virtual machines.   


* This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

