---
layout: page
title: Data Object - CertificateSSOCertificateDomainData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.CertificateSSOEnrollmentServer.DomainData  
Property of
     [CertificateSSOEnrollmentServerData](vdi.infrastructure.CertificateSSOEnrollmentServer.CertificateSSOEnrollmentServerData.md#field_detail)  
See also
     [ADDomainId](vdi.entity.ADDomainId.md), [CertificateSSOCertificateServerData](vdi.infrastructure.CertificateSSOEnrollmentServer.CertificateServerData.md), [CertificateSSOTemplateData](vdi.infrastructure.CertificateSSOEnrollmentServer.TemplateData.md)  
Since 
    Horizon 7.0

## Data Object Description 

Domain data. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**domain**| [ADDomainId](vdi.entity.ADDomainId.md)|  Id of the domain   
  
**dnsName**|  xsd:string|  DNS name of the domain.   
  
**forestDnsName**|  xsd:string|  DNS name of the domain's forest, if any.   


* This property need not be set.

  
**domainStatus**|  xsd:string|  The status of this domain to the enrollment server.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"READY"| The domain is ready.  
"CREATED"| The domain is created.  
"INITIALIZED"| The domain is initialized.  
"CONNECTING"| The domain is connecting.  
"ASSOCIATED"| This domain has been associated with a Forest, but we do not yet have a connection to this domain. We have no means of syncing objects for this forest from this domain, so it may only operate as long as there is another domain in the same forest that we can synchronize with.  
"STOPPING"| The domain is stopping. A domain with this status cannot be used in connector creation.  
"FAILED"| The domain is failed. A domain with this status cannot be used in connector creation.  
"UNKNOWN"| The domain status is unknown. A domain with this status cannot be used in connector creation.  

  
**domainStatusReason**|  xsd:string|  Additional non-localized explanation of the domain status.   


* This property need not be set.

  
**replicationStatus**|  xsd:string|  This domain's forest's replication status with the domain controller.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"OK"| The enrollment server has read the enrollment properties at least once and is successfully able to update them periodically.  
"DEGRADED"| The enrollment server has read the enrollment properties at least once, but has not been able to reach a domain controller for some time.  
"PENDING"| The enrollment server has not yet read the enrollment properties from a domain controller.  
"FAILED"| The enrollment server has read the enrollment properties at least once but either has not been able to reach a domain controller for an extended time or another issue exists. An enrollment server with this status cannot be used in connector creation.  

  
**replicationStatusReason**|  xsd:string|  Additional non-localized explanation of the replication status.   


* This property need not be set.

  
**enrollmentCertificateStatus**|  xsd:string|  The status of the enrollment server's certificate for this domain's forest.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"VALID"| A valid enrollment certificate for this domain's forest is installed on the enrollment server.  
"NOT_VALID"| No valid enrollment certificate for this domain's forest is installed on the enrollment server, or it may have expired. An enrollment server with this status cannot be used in connector creation.  

  
**certificateServers**| [CertificateSSOCertificateServerData[]](vdi.infrastructure.CertificateSSOEnrollmentServer.CertificateServerData.md)|  Collection of certificate server data available to this domain.   


* This property need not be set.
  * This property is an unordered array of unique values.
* This property cannot be updated.

  
**templates**| [CertificateSSOTemplateData[]](vdi.infrastructure.CertificateSSOEnrollmentServer.TemplateData.md)|  Collection of certificate template data available to certificate servers on this domain. Not all certificate servers may have access to all of these templates.   


* This property need not be set.
  * This property is an unordered array of unique values.
* This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

