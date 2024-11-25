---
layout: page
title: Service - Cluster
hide:
#  - navigation
  - toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.Cluster`

See also
> [Cluster_KeyInfo](vdi.utils.Cluster.KeyInfo.md)

Since
> Horizon 7.11





## Service Description

The interface to provide cluster level properties.

**Methods**

Methods defined in this Service:
Cluster_GetPublicKey




Fetch the public key of cluster.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Cluster](vdi.utils.Cluster.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[Cluster_KeyInfo](vdi.utils.Cluster.KeyInfo.md)| Cluster's public key info.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
