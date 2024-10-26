---
layout: page
title: Data Object - VirtualCenterStorageAcceleratorHostOverride
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.VirtualCenter.StorageAcceleratorHostOverride`

Property of
> [VirtualCenterStorageAcceleratorData](vdi.infrastructure.VirtualCenter.StorageAcceleratorData.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Hypervisor hosts involved in Content Based Read Caching (CBRC).

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**path**|  xsd:string|  The path of the host that supports View Storage Accelerator.
**cacheSizeMB**|  xsd:int|  Size of the cache in megabytes. For vCenter version 7.0 or above maximum supported cache size is 32 GB, otherwise it will be 2 GB. [^177] [^178]


 
