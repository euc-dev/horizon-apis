---
layout: page
title: Data Object - FarmImageMaintenanceSettings
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.ImageMaintenanceSettings`

Property of  
> [FarmMaintenanceSpec](vdi.resources.Farm.MaintenanceSpec.md#field_detail)

See also  
> [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md), [BaseImageVmId](vdi.entity.BaseImageVmId.md)

Since  
> Horizon 7.1


## Data Object Description 

Settings for the image maintenance. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**parentVm**| [BaseImageVmId](vdi.entity.BaseImageVmId.md)|  New base image VM for the farm. This must be in the same datacenter as the base image of the farm.   
  
**snapshot**| [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md)|  New base image snapshot for the farm. This must be a snapshot of the [parentVm](vdi.resources.Farm.ImageMaintenanceSettings.md#parentVm).   
  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
