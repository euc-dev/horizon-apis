---
layout: page
title: Data Object - DesktopPersistentDiskSettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.PersistentDiskSettings
Property of
     [DesktopViewComposerStorageSettings](vdi.resources.Desktop.ViewComposerStorageSettings.md#field_detail)
See also
     [DesktopVirtualCenterDatastoreSettings](vdi.resources.Desktop.VirtualCenterDatastoreSettings.md)
Since 
    Horizon View 6.0

## Data Object Description 

With View Composer, you can configure OS data and user information on separate disks in linked-clone machines. View Composer preserves the user information on the persistent disk when the OS data is updated, refreshed, or rebalanced. A View Composer persistent disk contains user settings and other user-generated data. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**redirectWindowsProfile**|  xsd:boolean|  Windows profiles will be redirected to persistent disks, which are not affected by View Composer operations such as refresh, recompose and rebalance. Note(s) :-   


  * For Instant clone desktops, this setting can only be set to false

  


  * This property has a default value of true.
[^2]

  
**useSeparateDatastoresPersistentAndOSDisks**|  xsd:boolean|  Whether to use separate datastores for persistent and OS disks. This must be false if [redirectWindowsProfile](vdi.resources.Desktop.PersistentDiskSettings.md#redirectWindowsProfile) is false.   


  * This property has a default value of false.
[^1]
  * This property is required if redirectWindowsProfile is set to true.

  
**persistentDiskDatastores**| [DesktopVirtualCenterDatastoreSettings[]](vdi.resources.Desktop.VirtualCenterDatastoreSettings.md)|  Datastores to store persistent disks for View Composer VMs.   


[^1]
  * This property is required if useSeparateDatastoresPersistentAndOSDisks is set to true.

  
**diskSizeMB**|  xsd:int|  Size of the persistent disk in MB.   


  * This property has a default value of 2048.
[^1]
  * This property has a minimum value of 128. 
  * This property is required if redirectWindowsProfile is set to true.

  
**diskDriveLetter**|  xsd:string|  Persistent disk drive letter. This must be different than [diskDriveLetter](vdi.resources.Desktop.NonPersistentDiskSettings.md#diskDriveLetter) if set.   


  * This property has a default value of D.
[^1]
  * This property must be single letters from D to Z. 
  * This property is required if redirectWindowsProfile is set to true.

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
