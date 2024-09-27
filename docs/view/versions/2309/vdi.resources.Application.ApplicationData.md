---
layout: page
title: Data Object - ApplicationData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Application.ApplicationData  
Property of
     [ApplicationInfo](vdi.resources.Application.ApplicationInfo.md#field_detail), [ApplicationSpec](vdi.resources.Application.ApplicationSpec.md#field_detail)  
See also
     [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

ApplicationData needed to create/update an Application. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  The Application name is the unique identifier used to identify this Application.   


 * This property cannot be updated.
  * This property must contain only alphanumerics, underscores, and dashes. The maximum length is 64 characters. 

  
**displayName**|  xsd:string|  The display name is the name that users will see when they connect to view client. If the display name is left blank, it defaults to [name](vdi.resources.Application.ApplicationData.md#name)   


 * This property need not be set.
  * This property has a maximum length of 256 characters. 

  
**description**|  xsd:string|  The description is a set of notes about the Application.   


 * This property need not be set.
  * This property has a maximum length of 1024 characters. 

  
**enabled**|  xsd:boolean|  Indicates if Application is enabled   


  * This property has a default value of true.
 * This property need not be set.

  
**globalApplicationEntitlement**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  Global Application Entitlement for this Application. This member will be null if not set or caller does not have global read permissions.  **_Since_** Horizon View 6.2  


 * This property need not be set.

  
**enableAntiAffinityRules**|  xsd:boolean|  Whether or not to enable rules for the launching of this application on RDSServers matching certain criteria. These criteria are based on a count of other applications running on that server whose process names match given patterns. If that count has been met, an RDSServer will reject a session for this Application. Additional RDSServers may be attempted based on their load preferences.  **_Since_** Horizon View 6.2  


  * This property has a default value of false.

  
**antiAffinityPatterns**|  xsd:string[]|  Set of pattern strings to match against process names on a RDSServer when attempting to launch a session for this Application. For each application running on an RDSServer that matches one of the patterns, the tally against the count threshold is incremented.  
  
Pattern strings may contain wildcard characters. '*' matches zero or more characters. '?' matches exactly one character.  **_Since_** Horizon View 6.2  


 * This property need not be set.
  * This property is an unordered array of unique values.
  * This property is required if enableAntiAffinityRules is set to true.

  
**antiAffinityCount**|  xsd:int|  Maximum number of applications running on an RDSServer that match any of the patterns before that RDSServer will reject a session for this Application.  **_Since_** Horizon View 6.2  


 * This property need not be set.
  * This property has a minimum value of 1. 
  * This property has a maximum value of 20. 
  * This property is required if enableAntiAffinityRules is set to true.

  
**enablePreLaunch**|  xsd:boolean|  Application can be pre-launched if value is true.  **_Since_** Horizon 7.2  


  * This property has a default value of false.
 * This property need not be set.

  
**connectionServerRestrictions**|  xsd:string[]|  Connection server restrictions. This is a list of tags that access to the application is restricted to. Empty/Null list means that the application can be accessed from any connection server.  **_Since_** Horizon 7.2  


 * This property need not be set.

  
**categoryFolderName**|  xsd:string|  Name of the category folder in the user's OS containing a shortcut to the application. Unset if the application does not belong to a category.  **_Since_** Horizon 7.3  


 * This property need not be set.
  * This property defines valid folder names with a max length of 64 characters and up to 4 subdirectory levels. The subdirectories can be specified using a backslash, e.g. (dir1\dir2\dir3\dir4). Folder names can't start or end with a backslash nor can there be 2 or more backslashes together. Combinations such as (\dir1, dir1\dir2\, dir1\\\dir2, dir1\\\\\dir2) are invalid. The windows reserved keywords (CON, PRN, NUL, AUX, COM1 - COM9, LPT1 - LPT9 etc.) are not allowed in subdirectory names. 

  
**clientRestrictions**|  xsd:boolean|  Client restrictions to be applied to Application. Currently it is valid for RDSH pools.  **_Since_** Horizon 7.3  


  * This property has a default value of false.
 * This property need not be set.

  
**shortcutLocations**|  xsd:string[]|  Locations of the category folder in the user's OS containing a shortcut to the desktop. The value must be set if [categoryFolderName](vdi.resources.Application.ApplicationData.md#categoryFolderName) is provided.  **_Since_** Horizon 7.5  


 * This property need not be set.

  
**multiSessionMode**|  xsd:string|  Multi-session mode for the application. An application launched in multi-session mode does not support reconnect behavior when user logs in from a different client instance. [enablePreLaunch](vdi.resources.Application.ApplicationData.md#enablePreLaunch) can be set to true only if multiSessionMode is disabled.  **_Since_** Horizon 7.7  


  * This property has a default value of "DISABLED".
 * This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"DISABLED"| Multi-session is not supported for this application.  
"ENABLED_DEFAULT_OFF"| Multi-session is supported for this application but is disabled by default. The client would need to explicitly request multi-session launch, if wanted. If a legacy client is used, this will always result in a single-session application launch.  
"ENABLED_DEFAULT_ON"| Multi-session mode is supported for this application and is enabled by default. The client can request explicitly for single-session launch, if wanted. If a legacy client is used, this will always result in a multi-session application launch.  
"ENABLED_ENFORCED"| Multi-session is supported for this application and it is enforced. The client can not select to launch this application as a single-session application.  

  
**maxMultiSessions**|  xsd:int|  Maximum number of multi-sessions a user can have in this application pool.  **_Since_** Horizon 7.7  


  * This property has a default value of 1.
 * This property need not be set.
  * This property has a minimum value of 1. 
  * This property is required if multiSessionMode is set to "ENABLED_DEFAULT_OFF", "ENABLED_DEFAULT_ON", or "ENABLED_ENFORCED".

  
**cloudBrokered**|  xsd:boolean|  Indicates whether the application pool is brokered by cloud broker.  **_Since_** Horizon 8.2  


  * This property has a default value of false.
 * This property need not be set.

  
**avApplicationPackageGuid**|  xsd:string|  Application package guid for the AV application. This will be set only for application pool published from app volumes manager.  **_Since_** Horizon 8.8  


 * This property cannot be updated.

  
**appLaunchLimitEnabled**|  xsd:boolean|  Indicates whether launch limit is enabled for the application pool. Only one instance of the application can be launched if it is enabled.  **_Since_** Horizon 8.11  


  * This property has a default value of false.
 * This property need not be set.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

