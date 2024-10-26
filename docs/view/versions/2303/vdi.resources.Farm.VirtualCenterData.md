---
layout: page
title: Data Object - FarmVirtualCenterData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.VirtualCenterData`

Property of
> [FarmProvisioningView](vdi.resources.Farm.FarmProvisioningView.md#field_detail)

See also
> [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md), [ImageManagementTagId](vdi.entity.ImageManagementTagId.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon 7.10


## Data Object Description

Paths for Virtual Center entities associated with the automated Farm.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  Virtual Center server. [^2]
**parentVmPath**|  xsd:string|  Base image path for View Composer RDS Servers or current image parent VM path for instant clone RDS Servers. The name is the last element of the path. [^1] [^2]
**snapshotPath**|  xsd:string|  Base image snapshot path for View Composer RDS Servers or current image snapshot path for instant clone RDS Servers. The name is the last element of the path. [^1] [^2]
**parentVmMoid**|  xsd:string|  MOID of base image for View Composer RDS Servers or MOID of current image parent VM for instant clone RDS Servers. [^1] [^2]
**snapshotMoid**|  xsd:string|  MOID of base image snapshot for View Composer RDS Servers or MOID of current image snapshot for instant clone RDS Servers. [^1] [^2]
**pendingImageParentVmPath**|  xsd:string|  Pending base image VM path for Instant clone farms. This is used to return the information about the parent VM of the pending Image. [^1] [^2]
**pendingImageSnapshotPath**|  xsd:string|  Pending base image snapshot path for Instant clone farms. This is used to return the information about the snapshot of the pending Image. [^1] [^2]
**pendingImageParentVmMoid**|  xsd:string|  MOID of pending base image VM for Instant clone farms. This is used to return the information about the parent VM of the pending image. [^1] [^2]
**pendingImageSnapshotMoid**|  xsd:string|  MOID of pending base image snapshot for Instant clone farms. This is used to return the information about the snapshot of the pending image. [^1] [^2]
**imageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  Image Management Stream associated with instant clone farms if source is image catalog. [^1] [^2]
**imageManagementTag**| [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)|  Image Management Tag associated with instant clone farms if source is image catalog. [^1] [^2]
**pendingImageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  Pending Image Management Stream associated with instant clone farms if source is image catalog. [^1] [^2]
**pendingImageManagementTag**| [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)|  Pending Image Management Tag associated with instant clone farms if source is image catalog. [^1] [^2]
 


 
