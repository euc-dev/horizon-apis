---
layout: page
title: Data Object - ApplicationData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Application.ApplicationData`

Property of
> [ApplicationInfo](vdi.resources.Application.ApplicationInfo.md#field_detail), [ApplicationSpec](vdi.resources.Application.ApplicationSpec.md#field_detail)

See also
> [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)

Since
> Horizon View 6.0


## Data Object Description

ApplicationData needed to create/update an Application.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**name**|  xsd:string|  The Application name is the unique identifier used to identify this Application. [^2] [^11]
**displayName**|  xsd:string|  The display name is the name that users will see when they connect to view client. If the display name is left blank, it defaults to [name](vdi.resources.Application.ApplicationData.md#name) [^1] [^12]
**description**|  xsd:string|  The description is a set of notes about the Application. [^1] [^13]
**enabled**|  xsd:boolean|  Indicates if Application is enabled [^6] [^1]
**globalApplicationEntitlement**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  Global Application Entitlement for this Application. This member will be null if not set or caller does not have global read permissions.  **_Since_** Horizon View 6.2 [^1]
**enableAntiAffinityRules**|  xsd:boolean|  Whether or not to enable rules for the launching of this application on RDSServers matching certain criteria. These criteria are based on a count of other applications running on that server whose process names match given patterns. If that count has been met, an RDSServer will reject a session for this Application. Additional RDSServers may be attempted based on their load preferences.  **_Since_** Horizon View 6.2 [^5]
**antiAffinityPatterns**|  xsd:string[]|  Set of pattern strings to match against process names on a RDSServer when attempting to launch a session for this Application. For each application running on an RDSServer that matches one of the patterns, the tally against the count threshold is incremented. <br>Pattern strings may contain wildcard characters. '*' matches zero or more characters. '?' matches exactly one character.  **_Since_** Horizon View 6.2 [^1] [^14] [^15]
**antiAffinityCount**|  xsd:int|  Maximum number of applications running on an RDSServer that match any of the patterns before that RDSServer will reject a session for this Application.  **_Since_** Horizon View 6.2 [^1] [^8] [^16] [^15]
**enablePreLaunch**|  xsd:boolean|  Application can be pre-launched if value is true.  **_Since_** Horizon 7.2 [^5] [^1]
**connectionServerRestrictions**|  xsd:string[]|  Connection server restrictions. This is a list of tags that access to the application is restricted to. Empty/Null list means that the application can be accessed from any connection server.  **_Since_** Horizon 7.2 [^1]
**categoryFolderName**|  xsd:string|  Name of the category folder in the user's OS containing a shortcut to the application. Unset if the application does not belong to a category.  **_Since_** Horizon 7.3 [^1] <br>* This property defines valid folder names with a max length of 64 characters and up to 4 subdirectory levels. The subdirectories can be specified using a backslash, e.g. (dir1\dir2\dir3\dir4). Folder names can't start or end with a backslash nor can there be 2 or more backslashes together. Combinations such as (\dir1, dir1\dir2\, dir1\\\dir2, dir1\\\\\dir2) are invalid. The windows reserved keywords (CON, PRN, NUL, AUX, COM1 - COM9, LPT1 - LPT9 etc.) are not allowed in subdirectory names.
**clientRestrictions**|  xsd:boolean|  Client restrictions to be applied to Application. Currently it is valid for RDSH pools.  **_Since_** Horizon 7.3 [^5] [^1]
**shortcutLocations**|  xsd:string[]|  Locations of the category folder in the user's OS containing a shortcut to the desktop. The value must be set if [categoryFolderName](vdi.resources.Application.ApplicationData.md#categoryFolderName) is provided.  **_Since_** Horizon 7.5 [^1]
**multiSessionMode**|  xsd:string|  Multi-session mode for the application. An application launched in multi-session mode does not support reconnect behavior when user logs in from a different client instance. [enablePreLaunch](vdi.resources.Application.ApplicationData.md#enablePreLaunch) can be set to true only if multiSessionMode is disabled.  **_Since_** Horizon 7.7 [^17] [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"DISABLED"</td><td>Multi-session is not supported for this application.</td></tr><tr><td>"ENABLED_DEFAULT_OFF"</td><td>Multi-session is supported for this application but is disabled by default. The client would need to explicitly request multi-session launch, if wanted.</td></tr><tr><td>"ENABLED_DEFAULT_ON"</td><td>Multi-session mode is supported for this application and is enabled by default. The client can request explicitly for single-session launch, if wanted.</td></tr><tr><td>"ENABLED_ENFORCED"</td><td>Multi-session is supported for this application and it is enforced. The client cannot select to launch this application as a single-session application.</td></tr></table>
**maxMultiSessions**|  xsd:int|  Maximum number of multi-sessions a user can have in this application pool.  **_Since_** Horizon 7.7 [^10] [^1] [^8] [^18]
**cloudBrokered**|  xsd:boolean|  Indicates whether the application pool is brokered by cloud broker.  **_Since_** Horizon 8.2 [^5] [^1]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^5]: This property has a default value of false.
[^6]: This property has a default value of true.
[^8]: This property has a minimum value of 1.
[^10]: This property has a default value of 1.
[^11]: This property must contain only alphanumerics, underscores, and dashes. The maximum length is 64 characters.
[^12]: This property has a maximum length of 256 characters.
[^13]: This property has a maximum length of 1024 characters.
[^14]: This property is an unordered array of unique values.
[^15]: This property is required if enableAntiAffinityRules is set to true.
[^16]: This property has a maximum value of 20.
[^17]: This property has a default value of 'DISABLED'.
[^18]: This property is required if multiSessionMode is set to 'ENABLED_DEFAULT_OFF', 'ENABLED_DEFAULT_ON', or 'ENABLED_ENFORCED'.