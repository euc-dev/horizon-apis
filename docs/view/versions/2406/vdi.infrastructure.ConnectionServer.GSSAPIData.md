---
layout: page
title: Data Object - ConnectionServerGSSAPIData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.ConnectionServer.GSSAPIData
Property of
     [ConnectionServerAuthenticationData](vdi.infrastructure.ConnectionServer.AuthenticationData.md#field_detail)
See also
     [GSSAPIAuthenticatorId](vdi.entity.GSSAPIAuthenticatorId.md)
Since 
    Horizon 7.13

## Data Object Description 

The GSSAPI settings for authentication to a connection server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**gssAPIEnabled**|  xsd:boolean|  Flag to specify if GSSAPI authentication is enabled.   
  
**allowReceivingNTLM**|  xsd:boolean|  Indicate whether connection server supports NTLM or not.   


  * This property has a default value of false.
[^2]

  
**gssAPIAuthenticator**| [GSSAPIAuthenticatorId](vdi.entity.GSSAPIAuthenticatorId.md)|  The GSSAPI Authenticator to use.   


[^1]

  
  

  

