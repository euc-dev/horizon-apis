---
layout: page
title: Data Object - UnderConstructionMachineCount
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Machine.UnderConstructionMachineCount`

Property of
> [StateCount](vdi.resources.Machine.StateCount.md#field_detail)

Since
> Horizon 8.4


## Data Object Description

Number of the machines which are in under construction state. Such machine's [basicState](vdi.resources.Machine.MachineBase.md#basicState) is one of the following : PROVISIONING,CUSTOMIZING,MAINTENANCE,DELETING,WAIT_FOR_AGENT,AGENT_ERR_STARTUP_IN_PROGRESS, VALIDATING

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**provisioning**|  xsd:int|  Number of machines which are in PROVISIONING [basicState](vdi.resources.Machine.MachineBase.md#basicState). Applicable for VC managed virtual machines. [^2]
**customizing**|  xsd:int|  Number of machines which are in CUSTOMIZING [basicState](vdi.resources.Machine.MachineBase.md#basicState). Applicable only for VC managed virtual machines. [^2]
**maintenance**|  xsd:int|  Number of machines which are in MAINTENANCE [basicState](vdi.resources.Machine.MachineBase.md#basicState). Applicable only for VC managed virtual machines. [^2]
**deleting**|  xsd:int|  Number of machines which are in DELETING [basicState](vdi.resources.Machine.MachineBase.md#basicState). Applicable only for VC managed virtual machines. [^2]
**waitForAgent**|  xsd:int|  Number of machines which are in WAIT_FOR_AGENT [basicState](vdi.resources.Machine.MachineBase.md#basicState). Applicable only for VC managed virtual machines. [^2]
**startupProgress**|  xsd:int|  Number of machines which are in AGENT_ERR_STARTUP_IN_PROGRESS [basicState](vdi.resources.Machine.MachineBase.md#basicState). [^2]
**validating**|  xsd:int|  Number of machines which are in VALIDATING [basicState](vdi.resources.Machine.MachineBase.md#basicState). Applicable only for unmanaged machines. [^2]
 


 


[^2]: This property cannot be updated.