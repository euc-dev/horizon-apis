---
layout: page
title: Data Object - PersistentDiskReplaceSpec
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.PersistentDisk.ReplaceSpec`

Parameter to
> [PersistentDisk_Replace](vdi.resources.PersistentDisk.md#replace)

See also
> [DatastorePathId](vdi.entity.DatastorePathId.md), [MachineId](vdi.entity.MachineId.md)

Since
> Horizon View 6.0


## Data Object Description

The specification for replacing a persistent disk on a machine.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**machine**| [MachineId](vdi.entity.MachineId.md)|  The ID of the machine to replace the persistent disk. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.
**archiveDatastorePath**| [DatastorePathId](vdi.entity.DatastorePathId.md)|  The datastore path to archive the virtual disk to.


 