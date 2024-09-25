---
layout: page
title: Data Object - MachineVirtualCenterData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Machine.VirtualCenterData
Property of
     [MachineManagedMachineData](vdi.resources.Machine.ManagedMachineData.md#field_detail)
See also
     [MachineNetworkLabelData](vdi.resources.Machine.NetworkLabelData.md), [MachineVirtualDiskData](vdi.resources.Machine.VirtualDiskData.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)
Since 
    Horizon View 6.0

## Data Object Description 

Fields specific to Virtual Center. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  The Id of the Virtual Center managing this Machine.   


[^2]

  
**hostname**|  xsd:string|  The name of the host on which this virtual machine is registered.   


[^1]
[^2]

  
**path**|  xsd:string|  The virtual machine path.   


[^2]

  
**virtualMachinePowerState**|  xsd:string|  The virtual machine state.   


[^1]
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"POWERED_OFF"|   
"POWERED_ON"| The virtual machine is powered on.  
"SUSPENDED"| The virtual machine is suspended.  

  
**viewStorageAcceleratorState**|  xsd:string|  The View Storage Accelerator state.   


[^1]
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"OFF"|   
"CURRENT"| The virtual machine cached data are current.  
"OUTOFDATE"| The virtual machine cached data are not current and require regeneration.  
"ERROR"| View Storage Accelerator has encountered an error.  

  
**memoryMB**|  xsd:int|  The virtual machine memory in MB.   


[^1]
[^2]

  
**virtualDisks**| [MachineVirtualDiskData[]](vdi.resources.Machine.VirtualDiskData.md)|  The virtual disks comprising the virtual machine.   


[^1]
  * This property is an unordered array of unique values.
[^2]

  
**missingInVCenter**|  xsd:boolean|  While a machine is in a particular basic state, it can be subject to further conditions. This condition determines if the virtual machine is missing in vCenter Server.   


[^2]

  
**inHoldCustomization**|  xsd:boolean|  While a machine is in a particular basic state, it can be subject to further conditions. This condition determines if this virtual machine should hold before customization is started.   


[^2]

  
**networkLabels**| [MachineNetworkLabelData[]](vdi.resources.Machine.NetworkLabelData.md)|  The network label(s) associated with this Machine. The network label(s) automatically assigned by View to this Machine. These may differ from the actual labels if manually changed after automatic assignment or if there was an error in assignment. Labels are only assigned if the feature is enabled on this Machine's Desktop   


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

