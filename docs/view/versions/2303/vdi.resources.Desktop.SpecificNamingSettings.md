---
layout: page
title: Data Object - DesktopSpecificNamingSettings
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.SpecificNamingSettings`

Property of
> [DesktopVirtualMachineNamingSettings](vdi.resources.Desktop.VirtualMachineNamingSettings.md#field_detail)

See also
> [DesktopSpecifiedName](vdi.resources.Desktop.SpecifiedName.md)

Since
> Horizon View 6.0


## Data Object Description

Settings related to specified naming of machines.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**startMachinesInMaintenanceMode**|  xsd:boolean|  Allows virtual machines to be customized manually before users can log in and access them. This mode must be exited manually. [^5]
**numUnassignedMachinesKeptPoweredOn**|  xsd:int|  Number of unassigned machines kept powered on. When updated, this value must be less than or equal to the total number of existing machines in the desktop. [^10] [^8]
**numMachines**|  xsd:int|  Number of machines in the pool.  **_Since_** Horizon 7.7 [^19] [^72]
**specifiedNames**| [DesktopSpecifiedName[]](vdi.resources.Desktop.SpecifiedName.md)|  New vm names that could be provided during update.  **_Since_** Horizon 7.7 [^1]
 


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.
[^8]: This property has a minimum value of 1.
[^10]: This property has a default value of 1.
[^19]: This property has a default value of 0.
[^72]: This property has a minimum value of 0.