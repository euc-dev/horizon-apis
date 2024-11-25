---
layout: page
title: Data Object - VirtualCenterStorageAcceleratorHostOverride
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.VirtualCenter.StorageAcceleratorHostOverride`

Property of
> [VirtualCenterStorageAcceleratorData](vdi.infrastructure.VirtualCenter.StorageAcceleratorData.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Hypervisor hosts involved in Content Based Read Caching (CBRC).

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**path**|  xsd:string|  The path of the host that supports View Storage Accelerator.
**cacheSizeMB**|  xsd:int|  Size of the cache in megabytes. [^177] [^178]


 


[^177]: This property has a minimum value of 100.
[^178]: This property has a maximum value of 32768.