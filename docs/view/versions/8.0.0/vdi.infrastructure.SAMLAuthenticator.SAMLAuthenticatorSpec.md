---
layout: page
title: Data Object - SAMLAuthenticatorSpec
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorSpec`

Parameter to  
> [SAMLAuthenticator_Create](vdi.infrastructure.SAMLAuthenticator.md#create)

See also  
> [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md), [ConnectionServerId](vdi.entity.ConnectionServerId.md), [SAMLAuthenticatorGeneralData](vdi.infrastructure.SAMLAuthenticator.GeneralData.md), [SAMLAuthenticatorServerData](vdi.infrastructure.SAMLAuthenticator.ServerData.md)

Since  
> Horizon View 6.0


## Data Object Description 

The specification for creating a SAML authenticator. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**general**| [SAMLAuthenticatorGeneralData](vdi.infrastructure.SAMLAuthenticator.GeneralData.md)|  General data on the SAML Authenticator.   
  
**server**| [SAMLAuthenticatorServerData](vdi.infrastructure.SAMLAuthenticator.ServerData.md)|  Data on the SAML authenticator server   
  
**certificateOverride**| [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md)|  The certificate override for the SAML authenticator.   


* This property need not be set.

  
**connectionServers**| [ConnectionServerId[]](vdi.entity.ConnectionServerId.md)|  The list of Connection Servers for which this SAML authenticator is enabled.  **_Since_** Horizon 7.8  


* This property need not be set.

  
  
  

  
  
