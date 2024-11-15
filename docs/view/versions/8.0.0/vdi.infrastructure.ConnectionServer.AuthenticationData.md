---
layout: page
title: Data Object - ConnectionServerAuthenticationData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.ConnectionServer.AuthenticationData`

Property of
> [ConnectionServerInfo](vdi.infrastructure.ConnectionServer.ConnectionServerInfo.md#field_detail)

See also
> [ConnectionServerRADIUSData](vdi.infrastructure.ConnectionServer.RADIUSData.md), [ConnectionServerRSASecureIdData](vdi.infrastructure.ConnectionServer.RSASecureIdData.md), [ConnectionServerSAMLData](vdi.infrastructure.ConnectionServer.SAMLData.md), [UnauthenticatedAccessConfig](vdi.infrastructure.ConnectionServer.UnauthenticatedAccessConfig.md)

Since
> Horizon View 6.0


## Data Object Description

The set of all supported authentication settings for a connection server.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**smartCardSupport**|  xsd:string|  Smart Card support option.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"OPTIONAL"</td><td>Indicates that the SmartCard usage is optional.</td></tr><tr><td>"REQUIRED"</td><td>Indicates that the SmartCard usage is necessary.</td></tr><tr><td>"OFF"</td><td>Indicates that the SmartCard usage is not allowed.</td></tr></table>
**enableSmartCardUserNameHint**|  xsd:boolean|  Whether username hints for smart card is enabled.  **_Since_** Horizon 7.8 [^5] [^1]
**logoffWhenRemoveSmartCard**|  xsd:boolean|  Whether user is logged off on removal of Smart Card.
**smartCardSupportForAdmin**|  xsd:string|  Indicates Smart card authentication configuration for administrators to login  **_Since_** Horizon 7.8<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"OPTIONAL"</td><td>Indicates that the SmartCard usage is optional.</td></tr><tr><td>"REQUIRED"</td><td>Indicates that the SmartCard usage is necessary.</td></tr><tr><td>"OFF"</td><td>Indicates that the SmartCard usage is not allowed.</td></tr></table>
**rsaSecureIdConfig**| [ConnectionServerRSASecureIdData](vdi.infrastructure.ConnectionServer.RSASecureIdData.md)|  SecurId authentication settings.
**radiusConfig**| [ConnectionServerRADIUSData](vdi.infrastructure.ConnectionServer.RADIUSData.md)|  RADIUS authentication settings.
**samlConfig**| [ConnectionServerSAMLData](vdi.infrastructure.ConnectionServer.SAMLData.md)|  SAML authentication settings.
**unauthenticatedAccessConfig**| [UnauthenticatedAccessConfig](vdi.infrastructure.ConnectionServer.UnauthenticatedAccessConfig.md)|  Unauthenticated access settings.  **_Since_** Horizon 7.1


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.