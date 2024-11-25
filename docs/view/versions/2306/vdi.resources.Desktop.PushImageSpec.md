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
> [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md), [BaseImageVmId](vdi.entity.BaseImageVmId.md), [DesktopComputeProfileSpec](vdi.resources.Desktop.ComputeProfileSpec.md), [DesktopPushImageSettings](vdi.resources.Desktop.PushImageSettings.md), [MachineId](vdi.entity.MachineId.md)

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
**selectivePushImage**|  xsd:boolean|  Set to true for selective push image. Indicates if the new image should be applied to a subset of the clones in the pool. The image published with this option, will be held as a pending image, unless it is either promoted or canceled.  **_Since_** Horizon 8.4 [^5] [^1]
**machines**| [MachineId[]](vdi.entity.MachineId.md)|  The list of machines from the pool on which the new image is to be applied  **_Since_** Horizon 8.4 [^1]
**computeProfile**| [DesktopComputeProfileSpec](vdi.resources.Desktop.ComputeProfileSpec.md)|  Compute Profile used to specify the CPU, RAM and cores per socket configuration to create VMs with.  **_Since_** Horizon 8.6 [^1]
 


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.