---
layout: page
title: Data Object - ConnectionServerSAMLData
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.infrastructure.ConnectionServer.SAMLData`

Property of
> [ConnectionServerAuthenticationData](vdi.infrastructure.ConnectionServer.AuthenticationData.md#field_detail)

See also
> [ConnectionServerWorkspaceOneData](vdi.infrastructure.ConnectionServer.WorkspaceOneData.md), [SAMLAuthenticatorId](vdi.entity.SAMLAuthenticatorId.md)

Since
> Horizon View 6.0


## Data Object Description

The SAML configuration settings for authentication to a connection server.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**samlSupport**|  xsd:string|  SAML support option.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"ENABLED"</td><td>This property is deprecated. Please use MULTI_ENABLED instead of ENABLED. Indicates that the Saml support is enabled but optional.</td></tr><tr><td>"REQUIRED"</td><td>This property is deprecated. Please use MULTI_REQUIRED instead of REQUIRED. Indicates that the Saml support is necessary.</td></tr><tr><td>"DISABLED"</td><td>Indicates that the Saml support is disabled.</td></tr><tr><td>"MULTI_ENABLED"</td><td>Indicates that the Saml multi auth support is enabled.</td></tr><tr><td>"MULTI_REQUIRED"</td><td>Indicates that the Saml multi auth support is mandatory.</td></tr></table>
**samlAuthenticator**| [SAMLAuthenticatorId](vdi.entity.SAMLAuthenticatorId.md)| **Deprecated.**_use[samlAuthenticators](vdi.infrastructure.ConnectionServer.SAMLData.md#samlAuthenticators) instead of this samlAuthenticator. _ [^1] [^251]
**samlAuthenticators**| [SAMLAuthenticatorId[]](vdi.entity.SAMLAuthenticatorId.md)|  List of SamlAuthenticators to use.  **_Since_** Horizon 7.0 [^1] [^14] [^252]
**workspaceOneData**| [ConnectionServerWorkspaceOneData](vdi.infrastructure.ConnectionServer.WorkspaceOneData.md)|  Workspace ONE data to use.  **_Since_** Horizon 7.2 [^1]


 


[^1]: This property need not be set.
[^14]: This property is an unordered array of unique values.
[^251]: This property is required if samlSupport is set to "ENABLED" or "REQUIRED".
[^252]: This property is required if samlSupport is set to "MULTI_ENABLED" or "MULTI_REQUIRED".