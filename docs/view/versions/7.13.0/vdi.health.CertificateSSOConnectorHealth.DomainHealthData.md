---
layout: page
title: Data Object - CertificateSSOConnectorHealthEnrollmentServerDomainHealthData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.CertificateSSOConnectorHealth.DomainHealthData
Property of
     [CertificateSSOConnectorConnectorHealthData](vdi.health.CertificateSSOConnectorHealth.ConnectorHealthData.md#field_detail)
See also
     [ADDomainId](vdi.entity.ADDomainId.md)
Since 
    Horizon 7.0

## Data Object Description 

The health data for a CertSSO connector domain. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**domain**| [ADDomainId](vdi.entity.ADDomainId.md)|  The id of the domain.   
  
**dnsName**|  xsd:string|  The DNS name of the domain.   
  
**state**|  xsd:string|  The state of the domain health, taken as the most severe reported by one of the enrollment servers.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"OK"| Domain is green.  
"WARN"| Domain is yellow.  
"ERROR"| Domain is red.  

  
**primaryEnrollmentServerStateReasons**|  xsd:string[]|  Reasons for the state from the primary enrollment server, if any.   


[^1]
  * This property will be one of:  
|  Value |  Description   
---|---  
"CONNECTION_ESTABLISHING"| Error: The enrollment server's connection to the domain is still being established (CREATED, INITIALIZED, or CONNECTING).  
"CONNECTION_FAILED"| Error: The enrollment server's connection to the domain is stopping or in a problematic state (ASSOCIATED, STOPPING, FAILED, or UNKNOWN).  
"REPLICATION_DEGRADED"| Warn: The enrollment server has read the enrollment properties at least once, but has not been able to reach a domain controller for some time.  
"NOT_FOUND"| Error: This domain does not exist on the enrollment server.  
"REPLICATION_PENDING"| Error: The enrollment server has not yet read the enrollment properties from a domain controller.  
"REPLICATION_FAILED"| Error: The enrollment server has read the enrollment properties at least once but either has not been able to reach a domain controller for an extended time or another issue exists. An enrollment server with this status cannot be used in connector creation.  
"CERTIFICATE_NOT_VALID"| Error: No valid enrollment certificate for this domain's forest is installed on the enrollment server, or it may have expired. An enrollment server with this status cannot be used in connector creation.  

  
**secondaryEnrollmentServerStateReasons**|  xsd:string[]|  Reasons for the state from the secondary enrollment server, if any.   


[^1]
  * This property will be one of:  
|  Value |  Description   
---|---  
"CONNECTION_ESTABLISHING"| Error: The enrollment server's connection to the domain is still being established (CREATED, INITIALIZED, or CONNECTING).  
"CONNECTION_FAILED"| Error: The enrollment server's connection to the domain is stopping or in a problematic state (ASSOCIATED, STOPPING, FAILED, or UNKNOWN).  
"REPLICATION_DEGRADED"| Warn: The enrollment server has read the enrollment properties at least once, but has not been able to reach a domain controller for some time.  
"NOT_FOUND"| Error: This domain does not exist on the enrollment server.  
"REPLICATION_PENDING"| Error: The enrollment server has not yet read the enrollment properties from a domain controller.  
"REPLICATION_FAILED"| Error: The enrollment server has read the enrollment properties at least once but either has not been able to reach a domain controller for an extended time or another issue exists. An enrollment server with this status cannot be used in connector creation.  
"CERTIFICATE_NOT_VALID"| Error: No valid enrollment certificate for this domain's forest is installed on the enrollment server, or it may have expired. An enrollment server with this status cannot be used in connector creation.  

  
**refId**|  xsd:string|  Reference ID used for this domain.  **_Since_** Horizon 7.11  


[^1]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
