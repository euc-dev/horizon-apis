---
layout: page
title: Data Object - DesktopImageManagementPushImageSpec
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.ImageManagementPushImageSpec  
Parameter to
     [Desktop_ImageManagementSchedulePushImage](vdi.resources.Desktop.md#imageManagementSchedulePushImage)  
See also
     [DesktopPushImageSettings](vdi.resources.Desktop.PushImageSettings.md), [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md), [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)  
Since 
    Horizon 7.10

## Data Object Description 

Specification for the Push Image operation if desktop is created using image catalog. This operation is only applicable to Instant clone desktops. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**imageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  New image management stream for the desktop.   
  
**imageManagementTag**| [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)|  New image management tag for the desktop. This tag must be within the stream [imageManagementStream](vdi.resources.Desktop.ImageManagementPushImageSpec.md#imageManagementStream).   
  
**settings**| [DesktopPushImageSettings](vdi.resources.Desktop.PushImageSettings.md)|  Settings for the Push Image operation.   
  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

