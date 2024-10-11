---
layout: page
title: Data Object - VirtualCenterStorageAcceleratorData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.VirtualCenter.StorageAcceleratorData`

Property of  
> [VirtualCenterInfo](vdi.infrastructure.VirtualCenter.VirtualCenterInfo.md#field_detail), [VirtualCenterSpec](vdi.infrastructure.VirtualCenter.VirtualCenterSpec.md#field_detail)

See also  
> [VirtualCenterStorageAcceleratorHostOverride](vdi.infrastructure.VirtualCenter.StorageAcceleratorHostOverride.md)

Since  
> Horizon View 6.0


## Data Object Description 

View Storage Accelerator configuration details. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**enabled**|  xsd:boolean|  Is View Storage Accelerator enabled?   


  * This property has a default value of false.

  
**defaultCacheSizeMB**|  xsd:int|  Default size of the cache in megabytes. For vCenter version 7.0 or above maximum supported cache size is 32 GB, otherwise it will be 2 GB.   


  * This property has a default value of 1024.
 * This property need not be set.
  * This property has a minimum value of 100. 
  * This property has a maximum value of 32768. 
  * This property is required if enabled is set to true.

  
**hostOverrides**| [VirtualCenterStorageAcceleratorHostOverride[]](vdi.infrastructure.VirtualCenter.StorageAcceleratorHostOverride.md)|  Cache size overrides for hosts which support View Storage Accelerator.   


 * This property need not be set.

  
  
  
   
  
  
