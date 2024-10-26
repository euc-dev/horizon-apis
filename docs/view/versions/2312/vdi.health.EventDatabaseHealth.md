---
layout: page
title: Service - EventDatabaseHealth
hide:
#- navigation
- toc
---







Java Class
> `com.vmware.vdi.vlsi.binding.vdi.health.EventDatabaseHealth`

See also
> [EventDatabaseHealthInfo](vdi.health.EventDatabaseHealth.EventDatabaseHealthInfo.md)

Since
> Horizon View 6.0





## Service Description

Service for retrieving health information on the event database.

Methods

Methods defined in this Service
---
EventDatabaseHealth_Get




Gets the health of the event database connection.

Parameters

Name| Type| Description
---|---|---
 **_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [EventDatabaseHealth](vdi.health.EventDatabaseHealth.md) used to make the method call.
**skipEventStatistics**|  xsd:boolean|  Indicates whether EventStatistics needs to be loaded or not. Default is false. [^135]





Return Value

Type |  Description
---|---
[EventDatabaseHealthInfo](vdi.health.EventDatabaseHealth.EventDatabaseHealthInfo.md)| The health of the event database connection.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
