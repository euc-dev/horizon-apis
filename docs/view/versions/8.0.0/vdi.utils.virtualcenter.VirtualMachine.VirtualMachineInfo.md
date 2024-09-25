---
layout: page
title: Data Object - VirtualMachineInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.VirtualMachine.VirtualMachineInfo
Returned by
     [VirtualMachine_List](vdi.utils.virtualcenter.VirtualMachine.md#list)
See also
     [MachineId](vdi.entity.MachineId.md), [VirtualMachineIncompatibleReasons](vdi.utils.virtualcenter.VirtualMachine.VirtualMachineIncompatibleReasons.md)
Since 
    Horizon View 6.0

## Data Object Description 

VirtualMachineInfo is a set of VM attributes for VMs retrieved from the VC. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [MachineId](vdi.entity.MachineId.md)|  VM Id   


[^2]

  
**name**|  xsd:string|  VM name   


[^2]

  
**path**|  xsd:string|  VM path   


[^2]

  
**operatingSystem**|  xsd:string|  Operating system enumeration as known to View.   


[^1]
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"Unknown"|   
"Windows XP"| Windows XP  
"Windows Vista"| Windows Vista  
"Windows 7"| Windows 7  
"Windows 8"| Windows 8  
"Windows 10"| Windows 10  
"Windows Server 2003"| Windows Server 2003  
"Windows Server 2008"| Windows Server 2008  
"Windows Server 2008R2"| Windows Server 2008R2  
"Windows Server 2012"| Windows Server 2012  
"Windows Server 2012R2"| Windows Server 2012R2  
"Windows Server 10"| null  
"Windows Server 2016"| null  
"Windows Server 2016 or above"| Windows Server 2016 or above  
"Linux (other)"| Linux (other)  
"Linux Server (other)"| Linux server (other)  
"Linux (Ubuntu)"| Linux (Ubuntu)  
"Linux (Red Hat Enterprise Linux)"| Linux (Red Hat Enterprise)  
"Linux (SUSE Linux Enterprise Server)"| Linux (Suse)  
"Linux (CentOS)"| Linux (CentOS)  

  
**operatingSystemDisplayName**|  xsd:string|  Operating system display name from Virtual Center.   


[^1]
[^2]

  
**hardwareVersion**|  xsd:int|  VM hardware version.   


[^1]
[^2]

  
**vGPUType**|  xsd:string|  NVIDIA GRID vGPU type configured on this virtual machine, if any.  **_Since_** Horizon View 6.1  


[^1]
[^2]

  
**incompatibleReasons**| [VirtualMachineIncompatibleReasons](vdi.utils.virtualcenter.VirtualMachine.VirtualMachineIncompatibleReasons.md)|  Reasons that may preclude this VirtualMachine from being used in manual desktop creation.   


[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

