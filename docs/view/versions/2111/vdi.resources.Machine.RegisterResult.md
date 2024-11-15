---
layout: page
title: Data Object - MachineRegisterResult
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.resources.Machine.RegisterResult`

Returned by
> [Machine_Register](vdi.resources.Machine.md#register)

See also
> [MachineId](vdi.entity.MachineId.md)

Since
> Horizon View 6.0


## Data Object Description

The result of registering a machine.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [MachineId](vdi.entity.MachineId.md)|  The ID of the newly registered machine. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.
**pairingToken**|  xsd:string|  The pairing token for the machine. This should be passed to the machine.


 
