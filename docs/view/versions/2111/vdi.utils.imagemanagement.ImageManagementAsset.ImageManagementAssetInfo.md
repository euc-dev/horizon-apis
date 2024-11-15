---
layout: page
title: Data Object - ImageManagementAssetInfo
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetInfo`

Returned by
> [ImageManagementAsset_Get](vdi.utils.imagemanagement.ImageManagementAsset.md#get), [ImageManagementAsset_GetByImageManagementTagAndVirtualCenter](vdi.utils.imagemanagement.ImageManagementAsset.md#getByImageManagementTagAndVirtualCenter), [ImageManagementAsset_ListByImageManagementVersion](vdi.utils.imagemanagement.ImageManagementAsset.md#listByImageManagementVersion)

See also
> [ImageManagementAssetBase](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetBase.md), [ImageManagementAssetId](vdi.entity.ImageManagementAssetId.md)

Since
> Horizon 7.10


## Data Object Description

Top level object describing a image management asset.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [ImageManagementAssetId](vdi.entity.ImageManagementAssetId.md)|  Entity id of image management asset. [^2]
**base**| [ImageManagementAssetBase](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetBase.md)|  Basic data about a image management asset.
**refId**|  xsd:string|  Reference ID used for this image management asset.  **_Since_** Horizon 8.1 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.