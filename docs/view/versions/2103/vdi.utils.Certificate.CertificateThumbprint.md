---
layout: page
title: Data Object - CertificateThumbprint
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.Certificate.CertificateThumbprint`

Property of
> [CertificateData](vdi.utils.Certificate.CertificateData.md#field_detail), [RCXClientSpec](vdi.infrastructure.RCX.RCXClientSpec.md#field_detail), [RCXServerInfo](vdi.infrastructure.RCX.RCXServerInfo.md#field_detail), [SAMLAuthenticatorInfo](vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorInfo.md#field_detail), [SAMLAuthenticatorSpec](vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorSpec.md#field_detail), [ServerDefinition](vdi.utils.Certificate.ServerDefinition.md#field_detail), [VirtualCenterInfo](vdi.infrastructure.VirtualCenter.VirtualCenterInfo.md#field_detail), [VirtualCenterSpec](vdi.infrastructure.VirtualCenter.VirtualCenterSpec.md#field_detail), [VirtualCenterViewComposerData](vdi.infrastructure.VirtualCenter.ViewComposerData.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Certificate thumbprint and corresponding algorithm.
 [^167]



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**sslCertThumbprint**|  xsd:string|  A digest of the certificate.
**sslCertThumbprintAlgorithm**|  xsd:string|  Algorithm used to compute the thumbprint.


 


[^167]: This data object must be updated as a whole.