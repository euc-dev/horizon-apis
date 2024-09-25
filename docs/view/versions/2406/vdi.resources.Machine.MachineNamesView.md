---
layout: page
title: Data Object - MachineNamesView
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Machine.MachineNamesView
See also
     [MachineBase](vdi.resources.Machine.MachineBase.md), [MachineId](vdi.entity.MachineId.md), [MachineManagedMachineNamesData](vdi.resources.Machine.ManagedMachineNamesData.md), [MachineMessageSecurityData](vdi.resources.Machine.MessageSecurityData.md), [MachineNamesData](vdi.resources.Machine.NamesData.md)
Since 
    Horizon View 6.0

## Data Object Description 

This View includes names of Users and Desktops related to this Machine. 

##  Queryable Data Object 

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService"). 

Cannot filter on the following MachineNamesView attributes: 

  * [base](vdi.resources.Machine.MachineNamesView.md#base).[operatingSystem](vdi.resources.Machine.MachineBase.md#operatingSystem)
  * [namesData](vdi.resources.Machine.MachineNamesView.md#namesData).[userName](vdi.resources.Machine.NamesData.md#userName)
  * [namesData](vdi.resources.Machine.MachineNamesView.md#namesData).[desktopName](vdi.resources.Machine.NamesData.md#desktopName)
  * [managedMachineNamesData](vdi.resources.Machine.MachineNamesView.md#managedMachineNamesData).[hostName](vdi.resources.Machine.ManagedMachineNamesData.md#hostName)
  * [managedMachineNamesData](vdi.resources.Machine.MachineNamesView.md#managedMachineNamesData).[datastorePaths](vdi.resources.Machine.ManagedMachineNamesData.md#datastorePaths)



Query Privileges 

Privilege |  Description   
---|---  
MACHINE_VIEW|  is required to query MachineNamesView.   
  


## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [MachineId](vdi.entity.MachineId.md)|  The id of the Machine.   
  
**base**| [MachineBase](vdi.resources.Machine.MachineBase.md)|  Container for all other summary fields common to all the types of Machines.   
  
**namesData**| [MachineNamesData](vdi.resources.Machine.NamesData.md)|  Names of entities related to this Machine   
  
**messageSecurityData**| [MachineMessageSecurityData](vdi.resources.Machine.MessageSecurityData.md)|  Message security data for this machine.  **_Since_** Horizon View 6.1  
  
**managedMachineNamesData**| [MachineManagedMachineNamesData](vdi.resources.Machine.ManagedMachineNamesData.md)|  Information applicable only to Managed Machines.   


[^1]

  
  

  

