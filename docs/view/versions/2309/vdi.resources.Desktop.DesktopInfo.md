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
**type**|  xsd:string|  Type of desktop. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>AUTOMATED</td><td>An automated desktop creates virtual machines cloned from a base template or snapshot.</td></tr><tr><td>MANUAL</td><td>A manual machine desktop allows selection of existing virtual machines and addition to the desktop of available machines to connect to.</td></tr><tr><td>RDS</td><td>An RDS Desktop.</td></tr></table>
**source**|  xsd:string|  Source of machines. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>VIRTUAL_CENTER</td><td>Virtual center virtual machines managed as view machines. This option is valid for Automated and Manual Desktop. In case of Automated Desktop, these refer to Full Virtual Machines that are created from a vCenter Server template.</td></tr><tr><td>VIEW_COMPOSER</td><td>View composer linked clones managed as view machines. They share the same base image and use less storage space than full virtual machines. The user profile for linked clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes. This option is only valid for Automated Desktop.</td></tr><tr><td>INSTANT_CLONE_ENGINE</td><td>Instant clone engine created 'instant clones' managed as view machines. Instant clone engine uses vmfork technology to create the instant clones, these clones take very less time for provisioning. Instant clones have many similarities to linked clones. This option is only valid for Automated Desktop.</td></tr><tr><td>UNMANAGED</td><td>Non-vCenter Server virtual machines managed as view machines. These can include physical computers, non-vCenter Server virtual machines, and blade PCs. This option is only valid for Manual Desktops.</td></tr><tr><td>RDS</td><td>This option is only valid for RDS Desktops.</td></tr></table>
**imageSource**|  xsd:string|  Source of image used in the desktop. Applicable for automated desktop.  **_Since_** Horizon 7.10 [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>VIRTUAL_CENTER</td><td>Image was created in virtual center.</td></tr><tr><td>IMAGE_CATALOG</td><td>Image was created in image catalog.</td></tr></table>
**automatedDesktopData**| [DesktopAutomatedDesktopData](vdi.resources.Desktop.AutomatedDesktopData.md)|  Automated desktop data. [^1] [^29]
**manualDesktopData**| [DesktopManualDesktopData](vdi.resources.Desktop.ManualDesktopData.md)|  Manual desktop data. [^1] [^26]
**rdsDesktopData**| [DesktopRDSDesktopData](vdi.resources.Desktop.RDSDesktopData.md)|  RDS Desktop data. [^1] [^27]
**globalEntitlementData**| [DesktopGlobalEntitlementData](vdi.resources.Desktop.GlobalEntitlementData.md)|  Global entitlement data.
**refId**|  xsd:string|  Reference ID used for this desktop pool.  **_Since_** Horizon 8.1 [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^26]: This property is required if type is set to 'MANUAL'.
[^27]: This property is required if type is set to 'RDS'.
[^29]: This property is required if type is set to 'AUTOMATED'.