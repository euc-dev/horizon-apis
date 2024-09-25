---
layout: page
title: Data Object - DesktopSummaryData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.DesktopSummaryData
Property of
     [DesktopSummaryView](vdi.resources.Desktop.DesktopSummaryView.md#field_detail)
See also
     [AccessGroupId](vdi.entity.AccessGroupId.md), [FarmId](vdi.entity.FarmId.md), [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)
Since 
    Horizon View 6.0

## Data Object Description 

Core attributes of a desktop instance. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  Unique name for the desktop   
  
**displayName**|  xsd:string|  Desktop display name.   
  
**enabled**|  xsd:boolean|  Determines if the desktop is enabled   
  
**deleting**|  xsd:boolean|  Determines if the desktop is in the process of being deleted.   
  
**type**|  xsd:string|  Type of desktop.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"AUTOMATED"| An automated desktop creates virtual machines cloned from a base template or snapshot.  
"MANUAL"| A manual machine desktop allows selection of existing virtual machines and addition to the desktop of available machines to connect to.  
"RDS"| An RDS Desktop Desktop.  

  
**source**|  xsd:string|  Source of machines.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"VIRTUAL_CENTER"| Virtual center virtual machines managed as view machines. This option is valid for Automated and Manual Desktop. In case of Automated Desktop, these refer to Full Virtual Machines that are created from a vCenter Server template.  
"VIEW_COMPOSER"| View composer linked clones managed as view machines. They share the same base image and use less storage space than full virtual machines. The user profile for linked clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes. This option is only valid for Automated Desktop.  
"INSTANT_CLONE_ENGINE"| Instant clone engine created 'instant clones' managed as view machines. Instant clone engine uses vmfork technology to create the instant clones, these clones take very less time for provisioning. Instant clones have many similarities to linked clones like :-  

    * Both instant and linked clones share the same base image and use less storage space than full virtual machines.
    * The user profile for both types clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes.
This option is only valid for Automated Desktop.  
"UNMANAGED"| Non-vCenter Server virtual machines managed as view machines. These can include physical computers, non-vCenter Server virtual machines, and blade PCs. This option is only valid for Manual Desktops.  
"RDS"| This option is only valid for RDS Desktops.  

  
**imageSource**|  xsd:string|  Source of image used in the desktop. Applicable for automated desktop.  **_Since_** Horizon 7.10  


[^1]
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"VIRTUAL_CENTER"| Image was created in virtual center.  
"IMAGE_CATALOG"| Image was created in image catalog.  

  
**userAssignment**|  xsd:string|  User assignment scheme.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"DEDICATED"| With dedicated assignment, a user returns to the same machine at each session.  
"FLOATING"| With floating assignment, a user may return to one of the available virtual machines for the next session.  

  
**allowMultipleAssignments**|  xsd:boolean|  Whether assignment of multiple users to a single machine is allowed.  **_Since_** Horizon 7.12  


  * This property has a default value of false.
[^1]

  
**accessGroup**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  View access groups can organize the desktops in your organization. They can also be used for delegated administration. For RDS Desktop, this has to be same as that of the corresponding Farm.   
  
**globalEntitlement**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  Global entitlement for this desktop. This member will be null if not set or caller does not have global read permissions.   


[^1]

  
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  Virtual Center server.   


[^1]

  
**provisioningEnabled**|  xsd:boolean|  Determines if provisioning is enabled   


[^1]

  
**numMachines**|  xsd:int|  Number of machines in the desktop. The machines may be queried using the query service for Machine. This field does not apply to RDS desktops. The RDS servers associated with an RDS desktop may be queried using the query service for RDSServer.   
  
**numSessions**|  xsd:int|  Number of desktop sessions. The sessions may be queried using the query service for Session.   
  
**farm**| [FarmId](vdi.entity.FarmId.md)|  EntityId of Farm that is associated with the Machine. This value is populated only when it is an RDS Desktop, and optional otherwise.   


[^1]

  
**supportedDomains**|  xsd:string[]|  Supported domains for the desktop. Applicable only for automated desktops.  **_Since_** Horizon 7.4  


[^1]
  * This property is an unordered array of unique values.

  
**lastProvisioningError**|  xsd:string|  String message detailing the last provisioning error on this desktop while [stopProvisioningOnError](vdi.resources.Desktop.VirtualCenterProvisioningSettings.md#stopProvisioningOnError) is enabled. This will be cleared when [enableProvisioning](vdi.resources.Desktop.VirtualCenterProvisioningSettings.md#enableProvisioning) is updated to true. This field is only applicable to automated desktops.  **_Since_** Horizon 7.5  


[^1]

  
**categoryFolderName**|  xsd:string|  Name of the category folder in the user's OS containing a shortcut to the desktop. Unset if the desktop does not belong to a category.  **_Since_** Horizon 7.6  


[^1]
  * This property defines valid folder names with a max length of 64 characters and up to 4 subdirectory levels. The subdirectories can be specified using a backslash, e.g. (dir1\dir2\dir3\dir4). Folder names can't start or end with a backslash nor can there be 2 or more backslashes together. Combinations such as (\dir1, dir1\dir2\, dir1\\\dir2, dir1\\\\\dir2) are invalid. The windows reserved keywords (CON, PRN, NUL, AUX, COM1 - COM9, LPT1 - LPT9 etc.) are not allowed in subdirectory names. 

  
**enableAppRemoting**|  xsd:boolean|  True, if this desktop can be used for application pool creation. This will be useful when the machines in the pool support application remoting.  **_Since_** Horizon 7.9  


  * This property has a default value of false.
[^1]

  
**applicationCount**|  xsd:int|  Count of all the applications that belong to the application remoting enabled Desktop which are in the machines of the desktop.  **_Since_** Horizon 7.9  


[^1]
[^2]

  
**supportedSessionType**|  xsd:string|  Supported session types for this desktop.  **_Since_** Horizon 7.9  


  * This property has a default value of "DESKTOP".
[^1]
  * This property will be one of:  
|  Value |  Description   
---|---  
"DESKTOP"| Only desktop sessions are supported for this desktop.  
"APPLICATION"| Only application sessions are supported for this desktop.  
"DESKTOP_AND_APPLICATION"| Both desktop and application sessions are supported for this desktop.  

  
**numApplicationSessions**|  xsd:int|  Number of application sessions of the Desktop when applications are associated with it.  **_Since_** Horizon 7.10  
  
**cloudManaged**|  xsd:boolean|  Indicates whether this desktop is managed by Horizon Cloud Services.  **_Since_** Horizon 7.11  


  * This property has a default value of false.
[^1]
[^2]

  
**cloudAssigned**|  xsd:boolean|  Indicates whether this desktop is assigned to a workspace in Horizon Cloud Services.  **_Since_** Horizon 7.11  


  * This property has a default value of false.
[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

