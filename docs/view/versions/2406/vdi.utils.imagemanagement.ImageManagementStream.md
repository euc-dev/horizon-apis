---
layout: page
title: Service - ImageManagementStream
hide:
#- navigation
- toc
---







Java Class
> `com.vmware.vdi.vlsi.binding.vdi.utils.imagemanagement.ImageManagementStream`

See also
> [ImageManagementStreamBase](vdi.utils.imagemanagement.ImageManagementStream.ImageManagementStreamBase.md), [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md), [ImageManagementStreamInfo](vdi.utils.imagemanagement.ImageManagementStream.ImageManagementStreamInfo.md), [ImageManagementStreamQuerySpec](vdi.utils.imagemanagement.ImageManagementStream.ImageManagementStreamQuerySpec.md), [MapEntry](vdi.util.MapEntry.md)

Since
> Horizon 7.10





## Service Description

The service interface for managing Image Management Streams.

Methods

Methods defined in this Service
---
ImageManagementStream_CreateStreams, ImageManagementStream_Delete, ImageManagementStream_Get, ImageManagementStream_ListBySpec, ImageManagementStream_Update




Adds multiple image management streams.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to create a image management stream.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ImageManagementStream](vdi.utils.imagemanagement.ImageManagementStream.md) used to make the method call.
**bases**| [ImageManagementStreamBase[]](vdi.utils.imagemanagement.ImageManagementStream.ImageManagementStreamBase.md)|  attributes needed to add multiple image management streams.




Return Value

Type |  Description
---|---
[ImageManagementStreamId[]](vdi.entity.ImageManagementStreamId.md)| Array of entity ids of each image management stream.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if all operations were not successful, a PartialFailureFault will be thrown indicating which streams were successfully added and which ones failed. The index of results in the PartialFailureFault correspond to the index of the original stream. The result entry will contain either the original return type (on success) or an exception (on failure).
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_IM_STREAM_ADDED|  For every image management stream successfully created.
VLSI_IM_STREAM_ADD_FAILED|  For every image management stream that could not be created.

Show WSDL type definition







Delete an image management stream. Allowed only if the Stream is not in use.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to delete a image management stream.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ImageManagementStream](vdi.utils.imagemanagement.ImageManagementStream.md) used to make the method call.
**id**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  entity id of the image management stream entry.




Return Value

Type |  Description
---|---
None



Faults

Type |  Description
---|---
[EntityInUse](vdi.fault.EntityInUse.md)| Thrown if a desktop/farm is associated with this image management stream.
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_IM_STREAM_DELETED|  If the image management stream was successfully deleted.
VLSI_IM_STREAM_DELETE_FAILED|  If the image management stream delete fails.

Show WSDL type definition







Gets the image management stream information (primarily the list of attributes about configured image management stream). Requires at least one of the listed privileges.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_VIEW|  Global configuration view is required to get a image management stream.
VC_CONFIG_VIEW|  privilege is required to get a image management stream.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ImageManagementStream](vdi.utils.imagemanagement.ImageManagementStream.md) used to make the method call.
**id**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  entity id of the image management stream entry.




Return Value

Type |  Description
---|---
[ImageManagementStreamInfo](vdi.utils.imagemanagement.ImageManagementStream.ImageManagementStreamInfo.md)| ImageManagementStreamInfo (attributes about configured Image Management Stream).



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Returns list of image management streams based on the spec. Requires at least one of the listed privileges.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_VIEW|  Global configuration view is required to list image management streams.
VC_CONFIG_VIEW|  privilege is required to list image management streams.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ImageManagementStream](vdi.utils.imagemanagement.ImageManagementStream.md) used to make the method call.
**spec**| [ImageManagementStreamQuerySpec](vdi.utils.imagemanagement.ImageManagementStream.ImageManagementStreamQuerySpec.md)|  query spec for filtering image management stream.




Return Value

Type |  Description
---|---
[ImageManagementStreamInfo[]](vdi.utils.imagemanagement.ImageManagementStream.ImageManagementStreamInfo.md)| list of image management streams.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Update image management stream with the set of attributes.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to update a image management stream.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ImageManagementStream](vdi.utils.imagemanagement.ImageManagementStream.md) used to make the method call.
**id**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  entity id of the image management stream entry.
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  key value pairs describing attributes to be updated [^147]





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
VLSI_IM_STREAM_UPDATED|  If the image management stream was successfully updated.
VLSI_IM_STREAM_UPDATE_FAILED|  If the image management stream update fails.

Show WSDL type definition












 


[^147]: This parameter is an update map based on [ImageManagementStreamInfo](vdi.utils.imagemanagement.ImageManagementStream.ImageManagementStreamInfo.md "ImageManagementStreamInfo").