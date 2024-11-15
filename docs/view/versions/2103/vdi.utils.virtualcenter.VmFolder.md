---
layout: page
title: Service - VmFolder
hide:
#- navigation
- toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.VmFolder`

See also
> [DatacenterId](vdi.entity.DatacenterId.md), [VmFolderInfo](vdi.utils.virtualcenter.VmFolder.VmFolderInfo.md)

Since
> Horizon View 6.0





## Service Description

The service for fetching Folders from VirtualCenter.

**Methods**

Methods defined in this Service:
VmFolder_GetVmFolderTree




Gets the root of the VmFolder tree from VC under the given datacenter. The VmFolder's may be suitable for desktop creation.
The datacenter id may be obtained from the Desktop's BaseImageVm, BaseImageSnapshot, or VmTemplate. Requires at least one of the listed privileges.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  privilege is required to get the VmFolderInfo.
VC_CONFIG_VIEW|  privilege is required to get the VmFolderInfo.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VmFolder](vdi.utils.virtualcenter.VmFolder.md) used to make the method call.
**datacenter**| [DatacenterId](vdi.entity.DatacenterId.md)|  datacenter to root the VmFolder tree




**Return Value**

Type | Description
:---|:---
[VmFolderInfo](vdi.utils.virtualcenter.VmFolder.VmFolderInfo.md)| VmFolderInfo the root of the tree from the given datacenter



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
