---
layout: page
title: Data Object - GSSAPIAuthenticatorInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.GSSAPIAuthenticator.GSSAPIAuthenticatorInfo`

Returned by
> [GSSAPIAuthenticator_Get](vdi.infrastructure.GSSAPIAuthenticator.md#get), [GSSAPIAuthenticator_List](vdi.infrastructure.GSSAPIAuthenticator.md#list)

See also
> [ConnectionServerId](vdi.entity.ConnectionServerId.md), [GSSAPIAuthenticatorGeneralData](vdi.infrastructure.GSSAPIAuthenticator.GeneralData.md), [GSSAPIAuthenticatorId](vdi.entity.GSSAPIAuthenticatorId.md)

Since
> Horizon 7.13


## Data Object Description

Information about a GSSAPI authenticator.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [GSSAPIAuthenticatorId](vdi.entity.GSSAPIAuthenticatorId.md)|  The ID of the GSSAPI authenticator/
**general**| [GSSAPIAuthenticatorGeneralData](vdi.infrastructure.GSSAPIAuthenticator.GeneralData.md)|  General data on the GSSAPI Authenticator.
**connectionServers**| [ConnectionServerId[]](vdi.entity.ConnectionServerId.md)|  The list of Connection Servers for which this GSSAPI authenticator is enabled. [^14]
**refId**|  xsd:string|  Reference ID used for this GSSAPI Authenticator.  **_Since_** Horizon 8.7 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^14]: This property is an unordered array of unique values.