---
layout: page
title: Service - ImageManagementVersion
hide:
#- navigation
- toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.imagemanagement.ImageManagementVersion`

See also
> [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md), [ImageManagementVersionBase](vdi.utils.imagemanagement.ImageManagementVersion.ImageManagementVersionBase.md), [ImageManagementVersionId](vdi.entity.ImageManagementVersionId.md), [ImageManagementVersionInfo](vdi.utils.imagemanagement.ImageManagementVersion.ImageManagementVersionInfo.md), [MapEntry](vdi.util.MapEntry.md)

Since
> Horizon 7.10





## Service Description

The service interface for managing Versions related to Image Management.

**Methods**

Methods defined in this Service:
ImageManagementVersion_CreateVersions, ImageManagementVersion_Delete, ImageManagementVersion_Get, ImageManagementVersion_ListByImageManagementStream, ImageManagementVersion_Update




Adds multiple image management versions.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to create a image management version.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ImageManagementVersion](vdi.utils.imagemanagement.ImageManagementVersion.md) used to make the method call.
**bases**| [ImageManagementVersionBase[]](vdi.utils.imagemanagement.ImageManagementVersion.ImageManagementVersionBase.md)|  attributes needed to add multiple image management versions.




**Return Value**

Type | Description
:---|:---
[ImageManagementVersionId[]](vdi.entity.ImageManagementVersionId.md)| Array of entity ids of each image management version.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if all operations were not successful, a PartialFailureFault will be thrown indicating which versions were successfully added and which ones failed. The index of results in the PartialFailureFault correspond to the index of the original version. The result entry will contain either the original return type (on success) or an exception (on failure).
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_IM_VERSION_ADDED|  For every image management version successfully created.
VLSI_IM_VERSION_ADD_FAILED|  For every image management version that could not be created.

Show WSDL type definition







Delete an image management version.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to delete a image management version.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ImageManagementVersion](vdi.utils.imagemanagement.ImageManagementVersion.md) used to make the method call.
**id**| [ImageManagementVersionId](vdi.entity.ImageManagementVersionId.md)|  entity id for the image management version entry.




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
VLSI_IM_VERSION_DELETED|  If the image management version was successfully deleted.
VLSI_IM_VERSION_DELETE_FAILED|  If the image management version delete fails.

Show WSDL type definition







Gets the image management version information (primarily the list of attributes about configured image management version).

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  Global configuration view is required to get a image management version.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ImageManagementVersion](vdi.utils.imagemanagement.ImageManagementVersion.md) used to make the method call.
**id**| [ImageManagementVersionId](vdi.entity.ImageManagementVersionId.md)|  entity id for the image management version entry.




**Return Value**

Type | Description
:---|:---
[ImageManagementVersionInfo](vdi.utils.imagemanagement.ImageManagementVersion.ImageManagementVersionInfo.md)| ImageManagementVersionInfo (attributes about configured Image Management Version).



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets list of image management version for a given Image Management Stream.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  Global configuration view is required to list image management versions.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ImageManagementVersion](vdi.utils.imagemanagement.ImageManagementVersion.md) used to make the method call.
**imageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|




**Return Value**

Type | Description
:---|:---
[ImageManagementVersionInfo[]](vdi.utils.imagemanagement.ImageManagementVersion.ImageManagementVersionInfo.md)| list of image management versions



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Update image management version with the set of attributes.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to update a image management version.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ImageManagementVersion](vdi.utils.imagemanagement.ImageManagementVersion.md) used to make the method call.
**id**| [ImageManagementVersionId](vdi.entity.ImageManagementVersionId.md)|  entity id for the image management version entry.
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  key value pairs describing attributes to be updated [^151]





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
VLSI_IM_VERSION_UPDATED|  If the image management version was successfully updated.
VLSI_IM_VERSION_UPDATE_FAILED|  If the image management version update fails.

Show WSDL type definition












 


[^151]: This parameter is an update map based on [ImageManagementVersionInfo](vdi.utils.imagemanagement.ImageManagementVersion.ImageManagementVersionInfo.md "ImageManagementVersionInfo").