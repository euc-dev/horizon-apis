---
layout: page
title: Data Object - DesktopVirtualCenterStorageSettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.VirtualCenterStorageSettings  
Property of
     [DesktopVirtualCenterProvisioningSettings](vdi.resources.Desktop.VirtualCenterProvisioningSettings.md#field_detail)  
See also
     [DesktopViewComposerStorageSettings](vdi.resources.Desktop.ViewComposerStorageSettings.md), [DesktopViewStorageAcceleratorSettings](vdi.resources.Desktop.ViewStorageAcceleratorSettings.md), [DesktopVirtualCenterDatastoreSettings](vdi.resources.Desktop.VirtualCenterDatastoreSettings.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Virtual Center storage settings. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**datastores**| [DesktopVirtualCenterDatastoreSettings[]](vdi.resources.Desktop.VirtualCenterDatastoreSettings.md)|  Datastore IDs to store the VM (or the OS disk using other options for View Composer or Instant Clone Engine VM storage).Note(s) :-  


  * For Instant clone desktops, this can be modified only if there are no current operations ( [operation](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md#operation) is NONE).
  * For Full clone desktops, if Storage DRS cluster is used then it can only have one element.

  
  
**useVSan**|  xsd:boolean|  Whether to use vSphere VSAN. This is applicable for vSphere 5.5 or later. [datastores](vdi.resources.Desktop.VirtualCenterStorageSettings.md#datastores) must specify exactly one datastore of file system type VSAN. If this desktop is sourced from View Composer or Instant Clone Engine, [useSeparateDatastoresPersistentAndOSDisks](vdi.resources.Desktop.PersistentDiskSettings.md#useSeparateDatastoresPersistentAndOSDisks) , [useSeparateDatastoresReplicaAndOSDisks](vdi.resources.Desktop.ViewComposerStorageSettings.md#useSeparateDatastoresReplicaAndOSDisks) and [reclaimVmDiskSpace](vdi.resources.Desktop.SpaceReclamationSettings.md#reclaimVmDiskSpace) must be disabled.   


  * This property has a default value of false.

  
**viewComposerStorageSettings**| [DesktopViewComposerStorageSettings](vdi.resources.Desktop.ViewComposerStorageSettings.md)|  View Composer storage settings. This must be set for View Composer sourced desktops.   


* This property need not be set.

  
**viewStorageAcceleratorSettings**| [DesktopViewStorageAcceleratorSettings](vdi.resources.Desktop.ViewStorageAcceleratorSettings.md)|  View Storage Accelerator settings.   
  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

