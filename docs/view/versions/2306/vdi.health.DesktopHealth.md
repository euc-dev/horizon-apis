---
layout: page
title: Service - DesktopHealth
hide:
#- navigation
- toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.DesktopHealth`

See also
> [DesktopHealthInfo](vdi.health.DesktopHealth.DesktopHealthInfo.md), [DesktopId](vdi.entity.DesktopId.md)

Since
> Horizon 7.9





## Service Description

Service that represents Desktop health status

Methods

Methods defined in this Service
---
DesktopHealth_Get




Get health and status details for the specified Desktop.

Privileges

Privilege |  Description
---|---
POOL_VIEW|  privilege is required to get desktop health information



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [DesktopHealth](vdi.health.DesktopHealth.md) used to make the method call.
**id**| [DesktopId](vdi.entity.DesktopId.md)|  The entityId of the Desktop whose health and status is being queried




Return Value

Type |  Description
---|---
[DesktopHealthInfo](vdi.health.DesktopHealth.DesktopHealthInfo.md)| The health and status details



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
