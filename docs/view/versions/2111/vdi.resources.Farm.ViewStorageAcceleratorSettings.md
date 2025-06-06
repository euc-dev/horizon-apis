---
layout: page
title: Data Object - FarmViewStorageAcceleratorSettings
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.resources.Farm.ViewStorageAcceleratorSettings`

Property of
> [FarmVirtualCenterStorageSettings](vdi.resources.Farm.VirtualCenterStorageSettings.md#field_detail)

Since
> Horizon 7.2


## Data Object Description

Settings related to the View Storage Accelerator feature.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**useViewStorageAccelerator**|  xsd:boolean|  Whether to use View Storage Accelerator. vSphere 5.x and higher hosts can be configured to improve performance by caching certain farm data. Enable this option to use View Storage Accelerator for this farm. View Storage Accelerator is most useful for shared disks that are read frequently, such as OS disks. <br>This is applicable only to Instant Clone Engine sourced farms and should be true. For other farms this value is ignored. <br>If true, VirtualCenter.StorageAcceleratorData#enabled must also be enabled. <br>This value cannot be updated for Instant Clone Engine sourced farms. [^5] [^1]


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.