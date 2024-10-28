---
layout: page
title: Data Object - DesktopVirtualCenterData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.VirtualCenterData`

Property of
> [DesktopProvisioningView](vdi.resources.Desktop.DesktopProvisioningView.md#field_detail)

See also
> [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md), [ImageManagementTagId](vdi.entity.ImageManagementTagId.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon 7.10


## Data Object Description

Paths for Virtual Center entities associated with this automated Desktop.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  Virtual Center server. [^2]
**templatePath**|  xsd:string|  Template path to deploy full clone VMs. The name is the last element of the path. [^1] [^2]
**templateMoid**|  xsd:string|  MOID of virtual machine template to deploy full clone VMs. [^1] [^2]
**parentVmPath**|  xsd:string|  Base image path for View Composer VMs and current image parent VM path for instant clone desktops. The name is the last element of the path. [^1] [^2]
**snapshotPath**|  xsd:string|  Base image snapshot path for View Composer desktops and current image snapshot path for instant clone desktops. The name is the last element of the path. [^1] [^2]
**parentVmMoid**|  xsd:string|  MOID of base image for View Composer VMs or MOID of current image parent VM for instant clone desktops. [^1] [^2]
**snapshotMoid**|  xsd:string|  MOID of base image snapshot for View Composer desktops or MOID of current image snapshot for instant clone desktops. [^1] [^2]
**pendingImageParentVmPath**|  xsd:string|  Pending base image VM path for Instant clone desktops. This is used to return the information about the parent VM of the pending Image. [^1] [^2]
**pendingImageSnapshotPath**|  xsd:string|  Pending base image snapshot path for Instant clone desktops. This is used to return the information about the snapshot of the pending Image. [^1] [^2]
**pendingImageParentVmMoid**|  xsd:string|  MOID of pending base image VM for Instant clone desktops. This is used to return the information about the parent VM of the pending image. [^1] [^2]
**pendingImageSnapshotMoid**|  xsd:string|  MOID of pending base image snapshot for Instant clone desktops. This is used to return the information about the snapshot of the pending image. [^1] [^2]
**imageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  Image Management Stream associated with full clone and instant clone desktops if source is image catalog. [^1] [^2]
**imageManagementTag**| [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)|  Image Management Tag associated with full clone and instant clone desktops if source is image catalog. [^1] [^2]
**pendingImageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  Pending Image Management Stream associated with instant clone desktops if source is image catalog. [^1] [^2]
**pendingImageManagementTag**| [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)|  Pending Image Management Tag associated with instant clone desktops if source is image catalog. [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.