---
layout: page
title: Data Object - DesktopSettings
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.DesktopSettings`

Property of
> [DesktopInfo](vdi.resources.Desktop.DesktopInfo.md#field_detail), [DesktopSpec](vdi.resources.Desktop.DesktopSpec.md#field_detail)

See also
> [DesktopAdobeFlashSettings](vdi.resources.Desktop.AdobeFlashSettings.md), [DesktopDisplayProtocolSettings](vdi.resources.Desktop.DisplayProtocolSettings.md), [DesktopLogoffSettings](vdi.resources.Desktop.LogoffSettings.md), [DesktopMirageConfigurationOverrides](vdi.resources.Desktop.MirageConfigurationOverrides.md)

Since
> Horizon View 6.0


## Data Object Description

Settings related to desktop configuration.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**enabled**|  xsd:boolean|  True if the desktop is enabled. [^6]
**deleting**|  xsd:boolean|  True if the desktop is in the process of being deleted. This cannot be set or updated. [^5] [^2]
**connectionServerRestrictions**|  xsd:string[]|  Connection server restrictions. This is a list of tags that access to the desktop is restricted to. No list means that the desktop can be accessed from any connection server. [^1]
**logoffSettings**| [DesktopLogoffSettings](vdi.resources.Desktop.LogoffSettings.md)|  Remote machine settings applicable when a user logs off or when a desktop is no longer keeping a machine as a spare. For RDS Desktops, this will be unset when retrieved, must be unset when created, and cannot be updated. The RDS Desktop's Farm's [FarmSessionSettings](vdi.resources.Farm.SessionSettings.md) will be used instead. Otherwise, this must be set. [^1]
**displayProtocolSettings**| [DesktopDisplayProtocolSettings](vdi.resources.Desktop.DisplayProtocolSettings.md)|  Remote display protocol settings. These relate to RDP/PCoIP/BLAST. For RDS Desktops, this will be unset when retrieved, must be unset when created, and cannot be updated. The RDS Desktop's Farm's [FarmDisplayProtocolSettings](vdi.resources.Farm.DisplayProtocolSettings.md) will be used instead. Otherwise, this must be set. [^1]
**flashSettings**| [DesktopAdobeFlashSettings](vdi.resources.Desktop.AdobeFlashSettings.md)| **Deprecated.**_This property is no longer in use for Horizon Components and will be ignored during[Desktop_Create](vdi.resources.Desktop.md#create) and [Desktop_Update](vdi.resources.Desktop.md#update) operations _ Adobe flash settings for remote sessions. [^1]
**mirageConfigurationOverrides**| [DesktopMirageConfigurationOverrides](vdi.resources.Desktop.MirageConfigurationOverrides.md)|  Override of the mirage configuration for this Desktop. For RDS Desktops, this will be unset when retrieved, must be unset when created, and cannot be updated. The RDS Desktop's Farm's [FarmMirageConfigurationOverrides](vdi.resources.Farm.MirageConfigurationOverrides.md) will be used instead. Otherwise, this must be set. [^1]
**categoryFolderName**|  xsd:string|  Name of the category folder in the user's OS containing a shortcut to the desktop. Unset if the desktop does not belong to a category.  **_Since_** Horizon 7.3 [^1]
* This property defines valid folder names with a max length of 64 characters and up to 4 subdirectory levels. The subdirectories can be specified using a backslash, e.g. (dir1\dir2\dir3\dir4). Folder names can't start or end with a backslash nor can there be 2 or more backslashes together. Combinations such as (\dir1, dir1\dir2\, dir1\\\dir2, dir1\\\\\dir2) are invalid. The windows reserved keywords (CON, PRN, NUL, AUX, COM1 - COM9, LPT1 - LPT9 etc.) are not allowed in subdirectory names.
**clientRestrictions**|  xsd:boolean|  Client restrictions to be applied to Desktop.  **_Since_** Horizon 7.3 [^5] [^1]
**shortcutLocations**|  xsd:string[]|  Locations of the category folder in the user's OS containing a shortcut to the desktop. The value must be set if [categoryFolderName](vdi.resources.Desktop.DesktopSettings.md#categoryFolderName) is provided.  **_Since_** Horizon 7.5 [^1]
**allowMultipleSessionsPerUser**|  xsd:boolean|  Whether multiple sessions are allowed per user for this pool. This is valid for RDS Desktops. For other Desktops use [allowMultipleSessionsPerUser](vdi.resources.Desktop.LogoffSettings.md#allowMultipleSessionsPerUser) **_Since_** Horizon 7.7 [^5] [^1]
**supportedSessionType**|  xsd:string|  Supported session types for this desktop. If application sessions are selected to be supported then this desktop can be used for application pool creation. This will be useful when the machines in the pool support application remoting.  **_Since_** Horizon 7.9 [^28] [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>DESKTOP</td><td>Only desktop sessions are supported for this desktop.</td></tr><tr><td>APPLICATION</td><td>Only application sessions are supported for this desktop.</td></tr><tr><td>DESKTOP_AND_APPLICATION</td><td>Both desktop and application sessions are supported for this desktop.</td></tr></table>
**cloudManaged**|  xsd:boolean|  Indicates whether this desktop is managed by Horizon Cloud Services. This can be set to false only when [cloudAssigned](vdi.resources.Desktop.DesktopSettings.md#cloudAssigned) is false. This cannot be set to true, if any of the conditions are satisfied: [^210] [^211] [^212] [^213] [^214] [^215] [^216] [^217]
**_Since_** Horizon 7.11 [^5] [^1]
**cloudAssigned**|  xsd:boolean|  Indicates whether this desktop is assigned to a workspace in Horizon Cloud Services. This can be set to true from cloud session only and only when [cloudManaged](vdi.resources.Desktop.DesktopSettings.md#cloudManaged) is true. This can be changed to false only if there are no entitlements.  **_Since_** Horizon 7.11 [^5] [^1]
**displayAssignedMachineName**|  xsd:boolean|  Indicates whether users should see the hostname of the machine assigned to them instead of [displayName](vdi.resources.Desktop.DesktopBase.md#displayName) when they connect using View Client. This is applicable for dedicated pools only. If no machine is assigned to the user then "displayName (No machine assigned)" will be displayed in the client.  **_Since_** Horizon 7.12 [^5] [^1]


 
