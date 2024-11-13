---
layout: page
title: Data Object - FarmViewComposerStorageSettings
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.resources.Farm.ViewComposerStorageSettings`

Property of
> [FarmVirtualCenterStorageSettings](vdi.resources.Farm.VirtualCenterStorageSettings.md#field_detail)

See also
> [DatastoreId](vdi.entity.DatastoreId.md), [FarmSpaceReclamationSettings](vdi.resources.Farm.SpaceReclamationSettings.md)

Since
> Horizon View 6.2


## Data Object Description

Settings for View Composer disks.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**useSeparateDatastoresReplicaAndOSDisks**|  xsd:boolean|  Whether to use separate datastores for replica and OS disks. This option enables control over the placement of the replica that linked clones use as their base image. It is recommended that a high performance datastore be chosen for these images. Depending on your hardware configuration, storing replicas on a separate datastore might create a single point of failure. Note - Fast NFS Clones (VAAI) will be unavailable if the Replica disks are stored separately from the OS disks. Datastores with file system type VVOL will also be unavailable if the Replica disks are stored separately from the OS disks. [^5]
**replicaDiskDatastore**| [DatastoreId](vdi.entity.DatastoreId.md)|  Datastore to store replica disks for View Composer and Instant clone engine RDS Servers. Note(s) :- [^126] [^1] [^86]
**useNativeSnapshots**|  xsd:boolean|  Native NFS Snapshots (VAAI - vStorage API for Array Integration) is a hardware feature of certain storage arrays. It uses native snapshotting technology to provide linked clone functionality. Only choose this option if you have appropriate hardware devices. All the selected OS disk datastores should support this. [^5]
**spaceReclamationSettings**| [FarmSpaceReclamationSettings](vdi.resources.Farm.SpaceReclamationSettings.md)|  Settings related to the Space Reclamation feature.


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.
[^86]: This property is required if useSeparateDatastoresReplicaAndOSDisks is set to true.
[^126]: For Instant clone farms, this can be modified only if there are no current operations ( [operation](vdi.resources.Farm.InstantCloneProvisioningStatusData.md#operation) is NONE).