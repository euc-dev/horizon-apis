---
layout: page
title: Data Object - MachineStateCounts
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Machine.MachineStateCounts`

Returned by
> [Machine_GetStateCounts](vdi.resources.Machine.md#getMachineStateCounts)

See also
> [StateCount](vdi.resources.Machine.StateCount.md)

Since
> Horizon 8.4


## Data Object Description

State counts of vCenter VMs and unmanaged machines.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**vCenterVmCounts**| [StateCount](vdi.resources.Machine.StateCount.md)|  Machine state count for vCenter managed VMs.
**unManagedMachineCounts**| [StateCount](vdi.resources.Machine.StateCount.md)|  Machine state count for unmanaged VMs.


 
