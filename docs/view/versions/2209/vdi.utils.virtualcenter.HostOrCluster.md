---
layout: page
title: Service - HostOrCluster
hide:
#  - navigation
  - toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.HostOrCluster`

See also
> [DatacenterId](vdi.entity.DatacenterId.md), [HostOrClusterTreeNode](vdi.utils.virtualcenter.HostOrCluster.HostOrClusterTreeNode.md)

Since
> Horizon View 6.0





## Service Description

The HostOrCluster service.

**Methods**

Methods defined in this Service:
HostOrCluster_GetHostOrClusterTree




Gets the HostOrClusterTree from VC for use in selecting the host or cluster for full or linked clone desktop creation. The returned root folder of the tree represents the top level datacenter which may contain hosts, clusters, or further nested containers. Requires at least one of the listed privileges.

The datacenter id may be obtained from the Desktop's BaseImageVm, BaseImageSnapshot, or VmTemplate.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  privilege is required to get the HostOrClusterTree root.
VC_CONFIG_VIEW|  privilege is required to get the HostOrClusterTree root.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [HostOrCluster](vdi.utils.virtualcenter.HostOrCluster.md) used to make the method call.
**datacenter**| [DatacenterId](vdi.entity.DatacenterId.md)|  datacenter id at the root of the tree




**Return Value**

Type | Description
:---|:---
[HostOrClusterTreeNode](vdi.utils.virtualcenter.HostOrCluster.HostOrClusterTreeNode.md)| folder tree root node representing the datacenter that stores the VM template



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
