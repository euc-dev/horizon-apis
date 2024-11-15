---
layout: page
title: Data Object - GatewayHealthInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.GatewayHealth.GatewayHealthInfo`

Returned by
> [GatewayHealth_Get](vdi.health.GatewayHealth.md#get), [GatewayHealth_List](vdi.health.GatewayHealth.md#list)

See also
> [GatewayHealthConnectionData](vdi.health.GatewayHealth.ConnectionData.md), [GatewayId](vdi.entity.GatewayId.md)

Since
> Horizon 7.7


## Data Object Description

Gateway Health Information

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [GatewayId](vdi.entity.GatewayId.md)|  Id for the gateway.
**name**|  xsd:string|  Name of the gateway. [^2]
**address**|  xsd:string|  IP address of the gateway. [^2]
**gatewayZoneInternal**|  xsd:boolean|  Flag to determine whether the gateway is internal. [^2]
**version**|  xsd:string|  Version of the gateway. [^2]
**type**|  xsd:string|  Type of the gateway. [^2]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"AP"</td><td>AP type is for UAG.</td></tr><tr><td>"F5"</td><td>F5 type is for F5 server.</td></tr><tr><td>"SG"</td><td>SG type is for Security Server.</td></tr><tr><td>"SG-cohosted"</td><td>SG-cohosted type is for Cohosted CS as gateway.</td></tr><tr><td>"Unknown"</td><td>Unknown type is for unrecognized gateway type.</td></tr></table>
**connectionData**| [GatewayHealthConnectionData](vdi.health.GatewayHealth.ConnectionData.md)|  The connection data of the gateway.
**gatewayStatusActive**|  xsd:boolean|  Flag to indicate gateway status. [^2]
**gatewayStatusStale**|  xsd:boolean|  Flag to indicate whether gateway is staled or not. [^2]
**gatewayContacted**|  xsd:boolean|  Flag to indicate whether gateway has contacted connection server. [^2]
**refId**|  xsd:string|  Reference ID of the gateway.  **_Since_** Horizon 7.10 [^1]
**lastUpdatedTimestamp**|  xsd:long|  The timestamp in milliseconds when the last update was obtained. Measured as epoch time.  **_Since_** Horizon 7.12 [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.