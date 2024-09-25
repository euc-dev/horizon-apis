---
layout: page
title: Data Object - ConnectionServerHealthConnectionData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.ConnectionServerHealth.ConnectionData
Property of
     [ConnectionServerHealthInfo](vdi.health.ConnectionServerHealth.ConnectionServerHealthInfo.md#field_detail)
Since 
    Horizon View 6.0

## Data Object Description 

Data on the number of connections to the connection server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**numConnections**|  xsd:int|  The number of connections to this connection server.   
  
**numConnectionsHigh**|  xsd:int|  The high water mark of connections to this connection server.   
  
**numViewComposerConnections**|  xsd:int| **Deprecated.**_This property is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._ The number of View Composer machine connections brokered by this connection server.   
  
**numViewComposerConnectionsHigh**|  xsd:int| **Deprecated.**_This property is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._ The high water mark of View Composer machine connections brokered by this connection server.   
  
**numTunneledSessions**|  xsd:int|  The number of connections tunneled through this connection server.   
  
**numPSGSessions**|  xsd:int|  The number of PCoIP Secure Gateway sessions.   


[^1]

  
**numBSGSessions**|  xsd:int|  The number of Blast Secure Gateway sessions.  **_Since_** Horizon 7.12  


[^1]

  
**numRDPGatewayedSessions**|  xsd:int|  The number of Secure Gateway sessions with the RDP.  **_Since_** Horizon 7.12  


[^1]

  
**sessionThreshold**|  xsd:int|  The maximum load of connections allowed for the connection server through the horizon client. This value represents one of the following. 

  * When all of the secure gateways (HTTP(S)/PCOIP/BLAST) are enabled, this field denotes the maximum load of connections allowed for the connection server. Once the number of connections to this connection server reaches this value, the subsequent connections from the horizon client will be blocked by secure gateway.
  * When none of the secure gateways(HTTP(S)/PCOIP/BLAST) are enabled, sessionThreshold value will not be set.

**_Since_** Horizon 7.10  


[^1]

  
**unrecognizedPcoipRequestsCount**|  xsd:int|  The number of unrecognized PCoIP Secure Gateway requests.  **_Since_** Horizon 8.7  


[^1]
[^2]

  
**unrecognizedBlastRequestsCount**|  xsd:int|  The number of unrecognized Blast Secure Gateway requests.  **_Since_** Horizon 8.7  


[^1]
[^2]

  
**unrecognizedTunnelRequestsCount**|  xsd:int|  The number of unrecognized tunnel requests.  **_Since_** Horizon 8.7  


[^1]
[^2]

  
**unrecognizedXMLApiRequestsCount**|  xsd:int|  The number of unrecognized XML API requests.  **_Since_** Horizon 8.7  


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
