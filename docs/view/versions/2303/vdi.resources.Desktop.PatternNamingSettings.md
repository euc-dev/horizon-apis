---
layout: page
title: Data Object - DesktopPatternNamingSettings
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.PatternNamingSettings`

Property of  
> [DesktopVirtualMachineNamingSettings](vdi.resources.Desktop.VirtualMachineNamingSettings.md#field_detail), [DesktopVirtualMachineNamingSpec](vdi.resources.Desktop.VirtualMachineNamingSpec.md#field_detail)

Since  
> Horizon View 6.0


## Data Object Description 

Settings related to specification of VMs with a naming pattern. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**namingPattern**|  xsd:string|  Virtual machines will be named according to the specified naming pattern. By default, view manager appends a unique number to the specified pattern to provide a unique name for each virtual machine. To place this unique number elsewhere in the pattern, use '{n}'. (For example: vm-{n}-sales.) The unique number can also be made a fixed length. (For example: vm-{n:fixed=3}-sales will name VMs from vm-001-sales to vm-999-sales).  
Machine names are constrained to a maximum size of 15 characters including the unique number. Therefore, care must be taken when choosing a pattern. If the maximum desktop size is 9 machines, the pattern must be at most 14 characters. For 99 machines, 13 characters, for 999 machines, 12 characters. For 9999 machines, 11 characters. If using a fixed size token, use a maximum of 14 characters for "n=1", 13 characters for "n=2", 12 characters for "n=3", and 11 characters for "n=4".  
If {n} is specified with no size, a size of 2 is automatically used and if no {} is specified, {n=2} is automatically appended to the end of the pattern.   


  * This property must contain only alphanumerics and dashes. It must contain at least one alpha character. It may also optionally contain a numeric placement token {n} or {n:fixed=#}. If the pattern does not specify the numeric placement token, the maximum length is 14 characters. 

  
**maxNumberOfMachines**|  xsd:int|  Maximum number of machines in the desktop.   


  * This property has a default value of 1.
  * This property has a minimum value of 1. 

  
**numberOfSpareMachines**|  xsd:int|  Number of spare powered on machines.   


  * This property has a default value of 1.
  * This property has a minimum value of 1. 

  
**provisioningTime**|  xsd:string|  Determines when machines are provisioned.   


  * This property has a default value of "UP_FRONT".
  * This property will be one of:  
|  Value |  Description   
---|---  
"ON_DEMAND"| Provision machines on demand.  
"UP_FRONT"| Provision all machines up-front.  

  
**minNumberOfMachines**|  xsd:int|  The minimum number of machines to have provisioned if on demand provisioning is selected.   


  * This property has a default value of 0.
* This property need not be set.
  * This property has a minimum value of 0. 
  * This property is required if provisioningTime is set to "ON_DEMAND".

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
