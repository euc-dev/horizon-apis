---
layout: page
title: Data Object - RDSServerAgentUpgradeInfo
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.RDSServer.AgentUpgradeInfo`

Property of
> [RDSServerAgentData](vdi.resources.RDSServer.RDSServerAgentData.md#field_detail)

Since
> Horizon 8.11


## Data Object Description

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**agentUpgradeState**|  xsd:string|  State of the agent upgrade. [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>READY</td><td>Agent is ready to be upgraded.</td></tr><tr><td>DOWNLOAD</td><td>Agent is downloading the upgrade binary.</td></tr><tr><td>WAIT</td><td>Agent is waiting for user to logoff or for reboot to complete</td></tr><tr><td>NOLOGON</td><td>Agent has no logged in user.</td></tr><tr><td>UPDATING</td><td>Agent is upgrading.</td></tr><tr><td>DONE</td><td>Agent upgrade task has ended.</td></tr><tr><td>UNKNOWN</td><td>Agent upgrade state is unknown.</td></tr></table>
**agentUpgradeResult**|  xsd:string|  Result of the agent upgrade. [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>OK</td><td>Agent upgrade is OK.</td></tr><tr><td>ERROR</td><td>Agent upgrade has unknown error.</td></tr><tr><td>FAILURE</td><td>Agent upgrade has failed.</td></tr><tr><td>INVALID</td><td>Agent received invalid values for upgrade.</td></tr><tr><td>DUPLICATE</td><td>Agent received duplicate upgrade request.</td></tr><tr><td>NOT_FOUND</td><td>Agent could not find upgrade request.</td></tr><tr><td>PROGRESS</td><td>Agent upgrade is in progress.</td></tr><tr><td>PREFLIGHTCHECK_INPROGRESS</td><td>Preflight check is in progress for agent upgrade.</td></tr><tr><td>PREFLIGHTCHECK_OK</td><td>Preflight check succeeded for agent upgrade.</td></tr><tr><td>PREFLIGHTCHECK_FAILURE</td><td>Preflight check failed for agent upgrade.</td></tr><tr><td>UNKNOWN</td><td>Agent upgrade result is unknown.</td></tr></table>
**agentUpgradeErrorMessage**|  xsd:string|  Error message of the agent upgrade failure. [^1] [^2]
 


 
