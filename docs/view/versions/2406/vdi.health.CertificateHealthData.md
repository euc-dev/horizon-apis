---
layout: page
title: Data Object - CertificateHealthData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.CertificateHealthData`

Property of
> [ConnectionServerHealthInfo](vdi.health.ConnectionServerHealth.ConnectionServerHealthInfo.md#field_detail), [SAMLAuthenticatorHealthConnectionServerConnectionData](vdi.health.SAMLAuthenticatorHealth.ConnectionServerConnectionData.md#field_detail), [SecurityServerHealthInfo](vdi.health.SecurityServerHealth.SecurityServerHealthInfo.md#field_detail), [ViewComposerHealthConnectionServerConnectionData](vdi.health.ViewComposerHealth.ConnectionServerConnectionData.md#field_detail), [VirtualCenterHealthConnectionServerConnectionData](vdi.health.VirtualCenterHealth.ConnectionServerConnectionData.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Health data about a server's certificate.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**valid**|  xsd:boolean|  Is the certificate valid? [^1]
**startTime**|  xsd:dateTime|  When is certificate valid from? [^1]
**expirationTime**|  xsd:dateTime|  When the certificate expires. [^1]
**invalidReason**|  xsd:string|  If the certificate is not valid, the reason why. [^1]
**connectionServerCertificate**|  xsd:string|  Connection server certificate in PEM format.  **_Since_** Horizon 7.2 [^1]
**ignoreSecureGatewayCertStatus**|  xsd:boolean|  If true, indicates that the certificate health of the Secure Gateway instances should be ignored when showing the overall health status of a connection server.  **_Since_** Horizon 7.10 [^1]
**certificateType**|  xsd:string|  A String indicating the type of the connection server certificate. It can be MACHINE, CLUSTER or CLUSTER_ENCRYPTION  **_Since_** Horizon 8.12 [^1]
**managed**|  xsd:boolean|  If true, it indicates that the given certificate renews automatically.  **_Since_** Horizon 8.12 [^1]


 


[^1]: This property need not be set.