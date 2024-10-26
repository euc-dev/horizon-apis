---
layout: page
title: Data Object - CertificateSSOCertificateDomainData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.CertificateSSOEnrollmentServer.DomainData`

Property of
> [CertificateSSOEnrollmentServerData](vdi.infrastructure.CertificateSSOEnrollmentServer.CertificateSSOEnrollmentServerData.md#field_detail)

See also
> [ADDomainId](vdi.entity.ADDomainId.md), [CertificateSSOCertificateServerData](vdi.infrastructure.CertificateSSOEnrollmentServer.CertificateServerData.md), [CertificateSSOTemplateData](vdi.infrastructure.CertificateSSOEnrollmentServer.TemplateData.md)

Since
> Horizon 7.0


## Data Object Description

Domain data.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**domain**| [ADDomainId](vdi.entity.ADDomainId.md)|  Id of the domain
**dnsName**|  xsd:string|  DNS name of the domain.
**forestDnsName**|  xsd:string|  DNS name of the domain's forest, if any. [^1]
**domainStatus**|  xsd:string|  The status of this domain to the enrollment server.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"READY"</td><td>The domain is ready.</td></tr><tr><td>"CREATED"</td><td>The domain is created.</td></tr><tr><td>"INITIALIZED"</td><td>The domain is initialized.</td></tr><tr><td>"CONNECTING"</td><td>The domain is connecting.</td></tr><tr><td>"ASSOCIATED"</td><td>This domain has been associated with a Forest, but we do not yet have a connection to this domain. We have no means of syncing objects for this forest from this domain, so it may only operate as long as there is another domain in the same forest that we can synchronize with.</td></tr><tr><td>"STOPPING"</td><td>The domain is stopping. A domain with this status cannot be used in connector creation.</td></tr><tr><td>"FAILED"</td><td>The domain is failed. A domain with this status cannot be used in connector creation.</td></tr><tr><td>"UNKNOWN"</td><td>The domain status is unknown. A domain with this status cannot be used in connector creation.</td></tr></table>
**domainStatusReason**|  xsd:string|  Additional non-localized explanation of the domain status. [^1]
**replicationStatus**|  xsd:string|  This domain's forest's replication status with the domain controller.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"OK"</td><td>The enrollment server has read the enrollment properties at least once and is successfully able to update them periodically.</td></tr><tr><td>"DEGRADED"</td><td>The enrollment server has read the enrollment properties at least once, but has not been able to reach a domain controller for some time.</td></tr><tr><td>"PENDING"</td><td>The enrollment server has not yet read the enrollment properties from a domain controller.</td></tr><tr><td>"FAILED"</td><td>The enrollment server has read the enrollment properties at least once but either has not been able to reach a domain controller for an extended time or another issue exists. An enrollment server with this status cannot be used in connector creation.</td></tr></table>
**replicationStatusReason**|  xsd:string|  Additional non-localized explanation of the replication status. [^1]
**enrollmentCertificateStatus**|  xsd:string|  The status of the enrollment server's certificate for this domain's forest.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"VALID"</td><td>A valid enrollment certificate for this domain's forest is installed on the enrollment server.</td></tr><tr><td>"NOT_VALID"</td><td>No valid enrollment certificate for this domain's forest is installed on the enrollment server, or it may have expired. An enrollment server with this status cannot be used in connector creation.</td></tr></table>
**certificateServers**| [CertificateSSOCertificateServerData[]](vdi.infrastructure.CertificateSSOEnrollmentServer.CertificateServerData.md)|  Collection of certificate server data available to this domain. [^1] [^14] [^2]
**templates**| [CertificateSSOTemplateData[]](vdi.infrastructure.CertificateSSOEnrollmentServer.TemplateData.md)|  Collection of certificate template data available to certificate servers on this domain. Not all certificate servers may have access to all of these templates. [^1] [^14] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^14]: This property is an unordered array of unique values.