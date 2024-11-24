---
layout: page
title: Data Object - LogoffSettings
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.ResourceSettings.LogoffSettings`

Property of
> [ResourceSettingsInfo](vdi.utils.ResourceSettings.ResourceSettingsInfo.md#field_detail)

Since
> Horizon 7.6


## Data Object Description

The Logoff Settings information.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**forcedLogoffTimeoutMinutes**|  xsd:int|  The number of minutes to wait after the warning is displayed and before logging off the user. [^164] [^2]
**forcedLogoffMessage**|  xsd:string|  The warning to be displayed before logging off the user. [^1] [^2]
**displayWarningBeforeForcedLogoff**|  xsd:boolean|  Displays a warning message when users are forced to log off because a scheduled or immediate update such as a machine-refresh operation is about to start.  **_Since_** Horizon 7.7 [^1]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^164]: This property has a default value of 5.