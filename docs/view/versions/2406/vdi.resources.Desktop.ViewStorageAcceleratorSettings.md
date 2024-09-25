---
layout: page
title: Data Object - DesktopViewStorageAcceleratorSettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.ViewStorageAcceleratorSettings
Property of
     [DesktopManualDesktopData](vdi.resources.Desktop.ManualDesktopData.md#field_detail), [DesktopManualDesktopSpec](vdi.resources.Desktop.ManualDesktopSpec.md#field_detail), [DesktopVirtualCenterStorageSettings](vdi.resources.Desktop.VirtualCenterStorageSettings.md#field_detail)
See also
     [DesktopBlackoutTime](vdi.resources.Desktop.BlackoutTime.md)
Since 
    Horizon View 6.0

## Data Object Description 

Settings related to the View Storage Accelerator feature. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**useViewStorageAccelerator**|  xsd:boolean|  Whether to use View Storage Accelerator. vSphere 5.x and higher hosts can be configured to improve performance by caching certain desktop data. Enable this option to use View Storage Accelerator for this desktop. View Storage Accelerator is most useful for shared disks that are read frequently, such as View Composer OS disks.   
This is applicable only to Virtual Center, View Composer, or Instant Clone Engine sourced manual or automatic desktops.   
If true, VirtualCenter.StorageAcceleratorData#enabled must also be enabled.   
This value cannot be updated for Instant Clone Engine sourced desktops.   


  * This property has a default value of false.

  
**viewComposerDiskTypes**|  xsd:string|  Disk types to enable for the View Storage Accelerator feature. This is only applicable to View Composer sourced desktops - the default value must be used for Virtual Center or Instant Clone Engine sourced desktops.   


  * This property has a default value of "OS_DISKS".
[^1]
  * This property is required if useViewStorageAccelerator is set to true.
  * This property will be one of:  
|  Value |  Description   
---|---  
"OS_DISKS"| OS disks.  
"OS_AND_PERSISTENT_DISKS"| OS and persistent disks.  

  
**regenerateViewStorageAcceleratorDays**|  xsd:int|  How often to regenerate the View Storage Accelerator cache. Measured in Days. This is not applicable to Instant Clone Engine sourced desktops - the default value should be used.   


  * This property has a default value of 7.
[^1]
  * This property has a minimum value of 1. 
  * This property has a maximum value of 999. 
  * This property is required if useViewStorageAccelerator is set to true.

  
**blackoutTimes**| [DesktopBlackoutTime[]](vdi.resources.Desktop.BlackoutTime.md)|  A list of blackout times. Storage accelerator regeneration and VM disk space reclamation do not occur during blackout times. The same blackout policy applies to both operations. If unset, no blackout times are used. This should not be set for Instant Clone Engine sourced desktops.   


[^1]

  
  

  

