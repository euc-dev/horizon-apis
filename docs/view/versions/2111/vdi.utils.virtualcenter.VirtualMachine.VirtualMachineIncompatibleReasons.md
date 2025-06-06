---
layout: page
title: Data Object - VirtualMachineIncompatibleReasons
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.VirtualMachine.VirtualMachineIncompatibleReasons`

Property of
> [VirtualMachineInfo](vdi.utils.virtualcenter.VirtualMachine.VirtualMachineInfo.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Reasons that may preclude this VirtualMachine from being used in manual desktop creation.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**inUseByLocalDesktop**|  xsd:boolean|  This VirtualMachine is already a machine that belongs to another desktop in this View deployment. If true, this cannot be used in manual desktop creation. [^2]
**inUseByNonLocalDesktop**|  xsd:boolean|  This VirtualMachine is already a machine that belongs to another desktop in another View deployment which shares the same VC. If true, it is not recommended to use this in manual desktop creation. [^2]
**viewComposerReplica**|  xsd:boolean|  This VirtualMachine is a View Composer replica. If true, this cannot be used in manual desktop creation. [^2]
**viewComposerBaseImage**|  xsd:boolean|  This VirtualMachine is a View Composer base image parent machine. If true, this cannot be used in manual desktop creation. [^2]
**unsupportedOS**|  xsd:boolean|  This VirtualMachine has an unsupported operating system. Certain server operating systems are only supported when [enableServerInSingleUserMode](vdi.infrastructure.GlobalSettings.GeneralData.md#enableServerInSingleUserMode) is enabled. If true, this cannot be used in manual desktop creation. [^2]
**incompatableGRIDvGPUs**|  xsd:boolean|  This VirtualMachine is on a host that doesn't support NVIDIA GRID vGPUs or the vGPU type required by this VirtualMachine. If true, this cannot be used in manual desktop creation with NVIDIA GRID vGPUs enabled.  **_Since_** Horizon View 6.1 [^2]
**instantInternal**|  xsd:boolean|  This VirtualMachine is a Instant Clone Engine internal virtual machine. If true, this cannot be used in manual desktop creation.  **_Since_** Horizon 7.6 [^5] [^2]
**instantCloneBaseImage**|  xsd:boolean|  This VirtualMachine is an Instant Clone base image parent machine. If true, this cannot be used in manual desktop creation.  **_Since_** Horizon 7.7 [^5] [^2]


 


[^2]: This property cannot be updated.
[^5]: This property has a default value of false.