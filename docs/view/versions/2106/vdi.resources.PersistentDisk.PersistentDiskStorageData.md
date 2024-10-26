---
layout: page
title: Data Object - PersistentDiskStorageData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.PersistentDisk.PersistentDiskStorageData`

Property of
> [PersistentDiskInfo](vdi.resources.PersistentDisk.PersistentDiskInfo.md#field_detail)

See also
> [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon View 6.0


## Data Object Description

**Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

The persistent disk's Virtual Center specific information.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  The Virtual Center server. [^2]
**datastoreName**|  xsd:string|  The datastore containing the persistent disk. [^2]
**capacityMB**|  xsd:long|  The capacity of the persistent disk in MB. [^1] [^2]


 
