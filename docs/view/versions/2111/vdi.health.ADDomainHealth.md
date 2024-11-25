---
layout: page
title: Service - ADDomainHealth
hide:
#  - navigation
  - toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.health.ADDomainHealth`

See also
> [ADDomainHealthInfo](vdi.health.ADDomainHealth.ADDomainHealthInfo.md)

Since
> Horizon View 6.0





## Service Description

Service for retrieving health information on domains.

**Methods**

Methods defined in this Service:
ADDomainHealth_List




Gets the health information for all domains.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ADDomainHealth](vdi.health.ADDomainHealth.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[ADDomainHealthInfo[]](vdi.health.ADDomainHealth.ADDomainHealthInfo.md)| An array of [ADDomainHealthInfo](vdi.health.ADDomainHealth.ADDomainHealthInfo.md) objects indicating the health of each domain.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
