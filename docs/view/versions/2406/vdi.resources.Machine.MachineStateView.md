---
layout: page
title: Data Object - MachineStateView
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Machine.MachineStateView`

See also
> [DesktopId](vdi.entity.DesktopId.md), [MachineId](vdi.entity.MachineId.md)

Since
> Horizon 7.7


## Data Object Description

This View includes baseState, powerState, dnsName and IP address of this Machine.

##  Queryable Data Object

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService").

Can filter on the all MachineStateView attributes.

Query Privileges

Privilege |  Description
---|---
MACHINE_VIEW|  is required to query MachineStateView.



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [MachineId](vdi.entity.MachineId.md)|  The id of the Machine. [^2]
**desktop**| [DesktopId](vdi.entity.DesktopId.md)|  The desktop id of the Machine. [^1] [^2]
**basicState**|  xsd:string|  The basic state of the Machine. For a Virtual Machine based Machine, the complete state is determined by basicState, isMissingInVCenter, operationState and isInHoldCustomization. In the Admin UI, the last three states are shown in brackets in the Machine State. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"PROVISIONING"</td><td>The virtual machine is being provisioned</td></tr><tr><td>"PROVISIONING_ERROR"</td><td>An error occurred during provisioning.</td></tr><tr><td>"WAIT_FOR_AGENT"</td><td>View Connection Server is waiting to establish communication with View Agent for one of these cases - a virtual machine in a manual desktop, unmanaged machine or terminal server.</td></tr><tr><td>"CUSTOMIZING"</td><td>The virtual machine in automated/provisioned desktop is being customized</td></tr><tr><td>"DELETING"</td><td>The virtual machine is marked for deletion. View Manager will delete the virtual machine soon.</td></tr><tr><td>"MAINTENANCE"</td><td>The virtual machine is in maintenance mode. Users cannot log in or use the virtual machine</td></tr><tr><td>"ERROR"</td><td>An unknown error occurred in the virtual machine.</td></tr><tr><td>"PROVISIONED"</td><td>The virtual machine is powered off or suspended.</td></tr><tr><td>"AGENT_UNREACHABLE"</td><td>View Connection Server cannot establish communication with View Agent on a virtual machine</td></tr><tr><td>"UNASSIGNED_USER_CONNECTED"</td><td>A user other than the assigned user is logged in to a virtual machine in a dedicated desktop</td></tr><tr><td>"CONNECTED"</td><td>The virtual machine is in an active session and has an active remote connection to a View client</td></tr><tr><td>"UNASSIGNED_USER_DISCONNECTED"</td><td>A user other than the assigned user is logged in and disconnected from a virtual machine in a dedicated desktop.</td></tr><tr><td>"DISCONNECTED"</td><td>The virtual machine is in an active session, but it is disconnected from the View client</td></tr><tr><td>"AGENT_ERR_STARTUP_IN_PROGRESS"</td><td>View Agent has started on the virtual machine, but other required services such as the display protocol are still starting</td></tr><tr><td>"AGENT_ERR_WAIT_FOR_HYBRID_JOIN"</td><td>View Agent is waiting for hybrid domain join</td></tr><tr><td>"AGENT_ERR_DISABLED"</td><td>View Agent is disabled</td></tr><tr><td>"AGENT_ERR_INVALID_IP"</td><td>View Agent has invalid IP</td></tr><tr><td>"AGENT_ERR_NEED_REBOOT"</td><td>View Agent needs reboot.</td></tr><tr><td>"AGENT_ERR_PROTOCOL_FAILURE"</td><td>Protocol such as RDP or PCoIP is not enabled.</td></tr><tr><td>"AGENT_ERR_DOMAIN_FAILURE"</td><td>View Agent has invalid domain.</td></tr><tr><td>"AGENT_CONFIG_ERROR"</td><td>The Remote Desktop Services role is not enabled.</td></tr><tr><td>"AGENT_DRAIN_MODE"</td><td>RDS host is configured for drain mode</td></tr><tr><td>"AGENT_DRAIN_UNTIL_RESTART"</td><td>RDS host is configured for drain until restart mode</td></tr><tr><td>"ALREADY_USED"</td><td>The virtual machine is configured to have only one session which is currently in progress and cannot accept new sessions</td></tr><tr><td>"AVAILABLE"</td><td>The virtual machine is powered on and ready for an active connection.</td></tr><tr><td>"IN_PROGRESS"</td><td>There is a virtual machine operation in-progress.</td></tr><tr><td>"DISABLED"</td><td>The machine is disabled</td></tr><tr><td>"DISABLE_IN_PROGRESS"</td><td>Disabled server still has some view brokered sessions. It can still accept re-connections</td></tr><tr><td>"VALIDATING"</td><td>The connection server is synchronizing state information with the agent.</td></tr><tr><td>"BLOCKED_AGENT_VERSION"</td><td>The agent version is blocked from establishing sessions.</td></tr><tr><td>"UNKNOWN"</td><td>Could not determine the state of the virtual machine.</td></tr></table>
**machinePowerState**|  xsd:string|  PowerState of the machine. [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"POWERED_OFF"</td><td></td></tr><tr><td>"POWERED_ON"</td><td>The virtual machine is powered on.</td></tr><tr><td>"SUSPENDED"</td><td>The virtual machine is suspended.</td></tr></table>
**ipV4**|  xsd:string|  IPV4 address of the machine. [^1] [^2]
**ipV6**|  xsd:string|  IPV6 address of the machine. [^1] [^2]
**dnsName**|  xsd:string|  DNS name of the machine. [^1] [^2]
**agentId**|  xsd:string|  agent Identity of the machine. [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.