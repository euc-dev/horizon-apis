---
layout: page
title: Data Object - DesktopMirageConfigurationOverrides
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.MirageConfigurationOverrides`

Property of
> [DesktopSettings](vdi.resources.Desktop.DesktopSettings.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Mirage configuration overrides.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**overrideGlobalSetting**|  xsd:boolean|  If set to true, then the Mirage configuration specified here will be used for this Desktop. Otherwise the Mirage configuration in [mirageConfiguration](vdi.infrastructure.GlobalSettings.GlobalSettingsInfo.md#mirageConfiguration) will be used. Notes :- [^51] [^5]
**enabled**|  xsd:boolean|  Whether a Mirage server is enabled. [^1] [^52]
**url**|  xsd:string|  The URL of the Mirage server. This should be in the form "<(DNS name)|(IPv4)|(IPv6)><:(port)>". IPv6 addresses must be enclosed in square brackets. [^1] [^53]


 
