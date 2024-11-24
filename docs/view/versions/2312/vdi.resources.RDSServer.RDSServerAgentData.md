---
layout: page
title: Data Object - RDSServerAgentData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.RDSServer.RDSServerAgentData`

Property of
> [RDSServerInfo](vdi.resources.RDSServer.RDSServerInfo.md#field_detail), [RDSServerSummaryView](vdi.resources.RDSServer.RDSServerSummaryView.md#field_detail)

See also
> [RDSServerAgentUpgradeInfo](vdi.resources.RDSServer.AgentUpgradeInfo.md)

Since
> Horizon View 6.0


## Data Object Description

RDSServer agent information

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**dnsName**|  xsd:string|  RDS server DNS name [^1] [^2]
**operatingSystem**|  xsd:string|  OS version [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>Unknown</td><td></td></tr><tr><td>Windows XP</td><td>Windows XP</td></tr><tr><td>Windows Vista</td><td>Windows Vista</td></tr><tr><td>Windows 7</td><td>Windows 7</td></tr><tr><td>Windows 8</td><td>Windows 8</td></tr><tr><td>Windows 10</td><td>Windows 10</td></tr><tr><td>Windows 11</td><td>Windows 11</td></tr><tr><td>Windows Server 2003</td><td>Windows Server 2003</td></tr><tr><td>Windows Server 2008</td><td>Windows Server 2008</td></tr><tr><td>Windows Server 2008R2</td><td>Windows Server 2008R2</td></tr><tr><td>Windows Server 2012</td><td>Windows Server 2012</td></tr><tr><td>Windows Server 2012R2</td><td>Windows Server 2012R2</td></tr><tr><td>Windows Server 10</td><td>null</td></tr><tr><td>Windows Server 2016</td><td>null</td></tr><tr><td>Windows Server 2016 or above</td><td>Windows Server 2016 or above</td></tr><tr><td>Linux (other)</td><td>Linux (other)</td></tr><tr><td>Linux Server (other)</td><td>Linux server (other)</td></tr><tr><td>Linux (Ubuntu)</td><td>Linux (Ubuntu)</td></tr><tr><td>Linux (Red Hat Enterprise Linux)</td><td>Linux (Red Hat Enterprise)</td></tr><tr><td>Linux (SUSE Linux Enterprise Server)</td><td>Linux (Suse)</td></tr><tr><td>Linux (CentOS)</td><td>Linux (CentOS)</td></tr></table>
**agentVersion**|  xsd:string|  Agent version [^1] [^2]
**agentBuildNumber**|  xsd:string|  Agent build number [^1] [^2]
**remoteExperienceAgentVersion**|  xsd:string|  Remote experience agent version [^1] [^2]
**remoteExperienceAgentBuildNumber**|  xsd:string|  Remote experience agent build number [^1] [^2]
**agentUpgradeInfo**| [RDSServerAgentUpgradeInfo](vdi.resources.RDSServer.AgentUpgradeInfo.md)|  Information about agent upgrade.  **_Since_** Horizon 8.11 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.