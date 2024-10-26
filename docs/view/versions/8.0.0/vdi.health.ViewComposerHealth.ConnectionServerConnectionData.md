---
layout: page
title: Data Object - ViewComposerHealthConnectionServerConnectionData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.health.ViewComposerHealth.ConnectionServerConnectionData`

Property of
> [ViewComposerHealthInfo](vdi.health.ViewComposerHealth.ViewComposerHealthInfo.md#field_detail)

See also
> [CertificateHealthData](vdi.health.CertificateHealthData.md), [ConnectionServerId](vdi.entity.ConnectionServerId.md)

Since
> Horizon View 6.0


## Data Object Description

Health information for a specific connection server's connection to the View Composer server.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [ConnectionServerId](vdi.entity.ConnectionServerId.md)|  The ID of the connection server.
**name**|  xsd:string|  The host name of the Connection Server.
**status**|  xsd:string|  The health status of the View Composer server.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"OK"</td><td>The connection to View Composer server is working properly.</td></tr><tr><td>"MALFORMED_URL"</td><td>The connection to View Composer server was not possible due to a mal-formed url.</td></tr><tr><td>"ERROR"</td><td>Error occurred when connecting to View Composer server.</td></tr><tr><td>"CERT_ERROR"</td><td>Connection to View Composer server encountered certificate validation error.</td></tr></table>
**errorMessage**|  xsd:string|  Error message if connection server failed to connect to View Composer server [^1]
**thumbprintAccepted**|  xsd:boolean|  Whether the thumbprint of the View Composer server was accepted. [^1]
**certificateHealth**| [CertificateHealthData](vdi.health.CertificateHealthData.md)|  The health of the certificate. [^1] [^244]
**refId**|  xsd:string|  Reference ID of the connection server.  **_Since_** Horizon 7.10 [^1]
**lastUpdatedTimestamp**|  xsd:long|  The timestamp in milliseconds when the last update was obtained. Measured as epoch time.  **_Since_** Horizon 7.12 [^1] [^2]


 
