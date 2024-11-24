---
layout: page
title: Data Object - VirtualMachineInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.VirtualMachine.VirtualMachineInfo`

Returned by
> [VirtualMachine_List](vdi.utils.virtualcenter.VirtualMachine.md#list)

See also
> [MachineId](vdi.entity.MachineId.md), [VirtualMachineIncompatibleReasons](vdi.utils.virtualcenter.VirtualMachine.VirtualMachineIncompatibleReasons.md)

Since
> Horizon View 6.0


## Data Object Description

VirtualMachineInfo is a set of VM attributes for VMs retrieved from the VC.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [MachineId](vdi.entity.MachineId.md)|  VM Id [^2]
**name**|  xsd:string|  VM name [^2]
**path**|  xsd:string|  VM path [^2]
**operatingSystem**|  xsd:string|  Operating system enumeration as known to View. [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>Unknown</td><td></td></tr><tr><td>Windows XP</td><td>Windows XP</td></tr><tr><td>Windows Vista</td><td>Windows Vista</td></tr><tr><td>Windows 7</td><td>Windows 7</td></tr><tr><td>Windows 8</td><td>Windows 8</td></tr><tr><td>Windows 10</td><td>Windows 10</td></tr><tr><td>Windows Server 2003</td><td>Windows Server 2003</td></tr><tr><td>Windows Server 2008</td><td>Windows Server 2008</td></tr><tr><td>Windows Server 2008R2</td><td>Windows Server 2008R2</td></tr><tr><td>Windows Server 2012</td><td>Windows Server 2012</td></tr><tr><td>Windows Server 2012R2</td><td>Windows Server 2012R2</td></tr><tr><td>Windows Server 10</td><td>null</td></tr><tr><td>Windows Server 2016</td><td>null</td></tr><tr><td>Windows Server 2016 or above</td><td>Windows Server 2016 or above</td></tr><tr><td>Linux (other)</td><td>Linux (other)</td></tr><tr><td>Linux Server (other)</td><td>Linux server (other)</td></tr><tr><td>Linux (Ubuntu)</td><td>Linux (Ubuntu)</td></tr><tr><td>Linux (Red Hat Enterprise Linux)</td><td>Linux (Red Hat Enterprise)</td></tr><tr><td>Linux (SUSE Linux Enterprise Server)</td><td>Linux (Suse)</td></tr><tr><td>Linux (CentOS)</td><td>Linux (CentOS)</td></tr></table>
**operatingSystemDisplayName**|  xsd:string|  Operating system display name from Virtual Center. [^1] [^2]
**hardwareVersion**|  xsd:int|  VM hardware version. [^1] [^2]
**vGPUType**|  xsd:string|  NVIDIA GRID vGPU type configured on this virtual machine, if any.  **_Since_** Horizon View 6.1 [^1] [^2]
**incompatibleReasons**| [VirtualMachineIncompatibleReasons](vdi.utils.virtualcenter.VirtualMachine.VirtualMachineIncompatibleReasons.md)|  Reasons that may preclude this VirtualMachine from being used in manual desktop creation. [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.