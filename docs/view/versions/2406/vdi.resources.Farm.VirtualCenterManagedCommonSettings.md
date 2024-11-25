---
layout: page
title: Data Object - FarmVirtualCenterManagedCommonSettings
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Farm.VirtualCenterManagedCommonSettings`

Property of
> [FarmAutomatedFarmData](vdi.resources.Farm.AutomatedFarmData.md#field_detail), [FarmAutomatedFarmSpec](vdi.resources.Farm.AutomatedFarmSpec.md#field_detail)

Since
> Horizon View 6.2


## Data Object Description

Settings common to Automated Farm RDS Servers managed by Virtual Center sources.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**transparentPageSharingScope**|  xsd:string|  The transparent page sharing scope. [^124] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"VM"</td><td>Inter-VM page sharing is not permitted.</td></tr><tr><td>"FARM"</td><td>Inter-VM page sharing among VMs belonging to the same Automated Farm is permitted.</td></tr><tr><td>"POD"</td><td>Inter-VM page sharing among VMs belonging to the same Pod is permitted.</td></tr><tr><td>"GLOBAL"</td><td>Inter-VM page sharing among all VMs on the same host is permitted.</td></tr></table>




 


[^124]: This property has a default value of 'VM'.