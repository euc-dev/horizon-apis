---
layout: page
title: Service - ADDomain
hide:
#- navigation
- toc
---







Java Class
> `com.vmware.vdi.vlsi.binding.vdi.utils.ADDomain`

See also
> [ADDomainInfo](vdi.utils.ADDomain.ADDomainInfo.md)

Since
> Horizon View 6.0





## Service Description

Provides the ability to retrieve domain information for the View Cluster.

Methods

Methods defined in this Service
---
ADDomain_List




Lists the Active Directory domains.

Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ADDomain](vdi.utils.ADDomain.md) used to make the method call.



Return Value

Type |  Description
---|---
[ADDomainInfo[]](vdi.utils.ADDomain.ADDomainInfo.md)| A list of [ADDomainInfo](vdi.utils.ADDomain.ADDomainInfo.md) containing information about the domains.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
