---
layout: page
title: Data Object - SAMLAuthenticatorServerData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.SAMLAuthenticator.ServerData`

Property of  
> [SAMLAuthenticatorInfo](vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorInfo.md#field_detail), [SAMLAuthenticatorSpec](vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorSpec.md#field_detail)

Since  
> Horizon View 6.0


## Data Object Description 

Server data for a SAML server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**authenticatorType**|  xsd:string|  The type of saml authenticator.  **_Since_** Horizon 7.0  


  * This property has a default value of "DYNAMIC".
* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"STATIC"| Static SAML Authenticator, which contains SAML metadata  
"DYNAMIC"| Dynamic SAML Authenticator fetches metadata dynamically using a provided URL  

  
**metadataURL**|  xsd:string|  The metadata URL that this SAML authenticator uses to fetch metadata. This must specify a protocol (scheme) of https. It must be unique among all other SAML authenticators.   


* This property need not be set.
  * This property is required if authenticatorType is set to "DYNAMIC".

  
**administratorURL**|  xsd:string|  The administrator URL for this SAML authenticator. This must specify a protocol (scheme) of http or https.   


* This property need not be set.

  
**staticMetadata**|  xsd:string|  **_Since_** Horizon 7.0  


* This property need not be set.
  * This property is required if authenticatorType is set to "STATIC".

  
  
  
 
  
  
