---
layout: page
title: Data Object - DesktopViewComposerStorageSettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.ViewComposerStorageSettings  
Property of
     [DesktopVirtualCenterStorageSettings](vdi.resources.Desktop.VirtualCenterStorageSettings.md#field_detail)  
See also
     [DatastoreId](vdi.entity.DatastoreId.md), [DesktopNonPersistentDiskSettings](vdi.resources.Desktop.NonPersistentDiskSettings.md), [DesktopPersistentDiskSettings](vdi.resources.Desktop.PersistentDiskSettings.md), [DesktopSpaceReclamationSettings](vdi.resources.Desktop.SpaceReclamationSettings.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Settings for View Composer disks. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**useSeparateDatastoresReplicaAndOSDisks**|  xsd:boolean|  Whether to use separate datastores for replica and OS disks. This option enables control over the placement of the replica that View Composer and Instant clone engine sourced desktops use as their base image. It is recommended that a high performance datastore be chosen for these images. Depending on your hardware configuration, storing replicas on a separate datastore might create a single point of failure. Note(s) :-  


  * Fast NFS Clones (VAAI) will be unavailable if the Replica disks are stored separately from the OS disks.
  * Datastores with file system type VVOL will also be unavailable if the Replica disks are stored separately from the OS disks.
  * This setting is applicable to both View Composer and Instant clone engine sourced desktops.

  


  * This property has a default value of false.

  
**replicaDiskDatastore**| [DatastoreId](vdi.entity.DatastoreId.md)|  Datastore to store replica disks for View Composer and Instant clone engine sourced machines. Note(s) :-  


  * For Instant clone desktops, this can be modified only if there are no current operations ( [operation](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md#operation) is NONE).

  


* This property need not be set.
  * This property is required if useSeparateDatastoresReplicaAndOSDisks is set to true.

  
**useNativeSnapshots**|  xsd:boolean|  Native NFS Snapshots (VAAI - vStorage API for Array Integration) is a hardware feature of certain storage arrays. It uses native snapshotting technology to provide linked clone functionality. Only choose this option if you have appropriate hardware devices. All the selected OS disk datastores should support this. Note(s) :-  


  * For Instant clone desktops, this setting can only be set to false.

  


  * This property has a default value of false.

  
**spaceReclamationSettings**| [DesktopSpaceReclamationSettings](vdi.resources.Desktop.SpaceReclamationSettings.md)|  Settings related to the Space Reclamation feature.   
  
**persistentDiskSettings**| [DesktopPersistentDiskSettings](vdi.resources.Desktop.PersistentDiskSettings.md)|  Instant clone preserves the user information on the persistent disk when the OS data is updated. This feature is supported for Instant clone pool from 2303 (8.9) release.   
  
**nonPersistentDiskSettings**| [DesktopNonPersistentDiskSettings](vdi.resources.Desktop.NonPersistentDiskSettings.md)| **Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._ Changes to this disk are discarded when the user's session ends.   
  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

