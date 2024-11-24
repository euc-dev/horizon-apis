---
layout: page
title: Data Object - RADIUSAuthenticatorGeneralData
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.infrastructure.RADIUSAuthenticator.GeneralData`

Property of
> [RADIUSAuthenticatorInfo](vdi.infrastructure.RADIUSAuthenticator.RADIUSAuthenticatorInfo.md#field_detail), [RADIUSAuthenticatorSpec](vdi.infrastructure.RADIUSAuthenticator.RADIUSAuthenticatorSpec.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

General data about a RADIUS authenticator.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**label**|  xsd:string|  The label for this RADIUS authenticator. [^294]
**description**|  xsd:string|  The description of this RADIUS authenticator. [^1] [^13]
**userNameLabel**|  xsd:string|  The label for the RADIUS authenticator user name.  **_Since_** Horizon 7.11 [^1] [^295]
**passcodeLabel**|  xsd:string|  The label for the RADIUS authenticator passcode.  **_Since_** Horizon 7.11 [^1] [^295]


 


[^1]: This property need not be set.
[^13]: This property has a maximum length of 1024 characters.
[^294]: This property has a maximum length of 50 characters.
[^295]: This property has a maximum length of 20 characters.