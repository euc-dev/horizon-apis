---
layout: page
title: Data Object - MachineAgentUpgradeInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Machine.MachineAgentUpgradeInfo
Property of
     [MachineBase](vdi.resources.Machine.MachineBase.md#field_detail), [MachineData](vdi.resources.Machine.MachineData.md#field_detail)
Since 
    Horizon 8.8

## Data Object Description 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**agentUpgradeState**|  xsd:string|  State of the agent upgrade on the machine.   


[^1]
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"READY"| Agent is ready to be upgraded.  
"DOWNLOAD"| Agent is downloading the upgrade binary.  
"WAIT"| Agent is waiting for user to logoff or for reboot to complete  
"NOLOGON"| Agent has no logged in user.  
"UPDATING"| Agent is upgrading.  
"DONE"| Agent upgrade task has ended.  
"UNKNOWN"| Agent upgrade state is unknown.  

  
**agentUpgradeResult**|  xsd:string|  Result of the agent upgrade on the machine.   


[^1]
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"OK"| Agent upgrade is OK.  
"ERROR"| Agent upgrade has unknown error.  
"FAILURE"| Agent upgrade has failed.  
"INVALID"| Agent received invalid values for upgrade.  
"DUPLICATE"| Agent received duplicate upgrade request.  
"NOT_FOUND"| Agent could not find upgrade request.  
"PROGRESS"| Agent upgrade is in progress.  
"PREFLIGHTCHECK_INPROGRESS"| Preflight check is in progress for agent upgrade.  
"PREFLIGHTCHECK_OK"| Preflight check succeeded for agent upgrade.  
"PREFLIGHTCHECK_FAILURE"| Preflight check failed for agent upgrade.  
"UNKNOWN"| Agent upgrade result is unknown.  

  
**agentUpgradeErrorMessage**|  xsd:string|  Error message of the agent upgrade failure on the machine.   


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

