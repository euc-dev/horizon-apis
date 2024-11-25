---
layout: page
title: Data Object - DesktopPersistentDiskSettings
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.PersistentDiskSettings`

Property of
> [DesktopViewComposerStorageSettings](vdi.resources.Desktop.ViewComposerStorageSettings.md#field_detail)

See also
> [DesktopVirtualCenterDatastoreSettings](vdi.resources.Desktop.VirtualCenterDatastoreSettings.md)

Since
> Horizon View 6.0


## Data Object Description

With View Composer, you can configure OS data and user information on separate disks in linked-clone machines. View Composer preserves the user information on the persistent disk when the OS data is updated, refreshed, or rebalanced. A View Composer persistent disk contains user settings and other user-generated data.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**redirectWindowsProfile**|  xsd:boolean|  Windows profiles will be redirected to persistent disks, which are not affected by View Composer operations such as refresh, recompose and rebalance. Note(s) :- [^193] [^6] [^2]
**useSeparateDatastoresPersistentAndOSDisks**|  xsd:boolean|  Whether to use separate datastores for persistent and OS disks. This must be false if [redirectWindowsProfile](vdi.resources.Desktop.PersistentDiskSettings.md#redirectWindowsProfile) is false. [^5] [^1] [^74]
**persistentDiskDatastores**| [DesktopVirtualCenterDatastoreSettings[]](vdi.resources.Desktop.VirtualCenterDatastoreSettings.md)|  Datastores to store persistent disks for View Composer VMs. [^1] [^75]
**diskSizeMB**|  xsd:int|  Size of the persistent disk in MB. [^76] [^1] [^77] [^74]
**diskDriveLetter**|  xsd:string|  Persistent disk drive letter. This must be different than [diskDriveLetter](vdi.resources.Desktop.NonPersistentDiskSettings.md#diskDriveLetter) if set. [^78] [^1] [^185] [^74]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^5]: This property has a default value of false.
[^6]: This property has a default value of true.
[^74]: This property is required if redirectWindowsProfile is set to true.
[^75]: This property is required if useSeparateDatastoresPersistentAndOSDisks is set to true.
[^76]: This property has a default value of 2048.
[^77]: This property has a minimum value of 128.
[^78]: This property has a default value of D.
[^185]: This property must be single letters from D to Z.
[^193]: For Instant clone desktops, this setting can only be set to false.