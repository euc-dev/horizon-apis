---
layout: page
title: Data Object - CertificateSSOCertificateServerData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.CertificateSSOEnrollmentServer.CertificateServerData  
Property of
     [CertificateSSOCertificateDomainData](vdi.infrastructure.CertificateSSOEnrollmentServer.DomainData.md#field_detail)  
Since 
    Horizon 7.0

## Data Object Description 

Certificate server data. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  Unique (common) name of this certificate server.   
  
**networkAddress**|  xsd:string|  DNS name network address of this certificate server.   


 * This property need not be set.

  
**connectionStatus**|  xsd:string|  The status of the enrollment server's connection to the certificate server.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"CONNECTED"| The enrollment server is connected to the certificate server.  
"CONNECTED_DEGRADED"| The enrollment server has connected to the certificate server, but the certificate server is in a degraded state. Either the database is loading and it can't yet issue certificates (for up to 20 seconds) OR the last request took an excessive time to complete (more than 1000 milliseconds).  
"SERVICE_UNAVAILABLE"| The enrollment server can connect to the certificate server, but the service is unavailable. A certificate server with a service in this status cannot be used in connector creation.  
"DISCONNECTED"| The enrollment server is not connected to the certificate server.  

  
**connectionStatusReason**|  xsd:string|  Additional non-localized explanation of the connection status.   


 * This property need not be set.

  
**certificateStatus**|  xsd:string|  The status of the certificate server's certificate.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"VALID"| The certificate is valid.  
"NOT_YET_VALID"| The certificate is not yet valid.  
"UNKNOWN"| The certificate status is unknown. A certificate server with a certificate with this status cannot be used in connector creation.  
"INVALID"| The certificate is corrupt or unable to be used. A certificate server with a certificate with this status cannot be used in connector creation.  
"EXPIRED"| The certificate has expired. A certificate server with a certificate with this status cannot be used in connector creation.  
"NOT_TRUSTED"| The certificate is not in the NTAuth (Enterprise) store. A certificate server with a certificate with this status cannot be used in connector creation.  

  
**templateNames**|  xsd:string[]|  Collection of certificate template names available to this certificate server.   


 * This property need not be set.
  * This property is an unordered array of unique values.
 * This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

