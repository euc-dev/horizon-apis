---
layout: page
title: Data Object - CertificateSSOConnectorHealthEnrollmentServerDomainHealthData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.CertificateSSOConnectorHealth.DomainHealthData`

Property of
> [CertificateSSOConnectorConnectorHealthData](vdi.health.CertificateSSOConnectorHealth.ConnectorHealthData.md#field_detail)

See also
> [ADDomainId](vdi.entity.ADDomainId.md)

Since
> Horizon 7.0


## Data Object Description

The health data for a CertSSO connector domain.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**domain**| [ADDomainId](vdi.entity.ADDomainId.md)|  The id of the domain.
**dnsName**|  xsd:string|  The DNS name of the domain.
**state**|  xsd:string|  The state of the domain health, taken as the most severe reported by one of the enrollment servers.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"OK"</td><td>Domain is green.</td></tr><tr><td>"WARN"</td><td>Domain is yellow.</td></tr><tr><td>"ERROR"</td><td>Domain is red.</td></tr></table>
**primaryEnrollmentServerStateReasons**|  xsd:string[]|  Reasons for the state from the primary enrollment server, if any. [^1]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"CONNECTION_ESTABLISHING"</td><td>Error: The enrollment server's connection to the domain is still being established (CREATED, INITIALIZED, or CONNECTING).</td></tr><tr><td>"CONNECTION_FAILED"</td><td>Error: The enrollment server's connection to the domain is stopping or in a problematic state (ASSOCIATED, STOPPING, FAILED, or UNKNOWN).</td></tr><tr><td>"REPLICATION_DEGRADED"</td><td>Warn: The enrollment server has read the enrollment properties at least once, but has not been able to reach a domain controller for some time.</td></tr><tr><td>"NOT_FOUND"</td><td>Error: This domain does not exist on the enrollment server.</td></tr><tr><td>"REPLICATION_PENDING"</td><td>Error: The enrollment server has not yet read the enrollment properties from a domain controller.</td></tr><tr><td>"REPLICATION_FAILED"</td><td>Error: The enrollment server has read the enrollment properties at least once but either has not been able to reach a domain controller for an extended time or another issue exists. An enrollment server with this status cannot be used in connector creation.</td></tr><tr><td>"CERTIFICATE_NOT_VALID"</td><td>Error: No valid enrollment certificate for this domain's forest is installed on the enrollment server, or it may have expired. An enrollment server with this status cannot be used in connector creation.</td></tr></table>
**secondaryEnrollmentServerStateReasons**|  xsd:string[]|  Reasons for the state from the secondary enrollment server, if any. [^1]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"CONNECTION_ESTABLISHING"</td><td>Error: The enrollment server's connection to the domain is still being established (CREATED, INITIALIZED, or CONNECTING).</td></tr><tr><td>"CONNECTION_FAILED"</td><td>Error: The enrollment server's connection to the domain is stopping or in a problematic state (ASSOCIATED, STOPPING, FAILED, or UNKNOWN).</td></tr><tr><td>"REPLICATION_DEGRADED"</td><td>Warn: The enrollment server has read the enrollment properties at least once, but has not been able to reach a domain controller for some time.</td></tr><tr><td>"NOT_FOUND"</td><td>Error: This domain does not exist on the enrollment server.</td></tr><tr><td>"REPLICATION_PENDING"</td><td>Error: The enrollment server has not yet read the enrollment properties from a domain controller.</td></tr><tr><td>"REPLICATION_FAILED"</td><td>Error: The enrollment server has read the enrollment properties at least once but either has not been able to reach a domain controller for an extended time or another issue exists. An enrollment server with this status cannot be used in connector creation.</td></tr><tr><td>"CERTIFICATE_NOT_VALID"</td><td>Error: No valid enrollment certificate for this domain's forest is installed on the enrollment server, or it may have expired. An enrollment server with this status cannot be used in connector creation.</td></tr></table>
**refId**|  xsd:string|  Reference ID used for this domain.  **_Since_** Horizon 7.11 [^1]
 


 


[^1]: This property need not be set.