---
layout: page
title: Data Object - MachineInfo
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Machine.MachineInfo`

Returned by
> [Machine_Get](vdi.resources.Machine.md#get), [Machine_GetInfos](vdi.resources.Machine.md#getInfos)

See also
> [MachineAgentPairingData](vdi.resources.Machine.MachineAgentPairingData.md), [MachineBase](vdi.resources.Machine.MachineBase.md), [MachineId](vdi.entity.MachineId.md), [MachineManagedMachineData](vdi.resources.Machine.ManagedMachineData.md), [MachineMessageSecurityData](vdi.resources.Machine.MessageSecurityData.md)

Since
> Horizon View 6.0


## Data Object Description

This class gives the description of a Machine instance.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [MachineId](vdi.entity.MachineId.md)|  The id of the Machine. [^2]
**base**| [MachineBase](vdi.resources.Machine.MachineBase.md)|  Container for all other summary fields common to all the types of Machines.
**messageSecurityData**| [MachineMessageSecurityData](vdi.resources.Machine.MessageSecurityData.md)|  Message security data for this machine.  **_Since_** Horizon View 6.1 [^2]
**managedMachineData**| [MachineManagedMachineData](vdi.resources.Machine.ManagedMachineData.md)|  Information applicable only to Managed Machines. [^1]
**machineAgentPairingData**| [MachineAgentPairingData](vdi.resources.Machine.MachineAgentPairingData.md)|  Agent pairing data for this Machine.  **_Since_** Horizon 7.5 [^1]


 
