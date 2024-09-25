---
layout: page
title: Data Object - RADIUSAuthenticatorServerSpec
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.RADIUSAuthenticator.ServerData
Property of
     [RADIUSAuthenticatorInfo](vdi.infrastructure.RADIUSAuthenticator.RADIUSAuthenticatorInfo.md#field_detail), [RADIUSAuthenticatorSpec](vdi.infrastructure.RADIUSAuthenticator.RADIUSAuthenticatorSpec.md#field_detail)
See also
     [SecureString](vdi.util.SecureString.md)
Since 
    Horizon View 6.0

## Data Object Description 

Information about a RADIUS authentication server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**hostname**|  xsd:string|  The hostname of the RADIUS authentication server.   
  
**authenticationPort**|  xsd:int|  The authentication port of the RADIUS authentication server.   


  * This property has a minimum value of 1. 
  * This property has a maximum value of 65535. 

  
**accountingPort**|  xsd:int|  The accounting port of the RADIUS authentication server.   


  * This property has a minimum value of 0. 
  * This property has a maximum value of 65535. 

  
**authenticationType**|  xsd:string|  The authentication type of the RADIUS authentication server.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"PAP"| Password authentication protocol  
"CHAP"| Challenge-handshake authentication protocol  
"MSCHAP1"| Microsoft challenge-handshake authentication protocol, version 1  
"MSCHAP2"| Microsoft challenge-handshake authentication protocol, version 2  

  
**sharedSecret**| [SecureString](vdi.util.SecureString.md)|  The shared secret of the RADIUS authentication server.   
  
**serverTimeoutSeconds**|  xsd:int|  The server timeout (in seconds) of the RADIUS authentication server.   


  * This property has a minimum value of 1. 

  
**maxAttempts**|  xsd:int|  The maximum number of authentication attempts for the RADIUS authentication server.   


  * This property has a minimum value of 1. 

  
**realmPrefix**|  xsd:string|  The realm prefix of the RADIUS authentication server.   


[^1]

  
**realmSuffix**|  xsd:string|  The realm suffix of the RADIUS authentication server.   


[^1]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

