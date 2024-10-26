---
layout: page
title: Data Object - ConnectionServerHealthConnectionData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.health.ConnectionServerHealth.ConnectionData`

Property of
> [ConnectionServerHealthInfo](vdi.health.ConnectionServerHealth.ConnectionServerHealthInfo.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Data on the number of connections to the connection server.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**numConnections**|  xsd:int|  The number of connections to this connection server.
**numConnectionsHigh**|  xsd:int|  The high water mark of connections to this connection server.
**numViewComposerConnections**|  xsd:int|  The number of View Composer machine connections brokered by this connection server.
**numViewComposerConnectionsHigh**|  xsd:int|  The high water mark of View Composer machine connections brokered by this connection server.
**numTunneledSessions**|  xsd:int|  The number of connections tunneled through this connection server.
**numPSGSessions**|  xsd:int|  The number of PCoIP Secure Gateway sessions. [^1]
**numBSGSessions**|  xsd:int|  The number of Blast Secure Gateway sessions.  **_Since_** Horizon 7.12 [^1]
**numRDPGatewayedSessions**|  xsd:int|  The number of Secure Gateway sessions with the RDP.  **_Since_** Horizon 7.12 [^1]
**sessionThreshold**|  xsd:int|  The maximum load of connections allowed for the connection server through the horizon client. This value represents one of the following. [^304] [^305]
**_Since_** Horizon 7.10 [^1]


 


[^1]: This property need not be set.
[^304]: When all of the secure gateways (HTTP(S)/PCOIP/BLAST) are enabled, this field denotes the maximum load of connections allowed for the connection server. Once the number of connections to this connection server reaches this value, the subsequent connections from the horizon client will be blocked by secure gateway.
[^305]: When none of the secure gateways(HTTP(S)/PCOIP/BLAST) are enabled, sessionThreshold value will not be set.