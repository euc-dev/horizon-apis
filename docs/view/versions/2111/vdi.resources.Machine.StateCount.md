---
layout: page
title: Data Object - StateCount
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.resources.Machine.StateCount`

Property of
> [MachineStateCounts](vdi.resources.Machine.MachineStateCounts.md#field_detail)

See also
> [PreparedMachineCount](vdi.resources.Machine.PreparedMachineCount.md), [ProblemMachineCount](vdi.resources.Machine.ProblemMachineCount.md), [UnderConstructionMachineCount](vdi.resources.Machine.UnderConstructionMachineCount.md)

Since
> Horizon 8.4


## Data Object Description

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**problemCount**| [ProblemMachineCount](vdi.resources.Machine.ProblemMachineCount.md)|  Counts of the machines which are in problem state. [^2]
**underConstructionCount**| [UnderConstructionMachineCount](vdi.resources.Machine.UnderConstructionMachineCount.md)|  Counts of the machines which are in under construction state. [^2]
**preparedCount**| [PreparedMachineCount](vdi.resources.Machine.PreparedMachineCount.md)|  Counts of the machines which are in prepared state. [^2]


 


[^2]: This property cannot be updated.