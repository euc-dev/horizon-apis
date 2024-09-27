---
layout: page
title: Data Object - SAMLAuthenticatorGeneralData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.SAMLAuthenticator.GeneralData  
Property of
     [SAMLAuthenticatorInfo](vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorInfo.md#field_detail), [SAMLAuthenticatorSpec](vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorSpec.md#field_detail)  
See also
     [SAMLAuthenticatorCertificateSSOData](vdi.infrastructure.SAMLAuthenticator.CertificateSSOData.md)  
Since 
    Horizon View 6.0

## Data Object Description 

General data for a SAML authenticator. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**label**|  xsd:string|  The label for this SAML authenticator. It must be unique among all other SAML authenticators.   


  * This property has a maximum length of 32 characters. 

  
**description**|  xsd:string|  The description of this SAML authenticator.   


* This property need not be set.
  * This property has a maximum length of 1024 characters. 

  
**certificateSSOData**| [SAMLAuthenticatorCertificateSSOData](vdi.infrastructure.SAMLAuthenticator.CertificateSSOData.md)|  Certificate SSO data for this SAML authenticator.  **_Since_** Horizon 7.0  
  
  
  
   
  
  

