---
layout: page
title: Data Object - RDSServerInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.RDSServer.RDSServerInfo
Returned by
     [RDSServer_Get](vdi.resources.RDSServer.md#get)
See also
     [RDSNetworkLabelData](vdi.resources.RDSServer.NetworkLabelData.md), [RDSServerAgentData](vdi.resources.RDSServer.RDSServerAgentData.md), [RDSServerBase](vdi.resources.RDSServer.RDSServerBase.md), [RDSServerId](vdi.entity.RDSServerId.md), [RDSServerMaintenanceData](vdi.resources.RDSServer.RDSServerMaintenanceData.md), [RDSServerMessageSecurityData](vdi.resources.RDSServer.RDSServerMessageSecurityData.md), [RDSServerRuntimeData](vdi.resources.RDSServer.RDSServerRuntimeData.md), [RDSServerSettings](vdi.resources.RDSServer.RDSServerSettings.md)
Since 
    Horizon View 6.0

## Data Object Description 

RDSServer information; queries require at least one of the listed privileges. 

##  Queryable Data Object 

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService"). 

Query Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  is required to query RDSServers that are not in-use. It is sufficient to get all RDSServers that may or may not be associated with a Farm.   
POOL_VIEW|  is required to query RDSServers that are associated with a Farm. All in-use RDSServers can be queried with POOL_VIEW on the Root access group. With POOL_VIEW privilege on a non-Root Farm access group, only the RDSServers associated with the Farm can be queried.   
  


## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [RDSServerId](vdi.entity.RDSServerId.md)|  RDS server entity ID   


[^2]

  
**base**| [RDSServerBase](vdi.resources.RDSServer.RDSServerBase.md)|  RDS server base   
  
**messageSecurityData**| [RDSServerMessageSecurityData](vdi.resources.RDSServer.RDSServerMessageSecurityData.md)|  RDS Server message security data.  **_Since_** Horizon View 6.1  


[^2]

  
**agentData**| [RDSServerAgentData](vdi.resources.RDSServer.RDSServerAgentData.md)|  RDSServer agent information   


[^2]

  
**settings**| [RDSServerSettings](vdi.resources.RDSServer.RDSServerSettings.md)|  RDS server settings   
  
**runtimeData**| [RDSServerRuntimeData](vdi.resources.RDSServer.RDSServerRuntimeData.md)|  RDSServer runtime information   


[^2]

  
**rdsServerMaintenanceData**| [RDSServerMaintenanceData](vdi.resources.RDSServer.RDSServerMaintenanceData.md)|  Maintenance details about the RDS Server. The data will be populated only for Linked clone or Instant clone provisioned RDS Server.  **_Since_** Horizon 7.9  


[^1]
[^2]

  
**refId**|  xsd:string|  Reference ID used for this RDS Server.  **_Since_** Horizon 8.1  


[^1]
[^2]

  
**networkLabels**| [RDSNetworkLabelData[]](vdi.resources.RDSServer.NetworkLabelData.md)|  The network label(s) associated with this Farm. The network label(s) automatically assigned by Connection Server to this Machine. These may differ from the actual labels if manually changed after automatic assignment or if there was an error in assignment.  **_Since_** Horizon 8.11  


[^1]
[^2]

  
  

  

