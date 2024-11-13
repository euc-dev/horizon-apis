---
layout: page
title: Service - AuditEvent
hide:
#- navigation
- toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.infrastructure.AuditEvent`

See also
> [AuditEventDetailsRecord](vdi.infrastructure.AuditEvent.AuditEventDetailsRecord.md)

Since
> Horizon 7.13





## Service Description

Methods

Methods defined in this Service
---
AuditEventDetails




Audit Event Details for input event ids.

Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [AuditEvent](vdi.infrastructure.AuditEvent.md) used to make the method call.
**eventsId**|  xsd:int[]|  Array of event ids.




Return Value

Type |  Description
---|---
[AuditEventDetailsRecord[]](vdi.infrastructure.AuditEvent.AuditEventDetailsRecord.md)|



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
