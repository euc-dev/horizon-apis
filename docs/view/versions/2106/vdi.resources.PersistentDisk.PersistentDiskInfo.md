---
layout: page
title: Data Object - PersistentDiskInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.PersistentDisk.PersistentDiskInfo`

Returned by  
> [PersistentDisk_Get](vdi.resources.PersistentDisk.md#get)

See also  
> [PersistentDiskGeneralData](vdi.resources.PersistentDisk.PersistentDiskGeneralData.md), [PersistentDiskId](vdi.entity.PersistentDiskId.md), [PersistentDiskStorageData](vdi.resources.PersistentDisk.PersistentDiskStorageData.md)

Since  
> Horizon View 6.0


## Data Object Description 

**Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Information on a persistent disk. 

##  Queryable Data Object 

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService"). 

All fields except [storage](vdi.resources.PersistentDisk.PersistentDiskInfo.md#storage).[capacityMB](vdi.resources.PersistentDisk.PersistentDiskStorageData.md#capacityMB) can be queried. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [PersistentDiskId](vdi.entity.PersistentDiskId.md)|  The ID of the persistent disk.   
  
**general**| [PersistentDiskGeneralData](vdi.resources.PersistentDisk.PersistentDiskGeneralData.md)|  General information on the persistent disk.   
  
**storage**| [PersistentDiskStorageData](vdi.resources.PersistentDisk.PersistentDiskStorageData.md)|  Storage information on the persistent disk.   
  
  
  

  
  
