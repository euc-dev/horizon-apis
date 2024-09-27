---
layout: page
title: Data Object - FarmHealthRDSServerHealthInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.FarmHealth.RDSServerHealthInfo  
Property of
     [FarmHealthInfo](vdi.health.FarmHealth.FarmHealthInfo.md#field_detail)  
See also
     [FarmHealthMissingApplicationInfo](vdi.health.FarmHealth.MissingApplicationInfo.md), [RDSServerId](vdi.entity.RDSServerId.md), [RDSServerSessionSettings](vdi.resources.RDSServer.RDSServerSessionSettings.md)  
Since 
    Horizon View 6.0

## Data Object Description 

RDS server health data 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [RDSServerId](vdi.entity.RDSServerId.md)|  RDS server entity ID   


* This property cannot be updated.

  
**name**|  xsd:string|  RDS Server name   


* This property need not be set.
* This property cannot be updated.

  
**operatingSystem**|  xsd:string|  OS version.  **_Since_** Horizon 7.9  


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

  
**agentVersion**|  xsd:string|  Agent version.  **_Since_** Horizon 7.9  


* This property need not be set.
* This property cannot be updated.

  
**agentBuildNumber**|  xsd:string|  Agent build number.  **_Since_** Horizon 7.9  


* This property need not be set.
* This property cannot be updated.

  
**status**|  xsd:string|  RDS server status   


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
"CONNECTED"| The virtual machine is in an active session and has an active remote connection to a View client  
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

  
**health**|  xsd:string|  RDS server health   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"OK"| RDSServer is reachable. All applications (defined on its farm) are verified installed on the server.  
"WARNING"| RDSServer is reachable. Some applications are detected as not installed on the server.  
"ERROR"| Server is unreachable, or, none of the applications are installed.  
"DISABLED"| Server is disabled.  

  
**available**|  xsd:boolean|  Indicates if RDS server is available   


* This property cannot be updated.

  
**missingApplications**| [FarmHealthMissingApplicationInfo[]](vdi.health.FarmHealth.MissingApplicationInfo.md)|  Missing Application info for those Applications that are missing on this RDSServer. An Application must be enabled in order for its health status to be collected.   


* This property need not be set.
* This property cannot be updated.

  
**loadPreference**|  xsd:string|  Based on the current load of this RDSServer, gives a measure of how preferential this server is to be chosen for new application sessions.  **_Since_** Horizon View 6.2  


* This property need not be set.
* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"BLOCK"| This RDSServer will not be chosen for new sessions.  
"HEAVY"| This RDSServer is experiencing heavy load and should likely not be chosen for new sessions.  
"NORMAL"| This RDSServer is experiencing normal load and is okay to be chosen for new sessions.  
"LIGHT"| This RDSServer is experiencing light load and is okay to be chosen for new sessions.  
"UNKNOWN"| This RDSServer did not report a load preference. This is potentially a configuration issue if other RDSServers in the same Farm do report load preferences.  

  
**loadIndex**|  xsd:int|  Represents the load on the RDSServer in the range of 0-100  **_Since_** Horizon 7.8  


* This property need not be set.
* This property cannot be updated.

  
**numSessions**|  xsd:int|  Number of sessions on this RDS Host.  **_Since_** Horizon 7.10  


* This property need not be set.

  
**sessionSettings**| [RDSServerSessionSettings](vdi.resources.RDSServer.RDSServerSessionSettings.md)|  RDSServer session settings  **_Since_** Horizon 7.9  


* This property need not be set.
* This property cannot be updated.

  
**refId**|  xsd:string|  Reference ID of the RDS Server.  **_Since_** Horizon 7.10  


* This property need not be set.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

