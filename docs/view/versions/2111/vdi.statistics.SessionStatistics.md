---
layout: page
title: Service - SessionStatistics
hide:
#- navigation
- toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.statistics.SessionStatistics`

See also
> [LocalSessionStatistics](vdi.statistics.SessionStatistics.LocalSessionStatistics.md)

Since
> Horizon 7.7





## Service Description

Sessions Statistics.

**Methods**

Methods defined in this Service:
SessionStatistics_GetLocalSessionStatistics




Get a local sessions Statistics.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [SessionStatistics](vdi.statistics.SessionStatistics.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[LocalSessionStatistics](vdi.statistics.SessionStatistics.LocalSessionStatistics.md)| local sessions Statistics.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
