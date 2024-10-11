---
layout: page
title: Data Object - SAMLAuthenticatorCertificateSSOData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.SAMLAuthenticator.CertificateSSOData`

Property of  
> [SAMLAuthenticatorGeneralData](vdi.infrastructure.SAMLAuthenticator.GeneralData.md#field_detail)

Since  
> Horizon 7.0


## Data Object Description 

Certificate SSO data for a SAML authenticator. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**triggerMode**|  xsd:string|  How to trigger Certificate SSO on sessions using this authenticator.   


  * This property has a default value of "DISABLED".
  * This property will be one of:  
|  Value |  Description   
---|---  
"DISABLED"| Do not use Certificate SSO.  
"ENABLE_IF_NO_PASSWORD"| If no password is supplied, use a valid (domain matching) connector if it exists.  
"REQUIRE_IF_NO_PASSWORD"| If no password is supplied, use and require a valid (domain matching) connector.  
"ENABLE_ALWAYS"| Regardless of a password, use a valid (domain matching) connector if it exists.  
"REQUIRE_ALWAYS"| Regardless of a password, use and require a valid (domain matching) connector.  

  
**passwordMode**|  xsd:string|  If Certificate SSO is triggered and a password is present in the SAML assertion, how to handle it.   


* This property need not be set.
  * This property is required if triggerMode is set to "ENABLE_ALWAYS"or "REQUIRE_ALWAYS".
  * This property will be one of:  
|  Value |  Description   
---|---  
"REMOVE"| Remove any passwords.  
"PASSTHRU"| Pass through any passwords.  
"ERROR"| Error if there is a password.  

  
  
  

  
  
