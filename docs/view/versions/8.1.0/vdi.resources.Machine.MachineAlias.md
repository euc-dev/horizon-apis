---
layout: page
title: Data Object - MachineAlias
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Machine.MachineAlias
Property of
     [MachineAliasUpdateSpec](vdi.resources.Machine.MachineAliasUpdateSpec.md#field_detail), [MachineBase](vdi.resources.Machine.MachineBase.md#field_detail), [MachineData](vdi.resources.Machine.MachineData.md#field_detail)
See also
     [UserOrGroupId](vdi.entity.UserOrGroupId.md)
Since 
    Horizon 7.13

## Data Object Description 

Fields specific to machine alias of an assigned user. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User id of the user for whom this machine alias corresponds to. This cannot be a group.   
  
**alias**|  xsd:string|  Machine alias of the assigned user. If no machine alias is set for the user, then the value will be null.   


[^1]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
