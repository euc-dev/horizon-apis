---
layout: page
title: Data Object - GSSAPIAuthenticatorSpec
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.GSSAPIAuthenticator.GSSAPIAuthenticatorSpec`

Parameter to
> [GSSAPIAuthenticator_Create](vdi.infrastructure.GSSAPIAuthenticator.md#create)

See also
> [ConnectionServerId](vdi.entity.ConnectionServerId.md), [GSSAPIAuthenticatorGeneralData](vdi.infrastructure.GSSAPIAuthenticator.GeneralData.md)

Since
> Horizon 7.13


## Data Object Description

The specification for creating a GSSAPI authenticator.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**general**| [GSSAPIAuthenticatorGeneralData](vdi.infrastructure.GSSAPIAuthenticator.GeneralData.md)|  General data on the GSSAPI Authenticator.
**connectionServers**| [ConnectionServerId[]](vdi.entity.ConnectionServerId.md)|  The list of Connection Servers for which this GSSAPI authenticator is enabled. [^14]
 


 
