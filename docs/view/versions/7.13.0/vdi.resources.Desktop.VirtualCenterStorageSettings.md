---
layout: page
title: Data Object - DesktopVirtualCenterStorageSettings
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.VirtualCenterStorageSettings`

Property of
> [DesktopVirtualCenterProvisioningSettings](vdi.resources.Desktop.VirtualCenterProvisioningSettings.md#field_detail)

See also
> [DesktopViewComposerStorageSettings](vdi.resources.Desktop.ViewComposerStorageSettings.md), [DesktopViewStorageAcceleratorSettings](vdi.resources.Desktop.ViewStorageAcceleratorSettings.md), [DesktopVirtualCenterDatastoreSettings](vdi.resources.Desktop.VirtualCenterDatastoreSettings.md)

Since
> Horizon View 6.0


## Data Object Description

Virtual Center storage settings.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**datastores**| [DesktopVirtualCenterDatastoreSettings[]](vdi.resources.Desktop.VirtualCenterDatastoreSettings.md)|  Datastore IDs to store the VM (or the OS disk using other options for View Composer or Instant Clone Engine VM storage).Note(s) :- [^85] [^101]
**useVSan**|  xsd:boolean|  Whether to use vSphere VSAN. This is applicable for vSphere 5.5 or later. [datastores](vdi.resources.Desktop.VirtualCenterStorageSettings.md#datastores) must specify exactly one datastore of file system type VSAN. If this desktop is sourced from View Composer or Instant Clone Engine, [useSeparateDatastoresPersistentAndOSDisks](vdi.resources.Desktop.PersistentDiskSettings.md#useSeparateDatastoresPersistentAndOSDisks) , [useSeparateDatastoresReplicaAndOSDisks](vdi.resources.Desktop.ViewComposerStorageSettings.md#useSeparateDatastoresReplicaAndOSDisks) and [reclaimVmDiskSpace](vdi.resources.Desktop.SpaceReclamationSettings.md#reclaimVmDiskSpace) must be disabled. [^5]
**viewComposerStorageSettings**| [DesktopViewComposerStorageSettings](vdi.resources.Desktop.ViewComposerStorageSettings.md)|  View Composer storage settings. This must be set for View Composer sourced desktops. [^1]
**viewStorageAcceleratorSettings**| [DesktopViewStorageAcceleratorSettings](vdi.resources.Desktop.ViewStorageAcceleratorSettings.md)|  View Storage Accelerator settings.


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.
[^85]: For Instant clone desktops, this can be modified only if there are no current operations ( [operation](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md#operation) is NONE).
[^101]: For Full clone desktops, if Storage DRS cluster is used then it can only have one element.