---
layout: page
title: Data Object - GlobalSettingsCertificateAuthenticationData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.GlobalSettings.CertificateAuthenticationData`

Property of
> [GlobalSettingsSecurityData](vdi.infrastructure.GlobalSettings.SecurityData.md#field_detail)

Since
> Horizon 8.10


## Data Object Description

Supports custom mapping for certificate authentication.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**certAuthMapping**|  xsd:string[]|  Indicates the custom certificate mapping and certificate validation will be done based on all the strings given in certAuthMapping. [^1]
**certAuthMappingControl**|  xsd:string[]|  Indicates the types of mapping to validate certificate. [^1]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"SID"</td><td>Denotes certificate validation on SID.</td></tr><tr><td>"CUSTOM"</td><td>Denotes certificate validation on custom mapping.</td></tr><tr><td>"LEGACY"</td><td>Denotes legacy certificate validation. In LEGACY mode, the certificate validation is based on User Principal Names(UPN) first, if UPN is unavailable we match X509IssuerSubject or X509SubjectOnly present at altSecurityIdentities attribute of the users Object.</td></tr></table>
**certAuthMappingNames**|  xsd:string[]|  List of all supported certificate mapping properties. [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.