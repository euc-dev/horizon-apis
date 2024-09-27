---
layout: page
title: Data Object - ImageManagementAssetSpec
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetSpec  
Parameter to
     [ImageManagementAsset_CreateAssets](vdi.utils.imagemanagement.ImageManagementAsset.md#createAssets)  
See also
     [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md), [ImageManagementVersionId](vdi.entity.ImageManagementVersionId.md), [MapEntry](vdi.util.MapEntry.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)  
Since 
    Horizon 7.10

## Data Object Description 

Data required for creating an Image Management Asset. 

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


 * This property need not be set.
 * This property cannot be updated.

  
**vmMoid**|  xsd:string|  MOID of virtual machine. Must be set if [vmTemplateMoid](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetSpec.md#vmTemplateMoid) is unset.   


 * This property need not be set.
 * This property cannot be updated.

  
**vmSnapshotMoid**|  xsd:string|  MOID of virtual machine snapshot. Must be set if [vmTemplateMoid](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetSpec.md#vmTemplateMoid) is unset and [vmMoid](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetSpec.md#vmMoid) is set.   


 * This property need not be set.
 * This property cannot be updated.

  
**imageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  Image management stream to which this asset belongs to.   


 * This property cannot be updated.

  
**imageManagementVersion**| [ImageManagementVersionId](vdi.entity.ImageManagementVersionId.md)|  Image management version to which this asset belongs to.   


 * This property cannot be updated.

  
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  Virtual Center where this asset is created.   


 * This property cannot be updated.

  
**additionalDetails**| [MapEntry[]](vdi.util.MapEntry.md)|  Additional details about image management asset.   


 * This property need not be set.

  
  

  

