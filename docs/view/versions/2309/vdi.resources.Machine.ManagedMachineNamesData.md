---
layout: page
title: Data Object - MachineManagedMachineNamesData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Machine.ManagedMachineNamesData`

Property of  
> [MachineNamesView](vdi.resources.Machine.MachineNamesView.md#field_detail)

Since  
> Horizon View 6.0


## Data Object Description 

Names of other entities related to this managed Machine. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**hostName**|  xsd:string|  The name of the host on which this Machine is registered.   


 * This property need not be set.
 * This property cannot be updated.

  
**datastorePaths**|  xsd:string[]|  The name(s) of datastore(s) occupied by this Machine.   


 * This property need not be set.
  * This property is an unordered array of unique values.
 * This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
