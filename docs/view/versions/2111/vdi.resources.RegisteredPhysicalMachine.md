---
layout: page
title: Service - RegisteredPhysicalMachine
hide:
#  - navigation
  - toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.resources.RegisteredPhysicalMachine`

See also
> [MachineId](vdi.entity.MachineId.md), [RegisteredPhysicalMachineInfo](vdi.resources.RegisteredPhysicalMachine.RegisteredPhysicalMachineInfo.md), [RegisteredPhysicalMachineRegisterResult](vdi.resources.RegisteredPhysicalMachine.RegisterResult.md), [RegisteredPhysicalMachineRegisterSpec](vdi.resources.RegisteredPhysicalMachine.RegisterSpec.md)

Since
> Horizon View 6.0





## Service Description

Service Interface for RegisteredPhysicalMachine. A RegisteredPhysicalMachine is a registered unmanaged physical Machine that is unassigned to any desktop.

**Methods**

Methods defined in this Service:
RegisteredPhysicalMachine_Delete, RegisteredPhysicalMachine_Get, RegisteredPhysicalMachine_Register




Deletes the RegisteredPhysicalMachine for the specified machineId.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_MANAGEMENT|  This privilege is required to delete the RegisteredPhysicalMachine.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [RegisteredPhysicalMachine](vdi.resources.RegisteredPhysicalMachine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  The ID of the RegisteredPhysicalMachine to delete. MachineIds of this type must originate from the [RegisteredPhysicalMachine](vdi.resources.RegisteredPhysicalMachine.md) service.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_REGISTERED_PHYSICAL_MACHINE_DELETED|  The RegisteredPhysicalMachine was successfully deleted.
VLSI_REGISTERED_PHYSICAL_MACHINE_DELETE_FAILED|  The RegisteredPhysicalMachine could not be deleted.

Show WSDL type definition







Gets the RegisteredPhysicalMachineInfo object for the specified machineId.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  This privilege is required to get the RegisteredPhysicalMachineInfo.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [RegisteredPhysicalMachine](vdi.resources.RegisteredPhysicalMachine.md) used to make the method call.
**id**| [MachineId](vdi.entity.MachineId.md)|  The ID of the RegisteredPhysicalMachine to get. MachineIds of this type must originate from the [RegisteredPhysicalMachine](vdi.resources.RegisteredPhysicalMachine.md) service.




**Return Value**

Type | Description
:---|:---
[RegisteredPhysicalMachineInfo](vdi.resources.RegisteredPhysicalMachine.RegisteredPhysicalMachineInfo.md)| The RegisteredPhysicalMachine information.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Registers a machine.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_MACHINE_REGISTER|  Global machine registration privilege is required to register a machine.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [RegisteredPhysicalMachine](vdi.resources.RegisteredPhysicalMachine.md) used to make the method call.
**spec**| [RegisteredPhysicalMachineRegisterSpec](vdi.resources.RegisteredPhysicalMachine.RegisterSpec.md)|  The specification for the register operation.




**Return Value**

Type | Description
:---|:---
[RegisteredPhysicalMachineRegisterResult](vdi.resources.RegisteredPhysicalMachine.RegisterResult.md)| The registration result.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_MACHINE_REGISTERED|  If the machine is successfully registered.
VLSI_MACHINE_REGISTRATION_FAILED|  If the machine could not be registered.

Show WSDL type definition












 
