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

  
**refId**|  xsd:string|  Reference ID used for this SAML Authenticator.  **_Since_** Horizon 8.7  


* This property need not be set.
* This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
