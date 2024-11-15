---
layout: page
title: Data Object - CertificateSSOConnectorConnectorHealthData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.CertificateSSOConnectorHealth.ConnectorHealthData`

Property of
> [CertificateSSOConnectorHealthInfo](vdi.health.CertificateSSOConnectorHealth.CertificateSSOConnectorHealthInfo.md#field_detail)

See also
> [CertificateSSOConnectorHealthEnrollmentServerCertificateServerHealthData](vdi.health.CertificateSSOConnectorHealth.CertificateServerHealthData.md), [CertificateSSOConnectorHealthEnrollmentServerDomainHealthData](vdi.health.CertificateSSOConnectorHealth.DomainHealthData.md), [CertificateSSOConnectorHealthEnrollmentServerHealthData](vdi.health.CertificateSSOConnectorHealth.EnrollmentServerHealthData.md), [CertificateSSOConnectorHealthEnrollmentServerTemplateHealthData](vdi.health.CertificateSSOConnectorHealth.TemplateHealthData.md)

Since
> Horizon 7.0


## Data Object Description

The health data for a CertSSO connector.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**overallState**|  xsd:string|  The overall state of the connector. This represents the most severe state of all the component health states.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"OK"</td><td>Overall state is green.</td></tr><tr><td>"WARN"</td><td>Overall state is yellow.</td></tr><tr><td>"ERROR"</td><td>Overall state is red.</td></tr></table>
**primaryEnrollmentServerHealth**| [CertificateSSOConnectorHealthEnrollmentServerHealthData](vdi.health.CertificateSSOConnectorHealth.EnrollmentServerHealthData.md)|  The primary enrollment server health.
**secondaryEnrollmentServerHealth**| [CertificateSSOConnectorHealthEnrollmentServerHealthData](vdi.health.CertificateSSOConnectorHealth.EnrollmentServerHealthData.md)|  The secondary enrollment server health. [^1]
**domainHealth**| [CertificateSSOConnectorHealthEnrollmentServerDomainHealthData](vdi.health.CertificateSSOConnectorHealth.DomainHealthData.md)|  The health of the domain.
**templateHealth**| [CertificateSSOConnectorHealthEnrollmentServerTemplateHealthData](vdi.health.CertificateSSOConnectorHealth.TemplateHealthData.md)|  The health of the template.
**certificateServerHealths**| [CertificateSSOConnectorHealthEnrollmentServerCertificateServerHealthData[]](vdi.health.CertificateSSOConnectorHealth.CertificateServerHealthData.md)|  The health of each certificate server.


 


[^1]: This property need not be set.