---
layout: page
title: Data Object - SAMLAuthenticatorSpec
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorSpec`

Parameter to
> [SAMLAuthenticator_Create](../2406/vdi.infrastructure.SAMLAuthenticator.md#create)

See also
> [CertificateThumbprint](../2406/vdi.utils.Certificate.CertificateThumbprint.md), [ConnectionServerId](../2406/vdi.entity.ConnectionServerId.md), [SAMLAuthenticatorGeneralData](vdi.infrastructure.SAMLAuthenticator.GeneralData.md), [SAMLAuthenticatorServerData](../2406/vdi.infrastructure.SAMLAuthenticator.ServerData.md)

Since
> Horizon View 6.0


## Data Object Description

The specification for creating a SAML authenticator.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**general**| [SAMLAuthenticatorGeneralData](vdi.infrastructure.SAMLAuthenticator.GeneralData.md)|  General data on the SAML Authenticator.
**server**| [SAMLAuthenticatorServerData](../2406/vdi.infrastructure.SAMLAuthenticator.ServerData.md)|  Data on the SAML authenticator server
**certificateOverride**| [CertificateThumbprint](../2406/vdi.utils.Certificate.CertificateThumbprint.md)|  The certificate override for the SAML authenticator. [^1]
**connectionServers**| [ConnectionServerId[]](../2406/vdi.entity.ConnectionServerId.md)|  The list of Connection Servers for which this SAML authenticator is enabled.  **_Since_** Horizon 7.8 [^1]


 


[^1]: This property need not be set.