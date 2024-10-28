---
layout: page
title: Data Object - MachineManagedMachineNamesData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Machine.ManagedMachineNamesData`

Property of
> [MachineNamesView](vdi.resources.Machine.MachineNamesView.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Names of other entities related to this managed Machine.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**hostName**|  xsd:string|  The name of the host on which this Machine is registered. [^1] [^2]
**datastorePaths**|  xsd:string[]|  The name(s) of datastore(s) occupied by this Machine. [^1] [^14] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^14]: This property is an unordered array of unique values.