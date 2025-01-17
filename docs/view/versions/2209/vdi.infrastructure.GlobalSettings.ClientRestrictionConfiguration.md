---
layout: page
title: Data Object - GlobalSettingsClientRestrictionConfiguration
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.GlobalSettings.ClientRestrictionConfiguration`

Property of
> [GlobalSettingsInfo](vdi.infrastructure.GlobalSettings.GlobalSettingsInfo.md#field_detail)

See also
> [GlobalSettingsClientData](vdi.infrastructure.GlobalSettings.ClientData.md)

Since
> Horizon 7.11


## Data Object Description

Client Restriction configuration indicates which client type and below what version of the client needs to be blocked for brokering to desktops or applications. Additional client types other than the supported client types can also be restricted for brokering to desktops or applications.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**clientData**| [GlobalSettingsClientData[]](vdi.infrastructure.GlobalSettings.ClientData.md)|  Client type and the version information needed to restrict or show warning message to the users using deprecated client versions. [^1]
**message**|  xsd:string|  The message to be shown for the blocked clients. [^1] [^268]
**blockAdditionalClients**|  xsd:boolean|  Whether additional clients need to be blocked. [^5] [^1]
**warningMessage**|  xsd:string|  The warning message to be shown to the users when the Horizon client version being used matches any of the restricted versions for the given client type  **_Since_** Horizon 8.0 [^1] [^268]


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.
[^268]: This property accepts all characters including new line with a maximum length of 1024 characters.