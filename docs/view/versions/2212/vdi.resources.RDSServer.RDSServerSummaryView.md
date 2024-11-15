---
layout: page
title: Data Object - RDSServerSummaryView
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.RDSServer.RDSServerSummaryView`

Returned by
> [RDSServer_GetSummaryView](vdi.resources.RDSServer.md#getSummaryView)

See also
> [RDSServerAgentData](vdi.resources.RDSServer.RDSServerAgentData.md), [RDSServerBase](vdi.resources.RDSServer.RDSServerBase.md), [RDSServerId](vdi.entity.RDSServerId.md), [RDSServerMessageSecurityData](vdi.resources.RDSServer.RDSServerMessageSecurityData.md), [RDSServerRuntimeData](vdi.resources.RDSServer.RDSServerRuntimeData.md), [RDSServerSettings](vdi.resources.RDSServer.RDSServerSettings.md), [RDSServerSummaryData](vdi.resources.RDSServer.RDSServerSummaryData.md)

Since
> Horizon View 6.0


## Data Object Description

RDSServer information; queries require at least one of the listed privileges.

##  Queryable Data Object

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService").

Cannot filter on the following RDSServerSummaryData attributes:

* [summaryData](vdi.resources.RDSServer.RDSServerSummaryView.md#summaryData).[desktopName](vdi.resources.RDSServer.RDSServerSummaryData.md#desktopName)
* [summaryData](vdi.resources.RDSServer.RDSServerSummaryView.md#summaryData).[farmName](vdi.resources.RDSServer.RDSServerSummaryData.md#farmName)



Query **Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  is required to query RDSServers that are not in-use. It is sufficient to get all RDSServers that may or may not be associated with a Farm.
POOL_VIEW|  is required to query RDSServers that are associated with a Farm. All in-use RDSServers can be queried with POOL_VIEW on the Root access group. With POOL_VIEW privilege on a non-Root Farm access group, only the RDSServers associated with the Farm can be queried.



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [RDSServerId](vdi.entity.RDSServerId.md)|  RDS server entity ID [^2]
**base**| [RDSServerBase](vdi.resources.RDSServer.RDSServerBase.md)|  RDS server base [^2]
**messageSecurityData**| [RDSServerMessageSecurityData](vdi.resources.RDSServer.RDSServerMessageSecurityData.md)|  RDS Server message security data  **_Since_** Horizon View 6.1 [^2]
**summaryData**| [RDSServerSummaryData](vdi.resources.RDSServer.RDSServerSummaryData.md)|  RDS server summary data [^2]
**agentData**| [RDSServerAgentData](vdi.resources.RDSServer.RDSServerAgentData.md)|  RDSServer agent information [^2]
**settings**| [RDSServerSettings](vdi.resources.RDSServer.RDSServerSettings.md)|  RDS server settings [^2]
**runtimeData**| [RDSServerRuntimeData](vdi.resources.RDSServer.RDSServerRuntimeData.md)|  RDSServer runtime information [^2]
**refId**|  xsd:string|  Reference ID used for this RDS Server.  **_Since_** Horizon 8.1 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.