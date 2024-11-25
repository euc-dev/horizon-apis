---
layout: page
title: Service - VirtualCenterHealth
hide:
#  - navigation
  - toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.VirtualCenterHealth`

See also
> [VirtualCenterHealthInfo](vdi.health.VirtualCenterHealth.VirtualCenterHealthInfo.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon View 6.0





## Service Description

Service for retrieving health information on Virtual Center servers.

**Methods**

Methods defined in this Service:
VirtualCenterHealth_Get, VirtualCenterHealth_List




Gets the Virtual Center health for a specified Virtual Center server.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  Global configuration (read-only) privilege is required to get information on virtual center health.
VC_CONFIG_VIEW|  privilege required to get information on virtual center health.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VirtualCenterHealth](vdi.health.VirtualCenterHealth.md) used to make the method call.
**id**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  The ID of the Virtual Center server.




**Return Value**

Type | Description
:---|:---
[VirtualCenterHealthInfo](vdi.health.VirtualCenterHealth.VirtualCenterHealthInfo.md)| Health information on the specified server.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets the Virtual Center health for all Virtual Center servers.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  Global configuration (read-only) privilege is required to get information on virtual center health.
VC_CONFIG_VIEW|  privilege required to get information on virtual center health.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VirtualCenterHealth](vdi.health.VirtualCenterHealth.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[VirtualCenterHealthInfo[]](vdi.health.VirtualCenterHealth.VirtualCenterHealthInfo.md)| A list of health information on all Virtual Center servers.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
