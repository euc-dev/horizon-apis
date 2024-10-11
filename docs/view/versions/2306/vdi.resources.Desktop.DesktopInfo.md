---
layout: page
title: Data Object - DesktopInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.DesktopInfo`

Returned by  
> [Desktop_Get](vdi.resources.Desktop.md#get), [Desktop_GetByNamingPattern](vdi.resources.Desktop.md#getByNamingPattern)

See also  
> [DesktopAutomatedDesktopData](vdi.resources.Desktop.AutomatedDesktopData.md), [DesktopBase](vdi.resources.Desktop.DesktopBase.md), [DesktopGlobalEntitlementData](vdi.resources.Desktop.GlobalEntitlementData.md), [DesktopId](vdi.entity.DesktopId.md), [DesktopManualDesktopData](vdi.resources.Desktop.ManualDesktopData.md), [DesktopRDSDesktopData](vdi.resources.Desktop.RDSDesktopData.md), [DesktopSettings](vdi.resources.Desktop.DesktopSettings.md)

Since  
> Horizon View 6.0


## Data Object Description 

A detailed description of a desktop instance. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [DesktopId](vdi.entity.DesktopId.md)|  Client reference to a specific desktop instance.   
  
**base**| [DesktopBase](vdi.resources.Desktop.DesktopBase.md)|  Desktop identification information.   
  
**desktopSettings**| [DesktopSettings](vdi.resources.Desktop.DesktopSettings.md)|  Configuration settings for the desktop.   
  
**type**|  xsd:string|  Type of desktop.   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"AUTOMATED"| An automated desktop creates virtual machines cloned from a base template or snapshot.  
"MANUAL"| A manual machine desktop allows selection of existing virtual machines and addition to the desktop of available machines to connect to.  
"RDS"| An RDS Desktop Desktop.  

  
**source**|  xsd:string|  Source of machines.   


* This property cannot be updated.
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


* This property need not be set.
* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"VIRTUAL_CENTER"| Image was created in virtual center.  
"IMAGE_CATALOG"| Image was created in image catalog.  

  
**automatedDesktopData**| [DesktopAutomatedDesktopData](vdi.resources.Desktop.AutomatedDesktopData.md)|  Automated desktop data.   


* This property need not be set.
  * This property is required if type is set to "AUTOMATED".

  
**manualDesktopData**| [DesktopManualDesktopData](vdi.resources.Desktop.ManualDesktopData.md)|  Manual desktop data.   


* This property need not be set.
  * This property is required if type is set to "MANUAL".

  
**rdsDesktopData**| [DesktopRDSDesktopData](vdi.resources.Desktop.RDSDesktopData.md)|  RDS Desktop data.   


* This property need not be set.
  * This property is required if type is set to "RDS".

  
**globalEntitlementData**| [DesktopGlobalEntitlementData](vdi.resources.Desktop.GlobalEntitlementData.md)|  Global entitlement data.   
  
**refId**|  xsd:string|  Reference ID used for this desktop pool.  **_Since_** Horizon 8.1  


* This property need not be set.
* This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
