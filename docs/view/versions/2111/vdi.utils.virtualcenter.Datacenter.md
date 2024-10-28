---
layout: page
title: Service - Datacenter
hide:
#- navigation
- toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.Datacenter`

See also
> [DatacenterInfo](vdi.utils.virtualcenter.Datacenter.DatacenterInfo.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon 7.8





## Service Description

Service for fetching Datacenters from VirtualCenter.

Methods

Methods defined in this Service
---
Datacenter_List




Lists all the datacenters of a vCenter. Requires at least one of the listed privileges.

Privileges

Privilege |  Description
---|---
VC_CONFIG_VIEW|  privilege is required to list datacenters of the vCenter.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Datacenter](vdi.utils.virtualcenter.Datacenter.md) used to make the method call.
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|




Return Value

Type |  Description
---|---
[DatacenterInfo[]](vdi.utils.virtualcenter.Datacenter.DatacenterInfo.md)| The DatacenterInfo list



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
