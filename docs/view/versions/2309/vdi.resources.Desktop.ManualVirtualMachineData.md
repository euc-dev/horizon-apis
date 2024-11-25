---
layout: page
title: Data Object - DesktopManualVirtualMachineData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.ManualVirtualMachineData`

Returned by
> [Desktop_ValidateVmNamesInfo](vdi.resources.Desktop.md#validateVmNamesInfo)

Since
> Horizon 7.4


## Data Object Description

Validated virtual machine data.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**vmName**|  xsd:string|  Virtual Machine name
**userName**|  xsd:string|  Virtual Machine user [^1]
**sid**|  xsd:string|  The user's sid [^1]
**manualVirtualMachineErrors**|  xsd:string[]|  Errors captured after validation [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>VM_NAME_TOO_LONG</td><td>Vm name is longer than 15 bytes</td></tr><tr><td>INVALID_VM_NAME</td><td>Invalid name for a VM</td></tr><tr><td>DUPLICATE_VM_NAME</td><td>Duplicate VM name</td></tr><tr><td>INVALID_USER_NAME</td><td>User not found</td></tr><tr><td>DUPLICATE_USER_NAME</td><td>Duplicate user</td></tr></table>
 


 


[^1]: This property need not be set.