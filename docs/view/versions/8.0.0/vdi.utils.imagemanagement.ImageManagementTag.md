---
layout: page
title: Service - ImageManagementTag
hide:
#- navigation
- toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.imagemanagement.ImageManagementTag`

See also
> [ImageManagementTagBase](vdi.utils.imagemanagement.ImageManagementTag.ImageManagementTagBase.md), [ImageManagementTagId](vdi.entity.ImageManagementTagId.md), [ImageManagementTagInfo](vdi.utils.imagemanagement.ImageManagementTag.ImageManagementTagInfo.md), [ImageManagementTagQuerySpec](vdi.utils.imagemanagement.ImageManagementTag.ImageManagementTagQuerySpec.md), [MapEntry](vdi.util.MapEntry.md)

Since
> Horizon 7.10





## Service Description

The service interface for managing Image Management Tags.

Methods

Methods defined in this Service
---
ImageManagementTag_CreateTags, ImageManagementTag_Delete, ImageManagementTag_Get, ImageManagementTag_ListBySpec, ImageManagementTag_Update




Adds multiple image management tags.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to create a image management tag.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ImageManagementTag](vdi.utils.imagemanagement.ImageManagementTag.md) used to make the method call.
**bases**| [ImageManagementTagBase[]](vdi.utils.imagemanagement.ImageManagementTag.ImageManagementTagBase.md)|  attributes needed to add multiple image management tags.




Return Value

Type |  Description
---|---
[ImageManagementTagId[]](vdi.entity.ImageManagementTagId.md)| Array of entity ids of each image management tag.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if all operations were not successful, a PartialFailureFault will be thrown indicating which tags were successfully added and which ones failed. The index of results in the PartialFailureFault correspond to the index of the original tag. The result entry will contain either the original return type (on success) or an exception (on failure).
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_IM_TAG_ADDED|  For every image management tag successfully created.
VLSI_IM_TAG_ADD_FAILED|  For every image management tag that could not be created.

Show WSDL type definition







Delete an image management tag. Allowed only if the Tag is not in use.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to delete a image management tag.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ImageManagementTag](vdi.utils.imagemanagement.ImageManagementTag.md) used to make the method call.
**id**| [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)|  entity id of the image management tag entry.




Return Value

Type |  Description
---|---
None



Faults

Type |  Description
---|---
[EntityInUse](vdi.fault.EntityInUse.md)| Thrown if a desktop/farm is associated with this image management tag.
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_IM_TAG_DELETED|  If the image management tag was successfully deleted.
VLSI_IM_TAG_DELETE_FAILED|  If the image management tag delete fails.

Show WSDL type definition







Gets the image management tag information (primarily the list of attributes about configured image management tag). Requires at least one of the listed privileges.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_VIEW|  Global configuration view is required to get a image management tag.
VC_CONFIG_VIEW|  privilege is required to get a image management tag.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ImageManagementTag](vdi.utils.imagemanagement.ImageManagementTag.md) used to make the method call.
**id**| [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)|  entity id of the image management tag entry.




Return Value

Type |  Description
---|---
[ImageManagementTagInfo](vdi.utils.imagemanagement.ImageManagementTag.ImageManagementTagInfo.md)| ImageManagementTagInfo (attributes about configured Image Management Tag).



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets list of only those image management tags of a given image management stream, whose version is in AVAILABLE or PARTIALLY_AVAILABLE state and asset of the given virtual center is in AVAILABLE status and has asset for given provisioning type. Requires at least one of the listed privileges.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_VIEW|  Global configuration view is required to list image management tags.
VC_CONFIG_VIEW|  privilege is required to list image management tags.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ImageManagementTag](vdi.utils.imagemanagement.ImageManagementTag.md) used to make the method call.
**spec**| [ImageManagementTagQuerySpec](vdi.utils.imagemanagement.ImageManagementTag.ImageManagementTagQuerySpec.md)|




Return Value

Type |  Description
---|---
[ImageManagementTagInfo[]](vdi.utils.imagemanagement.ImageManagementTag.ImageManagementTagInfo.md)| list of image management tags



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Update image management tag with the set of attributes.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to update a image management tag.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ImageManagementTag](vdi.utils.imagemanagement.ImageManagementTag.md) used to make the method call.
**id**| [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)|  entity id of the image management tag entry.
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  key value pairs describing attributes to be updated [^149]





Return Value

Type |  Description
---|---
None



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_IM_TAG_UPDATED|  If the image management tag was successfully updated.
VLSI_IM_TAG_UPDATE_FAILED|  If the image management tag update fails.

Show WSDL type definition












 


[^149]: This parameter is an update map based on [ImageManagementTagInfo](vdi.utils.imagemanagement.ImageManagementTag.ImageManagementTagInfo.md "ImageManagementTagInfo").