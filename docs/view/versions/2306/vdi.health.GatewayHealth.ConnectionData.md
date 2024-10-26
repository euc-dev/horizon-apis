---
layout: page
title: Data Object - GatewayHealthConnectionData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.health.GatewayHealth.ConnectionData`

Property of
> [GatewayHealthInfo](vdi.health.GatewayHealth.GatewayHealthInfo.md#field_detail)

Since
> Horizon 7.7


## Data Object Description

Information on the connections through the Gateway.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**numActiveConnections**|  xsd:int|  Number of active connections for the gateway. [^19] [^2] [^72]
**numPcoipConnections**|  xsd:int|  Number of PCOIP connections for the gateway. [^19] [^2] [^72]
**numBlastConnections**|  xsd:int|  Number of blast connections for the gateway. [^19] [^2] [^72]
**unrecognizedPcoipRequestsCount**|  xsd:int|  Number of unrecognized PCoIP Secure Gateway requests.  **_Since_** Horizon 8.7 [^1] [^2]
**unrecognizedBlastRequestsCount**|  xsd:int|  Number of unrecognized Blast Secure Gateway requests.  **_Since_** Horizon 8.7 [^1] [^2]
**unrecognizedTunnelRequestsCount**|  xsd:int|  Number of unrecognized tunnel requests.  **_Since_** Horizon 8.7 [^1] [^2]
**unrecognizedXMLApiRequestsCount**|  xsd:int|  Number of unrecognized XML API requests.  **_Since_** Horizon 8.7 [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^19]: This property has a default value of 0.
[^72]: This property has a minimum value of 0.