---
layout: page
title: Data Object - SAMLAuthenticatorHealthData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.health.SAMLAuthenticatorHealth.SAMLAuthenticatorHealthData
Property of
     [SAMLAuthenticatorHealthInfo](vdi.health.SAMLAuthenticatorHealth.SAMLAuthenticatorHealthInfo.md#field_detail)
Since 
    Horizon View 6.0

## Data Object Description 

Basic data about the SAML authenticator. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**label**|  xsd:string|  The label of the SAML Authenticator.   
  
**metadataURL**|  xsd:string|  The metadata URL of the SAML Authenticator.   


[^1]

  
**administratorURL**|  xsd:string|  The administrator URL for the SAML authenticator. This must specify a protocol (scheme) of http or https.  **_Since_** Horizon 7.9  


[^1]
[^2]

  
**description**|  xsd:string|  The description of the SAML authenticator.  **_Since_** Horizon 7.10  


[^1]

  
**certificateSsoTriggerMode**|  xsd:string|  How to trigger Certificate SSO on sessions using this authenticator.  **_Since_** Horizon 8.7  


  * This property has a default value of "DISABLED".
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"DISABLED"| Do not use Certificate SSO.  
"ENABLE_IF_NO_PASSWORD"| If no password is supplied, use a valid (domain matching) connector if it exists.  
"REQUIRE_IF_NO_PASSWORD"| If no password is supplied, use and require a valid (domain matching) connector.  
"ENABLE_ALWAYS"| Regardless of a password, use a valid (domain matching) connector if it exists.  
"REQUIRE_ALWAYS"| Regardless of a password, use and require a valid (domain matching) connector.  

  
  

  

