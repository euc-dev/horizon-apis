---
layout: page
title: Data Object - ConnectionServerSAMLData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.ConnectionServer.SAMLData  
Property of
     [ConnectionServerAuthenticationData](vdi.infrastructure.ConnectionServer.AuthenticationData.md#field_detail)  
See also
     [ConnectionServerWorkspaceOneData](vdi.infrastructure.ConnectionServer.WorkspaceOneData.md), [SAMLAuthenticatorId](vdi.entity.SAMLAuthenticatorId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

The SAML configuration settings for authentication to a connection server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**samlSupport**|  xsd:string|  SAML support option.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"ENABLED"| This property is deprecated. Please use MULTI_ENABLED instead of ENABLED. Indicates that the Saml support is enabled but optional.  
"REQUIRED"| This property is deprecated. Please use MULTI_REQUIRED instead of REQUIRED. Indicates that the Saml support is necessary.  
"DISABLED"| Indicates that the Saml support is disabled.  
"MULTI_ENABLED"| Indicates that the Saml multi auth support is enabled.  
"MULTI_REQUIRED"| Indicates that the Saml multi auth support is mandatory.  

  
**samlAuthenticator**| [SAMLAuthenticatorId](vdi.entity.SAMLAuthenticatorId.md)| **Deprecated.**_use[samlAuthenticators](vdi.infrastructure.ConnectionServer.SAMLData.md#samlAuthenticators) instead of this samlAuthenticator. _   


* This property need not be set.
  * This property is required if samlSupport is set to "ENABLED"or "REQUIRED".

  
**samlAuthenticators**| [SAMLAuthenticatorId[]](vdi.entity.SAMLAuthenticatorId.md)|  List of SamlAuthenticators to use.  **_Since_** Horizon 7.0  


* This property need not be set.
  * This property is an unordered array of unique values.
  * This property is required if samlSupport is set to "MULTI_ENABLED"or "MULTI_REQUIRED".

  
**workspaceOneData**| [ConnectionServerWorkspaceOneData](vdi.infrastructure.ConnectionServer.WorkspaceOneData.md)|  Workspace ONE data to use.  **_Since_** Horizon 7.2  


* This property need not be set.

  
  
  

  
  

