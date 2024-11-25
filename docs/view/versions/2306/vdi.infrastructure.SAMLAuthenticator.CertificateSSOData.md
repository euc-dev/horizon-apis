---
layout: page
title: Data Object - SAMLAuthenticatorCertificateSSOData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.SAMLAuthenticator.CertificateSSOData`

Property of
> [SAMLAuthenticatorGeneralData](vdi.infrastructure.SAMLAuthenticator.GeneralData.md#field_detail)

Since
> Horizon 7.0


## Data Object Description

Certificate SSO data for a SAML authenticator.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**triggerMode**|  xsd:string|  How to trigger Certificate SSO on sessions using this authenticator. [^17]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"DISABLED"</td><td>Do not use Certificate SSO.</td></tr><tr><td>"ENABLE_IF_NO_PASSWORD"</td><td>If no password is supplied, use a valid (domain matching) connector if it exists.</td></tr><tr><td>"REQUIRE_IF_NO_PASSWORD"</td><td>If no password is supplied, use and require a valid (domain matching) connector.</td></tr><tr><td>"ENABLE_ALWAYS"</td><td>Regardless of a password, use a valid (domain matching) connector if it exists.</td></tr><tr><td>"REQUIRE_ALWAYS"</td><td>Regardless of a password, use and require a valid (domain matching) connector.</td></tr></table>
**passwordMode**|  xsd:string|  If Certificate SSO is triggered and a password is present in the SAML assertion, how to handle it. [^1] [^308]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"REMOVE"</td><td>Remove any passwords.</td></tr><tr><td>"PASSTHRU"</td><td>Pass through any passwords.</td></tr><tr><td>"ERROR"</td><td>Error if there is a password.</td></tr></table>
 


 


[^1]: This property need not be set.
[^17]: This property has a default value of 'DISABLED'.
[^308]: This property is required if triggerMode is set to "ENABLE_ALWAYS" or "REQUIRE_ALWAYS".