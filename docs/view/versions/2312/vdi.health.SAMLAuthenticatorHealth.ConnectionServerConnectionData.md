---
layout: page
title: Data Object - SAMLAuthenticatorHealthConnectionServerConnectionData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.SAMLAuthenticatorHealth.ConnectionServerConnectionData  
Property of
     [SAMLAuthenticatorHealthInfo](vdi.health.SAMLAuthenticatorHealth.SAMLAuthenticatorHealthInfo.md#field_detail)  
See also
     [CertificateHealthData](vdi.health.CertificateHealthData.md), [ConnectionServerId](vdi.entity.ConnectionServerId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Health information for a specific connection server's connection to the SAML authenticator. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [ConnectionServerId](vdi.entity.ConnectionServerId.md)|  The ID of the connection server.   
  
**name**|  xsd:string|  The host name of the Connection Server.   
  
**status**|  xsd:string|  The health status of the SAML authenticator.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"OK"| The connection to SAML authenticator is working properly.  
"ERROR"| Error occurred when connecting to SAML authenticator.  
"WARN"| The connection to SAML authenticator has minor issues.  
"UNKNOWN"| State of SAML authenticator is unknown.  

  
**errorMessage**|  xsd:string|  Error message if connection server failed to connect to SAML authenticator   


 * This property need not be set.

  
**thumbprintAccepted**|  xsd:boolean|  Whether the thumbprint of the SAML authenticator was accepted.   


 * This property need not be set.

  
**certificateHealth**| [CertificateHealthData](vdi.health.CertificateHealthData.md)|  The health of the certificate.   


 * This property need not be set.
  * This property is required if thumbprintAccepted is set to false.

  
**refId**|  xsd:string|  Reference ID of the connection server.  **_Since_** Horizon 7.10  


 * This property need not be set.

  
**lastUpdatedTimestamp**|  xsd:long|  The timestamp in milliseconds when the last update was obtained. Measured as epoch time.  **_Since_** Horizon 7.12  


 * This property need not be set.
 * This property cannot be updated.

  
  
  
   
  
  

