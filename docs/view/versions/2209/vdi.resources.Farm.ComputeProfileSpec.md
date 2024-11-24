---
layout: page
title: Data Object - FarmComputeProfileSpec
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Farm.ComputeProfileSpec`

Property of
> [FarmInstantCloneProvisioningStatusData](vdi.resources.Farm.InstantCloneProvisioningStatusData.md#field_detail), [FarmMaintenanceSpec](vdi.resources.Farm.MaintenanceSpec.md#field_detail), [FarmVirtualCenterProvisioningData](vdi.resources.Farm.VirtualCenterProvisioningData.md#field_detail)

Since
> Horizon 8.6


## Data Object Description

Represents a compute profile which allows to customize clones with the specified attibutes of CPU, RAM and cores per socket.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**numCPU**|  xsd:int|  The number of CPUs to configure on clones [^10] [^8]
**ram**|  xsd:int|  The RAM in MB to configure on clones [^10] [^8]
**coresPerSocket**|  xsd:int|  Number of cores per socket for the CPU, the number CPU must be a multiple of coresPerSocket [^10] [^1] [^8]


 


[^1]: This property need not be set.
[^8]: This property has a minimum value of 1.
[^10]: This property has a default value of 1.