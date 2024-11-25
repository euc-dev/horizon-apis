---
layout: page
title: Data Object - PreparedMachineCount
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.resources.Machine.PreparedMachineCount`

Property of
> [StateCount](vdi.resources.Machine.StateCount.md#field_detail)

Since
> Horizon 8.4


## Data Object Description

Number of the machines which are in prepared state. Such machine's [basicState](vdi.resources.Machine.MachineBase.md#basicState) is one of the following : PROVISIONED,AVAILABLE,CONNECTED,DISCONNECTED.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**available**|  xsd:int|  Number of machines which are in AVAILABLE [basicState](vdi.resources.Machine.MachineBase.md#basicState). [^2]
**provisioned**|  xsd:int|  Number of machines which are in PROVISIONED [basicState](vdi.resources.Machine.MachineBase.md#basicState). Applicable for VC managed virtual machines. [^2]
**connected**|  xsd:int|  Number of machines which are in CONNECTED [basicState](vdi.resources.Machine.MachineBase.md#basicState). [^2]
**disconnected**|  xsd:int|  Number of machines which are in DISCONNECTED [basicState](vdi.resources.Machine.MachineBase.md#basicState). [^2]


 


[^2]: This property cannot be updated.