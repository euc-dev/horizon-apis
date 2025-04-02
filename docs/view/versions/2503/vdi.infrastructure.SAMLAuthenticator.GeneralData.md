---
layout: page
title: Data Object - SAMLAuthenticatorGeneralData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.SAMLAuthenticator.GeneralData`

Property of
> [SAMLAuthenticatorInfo](vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorInfo.md#field_detail), [SAMLAuthenticatorSpec](vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorSpec.md#field_detail)

See also
> [SAMLAuthenticatorCertificateSSOData](../2406/vdi.infrastructure.SAMLAuthenticator.CertificateSSOData.md)

Since
> Horizon View 6.0


## Data Object Description

General data for a SAML authenticator.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**label**|  xsd:string|  The label for this SAML authenticator. It must be unique among all other SAML authenticators. [^297]
**description**|  xsd:string|  The description of this SAML authenticator. [^1] [^13]
**certificateSSOData**| [SAMLAuthenticatorCertificateSSOData](../2406/vdi.infrastructure.SAMLAuthenticator.CertificateSSOData.md)|  Certificate SSO data for this SAML authenticator.  **_Since_** Horizon 7.0
**enforceEncryptedAssertion**|  xsd:boolean|  This indicates that particular Authenticator is for Workspace one or not. This property has a default value of false.
**workspaceOneEnabled**|  xsd:boolean|  This indicates that particular Authenticator is for Workspace one or not.
**forceSamlAuth**|  xsd:boolean|  This indicates that IDP will force the user to authenticate even if the user is already logged in.


 


[^1]: This property need not be set.
[^13]: This property has a maximum length of 1024 characters.
[^297]: This property has a maximum length of 32 characters.