---
layout: page
title: Data Object - MachineBase
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Machine.MachineBase`

Property of
> [MachineInfo](vdi.resources.Machine.MachineInfo.md#field_detail), [MachineNamesView](vdi.resources.Machine.MachineNamesView.md#field_detail), [MachineSummaryView](vdi.resources.Machine.MachineSummaryView.md#field_detail)

See also
> [AccessGroupId](vdi.entity.AccessGroupId.md), [DesktopId](vdi.entity.DesktopId.md), [SessionId](vdi.entity.SessionId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

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
**accessGroup**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  The access group of this Machine. [^2]
**desktop**| [DesktopId](vdi.entity.DesktopId.md)|  The id of the desktop that the machine belongs to. [^2]
**desktopName**|  xsd:string|  The name of the desktop that the machine belongs to.  **_Since_** Horizon 7.6 [^1] [^2]
**session**| [SessionId](vdi.entity.SessionId.md)|  The ID of the session on the machine (if one exists). [^1] [^2]
**basicState**|  xsd:string|  The basic state of the Machine. For a Virtual Machine based Machine, the complete state is determined by basicState, isMissingInVCenter, operationState and isInHoldCustomization. In the Admin UI, the last three states are shown in brackets in the Machine State. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"PROVISIONING"</td><td>The virtual machine is being provisioned</td></tr><tr><td>"PROVISIONING_ERROR"</td><td>An error occurred during provisioning.</td></tr><tr><td>"WAIT_FOR_AGENT"</td><td>View Connection Server is waiting to establish communication with View Agent for one of these cases - a virtual machine in a manual desktop, unmanaged machine or terminal server.</td></tr><tr><td>"CUSTOMIZING"</td><td>The virtual machine in automated/provisioned desktop is being customized</td></tr><tr><td>"DELETING"</td><td>The virtual machine is marked for deletion. View Manager will delete the virtual machine soon.</td></tr><tr><td>"MAINTENANCE"</td><td>The virtual machine is in maintenance mode. Users cannot log in or use the virtual machine</td></tr><tr><td>"ERROR"</td><td>An unknown error occurred in the virtual machine.</td></tr><tr><td>"PROVISIONED"</td><td>The virtual machine is powered off or suspended.</td></tr><tr><td>"AGENT_UNREACHABLE"</td><td>View Connection Server cannot establish communication with View Agent on a virtual machine</td></tr><tr><td>"UNASSIGNED_USER_CONNECTED"</td><td>A user other than the assigned user is logged in to a virtual machine in a dedicated desktop</td></tr><tr><td>"CONNECTED"</td><td>The virtual machine is in an active session and has an active remote connection to a View client</td></tr><tr><td>"UNASSIGNED_USER_DISCONNECTED"</td><td>A user other than the assigned user is logged in and disconnected from a virtual machine in a dedicated desktop.</td></tr><tr><td>"DISCONNECTED"</td><td>The virtual machine is in an active session, but it is disconnected from the View client</td></tr><tr><td>"AGENT_ERR_STARTUP_IN_PROGRESS"</td><td>View Agent has started on the virtual machine, but other required services such as the display protocol are still starting</td></tr><tr><td>"AGENT_ERR_DISABLED"</td><td>View Agent is disabled</td></tr><tr><td>"AGENT_ERR_INVALID_IP"</td><td>View Agent has invalid IP</td></tr><tr><td>"AGENT_ERR_NEED_REBOOT"</td><td>View Agent needs reboot.</td></tr><tr><td>"AGENT_ERR_PROTOCOL_FAILURE"</td><td>Protocol such as RDP or PCoIP is not enabled.</td></tr><tr><td>"AGENT_ERR_DOMAIN_FAILURE"</td><td>View Agent has invalid domain.</td></tr><tr><td>"AGENT_CONFIG_ERROR"</td><td>The Remote Desktop Services role is not enabled.</td></tr><tr><td>"AGENT_DRAIN_MODE"</td><td>RDS host is configured for drain mode</td></tr><tr><td>"AGENT_DRAIN_UNTIL_RESTART"</td><td>RDS host is configured for drain until restart mode</td></tr><tr><td>"ALREADY_USED"</td><td>The virtual machine is configured to have only one session which is currently in progress and cannot accept new sessions</td></tr><tr><td>"AVAILABLE"</td><td>The virtual machine is powered on and ready for an active connection.</td></tr><tr><td>"IN_PROGRESS"</td><td>There is a virtual machine operation in-progress.</td></tr><tr><td>"DISABLED"</td><td>The machine is disabled</td></tr><tr><td>"DISABLE_IN_PROGRESS"</td><td>Disabled server still has some view brokered sessions. It can still accept re-connections</td></tr><tr><td>"VALIDATING"</td><td>The connection server is synchronizing state information with the agent.</td></tr><tr><td>"UNKNOWN"</td><td>Could not determine the state of the virtual machine.</td></tr></table>
**type**|  xsd:string|  The type of Machine [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"MANAGED_VIRTUAL_MACHINE"</td><td>The machine is a managed virtual machine.</td></tr><tr><td>"UNMANAGED_MACHINE"</td><td>The machine is an unmanaged physical or virtual machine.</td></tr></table>
**operatingSystem**|  xsd:string|  The guest operating system. [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"Unknown"</td><td></td></tr><tr><td>"Windows XP"</td><td>Windows XP</td></tr><tr><td>"Windows Vista"</td><td>Windows Vista</td></tr><tr><td>"Windows 7"</td><td>Windows 7</td></tr><tr><td>"Windows 8"</td><td>Windows 8</td></tr><tr><td>"Windows 10"</td><td>Windows 10</td></tr><tr><td>"Windows Server 2003"</td><td>Windows Server 2003</td></tr><tr><td>"Windows Server 2008"</td><td>Windows Server 2008</td></tr><tr><td>"Windows Server 2008R2"</td><td>Windows Server 2008R2</td></tr><tr><td>"Windows Server 2012"</td><td>Windows Server 2012</td></tr><tr><td>"Windows Server 2012R2"</td><td>Windows Server 2012R2</td></tr><tr><td>"Windows Server 10"</td><td>null</td></tr><tr><td>"Windows Server 2016"</td><td>null</td></tr><tr><td>"Windows Server 2016 or above"</td><td>Windows Server 2016 or above</td></tr><tr><td>"Linux (other)"</td><td>Linux (other)</td></tr><tr><td>"Linux Server (other)"</td><td>Linux server (other)</td></tr><tr><td>"Linux (Ubuntu)"</td><td>Linux (Ubuntu)</td></tr><tr><td>"Linux (Red Hat Enterprise Linux)"</td><td>Linux (Red Hat Enterprise)</td></tr><tr><td>"Linux (SUSE Linux Enterprise Server)"</td><td>Linux (Suse)</td></tr><tr><td>"Linux (CentOS)"</td><td>Linux (CentOS)</td></tr></table>
**operatingSystemArchitecture**|  xsd:string|  The guest operating system architecture.  **_Since_** Horizon 7.5 [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"Unknown"</td><td>Operating System cannot be determined.</td></tr><tr><td>"32_bit"</td><td>32 bit Operating System Architecture.</td></tr><tr><td>"64_bit"</td><td>64 bit Operating System Architecture.</td></tr></table>
**agentVersion**|  xsd:string|  The agent version. [^1] [^2]
**agentBuildNumber**|  xsd:string|  The agent build number [^1] [^2]
**remoteExperienceAgentVersion**|  xsd:string|  The remote experience agent version [^1] [^2]
**remoteExperienceAgentBuildNumber**|  xsd:string|  The remote experience agent build number [^1] [^2]
**refId**|  xsd:string|  Reference ID used for this machine.  **_Since_** Horizon 7.12 [^1]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.