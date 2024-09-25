---
layout: page
title: Data Object - ImageManagementAssetBase
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetBase
Property of
     [ImageManagementAssetInfo](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetInfo.md#field_detail)
See also
     [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md), [BaseImageVmId](vdi.entity.BaseImageVmId.md), [DatacenterId](vdi.entity.DatacenterId.md), [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md), [ImageManagementVersionId](vdi.entity.ImageManagementVersionId.md), [MapEntry](vdi.util.MapEntry.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md), [VmTemplateId](vdi.entity.VmTemplateId.md)
Since 
    Horizon 7.10

## Data Object Description 

Basic data about an Image Management Asset. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**status**|  xsd:string|  Image management asset status.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"AVAILABLE"| Image management asset is available for pools/farms to be created.  
"DELETED"| Image management asset has been deleted.  
"DEPLOYING_VM"| Image management asset is deploying VM on the virtual center.  
"DEPLOYMENT_DONE"| Image management asset VM deployed on the virtual center.  
"DISABLED"| Image management asset has been disabled and no further pool/farm operation can be done using the same.  
"FAILED"| Image management asset creation has failed.  
"REPLICATING"| Copying the specialized images across all virtual centers.  
"RETRY_PENDING"| When image management asset creation has failed, retry action is pending for asset to be created.  
"SPECIALIZING_VM"| Image management asset is being published and specialized internally like installing agents etc.  

  
**cloneType**|  xsd:string|  Image management asset clone type.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"FULL_CLONE"| Image management asset to be used in full clone automated desktop.  
"INSTANT_CLONE"| Image management asset to be used in instant clone desktop/farm.  

  
**imageType**|  xsd:string|  Image management asset image type.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"RDSH_APP"| Image management asset to be used for farm creation which is be used in application.  
"RDSH_DESKTOP"| Image management asset is for farm creation to be created.  
"VDI_DESKTOP"| Image management asset is available for desktops/farms to be created.  

  
**vmTemplateMoid**|  xsd:string|  MOID of virtual machine template.   


[^1]
[^2]

  
**vmTemplateId**| [VmTemplateId](vdi.entity.VmTemplateId.md)|  Virtual Machine Template ID.   


[^1]
[^2]

  
**vmMoid**|  xsd:string|  MOID of virtual machine. Must be set if [vmTemplateMoid](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetBase.md#vmTemplateMoid) is unset.   


[^1]
[^2]

  
**vmId**| [BaseImageVmId](vdi.entity.BaseImageVmId.md)|  Virtual Machine ID.   


[^1]
[^2]

  
**vmSnapshotMoid**|  xsd:string|  MOID of virtual machine snapshot. Must be set if [vmTemplateMoid](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetBase.md#vmTemplateMoid) is unset and [vmMoid](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetBase.md#vmMoid) is set.   


[^1]
[^2]

  
**vmSnapshotId**| [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md)|  Virtual Machine Snapshot ID.   


[^1]
[^2]

  
**imageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  Image management stream to which this asset belongs to.   


[^2]

  
**imageManagementVersion**| [ImageManagementVersionId](vdi.entity.ImageManagementVersionId.md)|  Image management version to which this asset belongs to.   


[^2]

  
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  Virtual Center where this asset is created in.   


[^2]

  
**datacenter**| [DatacenterId](vdi.entity.DatacenterId.md)|  Datacenter where this asset is created in.   


[^2]

  
**additionalDetails**| [MapEntry[]](vdi.util.MapEntry.md)|  Additional details about image management asset.   


[^1]

  
  

  

