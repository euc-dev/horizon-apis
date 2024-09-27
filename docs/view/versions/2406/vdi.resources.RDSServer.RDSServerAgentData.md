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


 * This property need not be set.
 * This property cannot be updated.

  
**operatingSystem**|  xsd:string|  OS version   


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

  
**agentVersion**|  xsd:string|  Agent version   


 * This property need not be set.
 * This property cannot be updated.

  
**agentBuildNumber**|  xsd:string|  Agent build number   


 * This property need not be set.
 * This property cannot be updated.

  
**remoteExperienceAgentVersion**|  xsd:string|  Remote experience agent version   


 * This property need not be set.
 * This property cannot be updated.

  
**remoteExperienceAgentBuildNumber**|  xsd:string|  Remote experience agent build number   


 * This property need not be set.
 * This property cannot be updated.

  
**agentUpgradeInfo**| [RDSServerAgentUpgradeInfo](vdi.resources.RDSServer.AgentUpgradeInfo.md)|  Information about agent upgrade.  **_Since_** Horizon 8.11  


 * This property need not be set.
 * This property cannot be updated.

  
  

  

