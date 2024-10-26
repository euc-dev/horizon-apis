---
layout: page
title: Data Object - CertificateSSOCertificateServerData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.CertificateSSOEnrollmentServer.CertificateServerData`

Property of
> [CertificateSSOCertificateDomainData](vdi.infrastructure.CertificateSSOEnrollmentServer.DomainData.md#field_detail)

Since
> Horizon 7.0


## Data Object Description

Certificate server data.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**name**|  xsd:string|  Unique (common) name of this certificate server.
**networkAddress**|  xsd:string|  DNS name network address of this certificate server. [^1]
**connectionStatus**|  xsd:string|  The status of the enrollment server's connection to the certificate server.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"CONNECTED"</td><td>The enrollment server is connected to the certificate server.</td></tr><tr><td>"CONNECTED_DEGRADED"</td><td>The enrollment server has connected to the certificate server, but the certificate server is in a degraded state. Either the database is loading and it can't yet issue certificates (for up to 20 seconds) OR the last request took an excessive time to complete (more than 1000 milliseconds).</td></tr><tr><td>"SERVICE_UNAVAILABLE"</td><td>The enrollment server can connect to the certificate server, but the service is unavailable. A certificate server with a service in this status cannot be used in connector creation.</td></tr><tr><td>"DISCONNECTED"</td><td>The enrollment server is not connected to the certificate server.</td></tr></table>
**connectionStatusReason**|  xsd:string|  Additional non-localized explanation of the connection status. [^1]
**certificateStatus**|  xsd:string|  The status of the certificate server's certificate.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"VALID"</td><td>The certificate is valid.</td></tr><tr><td>"NOT_YET_VALID"</td><td>The certificate is not yet valid.</td></tr><tr><td>"UNKNOWN"</td><td>The certificate status is unknown. A certificate server with a certificate with this status cannot be used in connector creation.</td></tr><tr><td>"INVALID"</td><td>The certificate is corrupt or unable to be used. A certificate server with a certificate with this status cannot be used in connector creation.</td></tr><tr><td>"EXPIRED"</td><td>The certificate has expired. A certificate server with a certificate with this status cannot be used in connector creation.</td></tr><tr><td>"NOT_TRUSTED"</td><td>The certificate is not in the NTAuth (Enterprise) store. A certificate server with a certificate with this status cannot be used in connector creation.</td></tr></table>
**templateNames**|  xsd:string[]|  Collection of certificate template names available to this certificate server. [^1] [^14] [^2]


 
