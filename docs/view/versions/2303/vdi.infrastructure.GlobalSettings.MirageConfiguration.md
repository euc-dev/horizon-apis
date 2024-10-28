---
layout: page
title: Data Object - GlobalSettingsMirageConfiguration
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.GlobalSettings.MirageConfiguration`

Property of
> [GlobalSettingsInfo](vdi.infrastructure.GlobalSettings.GlobalSettingsInfo.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Mirage configuration.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**enabled**|  xsd:boolean|  Whether a Mirage server is enabled.
**url**|  xsd:string|  The URL of the Mirage server. This should be in the form "<(DNS name)|(IPv4)|(IPv6)><:(port)>". IPv6 addresses must be enclosed in square brackets. [^1] [^53]
 


 


[^1]: This property need not be set.
[^53]: This property is required if enabled is set to true.