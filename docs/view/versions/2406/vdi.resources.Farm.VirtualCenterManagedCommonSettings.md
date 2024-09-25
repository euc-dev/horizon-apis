---
layout: page
title: Data Object - FarmVirtualCenterManagedCommonSettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Farm.VirtualCenterManagedCommonSettings
Property of
     [FarmAutomatedFarmData](vdi.resources.Farm.AutomatedFarmData.md#field_detail), [FarmAutomatedFarmSpec](vdi.resources.Farm.AutomatedFarmSpec.md#field_detail)
Since 
    Horizon View 6.2

## Data Object Description 

Settings common to Automated Farm RDS Servers managed by Virtual Center sources. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**transparentPageSharingScope**|  xsd:string|  The transparent page sharing scope.   


  * This property has a default value of "VM".
  * This property will be one of:  
|  Value |  Description   
---|---  
"VM"| Inter-VM page sharing is not permitted.  
"FARM"| Inter-VM page sharing among VMs belonging to the same Automated Farm is permitted.  
"POD"| Inter-VM page sharing among VMs belonging to the same Pod is permitted.  
"GLOBAL"| Inter-VM page sharing among all VMs on the same host is permitted.  

  
  

  

