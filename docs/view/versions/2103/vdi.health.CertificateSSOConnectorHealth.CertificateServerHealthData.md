---
layout: page
title: Data Object - CertificateSSOConnectorHealthEnrollmentServerCertificateServerHealthData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.health.CertificateSSOConnectorHealth.CertificateServerHealthData`

Property of
> [CertificateSSOConnectorConnectorHealthData](vdi.health.CertificateSSOConnectorHealth.ConnectorHealthData.md#field_detail)

Since
> Horizon 7.0


## Data Object Description

The health data for a CertSSO certificate server.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**name**|  xsd:string|  The common name of the certificate server.
**state**|  xsd:string|  The state of the certificate server health, taken as the most severe reported by one of the enrollment servers.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"OK"</td><td>Certificate server is green.</td></tr><tr><td>"WARN"</td><td>Certificate server is yellow.</td></tr><tr><td>"ERROR"</td><td>Certificate server is red.</td></tr></table>
**primaryEnrollmentServerStateReasons**|  xsd:string[]|  Reasons for the state from the primary enrollment server, if any. [^1]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"CONNECTED_DEGRADED"</td><td>Warn: The enrollment server has connected to the certificate server, but the certificate server is in a degraded state.</td></tr><tr><td>"DISCONNECTED"</td><td>Error: The enrollment server is not connected to the certificate server.</td></tr><tr><td>"SERVICE_UNAVAILABLE"</td><td>Error: The enrollment server can connect to the certificate server, but the service is unavailable.</td></tr><tr><td>"NOT_FOUND"</td><td>Error: The certificate server does not exist on the enrollment server domain.</td></tr><tr><td>"CERTIFICATE_NOT_YET_VALID"</td><td>Error: The certificate is not yet valid.</td></tr><tr><td>"CERTIFICATE_UNKNOWN"</td><td>Error: The certificate status is unknown.</td></tr><tr><td>"CERTIFICATE_INVALID"</td><td>Error: The certificate is corrupt or unable to be used. A certificate server with a certificate with this status cannot be used in connector creation.</td></tr><tr><td>"CERTIFICATE_EXPIRED"</td><td>Error: The certificate has expired. A certificate server with a certificate with this status cannot be used in connector creation.</td></tr><tr><td>"CERTIFICATE_NOT_TRUSTED"</td><td>Error: The certificate is not in the NTAuth (Enterprise) store. A certificate server with a certificate with this status cannot be used in connector creation.</td></tr><tr><td>"CERTIFICATE_TEMPLATE_NOT_PUBLISHED"</td><td>Error: The certificate template is not published on this CA.</td></tr></table>
**secondaryEnrollmentServerStateReasons**|  xsd:string[]|  Reasons for the state from the secondary enrollment server, if any. [^1]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"CONNECTED_DEGRADED"</td><td>Warn: The enrollment server has connected to the certificate server, but the certificate server is in a degraded state.</td></tr><tr><td>"DISCONNECTED"</td><td>Error: The enrollment server is not connected to the certificate server.</td></tr><tr><td>"SERVICE_UNAVAILABLE"</td><td>Error: The enrollment server can connect to the certificate server, but the service is unavailable.</td></tr><tr><td>"NOT_FOUND"</td><td>Error: The certificate server does not exist on the enrollment server domain.</td></tr><tr><td>"CERTIFICATE_NOT_YET_VALID"</td><td>Error: The certificate is not yet valid.</td></tr><tr><td>"CERTIFICATE_UNKNOWN"</td><td>Error: The certificate status is unknown.</td></tr><tr><td>"CERTIFICATE_INVALID"</td><td>Error: The certificate is corrupt or unable to be used. A certificate server with a certificate with this status cannot be used in connector creation.</td></tr><tr><td>"CERTIFICATE_EXPIRED"</td><td>Error: The certificate has expired. A certificate server with a certificate with this status cannot be used in connector creation.</td></tr><tr><td>"CERTIFICATE_NOT_TRUSTED"</td><td>Error: The certificate is not in the NTAuth (Enterprise) store. A certificate server with a certificate with this status cannot be used in connector creation.</td></tr><tr><td>"CERTIFICATE_TEMPLATE_NOT_PUBLISHED"</td><td>Error: The certificate template is not published on this CA.</td></tr></table>


 
