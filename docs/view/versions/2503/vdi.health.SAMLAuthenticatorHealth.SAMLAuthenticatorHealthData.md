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
**certificateSsoTriggerMode**|  xsd:string|  How to trigger Certificate SSO on sessions using this authenticator.  **_Since_** Horizon 8.7 [^17] [^2]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"DISABLED"</td><td>Do not use Certificate SSO.</td></tr><tr><td>"ENABLE_IF_NO_PASSWORD"</td><td>If no password is supplied, use a valid (domain matching) connector if it exists.</td></tr><tr><td>"REQUIRE_IF_NO_PASSWORD"</td><td>If no password is supplied, use and require a valid (domain matching) connector.</td></tr><tr><td>"ENABLE_ALWAYS"</td><td>Regardless of a password, use a valid (domain matching) connector if it exists.</td></tr><tr><td>"REQUIRE_ALWAYS"</td><td>Regardless of a password, use and require a valid (domain matching) connector.</td></tr></table>
**enforceEncryptedAssertion**|  xsd:boolean|  This indicates that particular Authenticator is for Workspace one or not. This property has a default value of false.
**workspaceOneEnabled**|  xsd:boolean|  This indicates that particular Authenticator is for Workspace one or not. [^1] [^2]
**forceSamlAuth**|  xsd:boolean|  This indicates that IDP will force the user to authenticate even if the user is already logged in. [^1] [^2]




 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^17]: This property has a default value of 'DISABLED'.