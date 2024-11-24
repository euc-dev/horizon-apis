---
layout: page
title: Data Object - ImageManagementTagBase
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.imagemanagement.ImageManagementTag.ImageManagementTagBase`

Property of
> [ImageManagementTagInfo](vdi.utils.imagemanagement.ImageManagementTag.ImageManagementTagInfo.md#field_detail)

Parameter to
> [ImageManagementTag_CreateTags](vdi.utils.imagemanagement.ImageManagementTag.md#createTags)

See also
> [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md), [ImageManagementVersionId](vdi.entity.ImageManagementVersionId.md), [MapEntry](vdi.util.MapEntry.md)

Since
> Horizon 7.10


## Data Object Description

Basic data about an Image Management Tag.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**name**|  xsd:string|  The tag name used to identify this tag. It is unique among all the tags of a Stream. [^148]
**imageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  Entity id of image management stream to which this tag belongs. [^2]
**imageManagementVersion**| [ImageManagementVersionId](vdi.entity.ImageManagementVersionId.md)|  Entity id of image management version to which this tag is assigned.
**additionalDetails**| [MapEntry[]](vdi.util.MapEntry.md)|  Additional details about image management tag. [^1]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^148]: This property must contain only alphanumerics, underscores and dashes. The maximum length is 64 characters.