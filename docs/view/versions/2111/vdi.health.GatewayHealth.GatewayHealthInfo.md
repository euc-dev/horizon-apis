---
layout: page
title: Data Object - GatewayHealthInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.health.GatewayHealth.GatewayHealthInfo`

Returned by  
> [GatewayHealth_Get](vdi.health.GatewayHealth.md#get), [GatewayHealth_List](vdi.health.GatewayHealth.md#list)

See also  
> [GatewayHealthConnectionData](vdi.health.GatewayHealth.ConnectionData.md), [GatewayId](vdi.entity.GatewayId.md)

Since  
> Horizon 7.7


## Data Object Description 

Gateway Health Information 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [GatewayId](vdi.entity.GatewayId.md)|  Id for the gateway.   
  
**name**|  xsd:string|  Name of the gateway.   


* This property cannot be updated.

  
**address**|  xsd:string|  IP address of the gateway.   


* This property cannot be updated.

  
**gatewayZoneInternal**|  xsd:boolean|  Flag to determine whether the gateway is internal.   


* This property cannot be updated.

  
**version**|  xsd:string|  Version of the gateway.   


* This property cannot be updated.

  
**type**|  xsd:string|  Type of the gateway.   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"AP"| AP type is for UAG.  
"F5"| F5 type is for F5 server.  
"SG"| SG type is for Security Server.  
"SG-cohosted"| SG-cohosted type is for Cohosted CS as gateway.  
"Unknown"| Unknown type is for unrecognized gateway type.  

  
**connectionData**| [GatewayHealthConnectionData](vdi.health.GatewayHealth.ConnectionData.md)|  The connection data of the gateway.   
  
**gatewayStatusActive**|  xsd:boolean|  Flag to indicate gateway status.   


* This property cannot be updated.

  
**gatewayStatusStale**|  xsd:boolean|  Flag to indicate whether gateway is staled or not.   


* This property cannot be updated.

  
**gatewayContacted**|  xsd:boolean|  Flag to indicate whether gateway has contacted connection server.   


* This property cannot be updated.

  
**refId**|  xsd:string|  Reference ID of the gateway.  **_Since_** Horizon 7.10  


* This property need not be set.

  
**lastUpdatedTimestamp**|  xsd:long|  The timestamp in milliseconds when the last update was obtained. Measured as epoch time.  **_Since_** Horizon 7.12  


* This property need not be set.
* This property cannot be updated.

  
  
  
   
  
  
