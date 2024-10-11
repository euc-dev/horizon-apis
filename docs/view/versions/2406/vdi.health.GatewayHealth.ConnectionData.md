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
**numActiveConnections**|  xsd:int|  Number of active connections for the gateway.   


  * This property has a default value of 0.
 * This property cannot be updated.
  * This property has a minimum value of 0. 

  
**numPcoipConnections**|  xsd:int|  Number of PCOIP connections for the gateway.   


  * This property has a default value of 0.
 * This property cannot be updated.
  * This property has a minimum value of 0. 

  
**numBlastConnections**|  xsd:int|  Number of blast connections for the gateway.   


  * This property has a default value of 0.
 * This property cannot be updated.
  * This property has a minimum value of 0. 

  
**unrecognizedPcoipRequestsCount**|  xsd:int|  Number of unrecognized PCoIP Secure Gateway requests.  **_Since_** Horizon 8.7  


 * This property need not be set.
 * This property cannot be updated.

  
**unrecognizedBlastRequestsCount**|  xsd:int|  Number of unrecognized Blast Secure Gateway requests.  **_Since_** Horizon 8.7  


 * This property need not be set.
 * This property cannot be updated.

  
**unrecognizedTunnelRequestsCount**|  xsd:int|  Number of unrecognized tunnel requests.  **_Since_** Horizon 8.7  


 * This property need not be set.
 * This property cannot be updated.

  
**unrecognizedXMLApiRequestsCount**|  xsd:int|  Number of unrecognized XML API requests.  **_Since_** Horizon 8.7  


 * This property need not be set.
 * This property cannot be updated.

  
  

  
