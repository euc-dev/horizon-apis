---
layout: page
title: Data Object - FarmVirtualCenterProvisioningData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.VirtualCenterProvisioningData`

Property of
> [FarmVirtualCenterProvisioningSettings](vdi.resources.Farm.VirtualCenterProvisioningSettings.md#field_detail)

See also
> [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md), [BaseImageVmId](vdi.entity.BaseImageVmId.md), [DatacenterId](vdi.entity.DatacenterId.md), [FarmComputeProfileSpec](vdi.resources.Farm.ComputeProfileSpec.md), [HostOrClusterId](vdi.entity.HostOrClusterId.md), [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md), [ImageManagementTagId](vdi.entity.ImageManagementTagId.md), [ResourcePoolId](vdi.entity.ResourcePoolId.md), [VmFolderId](vdi.entity.VmFolderId.md)

Since
> Horizon View 6.2


## Data Object Description

Virtual Center entities associated with this Automated Farm that may not be retrievable.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**parentVm**| [BaseImageVmId](vdi.entity.BaseImageVmId.md)|  Base image VM for RDS Servers. Applicable only to View Composer sourced RDS Servers. [^1]
**snapshot**| [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md)|  Base image snapshot for RDS Servers. Applicable only to View Composer sourced RDS Servers. [^1]
**datacenter**| [DatacenterId](vdi.entity.DatacenterId.md)|  Datacenter within which the RDS Servers are configured. [^2]
**vmFolder**| [VmFolderId](vdi.entity.VmFolderId.md)|  VM folder to deploy the RDS Servers to. [^2]
**hostOrCluster**| [HostOrClusterId](vdi.entity.HostOrClusterId.md)|  Host or cluster to deploy the RDS Servers in. Note(s) :- [^125] [^187]
**resourcePool**| [ResourcePoolId](vdi.entity.ResourcePoolId.md)|  Resource pool to deploy the RDS Servers.
**imageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  Image Management Stream to be used in Farm creation when Image Management feature is enabled. This is applicable for Instant clone Farms only. This is required when [parentVm](vdi.resources.Farm.VirtualCenterProvisioningData.md#parentVm) and [snapshot](vdi.resources.Farm.VirtualCenterProvisioningData.md#snapshot) are unset.  **_Since_** Horizon 7.10 [^1]
**imageManagementTag**| [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)|  Image Management Tag associated with the selected image management stream to be used in Farm creation when Image Management feature is enabled. This is applicable for Instant clone Farms only. This is required when [imageManagementStream](vdi.resources.Farm.VirtualCenterProvisioningData.md#imageManagementStream) is set.  **_Since_** Horizon 7.10 [^1]
**computeProfile**| [FarmComputeProfileSpec](vdi.resources.Farm.ComputeProfileSpec.md)|  Compute Profile used to specify the CPU, RAM and cores per socket configuration to create VMs with.  **_Since_** Horizon 8.6 [^1]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^125]: For Instant clone farms only it can be only a cluster and not a host.
[^187]: For Instant clone farms, this can be modified only if there are no current operations ( [operation](vdi.resources.Farm.InstantCloneProvisioningStatusData.md#operation) is NONE).