---
layout: page
title: Data Object - SAMLAuthenticatorInfo
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorInfo`

Returned by
> [SAMLAuthenticator_Get](vdi.infrastructure.SAMLAuthenticator.md#get), [SAMLAuthenticator_List](vdi.infrastructure.SAMLAuthenticator.md#list)

See also
> [CertificateThumbprint](../2406/vdi.utils.Certificate.CertificateThumbprint.md), [SAMLAuthenticatorGeneralData](vdi.infrastructure.SAMLAuthenticator.GeneralData.md), [SAMLAuthenticatorId](vdi.entity.SAMLAuthenticatorId.md), [SAMLAuthenticatorServerData](../2406/vdi.infrastructure.SAMLAuthenticator.ServerData.md)

Since
> Horizon View 6.0


## Data Object Description

Information about a SAML authenticator.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [SAMLAuthenticatorId](../2406/vdi.entity.SAMLAuthenticatorId.md)|  The ID of the SAML authenticator/
**general**| [SAMLAuthenticatorGeneralData](vdi.infrastructure.SAMLAuthenticator.GeneralData.md)|  General data on the SAML Authenticator.
**server**| [SAMLAuthenticatorServerData](../2406/vdi.infrastructure.SAMLAuthenticator.ServerData.md)|  Data on the SAML authenticator server
**certificateOverride**| [CertificateThumbprint](../2406/vdi.utils.Certificate.CertificateThumbprint.md)|  The certificate override for the SAML authenticator. [^1]
**refId**|  xsd:string|  Reference ID used for this SAML Authenticator.  **_Since_** Horizon 8.7 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.