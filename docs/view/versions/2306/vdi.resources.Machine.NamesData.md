---
layout: page
title: Data Object - MachineNamesData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Machine.NamesData`

Property of
> [MachineNamesView](vdi.resources.Machine.MachineNamesView.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Names of other entities related to this Machine.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**desktopName**|  xsd:string|  The name of the Desktop to which this Machine belongs. [^2]
**userName**|  xsd:string| **Deprecated.**_use[userNames](vdi.resources.Machine.NamesData.md#userNames) instead. This field will not be populated for machine belonging to pool which support multiple assignment. _ The name of the user to whom this Machine has been assigned. [^1] [^2]
**userNames**|  xsd:string[]|  Names of the users assigned to this Machine. This cannot be a group.  **_Since_** Horizon 7.12 [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.