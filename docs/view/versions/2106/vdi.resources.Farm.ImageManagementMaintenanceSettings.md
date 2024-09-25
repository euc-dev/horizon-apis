---
layout: page
title: Data Object - FarmImageManagementMaintenanceSettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Farm.ImageManagementMaintenanceSettings
Property of
     [FarmMaintenanceSpec](vdi.resources.Farm.MaintenanceSpec.md#field_detail)
See also
     [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md), [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)
Since 
    Horizon 7.10

## Data Object Description 

Settings for the image maintenance if farm is created using image catalog. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**imageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  New image management stream for the farm.   
  
**imageManagementTag**| [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)|  New image management tag for the farm. This tag must be within the [imageManagementStream](vdi.resources.Farm.ImageManagementMaintenanceSettings.md#imageManagementStream).   
  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
