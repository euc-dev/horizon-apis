---
layout: page
title: Data Object - SAMLAuthenticatorInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorInfo`

Returned by  
> [SAMLAuthenticator_Get](vdi.infrastructure.SAMLAuthenticator.md#get), [SAMLAuthenticator_List](vdi.infrastructure.SAMLAuthenticator.md#list)

See also  
> [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md), [SAMLAuthenticatorGeneralData](vdi.infrastructure.SAMLAuthenticator.GeneralData.md), [SAMLAuthenticatorId](vdi.entity.SAMLAuthenticatorId.md), [SAMLAuthenticatorServerData](vdi.infrastructure.SAMLAuthenticator.ServerData.md)

Since  
> Horizon View 6.0


## Data Object Description 

Information about a SAML authenticator. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [SAMLAuthenticatorId](vdi.entity.SAMLAuthenticatorId.md)|  The ID of the SAML authenticator/   
  
**general**| [SAMLAuthenticatorGeneralData](vdi.infrastructure.SAMLAuthenticator.GeneralData.md)|  General data on the SAML Authenticator.   
  
**server**| [SAMLAuthenticatorServerData](vdi.infrastructure.SAMLAuthenticator.ServerData.md)|  Data on the SAML authenticator server   
  
**certificateOverride**| [CertificateThumbprint](vdi.utils.Certificate.CertificateThumbprint.md)|  The certificate override for the SAML authenticator.   


* This property need not be set.

  
  
  
  
  
  
