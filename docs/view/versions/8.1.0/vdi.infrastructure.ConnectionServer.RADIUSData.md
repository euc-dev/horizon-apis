---
layout: page
title: Data Object - ConnectionServerRADIUSData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.ConnectionServer.RADIUSData
Property of
     [ConnectionServerAuthenticationData](vdi.infrastructure.ConnectionServer.AuthenticationData.md#field_detail)
See also
     [RADIUSAuthenticatorId](vdi.entity.RADIUSAuthenticatorId.md)
Since 
    Horizon View 6.0

## Data Object Description 

The RADIUS settings for authentication to a connection server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**radiusEnabled**|  xsd:boolean|  Flag to specify if RADIUS authentication is enabled.   
  
**radiusAuthenticator**| [RADIUSAuthenticatorId](vdi.entity.RADIUSAuthenticatorId.md)|  The RADIUS Authenticator to use.   


[^1]
  * This property is required if radiusEnabled is set to true.

  
**radiusNameMapping**|  xsd:boolean|  Flag to specify if RADIUS name mapping is enabled.   


[^1]

  
**radiusSSO**|  xsd:boolean|  Flag to specify if RADIUS Windows Single Sign-On is enabled.   


[^1]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

