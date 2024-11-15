---
layout: page
title: Data Object - VsanDatastoreCost
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.VirtualSAN.VsanDatastoreCost`

Returned by
> [VirtualSAN_GetVsanDatastoreCostForFullClone](vdi.utils.virtualcenter.VirtualSAN.md#getVsanDatastoreCostForFullClone), [VirtualSAN_GetVsanDatastoreCostForInstantClone](vdi.utils.virtualcenter.VirtualSAN.md#getVsanDatastoreCostForInstantClone), [VirtualSAN_GetVsanDatastoreCostForLinkedClone](vdi.utils.virtualcenter.VirtualSAN.md#getVsanDatastoreCostForLinkedClone)

Since
> Horizon 7.4


## Data Object Description

Represents the cost factor for different types of disks when VSAN is used.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**osFactor**|  xsd:int|  Multiplicative factor for OS disk that is needed to account for the extra copies that are created for VSAN. [^10] [^1] [^2]
**replicaFactor**|  xsd:int|  Multiplicative factor for replica disk that is needed to account for the extra copies that are created for VSAN. [^10] [^1] [^2]
**userDataFactor**|  xsd:int|  Multiplicative factor for user data disk that is needed to account for the extra copies that are created for VSAN. [^10] [^1] [^2]
**fullCloneFactor**|  xsd:int|  Multiplicative factor for full clone disk that is needed to account for the extra copies that are created for VSAN. [^10] [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^10]: This property has a default value of 1.