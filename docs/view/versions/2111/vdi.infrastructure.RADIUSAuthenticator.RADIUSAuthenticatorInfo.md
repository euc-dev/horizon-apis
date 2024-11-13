---
layout: page
title: Data Object - RADIUSAuthenticatorInfo
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.infrastructure.RADIUSAuthenticator.RADIUSAuthenticatorInfo`

Returned by
> [RADIUSAuthenticator_Get](vdi.infrastructure.RADIUSAuthenticator.md#get), [RADIUSAuthenticator_List](vdi.infrastructure.RADIUSAuthenticator.md#list)

See also
> [RADIUSAuthenticatorGeneralData](vdi.infrastructure.RADIUSAuthenticator.GeneralData.md), [RADIUSAuthenticatorId](vdi.entity.RADIUSAuthenticatorId.md), [RADIUSAuthenticatorServerSpec](vdi.infrastructure.RADIUSAuthenticator.ServerData.md)

Since
> Horizon View 6.0


## Data Object Description

Information about a RADIUS authenticator.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [RADIUSAuthenticatorId](vdi.entity.RADIUSAuthenticatorId.md)|  The ID of the RADIUS authenticator/
**general**| [RADIUSAuthenticatorGeneralData](vdi.infrastructure.RADIUSAuthenticator.GeneralData.md)|  General data on the RADIUS authenticator.
**primaryServer**| [RADIUSAuthenticatorServerSpec](vdi.infrastructure.RADIUSAuthenticator.ServerData.md)|  Information about the primary server for this RADIUS authenticator.
**secondaryServer**| [RADIUSAuthenticatorServerSpec](vdi.infrastructure.RADIUSAuthenticator.ServerData.md)|  Information about the (optional) secondary server for this RADIUS authenticator. [^1]


 


[^1]: This property need not be set.