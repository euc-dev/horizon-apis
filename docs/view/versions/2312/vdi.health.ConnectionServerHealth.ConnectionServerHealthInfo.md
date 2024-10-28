---
layout: page
title: Data Object - ConnectionServerHealthInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.ConnectionServerHealth.ConnectionServerHealthInfo`

Returned by
> [ConnectionServerHealth_Get](vdi.health.ConnectionServerHealth.md#get), [ConnectionServerHealth_List](vdi.health.ConnectionServerHealth.md#list)

See also
> [CertificateHealthData](vdi.health.CertificateHealthData.md), [ConnectionServerHealthConnectionData](vdi.health.ConnectionServerHealth.ConnectionData.md), [ConnectionServerHealthLdapReplicationStatusData](vdi.health.ConnectionServerHealth.LdapReplicationStatusData.md), [ConnectionServerHealthResourcesData](vdi.health.ConnectionServerHealth.ConnectionServerHealthResourcesData.md), [ConnectionServerId](vdi.entity.ConnectionServerId.md), [ConnectionServerServiceStatus](vdi.health.ConnectionServerHealth.ConnectionServerServiceStatus.md), [ConnectionServerSessionProtocolData](vdi.health.ConnectionServerHealth.ConnectionServerSessionProtocolData.md)

Since
> Horizon View 6.0


## Data Object Description

Health information on a connection server.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [ConnectionServerId](vdi.entity.ConnectionServerId.md)|  The ID for this connection server.
**name**|  xsd:string|  The name of this connection server.
**status**|  xsd:string|  The status of this connection server.  **_Since_** Horizon 7.0<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"OK"</td><td>The connection to the connection server is working properly.</td></tr><tr><td>"NOT_RESPONDING"</td><td>The connection server is not responding.</td></tr><tr><td>"UNKNOWN"</td><td>The status of the connection server is not known.</td></tr><tr><td>"ERROR"</td><td>Error occurred when connecting to connection server.</td></tr><tr><td>"RESTART_REQUIRED"</td><td>Connection server needs a restart.</td></tr></table>
**version**|  xsd:string|  The version of the Connection Server.
**build**|  xsd:string|  Build number of the connection server.
**connectionData**| [ConnectionServerHealthConnectionData](vdi.health.ConnectionServerHealth.ConnectionData.md)|  The connection data for this connection server. [^1]
**defaultCertificate**|  xsd:boolean|  Is this the default certificate? [^1]
**certificateHealth**| [CertificateHealthData](vdi.health.CertificateHealthData.md)|  The certificate data for this connection server. [^1]
**signingCertificateHealth**| [CertificateHealthData](vdi.health.CertificateHealthData.md)|  The signing certificate data for this connection server.  **_Since_** Horizon 8.12 [^1]
**encryptionCertificateHealth**| [CertificateHealthData](vdi.health.CertificateHealthData.md)|  The encryption certificate data for this connection server.  **_Since_** Horizon 8.12 [^1]
**unauthenticatedAccess**|  xsd:boolean|  Whether unauthenticated access is enabled.  **_Since_** Horizon 7.10 [^5]
**defaultUnauthenticatedAccessUser**|  xsd:string|  Default username for unauthenticated access.  **_Since_** Horizon 7.10 [^1]
**bypassPCoIPGateway**|  xsd:boolean|  Whether to bypass PCoIP Secure Gateway  **_Since_** Horizon 7.10 [^1]
**bypassTunnel**|  xsd:boolean|  Whether to bypass HTTP(S) secure tunnel connection.  **_Since_** Horizon 7.10 [^1]
**bypassAppBlastGateway**|  xsd:boolean|  Whether to bypass Blast Secure Gateway  **_Since_** Horizon 7.10 [^1]
**replicationStatus**| [ConnectionServerHealthLdapReplicationStatusData[]](vdi.health.ConnectionServerHealth.LdapReplicationStatusData.md)|  Details about the Ldap replication from replica servers.  **_Since_** Horizon 7.10 [^1]
**servicesStatus**| [ConnectionServerServiceStatus[]](vdi.health.ConnectionServerHealth.ConnectionServerServiceStatus.md)|  Status of the connection server services.  **_Since_** Horizon 7.10 [^1]
**sessionProtocolData**| [ConnectionServerSessionProtocolData[]](vdi.health.ConnectionServerHealth.ConnectionServerSessionProtocolData.md)|  PCoIP, BLAST, or RDP sessions when client directly connects to the connection server.  **_Since_** Horizon 7.10 [^1]
**refId**|  xsd:string|  Reference ID used for this connection server.  **_Since_** Horizon 7.10 [^1]
**resourcesData**| [ConnectionServerHealthResourcesData](vdi.health.ConnectionServerHealth.ConnectionServerHealthResourcesData.md)|  Resources data of the connection server.  **_Since_** Horizon 7.11 [^1]
**lastUpdatedTimestamp**|  xsd:long|  The timestamp in milliseconds when the last update was obtained. Measured as epoch time.  **_Since_** Horizon 7.12 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^5]: This property has a default value of false.