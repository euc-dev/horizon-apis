---
layout: page
title: Data Object - MachineManagedMachineData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Machine.ManagedMachineData`

Property of
> [MachineInfo](vdi.resources.Machine.MachineInfo.md#field_detail)

See also
> [MachineViewComposerData](vdi.resources.Machine.ViewComposerData.md), [MachineVirtualCenterData](vdi.resources.Machine.VirtualCenterData.md)

Since
> Horizon View 6.0


## Data Object Description

Fields specific to a Managed Machine.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**virtualCenterData**| [MachineVirtualCenterData](vdi.resources.Machine.VirtualCenterData.md)|  The Virtual Center information for this Machine. [^2]
**viewComposerData**| [MachineViewComposerData](vdi.resources.Machine.ViewComposerData.md)|  The View Composer information for this Machine. [^1] [^2]
**createTime**|  xsd:dateTime|  Time the machine was created. [^1] [^2]
**cloneErrorMessage**|  xsd:string|  Cloning error message for this machine. This will be set for machine belonging to automated desktops when the machine's [basicState](vdi.resources.Machine.MachineBase.md#basicState) is in PROVISIONING_ERROR or ERROR state.  **_Since_** Horizon 7.5 [^1] [^2]
**cloneErrorTime**|  xsd:dateTime|  Cloning error time for this machine. This will be set for machine belonging to automated desktops when the machine's [basicState](vdi.resources.Machine.MachineBase.md#basicState) is in PROVISIONING_ERROR or ERROR state.  **_Since_** Horizon 7.5 [^1] [^2]
**inMaintenanceMode**|  xsd:boolean|  True if the Machine is in maintenance mode.


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.