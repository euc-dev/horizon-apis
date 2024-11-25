---
layout: page
title: Data Object - ImageManagementVersionInfo
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.imagemanagement.ImageManagementVersion.ImageManagementVersionInfo`

Returned by
> [ImageManagementVersion_Get](vdi.utils.imagemanagement.ImageManagementVersion.md#get), [ImageManagementVersion_ListByImageManagementStream](vdi.utils.imagemanagement.ImageManagementVersion.md#listByImageManagementStream)

See also
> [ImageManagementVersionBase](vdi.utils.imagemanagement.ImageManagementVersion.ImageManagementVersionBase.md), [ImageManagementVersionId](vdi.entity.ImageManagementVersionId.md)

Since
> Horizon 7.10


## Data Object Description

Top level object describing a image management version.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [ImageManagementVersionId](vdi.entity.ImageManagementVersionId.md)|  Entity id image management version. [^2]
**base**| [ImageManagementVersionBase](vdi.utils.imagemanagement.ImageManagementVersion.ImageManagementVersionBase.md)|  Basic data about a image management version.
**refId**|  xsd:string|  Reference ID used for this image management version.  **_Since_** Horizon 8.1 [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.