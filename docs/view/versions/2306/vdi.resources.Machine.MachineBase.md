---
layout: page
title: Data Object - MachineBase
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Machine.MachineBase`

Property of
> [MachineInfo](vdi.resources.Machine.MachineInfo.md#field_detail), [MachineNamesView](vdi.resources.Machine.MachineNamesView.md#field_detail), [MachineSummaryView](vdi.resources.Machine.MachineSummaryView.md#field_detail)

See also
> [AccessGroupId](vdi.entity.AccessGroupId.md), [DesktopId](vdi.entity.DesktopId.md), [MachineAgentUpgradeInfo](vdi.resources.Machine.MachineAgentUpgradeInfo.md), [MachineAlias](vdi.resources.Machine.MachineAlias.md), [SessionId](vdi.entity.SessionId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0


## Data Object Description

Fields common to all types of Machines.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**name**|  xsd:string|  The name of the Machine. [^2]
**dnsName**|  xsd:string|  DNS name for the Machine. [^1] [^2]
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)| **Deprecated.**_use[users](vdi.resources.Machine.MachineBase.md#users) instead. This field will not be populated for machine belonging to pool which support multiple assignment. _ The user assigned to the Machine. This cannot be a group. [^1]
**users**| [UserOrGroupId[]](vdi.entity.UserOrGroupId.md)|  The users assigned to the Machine. This cannot be a group.  **_Since_** Horizon 7.12 [^1] [^2]
**aliases**| [MachineAlias[]](vdi.resources.Machine.MachineAlias.md)|  Machine aliases for all the assigned users.  **_Since_** Horizon 7.13 [^1] [^2]
**accessGroup**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  The access group of this Machine. [^2]
**desktop**| [DesktopId](vdi.entity.DesktopId.md)|  The id of the desktop that the machine belongs to. [^2]
**desktopName**|  xsd:string|  The name of the desktop that the machine belongs to.  **_Since_** Horizon 7.6 [^1] [^2]
**session**| [SessionId](vdi.entity.SessionId.md)|  The ID of the session on the machine (if one exists). [^1] [^2]
**basicState**|  xsd:string|  The basic state of the Machine. For a Virtual Machine based Machine, the complete state is determined by basicState, isMissingInVCenter, operationState and isInHoldCustomization. In the Admin UI, the last three states are shown in brackets in the Machine State. [^2]
* This property will be one of:
|  Value |  Description
---|---
"PROVISIONING"| The virtual machine is being provisioned
"PROVISIONING_ERROR"| An error occurred during provisioning.
"WAIT_FOR_AGENT"| View Connection Server is waiting to establish communication with View Agent for one of these cases - a virtual machine in a manual desktop, unmanaged machine or terminal server.
"CUSTOMIZING"| The virtual machine in automated/provisioned desktop is being customized
"DELETING"| The virtual machine is marked for deletion. View Manager will delete the virtual machine soon.
"MAINTENANCE"| The virtual machine is in maintenance mode. Users cannot log in or use the virtual machine
"ERROR"| An unknown error occurred in the virtual machine.
"PROVISIONED"| The virtual machine is powered off or suspended.
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
"AGENT_DRAIN_MODE"| RDS host is configured for drain mode
"AGENT_DRAIN_UNTIL_RESTART"| RDS host is configured for drain until restart mode
"ALREADY_USED"| The virtual machine is configured to have only one session which is currently in progress and cannot accept new sessions
"AVAILABLE"| The virtual machine is powered on and ready for an active connection.
"IN_PROGRESS"| There is a virtual machine operation in-progress.
"DISABLED"| The machine is disabled
"DISABLE_IN_PROGRESS"| Disabled server still has some view brokered sessions. It can still accept re-connections
"VALIDATING"| The connection server is synchronizing state information with the agent.
"BLOCKED_AGENT_VERSION"| The agent version is blocked from establishing sessions.
"UNKNOWN"| Could not determine the state of the virtual machine.
**type**|  xsd:string|  The type of Machine [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"MANAGED_VIRTUAL_MACHINE"</td><td>The machine is a managed virtual machine.</td></tr><tr><td>"UNMANAGED_MACHINE"</td><td>The machine is an unmanaged physical or virtual machine.</td></tr></table>
**operatingSystem**|  xsd:string|  The guest operating system. [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"Unknown"</td><td></td></tr><tr><td>"Windows XP"</td><td>Windows XP</td></tr><tr><td>"Windows Vista"</td><td>Windows Vista</td></tr><tr><td>"Windows 7"</td><td>Windows 7</td></tr><tr><td>"Windows 8"</td><td>Windows 8</td></tr><tr><td>"Windows 10"</td><td>Windows 10</td></tr><tr><td>"Windows 11"</td><td>Windows 11</td></tr><tr><td>"Windows Server 2003"</td><td>Windows Server 2003</td></tr><tr><td>"Windows Server 2008"</td><td>Windows Server 2008</td></tr><tr><td>"Windows Server 2008R2"</td><td>Windows Server 2008R2</td></tr><tr><td>"Windows Server 2012"</td><td>Windows Server 2012</td></tr><tr><td>"Windows Server 2012R2"</td><td>Windows Server 2012R2</td></tr><tr><td>"Windows Server 10"</td><td>null</td></tr><tr><td>"Windows Server 2016"</td><td>null</td></tr><tr><td>"Windows Server 2016 or above"</td><td>Windows Server 2016 or above</td></tr><tr><td>"Linux (other)"</td><td>Linux (other)</td></tr><tr><td>"Linux Server (other)"</td><td>Linux server (other)</td></tr><tr><td>"Linux (Ubuntu)"</td><td>Linux (Ubuntu)</td></tr><tr><td>"Linux (Red Hat Enterprise Linux)"</td><td>Linux (Red Hat Enterprise)</td></tr><tr><td>"Linux (SUSE Linux Enterprise Server)"</td><td>Linux (Suse)</td></tr><tr><td>"Linux (CentOS)"</td><td>Linux (CentOS)</td></tr></table>
**operatingSystemArchitecture**|  xsd:string|  The guest operating system architecture.  **_Since_** Horizon 7.5 [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"Unknown"</td><td>Operating System cannot be determined.</td></tr><tr><td>"32_bit"</td><td>32 bit Operating System Architecture.</td></tr><tr><td>"64_bit"</td><td>64 bit Operating System Architecture.</td></tr></table>
**agentVersion**|  xsd:string|  The agent version. [^1] [^2]
**agentBuildNumber**|  xsd:string|  The agent build number [^1] [^2]
**remoteExperienceAgentVersion**|  xsd:string|  The remote experience agent version [^1] [^2]
**remoteExperienceAgentBuildNumber**|  xsd:string|  The remote experience agent build number [^1] [^2]
**refId**|  xsd:string|  Reference ID used for this machine.  **_Since_** Horizon 7.12 [^1]
**held**|  xsd:boolean|  Held status of the machine  **_Since_** Horizon 8.8 [^1] [^2]
**agentUpgradeInfo**| [MachineAgentUpgradeInfo](vdi.resources.Machine.MachineAgentUpgradeInfo.md)|  Information about agent upgrade on the machine  **_Since_** Horizon 8.8 [^1] [^2]
 


 
