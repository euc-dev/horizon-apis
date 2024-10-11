---
layout: page
title: Data Object - RegisteredPhysicalMachineInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.RegisteredPhysicalMachine.RegisteredPhysicalMachineInfo`

Returned by  
> [RegisteredPhysicalMachine_Get](vdi.resources.RegisteredPhysicalMachine.md#get)

See also  
> [MachineId](vdi.entity.MachineId.md), [RegisteredPhysicalMachineBase](vdi.resources.RegisteredPhysicalMachine.RegisteredPhysicalMachineBase.md), [RegisteredPhysicalMachineMessageSecurityData](vdi.resources.RegisteredPhysicalMachine.MessageSecurityData.md)

Since  
> Horizon View 6.0


## Data Object Description 

This has list of attributes that is for an unmanaged physical Machine. 

##  Queryable Data Object 

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService"). 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [MachineId](vdi.entity.MachineId.md)|  Client reference to a specific RegisteredPhysicalMachine instance.   


 * This property cannot be updated.

  
**status**|  xsd:string|  The status of the Machine.   


 * This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"AGENT_UNREACHABLE"| View Connection Server cannot establish communication with View Agent on a virtual machine  
"UNASSIGNED_USER_CONNECTED"| A user other than the assigned user is logged in to a virtual machine in a dedicated desktop  
"CONNECTED"| The virtual machine is in an active session and has an active remote connection to a View client  
"UNASSIGNED_USER_DISCONNECTED"| A user other than the assigned user is logged in and disconnected from a virtual machine in a dedicated desktop.  
"DISCONNECTED"| The virtual machine is in an active session, but it is disconnected from the View client  
"AGENT_ERR_STARTUP_IN_PROGRESS"| View Agent has started on the virtual machine, but other required services such as the display protocol are still starting  
"AGENT_ERR_DISABLED"| View Agent is disabled  
"AGENT_ERR_INVALID_IP"| View Agent has invalid IP  
"AGENT_ERR_NEED_REBOOT"| View Agent needs reboot.  
"AGENT_ERR_PROTOCOL_FAILURE"| Protocol such as RDP or PCoIP is not enabled.  
"AGENT_ERR_DOMAIN_FAILURE"| View Agent has invalid domain.  
"AGENT_CONFIG_ERROR"| The Remote Desktop Services role is not enabled.  
"AVAILABLE"| The virtual machine is powered on and ready for an active connection.  
"VALIDATING"| The connection server is synchronizing state information with the agent.  
"UNKNOWN"| Could not determine the state of the virtual machine.  

  
**machineBase**| [RegisteredPhysicalMachineBase](vdi.resources.RegisteredPhysicalMachine.RegisteredPhysicalMachineBase.md)|  The MachineBase attributes.   


 * This property cannot be updated.

  
**messageSecurityData**| [RegisteredPhysicalMachineMessageSecurityData](vdi.resources.RegisteredPhysicalMachine.MessageSecurityData.md)|  Message security data for this registered physical machine.  **_Since_** Horizon View 6.1  


 * This property cannot be updated.

  
**refId**|  xsd:string|  Reference ID used for this machine.  **_Since_** Horizon 8.1  


 * This property need not be set.
 * This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
