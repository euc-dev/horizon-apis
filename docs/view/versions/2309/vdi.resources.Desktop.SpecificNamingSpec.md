---
layout: page
title: Data Object - DesktopSpecificNamingSpec
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.SpecificNamingSpec`

Property of
> [DesktopVirtualMachineNamingSpec](vdi.resources.Desktop.VirtualMachineNamingSpec.md#field_detail)

See also
> [DesktopSpecifiedName](vdi.resources.Desktop.SpecifiedName.md)

Since
> Horizon View 6.0


## Data Object Description

Settings related to specified naming of machines for creation.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**specifiedNames**| [DesktopSpecifiedName[]](vdi.resources.Desktop.SpecifiedName.md)|  Initial specified names of machines in the desktop.
**startMachinesInMaintenanceMode**|  xsd:boolean|  Allows virtual machines to be customized manually before users can log in and access them. This mode must be exited manually. [^5]
**numUnassignedMachinesKeptPoweredOn**|  xsd:int|  Number of unassigned machines kept powered on. This value must be less than or equal to the number of specified names. [^10] [^8]
 


 


[^5]: This property has a default value of false.
[^8]: This property has a minimum value of 1.
[^10]: This property has a default value of 1.