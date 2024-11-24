---
layout: page
title: Data Object - DesktopVirtualCenterProvisioningData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.VirtualCenterProvisioningData`

Property of
> [DesktopVirtualCenterProvisioningSettings](vdi.resources.Desktop.VirtualCenterProvisioningSettings.md#field_detail)

See also
> [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md), [BaseImageVmId](vdi.entity.BaseImageVmId.md), [DatacenterId](vdi.entity.DatacenterId.md), [DesktopComputeProfileSpec](vdi.resources.Desktop.ComputeProfileSpec.md), [HostOrClusterId](vdi.entity.HostOrClusterId.md), [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md), [ImageManagementTagId](vdi.entity.ImageManagementTagId.md), [ResourcePoolId](vdi.entity.ResourcePoolId.md), [VmFolderId](vdi.entity.VmFolderId.md), [VmTemplateId](vdi.entity.VmTemplateId.md)

Since
> Horizon View 6.0


## Data Object Description

Virtual Center entities associated with this Desktop that may not be retrievable.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**template**| [VmTemplateId](vdi.entity.VmTemplateId.md)|  Template to deploy full clone VMs. Must be set if and only if [parentVm](vdi.resources.Desktop.VirtualCenterProvisioningData.md#parentVm) and [snapshot](vdi.resources.Desktop.VirtualCenterProvisioningData.md#snapshot) are unset. Applicable only to Virtual Center sourced desktops. [^1]
**parentVm**| [BaseImageVmId](vdi.entity.BaseImageVmId.md)|  Base image VM for View Composer VMs and current Image for Instant clone desktops. Must be set if and only if [template](vdi.resources.Desktop.VirtualCenterProvisioningData.md#template) is unset and [snapshot](vdi.resources.Desktop.VirtualCenterProvisioningData.md#snapshot) is set. Applicable only to View Composer and Instant Clone Engine sourced desktops. For Instant Clone Engine desktops, this must be set on creation and cannot be updated. To update base image VM of instant clone desktops use [Desktop_SchedulePushImage](vdi.resources.Desktop.md#schedulePushImage) method. [^1]
**snapshot**| [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md)|  Base image snapshot for View Composer and current Image snapshot for Instant clone desktops. Must be set only in case of View Composer sourced desktops and if and only if [template](vdi.resources.Desktop.VirtualCenterProvisioningData.md#template) is unset and [parentVm](vdi.resources.Desktop.VirtualCenterProvisioningData.md#parentVm) is set. Applicable only to View Composer and Instant Clone Engine sourced desktops. For Instant Clone Engine desktops, this must be set on creation and cannot be updated. To update the base image snapshot of instant clone desktops use [Desktop_SchedulePushImage](vdi.resources.Desktop.md#schedulePushImage) method. [^1]
**datacenter**| [DatacenterId](vdi.entity.DatacenterId.md)|  Datacenter within which the desktop is configured. [^2]
**vmFolder**| [VmFolderId](vdi.entity.VmFolderId.md)|  VM folder to deploy the VMs to. [^2]
**hostOrCluster**| [HostOrClusterId](vdi.entity.HostOrClusterId.md)|  Host or cluster to deploy the VMs in. Note(s) :- [^98] [^99]
**resourcePool**| [ResourcePoolId](vdi.entity.ResourcePoolId.md)|  Resource pool to deploy the VMs.
**imageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  Image management Stream to be used in Desktop creation when Image Management feature is enabled. This is applicable for Instant clone and Full clone Desktops only. This is required when [template](vdi.resources.Desktop.VirtualCenterProvisioningData.md#template), [parentVm](vdi.resources.Desktop.VirtualCenterProvisioningData.md#parentVm) and [snapshot](vdi.resources.Desktop.VirtualCenterProvisioningData.md#snapshot) are unset.  **_Since_** Horizon 7.10 [^1]
**imageManagementTag**| [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)|  Image Management Tag associated with the selected image management stream to be used in Desktop creation when Image Management feature is enabled. This is applicable for Instant clone and Full clone Desktops only. This is required when [imageManagementStream](vdi.resources.Desktop.VirtualCenterProvisioningData.md#imageManagementStream) is set.  **_Since_** Horizon 7.10 [^1]
**computeProfile**| [DesktopComputeProfileSpec](vdi.resources.Desktop.ComputeProfileSpec.md)|  Compute Profile used to specify the CPU, RAM and cores per socket configuration to create VMs with.  **_Since_** Horizon 8.6 [^1]

[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^98]: For Instant clone desktops only it can be only a cluster and not a host.
[^99]: For Instant clone desktops, this can be modified only if there are no current operations ( [operation](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md#operation) is NONE).