---
layout: page
title: Data Object - GlobalEntitlementBase
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.federation.GlobalEntitlement.GlobalEntitlementBase`

Property of  
> [GlobalEntitlementInfo](vdi.federation.GlobalEntitlement.GlobalEntitlementInfo.md#field_detail), [GlobalEntitlementSummaryView](vdi.federation.GlobalEntitlement.GlobalEntitlementSummaryView.md#field_detail)

Parameter to  
> [GlobalEntitlement_Create](vdi.federation.GlobalEntitlement.md#create)

See also  
> [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)

Since  
> Horizon View 6.0


## Data Object Description 

Parameters to create a Global Entitlement. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**displayName**|  xsd:string|  The display name is the unique name used to identify the Global Entitlement.   


  * This property has a maximum length of 64 characters. 

  
**aliasName**|  xsd:string|  The alias name is the name that users will see when they connect using Horizon View Client. If the alias name is left blank, while creating or updating the Global Entitlement alias name value will be same as display name.  **_Since_** Horizon 8.0  


* This property need not be set.
  * This property has a maximum length of 64 characters. 

  
**description**|  xsd:string|  Description of Global Entitlement.   


* This property need not be set.
  * This property has a maximum length of 1024 characters. 

  
**scope**|  xsd:string|  Scope for this global entitlement. Visibility and Placement policies are defined by this value.   


  * This property has a default value of "ANY".
* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"LOCAL"| Local Policy: Local pod will be used for this policy.  
If this policy is for visibility, search for existing session will happen only in local pod.  
If this policy is for placement, session will always be placed on local pod.  
  
"SITE"| Site Policy: Site will be used for this policy.  
If this policy is for visibility, search for existing session will happen only from site.  
If this policy is for placement, session will be placed on site.  
  
"ANY"| Any Policy: Any pod can be used for this action.  
If this policy is for visibility, search for existing session will span all pods in LMV set.  
If this policy is for placement, session can be placed on any pod in LMV set.  
  

  
**dedicated**|  xsd:boolean|  If this is a dedicated entitlement. If so, only dedicated desktops can be associated with this Global Entitlement. Otherwise, only floating desktops, can be associated with it. Can only be set at time of creation.   


* This property cannot be updated.

  
**fromHome**|  xsd:boolean|  This value defines the starting location for resource placement and search. When true, a pod in the user's home site is used to start the search. When false, the current site is used.   
  
**requireHomeSite**|  xsd:boolean|  This value determines whether we fail if a home site isn't defined for this Global Entitlement.   
  
**multipleSessionAutoClean**|  xsd:boolean|  This value is used to determine if automatic session clean up is enabled. This cannot be enabled when this Global Entitlement is associated with a Desktop that has dedicated user assignment.   
  
**enabled**|  xsd:boolean|  If this Global Entitlement is enabled.   
  
**supportedDisplayProtocols**|  xsd:string[]|  The set of supported display protocols for the Global Entitlement. All the desktops associated with this Global Entitlement must support these protocols [supportedDisplayProtocols](vdi.resources.Desktop.DisplayProtocolSettings.md#supportedDisplayProtocols) . Clients connecting through this Global Entitlement that are allowed to select their protocol will see these display protocol options.   


  * This property has a default value of ["PCOIP", "RDP", "BLAST"].
* This property need not be set.
  * This property is an unordered array of unique values.
* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"RDP"| Microsoft Remote Desktop Protocol.  
"PCOIP"| PC over IP.  
"BLAST"| BLAST.  

  
**defaultDisplayProtocol**|  xsd:string|  The default display protocol for the Global Entitlement. Must be a protocol in the supportedDisplayProtocols list. Clients connecting through this Global Entitlement that do not specify a protocol will use this value, not the value specified directly on the desktop to which they connect (if different).   


  * This property has a default value of "PCOIP".
* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"RDP"| Microsoft Remote Desktop Protocol.  
"PCOIP"| PC over IP.  
"BLAST"| BLAST.  

  
**allowUsersToChooseProtocol**|  xsd:boolean|  Whether the users can choose the protocol used. If set to true, the desktops that are associated with this GlobalEntitlement must also allow users to choose display protocol with [allowUsersToChooseProtocol](vdi.resources.Desktop.DisplayProtocolSettings.md#allowUsersToChooseProtocol).   


  * This property has a default value of true.
* This property need not be set.
* This property cannot be updated.

  
**allowUsersToResetMachines**|  xsd:boolean|  Whether users are allowed to reset/restart their machines. If set to true, the desktops that are associated with this GlobalEntitlement must also allow users to reset/restart machines with [allowUsersToResetMachines](vdi.resources.Desktop.LogoffSettings.md#allowUsersToResetMachines).   


  * This property has a default value of false.
* This property need not be set.
* This property cannot be updated.

  
**enableHTMLAccess**|  xsd:boolean| **Deprecated.**_This property is no longer in use for Horizon Components. It is always set to true._ HTML Access, enabled by VMware Blast technology, allows users to connect to View machines from Web browsers. View Client software does not have to be installed on the client devices. To enable HTML Access, you must install the HTML Machine Access feature pack. If set to true, the desktops that are associated with this GlobalEntitlement must also have HTML Access enabled with [enableHTMLAccess](vdi.resources.Desktop.DisplayProtocolSettings.md#enableHTMLAccess). Also, Blast must be configured as a supported protocol in [supportedDisplayProtocols](vdi.federation.GlobalEntitlement.GlobalEntitlementBase.md#supportedDisplayProtocols).  
**_Since_** Horizon View 6.2  


  * This property has a default value of true.
* This property need not be set.

  
**allowMultipleSessionsPerUser**|  xsd:boolean|  Whether users can have multiple sessions when accessed from different client devices, this is also called Class room mode and applicable only to floating user assignment. If value is set to true, the desktops that are associated with this GlobalEntitlement must also allow users to have multiple sessions with [allowMultipleSessionsPerUser](vdi.resources.Desktop.LogoffSettings.md#allowMultipleSessionsPerUser) **_Since_** Horizon 7.1  


  * This property has a default value of false.
* This property need not be set.

  
**connectionServerRestrictions**|  xsd:string[]|  Connection server restrictions. This is a list of tags that access to the entitlement is restricted to. No list means that the entitlement can be accessed from any connection server.  **_Since_** Horizon 7.1  


* This property need not be set.

  
**categoryFolderName**|  xsd:string|  Name of the category folder in the user's OS containing a shortcut to the entitlement. Unset if the entitlement does not belong to a category.  **_Since_** Horizon 7.3  


* This property need not be set.
  * This property defines valid folder names with a max length of 64 characters and up to 4 subdirectory levels. The subdirectories can be specified using a backslash, e.g. (dir1\dir2\dir3\dir4). Folder names can't start or end with a backslash nor can there be 2 or more backslashes together. Combinations such as (\dir1, dir1\dir2\, dir1\\\dir2, dir1\\\\\dir2) are invalid. The windows reserved keywords (CON, PRN, NUL, AUX, COM1 - COM9, LPT1 - LPT9 etc.) are not allowed in subdirectory names. 

  
**clientRestrictions**|  xsd:boolean|  Client restrictions to be applied to Global Entitlement. Currently it is valid for RDSH pools.  **_Since_** Horizon 7.3  


  * This property has a default value of false.
* This property need not be set.

  
**enableCollaboration**|  xsd:boolean|  Enable session collaboration feature. Session collaboration allows a user to share their remote session with other users. Blast must be configured as a supported protocol in [supportedDisplayProtocols](vdi.federation.GlobalEntitlement.GlobalEntitlementBase.md#supportedDisplayProtocols). If set to true, the desktops that are associated with this GlobalEntitlement must also have session collaboration enabled with [enableCollaboration](vdi.resources.Desktop.DisplayProtocolSettings.md#enableCollaboration).  **_Since_** Horizon 7.4  


  * This property has a default value of false.
* This property need not be set.

  
**shortcutLocations**|  xsd:string[]|  Locations of the category folder in the user's OS containing a shortcut to the desktop. The value must be set if [categoryFolderName](vdi.federation.GlobalEntitlement.GlobalEntitlementBase.md#categoryFolderName) is provided.  **_Since_** Horizon 7.5  


* This property need not be set.

  
**cloudManaged**|  xsd:boolean|  Indicates whether this global entitlement is managed from cloud.  **_Since_** Horizon 7.9  


* This property need not be set.

  
**backupGE**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  Indicates the Global Entitlement that can be used as backup for this Global Entitlement.  **_Since_** Horizon 7.11  


* This property need not be set.

  
**displayAssignedMachineName**|  xsd:boolean|  Indicates whether users should see the hostname of the machine assigned to them instead of [displayName](vdi.federation.GlobalEntitlement.GlobalEntitlementBase.md#displayName) when they connect using View Client. This is applicable for dedicated Global Entitlements only. If no machine is assigned to the user then "displayName (No machine assigned)" will be displayed in the client.  **_Since_** Horizon 7.12  


  * This property has a default value of false.
* This property need not be set.

  
  
  

  
  
