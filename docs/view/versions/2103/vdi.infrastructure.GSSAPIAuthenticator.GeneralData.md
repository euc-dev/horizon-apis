---
layout: page
title: Data Object - GSSAPIAuthenticatorGeneralData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.GSSAPIAuthenticator.GeneralData  
Property of
     [GSSAPIAuthenticatorInfo](vdi.infrastructure.GSSAPIAuthenticator.GSSAPIAuthenticatorInfo.md#field_detail), [GSSAPIAuthenticatorSpec](vdi.infrastructure.GSSAPIAuthenticator.GSSAPIAuthenticatorSpec.md#field_detail)  

## Data Object Description 

General data for a GSSAPI authenticator. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**enableLoginAsCurrentUser**|  xsd:boolean|  Indicate whether login as current user is enabled.   


  * This property has a default value of false.

  
**allowLegacyClients**|  xsd:boolean|  Indicate whether the legacy Horizon clients will be allowed to use login as current user.   


  * This property has a default value of true.

  
**allowNTLMFallback**|  xsd:boolean|  Indicate whether NTLM is allowed for GSS API authentication. If kerberos authentication fails when the client does not have access to the domain controllers in the hosted environment, clients can fall back to NTLM authentication if allowNTLMFallback is set to true.   


  * This property has a default value of false.

  
**enforceChannelBindings**|  xsd:boolean|  Indicate whether channel bindings is supported or not.   


  * This property has a default value of true.

  
**triggerMode**|  xsd:string|  Indicates True SSO trigger mode on sessions using this authenticator.   


  * This property has a default value of "DISABLED".
  * This property will be one of:  
|  Value |  Description   
---|---  
"DISABLED"| Do not use True SSO.  
"OPTIONAL"| If no SSO credentials are provided then use True SSO, otherwise use the supplied SSO credentials.  
"ENABLED"| Always use True SSO even if client supplied SSO credentials.  

  
  
  

  
  

