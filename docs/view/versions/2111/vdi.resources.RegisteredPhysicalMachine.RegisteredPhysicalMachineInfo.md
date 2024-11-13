---
layout: page
title: Data Object - RegisteredPhysicalMachineInfo
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.resources.RegisteredPhysicalMachine.RegisteredPhysicalMachineInfo`

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
**id**| [MachineId](vdi.entity.MachineId.md)|  Client reference to a specific RegisteredPhysicalMachine instance. [^2]
**status**|  xsd:string|  The status of the Machine. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>AGENT_UNREACHABLE</td><td>View Connection Server cannot establish communication with View Agent on a virtual machine</td></tr><tr><td>UNASSIGNED_USER_CONNECTED</td><td>A user other than the assigned user is logged in to a virtual machine in a dedicated desktop</td></tr><tr><td>CONNECTED</td><td>The virtual machine is in an active session and has an active remote connection to a View client</td></tr><tr><td>UNASSIGNED_USER_DISCONNECTED</td><td>A user other than the assigned user is logged in and disconnected from a virtual machine in a dedicated desktop.</td></tr><tr><td>DISCONNECTED</td><td>The virtual machine is in an active session, but it is disconnected from the View client</td></tr><tr><td>AGENT_ERR_STARTUP_IN_PROGRESS</td><td>View Agent has started on the virtual machine, but other required services such as the display protocol are still starting</td></tr><tr><td>AGENT_ERR_DISABLED</td><td>View Agent is disabled</td></tr><tr><td>AGENT_ERR_INVALID_IP</td><td>View Agent has invalid IP</td></tr><tr><td>AGENT_ERR_NEED_REBOOT</td><td>View Agent needs reboot.</td></tr><tr><td>AGENT_ERR_PROTOCOL_FAILURE</td><td>Protocol such as RDP or PCoIP is not enabled.</td></tr><tr><td>AGENT_ERR_DOMAIN_FAILURE</td><td>View Agent has invalid domain.</td></tr><tr><td>AGENT_CONFIG_ERROR</td><td>The Remote Desktop Services role is not enabled.</td></tr><tr><td>AVAILABLE</td><td>The virtual machine is powered on and ready for an active connection.</td></tr><tr><td>VALIDATING</td><td>The connection server is synchronizing state information with the agent.</td></tr><tr><td>UNKNOWN</td><td>Could not determine the state of the virtual machine.</td></tr></table>
**machineBase**| [RegisteredPhysicalMachineBase](vdi.resources.RegisteredPhysicalMachine.RegisteredPhysicalMachineBase.md)|  The MachineBase attributes. [^2]
**messageSecurityData**| [RegisteredPhysicalMachineMessageSecurityData](vdi.resources.RegisteredPhysicalMachine.MessageSecurityData.md)|  Message security data for this registered physical machine.  **_Since_** Horizon View 6.1 [^2]
**refId**|  xsd:string|  Reference ID used for this machine.  **_Since_** Horizon 8.1 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.