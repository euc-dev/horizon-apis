---
layout: page
title: Service - VirtualMachine
hide:
#  - navigation
  - toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.VirtualMachine`

See also
> [VirtualCenterId](vdi.entity.VirtualCenterId.md), [VirtualMachineInfo](vdi.utils.virtualcenter.VirtualMachine.VirtualMachineInfo.md)

Since
> Horizon View 6.0





## Service Description

The object for fetching VirtualMachines from VirtualCenter for manual desktop creation

**Methods**

Methods defined in this Service:
VirtualMachine_List




Gets a list of VMs from VC for manual managed desktop creation. Requires at least one of the listed privileges.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  privilege is required to get the list of VirtualMachineInfo.
VC_CONFIG_VIEW|  privilege is required to get the list of VirtualMachineInfo.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VirtualMachine](vdi.utils.virtualcenter.VirtualMachine.md) used to make the method call.
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  unique identifier for vc entry




**Return Value**

Type | Description
:---|:---
[VirtualMachineInfo[]](vdi.utils.virtualcenter.VirtualMachine.VirtualMachineInfo.md)| Array of VirtualMachineInfo



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
