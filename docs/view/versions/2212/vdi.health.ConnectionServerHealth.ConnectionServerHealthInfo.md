---
layout: page
title: Data Object - ConnectionServerHealthInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.ConnectionServerHealth.ConnectionServerHealthInfo  
Returned by
     [ConnectionServerHealth_Get](vdi.health.ConnectionServerHealth.md#get), [ConnectionServerHealth_List](vdi.health.ConnectionServerHealth.md#list)  
See also
     [CertificateHealthData](vdi.health.CertificateHealthData.md), [ConnectionServerHealthConnectionData](vdi.health.ConnectionServerHealth.ConnectionData.md), [ConnectionServerHealthLdapReplicationStatusData](vdi.health.ConnectionServerHealth.LdapReplicationStatusData.md), [ConnectionServerHealthResourcesData](vdi.health.ConnectionServerHealth.ConnectionServerHealthResourcesData.md), [ConnectionServerId](vdi.entity.ConnectionServerId.md), [ConnectionServerServiceStatus](vdi.health.ConnectionServerHealth.ConnectionServerServiceStatus.md), [ConnectionServerSessionProtocolData](vdi.health.ConnectionServerHealth.ConnectionServerSessionProtocolData.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Health information on a connection server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [ConnectionServerId](vdi.entity.ConnectionServerId.md)|  The ID for this connection server.   
  
**name**|  xsd:string|  The name of this connection server.   
  
**status**|  xsd:string|  The status of this connection server.  **_Since_** Horizon 7.0  


  * This property will be one of:  
|  Value |  Description   
---|---  
"OK"| The connection to the connection server is working properly.  
"NOT_RESPONDING"| The connection server is not responding.  
"UNKNOWN"| The status of the connection server is not known.  
"ERROR"| Error occurred when connecting to connection server.  
"RESTART_REQUIRED"| Connection server needs a restart  

  
**version**|  xsd:string|  The version of the Connection Server.   
  
**build**|  xsd:string|  Build number of the connection server.   
  
**connectionData**| [ConnectionServerHealthConnectionData](vdi.health.ConnectionServerHealth.ConnectionData.md)|  The connection data for this connection server.   


* This property need not be set.

  
**defaultCertificate**|  xsd:boolean|  Is this the default certificate?   


* This property need not be set.

  
**certificateHealth**| [CertificateHealthData](vdi.health.CertificateHealthData.md)|  The certificate data for this connection server.   


* This property need not be set.

  
**unauthenticatedAccess**|  xsd:boolean|  Whether unauthenticated access is enabled.  **_Since_** Horizon 7.10  


  * This property has a default value of false.

  
**defaultUnauthenticatedAccessUser**|  xsd:string|  Default username for unauthenticated access.  **_Since_** Horizon 7.10  


* This property need not be set.

  
**bypassPCoIPGateway**|  xsd:boolean|  Whether to bypass PCoIP Secure Gateway  **_Since_** Horizon 7.10  


* This property need not be set.

  
**bypassTunnel**|  xsd:boolean|  Whether to bypass HTTP(S) secure tunnel connection.  **_Since_** Horizon 7.10  


* This property need not be set.

  
**bypassAppBlastGateway**|  xsd:boolean|  Whether to bypass Blast Secure Gateway  **_Since_** Horizon 7.10  


* This property need not be set.

  
**replicationStatus**| [ConnectionServerHealthLdapReplicationStatusData[]](vdi.health.ConnectionServerHealth.LdapReplicationStatusData.md)|  Details about the Ldap replication from replica servers.  **_Since_** Horizon 7.10  


* This property need not be set.

  
**servicesStatus**| [ConnectionServerServiceStatus[]](vdi.health.ConnectionServerHealth.ConnectionServerServiceStatus.md)|  Status of the connection server services.  **_Since_** Horizon 7.10  


* This property need not be set.

  
**sessionProtocolData**| [ConnectionServerSessionProtocolData[]](vdi.health.ConnectionServerHealth.ConnectionServerSessionProtocolData.md)|  PCoIP, BLAST, or RDP sessions when client directly connects to the connection server.  **_Since_** Horizon 7.10  


* This property need not be set.

  
**refId**|  xsd:string|  Reference ID used for this connection server.  **_Since_** Horizon 7.10  


* This property need not be set.

  
**resourcesData**| [ConnectionServerHealthResourcesData](vdi.health.ConnectionServerHealth.ConnectionServerHealthResourcesData.md)|  Resources data of the connection server.  **_Since_** Horizon 7.11  


* This property need not be set.

  
**lastUpdatedTimestamp**|  xsd:long|  The timestamp in milliseconds when the last update was obtained. Measured as epoch time.  **_Since_** Horizon 7.12  


* This property need not be set.
* This property cannot be updated.

  
  
  
  
  
  

