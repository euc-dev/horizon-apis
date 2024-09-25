---
layout: page
title: Data Object - PreparedMachineCount
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Machine.PreparedMachineCount
Property of
     [StateCount](vdi.resources.Machine.StateCount.md#field_detail)
Since 
    Horizon 8.4

## Data Object Description 

Number of the machines which are in prepared state. Such machine's [basicState](vdi.resources.Machine.MachineBase.md#basicState) is one of the following : PROVISIONED,AVAILABLE,CONNECTED,DISCONNECTED. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**available**|  xsd:int|  Number of machines which are in AVAILABLE [basicState](vdi.resources.Machine.MachineBase.md#basicState).   


[^2]

  
**provisioned**|  xsd:int|  Number of machines which are in PROVISIONED [basicState](vdi.resources.Machine.MachineBase.md#basicState). Applicable for VC managed virtual machines.   


[^2]

  
**connected**|  xsd:int|  Number of machines which are in CONNECTED [basicState](vdi.resources.Machine.MachineBase.md#basicState).   


[^2]

  
**disconnected**|  xsd:int|  Number of machines which are in DISCONNECTED [basicState](vdi.resources.Machine.MachineBase.md#basicState).   


[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

