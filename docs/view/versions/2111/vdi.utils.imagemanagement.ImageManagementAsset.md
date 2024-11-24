---
layout: page
title: Service - ImageManagementAsset
hide:
#- navigation
- toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.imagemanagement.ImageManagementAsset`

See also
> [ImageManagementAssetId](vdi.entity.ImageManagementAssetId.md), [ImageManagementAssetInfo](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetInfo.md), [ImageManagementAssetSpec](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetSpec.md), [ImageManagementTagId](vdi.entity.ImageManagementTagId.md), [ImageManagementVersionId](vdi.entity.ImageManagementVersionId.md), [MapEntry](vdi.util.MapEntry.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon 7.10





## Service Description

The service interface for managing Image Management Assets.

**Methods**

Methods defined in this Service:
ImageManagementAsset_CreateAssets, ImageManagementAsset_Delete, ImageManagementAsset_Get, ImageManagementAsset_GetByImageManagementTagAndVirtualCenter, ImageManagementAsset_ListByImageManagementVersion, ImageManagementAsset_Update




Adds multiple image management assets.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to create a image management asset.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ImageManagementAsset](vdi.utils.imagemanagement.ImageManagementAsset.md) used to make the method call.
**specs**| [ImageManagementAssetSpec[]](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetSpec.md)|  attributes needed to add multiple image management assets.




**Return Value**

Type | Description
:---|:---
[ImageManagementAssetId[]](vdi.entity.ImageManagementAssetId.md)| Array of entity ids of each image management asset.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if all operations were not successful, a PartialFailureFault will be thrown indicating which assets were successfully added and which ones failed. The index of results in the PartialFailureFault correspond to the index of the original asset in the specs. The result entry will contain either the original return type (on success) or an exception (on failure).
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_IM_ASSET_ADDED|  For every image management asset successfully created.
VLSI_IM_ASSET_ADD_FAILED|  For every image management asset that could not be created.

Show WSDL type definition







Delete an image management asset. Allowed only if the respective stream is not in use.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to delete a image management asset.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ImageManagementAsset](vdi.utils.imagemanagement.ImageManagementAsset.md) used to make the method call.
**id**| [ImageManagementAssetId](vdi.entity.ImageManagementAssetId.md)|  entity id of the image management asset entry.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityInUse](vdi.fault.EntityInUse.md)| Thrown if a desktop/farm is associated with this image management asset.
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_IM_ASSET_DELETED|  If the image management asset was successfully deleted.
VLSI_IM_ASSET_DELETE_FAILED|  If the image management asset could not be deleted.

Show WSDL type definition







Gets the image management asset information (primarily the list of attributes about configured image management asset).

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  Global configuration view is required to get a image management asset.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ImageManagementAsset](vdi.utils.imagemanagement.ImageManagementAsset.md) used to make the method call.
**id**| [ImageManagementAssetId](vdi.entity.ImageManagementAssetId.md)|  entity id of the image management asset entry.




**Return Value**

Type | Description
:---|:---
[ImageManagementAssetInfo](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetInfo.md)| ImageManagementAssetInfo (attributes about configured Image Management Asset).



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets the image management asset information (primarily the list of attributes about configured image management asset) associated with image management tag and virtual center.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  Global configuration view is required to get a image management asset.
VC_CONFIG_VIEW|  privilege is required to get a image management asset.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ImageManagementAsset](vdi.utils.imagemanagement.ImageManagementAsset.md) used to make the method call.
**imageManagementTag**| [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)|  entity id of the image management tag entry.
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  entity id of the virtual center entry.




**Return Value**

Type | Description
:---|:---
[ImageManagementAssetInfo](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetInfo.md)| ImageManagementAssetInfo (attributes about configured Image Management Asset).



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets list of image management assets for a given image management version.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  Global configuration view is required to list image management assets.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ImageManagementAsset](vdi.utils.imagemanagement.ImageManagementAsset.md) used to make the method call.
**imageManagementVersion**| [ImageManagementVersionId](vdi.entity.ImageManagementVersionId.md)|  entity id of the image management version.




**Return Value**

Type | Description
:---|:---
[ImageManagementAssetInfo[]](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetInfo.md)| list of image management assets



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Update image management asset with the set of attributes.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to update a image management asset.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ImageManagementAsset](vdi.utils.imagemanagement.ImageManagementAsset.md) used to make the method call.
**id**| [ImageManagementAssetId](vdi.entity.ImageManagementAssetId.md)|  entity id of the image management asset entry.
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  key value pairs describing attributes to be updated [^191]





**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_IM_ASSET_UPDATED|  If the image management asset was successfully updated.
VLSI_IM_ASSET_UPDATE_FAILED|  If the image management asset could not be updated.

Show WSDL type definition












 


[^191]: This parameter is an update map based on [ImageManagementAssetInfo](vdi.utils.imagemanagement.ImageManagementAsset.ImageManagementAssetInfo.md "ImageManagementAssetInfo").