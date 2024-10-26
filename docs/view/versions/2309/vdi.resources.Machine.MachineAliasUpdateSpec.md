---
layout: page
title: Data Object - MachineAliasUpdateSpec
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Machine.MachineAliasUpdateSpec`

Parameter to
> [Machine_UpdateMachineAliases](vdi.resources.Machine.md#updateMachineAliases)

See also
> [MachineAlias](vdi.resources.Machine.MachineAlias.md), [MachineId](vdi.entity.MachineId.md)

Since
> Horizon 7.13


## Data Object Description

The specification for updating machine aliases of assigned users.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [MachineId](vdi.entity.MachineId.md)|  Unique identifier of the machine for which machine aliases needs to be updated. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service.
**aliases**| [MachineAlias[]](vdi.resources.Machine.MachineAlias.md)|  Machine aliases of assigned users of the given machine that needs to be updated. If the machine alias for a user needs to be removed, set the [alias](vdi.resources.Machine.MachineAlias.md#alias) field to null.
 


 
