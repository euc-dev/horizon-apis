---
layout: page
title: Data Object - GlobalSettingsClientData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.GlobalSettings.ClientData`

Property of
> [GlobalSettingsClientRestrictionConfiguration](vdi.infrastructure.GlobalSettings.ClientRestrictionConfiguration.md#field_detail)

Since
> Horizon 7.11


## Data Object Description

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**type**|  xsd:string|  The type of the client.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"WINDOWS"</td><td>Client type is Windows client</td></tr><tr><td>"MAC"</td><td>Client type is Mac client</td></tr><tr><td>"HTMLACCESS"</td><td>Client type is web client</td></tr><tr><td>"LINUX"</td><td>Client type is Linux client</td></tr><tr><td>"IOS"</td><td>Client type is iOS client</td></tr><tr><td>"ANDROID"</td><td>Client type is Android client</td></tr><tr><td>"WINSTORE"</td><td>Client type is UWP client</td></tr><tr><td>"CHROME"</td><td>Client type is chrome client</td></tr></table>
**version**|  xsd:string|  Restrict access for all the Horizon clients that have version less than the [version](vdi.infrastructure.GlobalSettings.ClientData.md#version). This is applicable only for Horizon Clients 4.5.0 or later (or Horizon Client for Chrome 4.8.0 or later) [^264] [^265] [^1]
**warnSpecificVersions**|  xsd:string|  Warn users when connecting with the Horizon client having version that matches any of the comma separated specified versions. This is applicable only for Horizon Clients 8.0.0 or later [^264]
* This property cannot be used for [type](vdi.infrastructure.GlobalSettings.ClientData.md#type) "WINSTORE", "HTMLACCESS" and "CHROME".
**_Since_** Horizon 8.0 [^1] [^267]
**blockSpecificVersions**|  xsd:string|  Restrict users when connecting with the Horizon client having version that matches any of the comma separated specified versions. This is applicable only for Horizon Clients 4.5.0 or later (or Horizon Client for Chrome 4.8.0 or later) [^264] [^265]
* This property cannot be used for [type](vdi.infrastructure.GlobalSettings.ClientData.md#type) "WINSTORE", "HTMLACCESS" and "CHROME".
**_Since_** Horizon 8.0 [^1] [^267]


 


[^1]: This property need not be set.
[^264]: One of [version](vdi.infrastructure.GlobalSettings.ClientData.md#version), [blockSpecificVersions](vdi.infrastructure.GlobalSettings.ClientData.md#blockSpecificVersions), [warnSpecificVersions](vdi.infrastructure.GlobalSettings.ClientData.md#warnSpecificVersions) is mandatory.
[^265]: Only one of [version](vdi.infrastructure.GlobalSettings.ClientData.md#version) or [blockSpecificVersions](vdi.infrastructure.GlobalSettings.ClientData.md#blockSpecificVersions) can be set.
[^267]: This property has a maximum length of 128 characters.