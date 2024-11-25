---
layout: page
title: Data Object - DesktopPushImageSpec
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.PushImageSpec`

Parameter to
> [Desktop_SchedulePushImage](vdi.resources.Desktop.md#schedulePushImage)

See also
> [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md), [BaseImageVmId](vdi.entity.BaseImageVmId.md), [DesktopPushImageSettings](vdi.resources.Desktop.PushImageSettings.md)

Since
> Horizon 7.0


## Data Object Description

Specification for the Push Image operation. This operation is only applicable to Instant clone desktops.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**parentVm**| [BaseImageVmId](vdi.entity.BaseImageVmId.md)|  New base image VM for the desktop. This must be in the same datacenter as the base image of the desktop.
**snapshot**| [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md)|  New base image snapshot for the desktop. This must be a snapshot of the [parentVm](vdi.resources.Desktop.PushImageSpec.md#parentVm).
**settings**| [DesktopPushImageSettings](vdi.resources.Desktop.PushImageSettings.md)|  Settings for the Push Image operation.


 
