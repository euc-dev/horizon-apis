---
layout: page
title: Data Object - MachineVirtualDiskData
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.resources.Machine.VirtualDiskData`

Property of
> [MachineVirtualCenterData](vdi.resources.Machine.VirtualCenterData.md#field_detail), [ManagedMachineDetailsData](vdi.resources.Machine.ManagedMachineDetailsData.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Fields specific to a Machine's Virtual Disks.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**path**|  xsd:string|  The disk path. [^2]
**datastorePath**|  xsd:string|  The disk's datastore. [^2]
**capacityMB**|  xsd:long|  The disk capacity, in MB. [^2]


 


[^2]: This property cannot be updated.