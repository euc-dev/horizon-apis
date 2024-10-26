---
layout: page
title: Data Object - DesktopComputeProfileSpec
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.ComputeProfileSpec`

Property of
> [DesktopInstantCloneDesktopProvisioningStatusData](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md#field_detail), [DesktopPushImageSpec](vdi.resources.Desktop.PushImageSpec.md#field_detail), [DesktopVirtualCenterProvisioningData](vdi.resources.Desktop.VirtualCenterProvisioningData.md#field_detail)

Since
> Horizon 8.6


## Data Object Description

Represents a compute profile which allows to customize clones with the specified attibutes of CPU, RAM and cores per socket.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**numCPU**|  xsd:int|  The number of CPUs to configure on clones [^10] [^8]
**ram**|  xsd:int|  The RAM in MB to configure on clones [^10] [^8]
**coresPerSocket**|  xsd:int|  Number of cores per socket for the CPU, the number CPU must be a multiple of coresPerSocket [^10] [^1] [^8]
 


 
