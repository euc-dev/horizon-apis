---
layout: page
title: Data Object - DesktopManualVirtualMachineData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.ManualVirtualMachineData  
Returned by
     [Desktop_ValidateVmNamesInfo](vdi.resources.Desktop.md#validateVmNamesInfo)  
Since 
    Horizon 7.4

## Data Object Description 

Validated virtual machine data. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**vmName**|  xsd:string|  Virtual Machine name   
  
**userName**|  xsd:string|  Virtual Machine user   


* This property need not be set.

  
**sid**|  xsd:string|  The user's sid   


* This property need not be set.

  
**manualVirtualMachineErrors**|  xsd:string[]|  Errors captured after validation   


* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"VM_NAME_TOO_LONG"| Vm name is longer than 15 bytes  
"INVALID_VM_NAME"| Invalid name for a VM  
"DUPLICATE_VM_NAME"| Duplicate VM name  
"INVALID_USER_NAME"| User not found  
"DUPLICATE_USER_NAME"| Duplicate user  

  
  
  
  
  
  

