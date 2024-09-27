---
layout: page
title: Data Object - MachineBase
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Machine.MachineBase  
Property of
     [MachineInfo](vdi.resources.Machine.MachineInfo.md#field_detail), [MachineNamesView](vdi.resources.Machine.MachineNamesView.md#field_detail), [MachineSummaryView](vdi.resources.Machine.MachineSummaryView.md#field_detail)  
See also
     [AccessGroupId](vdi.entity.AccessGroupId.md), [DesktopId](vdi.entity.DesktopId.md), [MachineAgentUpgradeInfo](vdi.resources.Machine.MachineAgentUpgradeInfo.md), [MachineAlias](vdi.resources.Machine.MachineAlias.md), [SessionId](vdi.entity.SessionId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Fields common to all types of Machines. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  The name of the Machine.   


* This property cannot be updated.

  
**dnsName**|  xsd:string|  DNS name for the Machine.   


* This property need not be set.
* This property cannot be updated.

  
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)| **Deprecated.**_use[users](vdi.resources.Machine.MachineBase.md#users) instead. This field will not be populated for machine belonging to pool which support multiple assignment. _ The user assigned to the Machine. This cannot be a group.  
  


* This property need not be set.

  
**users**| [UserOrGroupId[]](vdi.entity.UserOrGroupId.md)|  The users assigned to the Machine. This cannot be a group.  **_Since_** Horizon 7.12  


* This property need not be set.
* This property cannot be updated.

  
**aliases**| [MachineAlias[]](vdi.resources.Machine.MachineAlias.md)|  Machine aliases for all the assigned users.  **_Since_** Horizon 7.13  


* This property need not be set.
* This property cannot be updated.

  
**accessGroup**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  The access group of this Machine.   


* This property cannot be updated.

  
**desktop**| [DesktopId](vdi.entity.DesktopId.md)|  The id of the desktop that the machine belongs to.   


* This property cannot be updated.

  
**desktopName**|  xsd:string|  The name of the desktop that the machine belongs to.  **_Since_** Horizon 7.6  


* This property need not be set.
* This property cannot be updated.

  
**session**| [SessionId](vdi.entity.SessionId.md)|  The ID of the session on the machine (if one exists).   


* This property need not be set.
* This property cannot be updated.

  
**basicState**|  xsd:string|  The basic state of the Machine. For a Virtual Machine based Machine, the complete state is determined by basicState, isMissingInVCenter, operationState and isInHoldCustomization. In the Admin UI, the last three states are shown in brackets in the Machine State.   


* This property cannot be updated.
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
"UNKNOWN"| Could not determine the state of the virtual machine.  

  
**type**|  xsd:string|  The type of Machine   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"MANAGED_VIRTUAL_MACHINE"| The machine is a managed virtual machine.  
"UNMANAGED_MACHINE"| The machine is an unmanaged physical or virtual machine.  

  
**operatingSystem**|  xsd:string|  The guest operating system.   


* This property need not be set.
* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"Unknown"|   
"Windows XP"| Windows XP  
"Windows Vista"| Windows Vista  
"Windows 7"| Windows 7  
"Windows 8"| Windows 8  
"Windows 10"| Windows 10  
"Windows 11"| Windows 11  
"Windows Server 2003"| Windows Server 2003  
"Windows Server 2008"| Windows Server 2008  
"Windows Server 2008R2"| Windows Server 2008R2  
"Windows Server 2012"| Windows Server 2012  
"Windows Server 2012R2"| Windows Server 2012R2  
"Windows Server 10"| null  
"Windows Server 2016"| null  
"Windows Server 2016 or above"| Windows Server 2016 or above  
"Linux (other)"| Linux (other)  
"Linux Server (other)"| Linux server (other)  
"Linux (Ubuntu)"| Linux (Ubuntu)  
"Linux (Red Hat Enterprise Linux)"| Linux (Red Hat Enterprise)  
"Linux (SUSE Linux Enterprise Server)"| Linux (Suse)  
"Linux (CentOS)"| Linux (CentOS)  

  
**operatingSystemArchitecture**|  xsd:string|  The guest operating system architecture.  **_Since_** Horizon 7.5  


* This property need not be set.
* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"Unknown"| Operating System cannot be determined.  
"32_bit"| 32 bit Operating System Architecture.  
"64_bit"| 64 bit Operating System Architecture.  

  
**agentVersion**|  xsd:string|  The agent version.   


* This property need not be set.
* This property cannot be updated.

  
**agentBuildNumber**|  xsd:string|  The agent build number   


* This property need not be set.
* This property cannot be updated.

  
**remoteExperienceAgentVersion**|  xsd:string|  The remote experience agent version   


* This property need not be set.
* This property cannot be updated.

  
**remoteExperienceAgentBuildNumber**|  xsd:string|  The remote experience agent build number   


* This property need not be set.
* This property cannot be updated.

  
**refId**|  xsd:string|  Reference ID used for this machine.  **_Since_** Horizon 7.12  


* This property need not be set.

  
**held**|  xsd:boolean|  Held status of the machine  **_Since_** Horizon 8.8  


* This property need not be set.
* This property cannot be updated.

  
**agentUpgradeInfo**| [MachineAgentUpgradeInfo](vdi.resources.Machine.MachineAgentUpgradeInfo.md)|  Information about agent upgrade on the machine  **_Since_** Horizon 8.8  


* This property need not be set.
* This property cannot be updated.

  
  
  
  
  
  

