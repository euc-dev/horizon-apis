---
layout: page
title: Data Object - CertificateSSOConnectorHealthEnrollmentServerCertificateServerHealthData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.CertificateSSOConnectorHealth.CertificateServerHealthData  
Property of
     [CertificateSSOConnectorConnectorHealthData](vdi.health.CertificateSSOConnectorHealth.ConnectorHealthData.md#field_detail)  
Since 
    Horizon 7.0

## Data Object Description 

The health data for a CertSSO certificate server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  The common name of the certificate server.   
  
**state**|  xsd:string|  The state of the certificate server health, taken as the most severe reported by one of the enrollment servers.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"OK"| Certificate server is green.  
"WARN"| Certificate server is yellow.  
"ERROR"| Certificate server is red.  

  
**primaryEnrollmentServerStateReasons**|  xsd:string[]|  Reasons for the state from the primary enrollment server, if any.   


* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"CONNECTED_DEGRADED"| Warn: The enrollment server has connected to the certificate server, but the certificate server is in a degraded state  
"DISCONNECTED"| Error: The enrollment server is not connected to the certificate server.  
"SERVICE_UNAVAILABLE"| Error: The enrollment server can connect to the certificate server, but the service is unavailable.  
"NOT_FOUND"| Error: The certificate server does not exist on the enrollment server domain.  
"CERTIFICATE_NOT_YET_VALID"| Error: The certificate is not yet valid.  
"CERTIFICATE_UNKNOWN"| Error: The certificate status is unknown.  
"CERTIFICATE_INVALID"| Error: The certificate is corrupt or unable to be used. A certificate server with a certificate with this status cannot be used in connector creation.  
"CERTIFICATE_EXPIRED"| Error: The certificate has expired. A certificate server with a certificate with this status cannot be used in connector creation.  
"CERTIFICATE_NOT_TRUSTED"| Error: The certificate is not in the NTAuth (Enterprise) store. A certificate server with a certificate with this status cannot be used in connector creation.  
"CERTIFICATE_TEMPLATE_NOT_PUBLISHED"| Error: The certificate template is not published on this CA.  

  
**secondaryEnrollmentServerStateReasons**|  xsd:string[]|  Reasons for the state from the secondary enrollment server, if any.   


* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"CONNECTED_DEGRADED"| Warn: The enrollment server has connected to the certificate server, but the certificate server is in a degraded state  
"DISCONNECTED"| Error: The enrollment server is not connected to the certificate server.  
"SERVICE_UNAVAILABLE"| Error: The enrollment server can connect to the certificate server, but the service is unavailable.  
"NOT_FOUND"| Error: The certificate server does not exist on the enrollment server domain.  
"CERTIFICATE_NOT_YET_VALID"| Error: The certificate is not yet valid.  
"CERTIFICATE_UNKNOWN"| Error: The certificate status is unknown.  
"CERTIFICATE_INVALID"| Error: The certificate is corrupt or unable to be used. A certificate server with a certificate with this status cannot be used in connector creation.  
"CERTIFICATE_EXPIRED"| Error: The certificate has expired. A certificate server with a certificate with this status cannot be used in connector creation.  
"CERTIFICATE_NOT_TRUSTED"| Error: The certificate is not in the NTAuth (Enterprise) store. A certificate server with a certificate with this status cannot be used in connector creation.  
"CERTIFICATE_TEMPLATE_NOT_PUBLISHED"| Error: The certificate template is not published on this CA.  

  
  
  
   
  
  

