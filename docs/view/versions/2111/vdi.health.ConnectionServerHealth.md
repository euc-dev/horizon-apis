---
layout: page
title: Service - ConnectionServerHealth
hide:
#  - navigation
  - toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.health.ConnectionServerHealth`

See also
> [ConnectionServerHealthInfo](vdi.health.ConnectionServerHealth.ConnectionServerHealthInfo.md), [ConnectionServerId](vdi.entity.ConnectionServerId.md)

Since
> Horizon View 6.0





## Service Description

Service for retrieving health information on connection servers.

**Methods**

Methods defined in this Service:
ConnectionServerHealth_Get, ConnectionServerHealth_List




Gets the health information for an individual connection server.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ConnectionServerHealth](vdi.health.ConnectionServerHealth.md) used to make the method call.
**id**| [ConnectionServerId](vdi.entity.ConnectionServerId.md)|  The ID of the connection server.




**Return Value**

Type | Description
:---|:---
[ConnectionServerHealthInfo](vdi.health.ConnectionServerHealth.ConnectionServerHealthInfo.md)| The health information for an individual connection server.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets the health information for all connection servers.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ConnectionServerHealth](vdi.health.ConnectionServerHealth.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[ConnectionServerHealthInfo[]](vdi.health.ConnectionServerHealth.ConnectionServerHealthInfo.md)| The health information for all connection servers.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
