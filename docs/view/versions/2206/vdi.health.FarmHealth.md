---
layout: page
title: Service - FarmHealth
hide:
#- navigation
- toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.FarmHealth`

See also
> [FarmHealthInfo](vdi.health.FarmHealth.FarmHealthInfo.md), [FarmId](vdi.entity.FarmId.md)

Since
> Horizon View 6.0





## Service Description

Service that represents Farm health status

Methods

Methods defined in this Service
---
FarmHealth_Get




Get health and status details for the specified Farm.

Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [FarmHealth](vdi.health.FarmHealth.md) used to make the method call.
**id**| [FarmId](vdi.entity.FarmId.md)|  The entityId of the Farm whose health and status is being queried




Return Value

Type |  Description
---|---
[FarmHealthInfo](vdi.health.FarmHealth.FarmHealthInfo.md)| The health and status details



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
