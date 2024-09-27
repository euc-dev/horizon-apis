---
layout: page
title: Data Object - CertificateSSOConnectorConnectorHealthData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.CertificateSSOConnectorHealth.ConnectorHealthData  
Property of
     [CertificateSSOConnectorHealthInfo](vdi.health.CertificateSSOConnectorHealth.CertificateSSOConnectorHealthInfo.md#field_detail)  
See also
     [CertificateSSOConnectorHealthEnrollmentServerCertificateServerHealthData](vdi.health.CertificateSSOConnectorHealth.CertificateServerHealthData.md), [CertificateSSOConnectorHealthEnrollmentServerDomainHealthData](vdi.health.CertificateSSOConnectorHealth.DomainHealthData.md), [CertificateSSOConnectorHealthEnrollmentServerHealthData](vdi.health.CertificateSSOConnectorHealth.EnrollmentServerHealthData.md), [CertificateSSOConnectorHealthEnrollmentServerTemplateHealthData](vdi.health.CertificateSSOConnectorHealth.TemplateHealthData.md)  
Since 
    Horizon 7.0

## Data Object Description 

The health data for a CertSSO connector. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**overallState**|  xsd:string|  The overall state of the connector. This represents the most severe state of all the component health states.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"OK"| Overall state is green.  
"WARN"| Overall state is yellow.  
"ERROR"| Overall state is red.  

  
**primaryEnrollmentServerHealth**| [CertificateSSOConnectorHealthEnrollmentServerHealthData](vdi.health.CertificateSSOConnectorHealth.EnrollmentServerHealthData.md)|  The primary enrollment server health.   
  
**secondaryEnrollmentServerHealth**| [CertificateSSOConnectorHealthEnrollmentServerHealthData](vdi.health.CertificateSSOConnectorHealth.EnrollmentServerHealthData.md)|  The secondary enrollment server health.   


* This property need not be set.

  
**domainHealth**| [CertificateSSOConnectorHealthEnrollmentServerDomainHealthData](vdi.health.CertificateSSOConnectorHealth.DomainHealthData.md)|  The health of the domain.   
  
**templateHealth**| [CertificateSSOConnectorHealthEnrollmentServerTemplateHealthData](vdi.health.CertificateSSOConnectorHealth.TemplateHealthData.md)|  The health of the template.   
  
**certificateServerHealths**| [CertificateSSOConnectorHealthEnrollmentServerCertificateServerHealthData[]](vdi.health.CertificateSSOConnectorHealth.CertificateServerHealthData.md)|  The health of each certificate server.   
  
  
  
   
  
  

