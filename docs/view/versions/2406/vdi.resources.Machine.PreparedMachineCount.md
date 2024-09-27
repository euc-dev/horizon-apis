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


 * This property cannot be updated.

  
**provisioned**|  xsd:int|  Number of machines which are in PROVISIONED [basicState](vdi.resources.Machine.MachineBase.md#basicState). Applicable for VC managed virtual machines.   


 * This property cannot be updated.

  
**connected**|  xsd:int|  Number of machines which are in CONNECTED [basicState](vdi.resources.Machine.MachineBase.md#basicState).   


 * This property cannot be updated.

  
**disconnected**|  xsd:int|  Number of machines which are in DISCONNECTED [basicState](vdi.resources.Machine.MachineBase.md#basicState).   


 * This property cannot be updated.

  
  

  

