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
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  Virtual Center server.   


* This property cannot be updated.

  
**parentVmPath**|  xsd:string|  Base image path for View Composer RDS Servers or current image parent VM path for instant clone RDS Servers. The name is the last element of the path.   


* This property need not be set.
* This property cannot be updated.

  
**snapshotPath**|  xsd:string|  Base image snapshot path for View Composer RDS Servers or current image snapshot path for instant clone RDS Servers. The name is the last element of the path.   


* This property need not be set.
* This property cannot be updated.

  
**parentVmMoid**|  xsd:string|  MOID of base image for View Composer RDS Servers or MOID of current image parent VM for instant clone RDS Servers.   


* This property need not be set.
* This property cannot be updated.

  
**snapshotMoid**|  xsd:string|  MOID of base image snapshot for View Composer RDS Servers or MOID of current image snapshot for instant clone RDS Servers.   


* This property need not be set.
* This property cannot be updated.

  
**pendingImageParentVmPath**|  xsd:string|  Pending base image VM path for Instant clone farms. This is used to return the information about the parent VM of the pending Image.   


* This property need not be set.
* This property cannot be updated.

  
**pendingImageSnapshotPath**|  xsd:string|  Pending base image snapshot path for Instant clone farms. This is used to return the information about the snapshot of the pending Image.   


* This property need not be set.
* This property cannot be updated.

  
**pendingImageParentVmMoid**|  xsd:string|  MOID of pending base image VM for Instant clone farms. This is used to return the information about the parent VM of the pending image.   


* This property need not be set.
* This property cannot be updated.

  
**pendingImageSnapshotMoid**|  xsd:string|  MOID of pending base image snapshot for Instant clone farms. This is used to return the information about the snapshot of the pending image.   


* This property need not be set.
* This property cannot be updated.

  
**imageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  Image Management Stream associated with instant clone farms if source is image catalog.   


* This property need not be set.
* This property cannot be updated.

  
**imageManagementTag**| [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)|  Image Management Tag associated with instant clone farms if source is image catalog.   


* This property need not be set.
* This property cannot be updated.

  
**pendingImageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  Pending Image Management Stream associated with instant clone farms if source is image catalog.   


* This property need not be set.
* This property cannot be updated.

  
**pendingImageManagementTag**| [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)|  Pending Image Management Tag associated with instant clone farms if source is image catalog.   


* This property need not be set.
* This property cannot be updated.

  
  
  

  
  
