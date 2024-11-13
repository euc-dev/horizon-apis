---
layout: page
title: Service - ViewComposerHealth
hide:
#- navigation
- toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.ViewComposerHealth`

See also
> [ViewComposerHealthInfo](vdi.health.ViewComposerHealth.ViewComposerHealthInfo.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon View 6.0





## Service Description

Service for retrieving health information on View Composer servers.

Methods

Methods defined in this Service
---
ViewComposerHealth_Get, ViewComposerHealth_List




Gets the health of the View Composer server associated with the specified Virtual Center server.

Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ViewComposerHealth](vdi.health.ViewComposerHealth.md) used to make the method call.
**id**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  The ID of the associated Virtual Center server.




Return Value

Type |  Description
---|---
[ViewComposerHealthInfo](vdi.health.ViewComposerHealth.ViewComposerHealthInfo.md)| The health of the View Composer server.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets the health of all View Composer servers associated with this View cluster.

Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ViewComposerHealth](vdi.health.ViewComposerHealth.md) used to make the method call.



Return Value

Type |  Description
---|---
[ViewComposerHealthInfo[]](vdi.health.ViewComposerHealth.ViewComposerHealthInfo.md)| The health of all View Composer servers.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
