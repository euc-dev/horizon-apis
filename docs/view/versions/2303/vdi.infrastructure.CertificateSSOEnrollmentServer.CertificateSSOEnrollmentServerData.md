---
layout: page
title: Data Object - CertificateSSOEnrollmentServerData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.CertificateSSOEnrollmentServer.CertificateSSOEnrollmentServerData`

Property of
> [CertificateSSOEnrollmentServerInfo](vdi.infrastructure.CertificateSSOEnrollmentServer.CertificateSSOEnrollmentServerInfo.md#field_detail)

See also
> [CertificateSSOCertificateDomainData](vdi.infrastructure.CertificateSSOEnrollmentServer.DomainData.md), [CertificateSSOConnectorId](vdi.entity.CertificateSSOConnectorId.md)

Since
> Horizon 7.0


## Data Object Description

Configuration data for a Certificate SSO Enrollment Server.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**name**|  xsd:string|  Name of this enrollment server. [^1] [^2]
**networkAddress**|  xsd:string|  DNS name network address of this enrollment server. [^1] [^2]
**version**|  xsd:string|  Version number of this enrollment server. [^1] [^2]
**status**|  xsd:string|  The status of this enrollment server. [^2]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"ONLINE"</td><td>The connection to the enrollment server is working properly.</td></tr><tr><td>"OFFLINE"</td><td>The enrollment server is not responding. An enrollment server with this status cannot be used in connector creation.</td></tr></table>
**connectors**| [CertificateSSOConnectorId[]](vdi.entity.CertificateSSOConnectorId.md)|  CertSSO connectors, if any, associated with this enrollment server. [^1] [^2]
**domains**| [CertificateSSOCertificateDomainData[]](vdi.infrastructure.CertificateSSOEnrollmentServer.DomainData.md)|  Collection of domain data available to this enrollment server. [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.