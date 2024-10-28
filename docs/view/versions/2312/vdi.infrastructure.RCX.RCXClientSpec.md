---
layout: page
title: Data Object - RCXClientSpec
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.RCX.RCXClientSpec`

See also
> [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md)

Since
> Horizon 7.11


## Data Object Description

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**name**|  xsd:string|  The cn of the RCX client certificate.
**thumbprints**| [CertificateThumbprint[]](vdi.utils.Certificate.CertificateThumbprint.md)|  Thumbprints of the RCX client certificate.
**address**|  xsd:string|  IP address of the RCX client. [^1]


 


[^1]: This property need not be set.