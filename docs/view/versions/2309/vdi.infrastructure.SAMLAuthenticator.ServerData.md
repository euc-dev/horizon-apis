---
layout: page
title: Data Object - SAMLAuthenticatorServerData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.SAMLAuthenticator.ServerData`

Property of
> [SAMLAuthenticatorInfo](vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorInfo.md#field_detail), [SAMLAuthenticatorSpec](vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorSpec.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Server data for a SAML server.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**authenticatorType**|  xsd:string|  The type of saml authenticator.  **_Since_** Horizon 7.0 [^299] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"STATIC"</td><td>Static SAML Authenticator, which contains SAML metadata</td></tr><tr><td>"DYNAMIC"</td><td>Dynamic SAML Authenticator fetches metadata dynamically using a provided URL</td></tr></table>
**metadataURL**|  xsd:string|  The metadata URL that this SAML authenticator uses to fetch metadata. This must specify a protocol (scheme) of https. It must be unique among all other SAML authenticators. [^1] [^300]
**administratorURL**|  xsd:string|  The administrator URL for this SAML authenticator. This must specify a protocol (scheme) of http or https. [^1]
**staticMetadata**|  xsd:string|  **_Since_** Horizon 7.0 [^1] [^301]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^299]: This property has a default value of "DYNAMIC".
[^300]: This property is required if authenticatorType is set to "DYNAMIC".
[^301]: This property is required if authenticatorType is set to "STATIC".