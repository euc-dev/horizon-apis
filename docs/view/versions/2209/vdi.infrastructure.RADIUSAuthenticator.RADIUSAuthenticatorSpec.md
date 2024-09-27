---
layout: page
title: Data Object - RADIUSAuthenticatorSpec
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.RADIUSAuthenticator.RADIUSAuthenticatorSpec  
Parameter to
     [RADIUSAuthenticator_Create](vdi.infrastructure.RADIUSAuthenticator.md#create)  
See also
     [RADIUSAuthenticatorGeneralData](vdi.infrastructure.RADIUSAuthenticator.GeneralData.md), [RADIUSAuthenticatorServerSpec](vdi.infrastructure.RADIUSAuthenticator.ServerData.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Specification for creating a RADIUS authenticator. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**general**| [RADIUSAuthenticatorGeneralData](vdi.infrastructure.RADIUSAuthenticator.GeneralData.md)|  General data on the RADIUS authenticator.   
  
**primaryServer**| [RADIUSAuthenticatorServerSpec](vdi.infrastructure.RADIUSAuthenticator.ServerData.md)|  Information about the primary server for this RADIUS authenticator.   
  
**secondaryServer**| [RADIUSAuthenticatorServerSpec](vdi.infrastructure.RADIUSAuthenticator.ServerData.md)|  Information about the (optional) secondary server for this RADIUS authenticator.   


* This property need not be set.

  
  
  
 
  
  

