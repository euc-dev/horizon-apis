---
layout: page
title: Data Object - SAMLAuthenticatorHealthData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.SAMLAuthenticatorHealth.SAMLAuthenticatorHealthData`

Property of
> [SAMLAuthenticatorHealthInfo](vdi.health.SAMLAuthenticatorHealth.SAMLAuthenticatorHealthInfo.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Basic data about the SAML authenticator.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**label**|  xsd:string|  The label of the SAML Authenticator.
**metadataURL**|  xsd:string|  The metadata URL of the SAML Authenticator. [^1]
**administratorURL**|  xsd:string|  The administrator URL for the SAML authenticator. This must specify a protocol (scheme) of http or https.  **_Since_** Horizon 7.9 [^1] [^2]
**description**|  xsd:string|  The description of the SAML authenticator.  **_Since_** Horizon 7.10 [^1]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.