---
layout: page
title: Data Object - VirtualCenterHealthConnectionServerConnectionData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.VirtualCenterHealth.ConnectionServerConnectionData`

Property of
> [VirtualCenterHealthInfo](vdi.health.VirtualCenterHealth.VirtualCenterHealthInfo.md#field_detail)

See also
> [CertificateHealthData](vdi.health.CertificateHealthData.md), [ConnectionServerId](vdi.entity.ConnectionServerId.md)

Since
> Horizon View 6.0


## Data Object Description

Health information for a specific connection server's connection to the virtual center server.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [ConnectionServerId](vdi.entity.ConnectionServerId.md)|  The ID of the connection server.
**name**|  xsd:string|  The name of the Connection Server.
**status**|  xsd:string|  The status of the connection to the Virtual Center server.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"STATUS_UP"</td><td>The connection to Virtual Center server is working properly.</td></tr><tr><td>"STATUS_DOWN"</td><td>The connection to Virtual Center server was down.</td></tr><tr><td>"STATUS_RECONNECTING"</td><td>The connection to Virtual Center server was lost and is being reconnected to.</td></tr><tr><td>"STATUS_UNKNOWN"</td><td>Connection state to Virtual Center server is unknown.</td></tr><tr><td>"STATUS_INVALIDCREDENTIALS"</td><td>The supplied credentials cannot be used to authenticate to the Virtual Center server.</td></tr><tr><td>"STATUS_CANNOTLOGIN"</td><td>The connection server cannot login to the Virtual Center server.</td></tr><tr><td>"STATUS_NOT_YET_CONNECTED"</td><td>Connection server has not yet connect to Virtual Center server.</td></tr></table>
**thumbprintAccepted**|  xsd:boolean|  Whether the thumbprint of the Virtual Center server was accepted. [^1]
**certificateHealth**| [CertificateHealthData](vdi.health.CertificateHealthData.md)|  The health of the certificate. [^1] [^244]
**refId**|  xsd:string|  Reference ID of the connection server.  **_Since_** Horizon 7.10 [^1]
**lastUpdatedTimestamp**|  xsd:long|  The timestamp in milliseconds when the last update was obtained. Measured as epoch time.  **_Since_** Horizon 7.12 [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^244]: This property is required if thumbprintAccepted is set to false.