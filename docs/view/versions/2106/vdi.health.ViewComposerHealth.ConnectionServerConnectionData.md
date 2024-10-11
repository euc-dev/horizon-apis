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

**Deprecated.**_This service is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Health information for a specific connection server's connection to the View Composer server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [ConnectionServerId](vdi.entity.ConnectionServerId.md)|  The ID of the connection server.   
  
**name**|  xsd:string|  The host name of the Connection Server.   
  
**status**|  xsd:string|  The health status of the View Composer server.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"OK"| The connection to View Composer server is working properly.  
"MALFORMED_URL"| The connection to View Composer server was not possible due to a mal-formed url  
"ERROR"| Error occurred when connecting to View Composer server  
"CERT_ERROR"| Connection to View Composer server encountered certificate validation error.  

  
**errorMessage**|  xsd:string|  Error message if connection server failed to connect to View Composer server   


* This property need not be set.

  
**thumbprintAccepted**|  xsd:boolean|  Whether the thumbprint of the View Composer server was accepted.   


* This property need not be set.

  
**certificateHealth**| [CertificateHealthData](vdi.health.CertificateHealthData.md)|  The health of the certificate.   


* This property need not be set.
  * This property is required if thumbprintAccepted is set to false.

  
**refId**|  xsd:string|  Reference ID of the connection server.  **_Since_** Horizon 7.10  


* This property need not be set.

  
**lastUpdatedTimestamp**|  xsd:long|  The timestamp in milliseconds when the last update was obtained. Measured as epoch time.  **_Since_** Horizon 7.12  


* This property need not be set.
* This property cannot be updated.

  
  
  

  
  
