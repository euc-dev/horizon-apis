---
layout: page
title: Data Object - RDSServerAgentData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.RDSServer.RDSServerAgentData
Property of
     [RDSServerInfo](vdi.resources.RDSServer.RDSServerInfo.md#field_detail), [RDSServerSummaryView](vdi.resources.RDSServer.RDSServerSummaryView.md#field_detail)
See also
     [RDSServerAgentUpgradeInfo](vdi.resources.RDSServer.AgentUpgradeInfo.md)
Since 
    Horizon View 6.0

## Data Object Description 

RDSServer agent information 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**dnsName**|  xsd:string|  RDS server DNS name   


[^1]
[^2]

  
**operatingSystem**|  xsd:string|  OS version   


[^1]
[^2]
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

  
**agentVersion**|  xsd:string|  Agent version   


[^1]
[^2]

  
**agentBuildNumber**|  xsd:string|  Agent build number   


[^1]
[^2]

  
**remoteExperienceAgentVersion**|  xsd:string|  Remote experience agent version   


[^1]
[^2]

  
**remoteExperienceAgentBuildNumber**|  xsd:string|  Remote experience agent build number   


[^1]
[^2]

  
**agentUpgradeInfo**| [RDSServerAgentUpgradeInfo](vdi.resources.RDSServer.AgentUpgradeInfo.md)|  Information about agent upgrade.  **_Since_** Horizon 8.11  


[^1]
[^2]

  
  

  

