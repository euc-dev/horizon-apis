---
layout: page
title: Data Object - ImageManagementAssetSpec
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetSpec`

Parameter to
> [ImageManagementAsset_CreateAssets](vdi.utils.imagemanagement.ImageManagementAsset.md#createAssets)

See also
> [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md), [ImageManagementVersionId](vdi.entity.ImageManagementVersionId.md), [MapEntry](vdi.util.MapEntry.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon 7.10


## Data Object Description

Data required for creating an Image Management Asset.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**status**|  xsd:string|  Image management asset status. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>AVAILABLE</td><td>Image management asset is available for pools/farms to be created.</td></tr><tr><td>DELETED</td><td>Image management asset has been deleted.</td></tr><tr><td>DEPLOYING_VM</td><td>Image management asset is deploying VM on the virtual center.</td></tr><tr><td>DEPLOYMENT_DONE</td><td>Image management asset VM deployed on the virtual center.</td></tr><tr><td>DISABLED</td><td>Image management asset has been disabled and no further pool/farm operation can be done using the same.</td></tr><tr><td>FAILED</td><td>Image management asset creation has failed.</td></tr><tr><td>REPLICATING</td><td>Copying the specialized images across all virtual centers.</td></tr><tr><td>RETRY_PENDING</td><td>When image management asset creation has failed, retry action is pending for asset to be created.</td></tr><tr><td>SPECIALIZING_VM</td><td>Image management asset is being published and specialized internally like installing agents etc.</td></tr></table>
**cloneType**|  xsd:string|  Image management asset clone type. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>FULL_CLONE</td><td>Image management asset to be used in full clone automated desktop.</td></tr><tr><td>INSTANT_CLONE</td><td>Image management asset to be used in instant clone desktop/farm.</td></tr></table>
**imageType**|  xsd:string|  Image management asset image type. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>RDSH_APP</td><td>Image management asset to be used for farm creation which is be used in application.</td></tr><tr><td>RDSH_DESKTOP</td><td>Image management asset is for farm creation to be created.</td></tr><tr><td>VDI_DESKTOP</td><td>Image management asset is available for desktops/farms to be created.</td></tr></table>
**vmTemplateMoid**|  xsd:string|  MOID of virtual machine template. [^1] [^2]
**vmMoid**|  xsd:string|  MOID of virtual machine. Must be set if [vmTemplateMoid](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetSpec.md#vmTemplateMoid) is unset. [^1] [^2]
**vmSnapshotMoid**|  xsd:string|  MOID of virtual machine snapshot. Must be set if [vmTemplateMoid](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetSpec.md#vmTemplateMoid) is unset and [vmMoid](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetSpec.md#vmMoid) is set. [^1] [^2]
**imageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  Image management stream to which this asset belongs to. [^2]
**imageManagementVersion**| [ImageManagementVersionId](vdi.entity.ImageManagementVersionId.md)|  Image management version to which this asset belongs to. [^2]
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  Virtual Center where this asset is created. [^2]
**additionalDetails**| [MapEntry[]](vdi.util.MapEntry.md)|  Additional details about image management asset. [^1]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.