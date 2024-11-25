---
layout: page
title: Data Object - FarmRDSServerMaxSessionsData
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.resources.Farm.RDSServerMaxSessionsData`

Property of
> [FarmAutomatedFarmData](vdi.resources.Farm.AutomatedFarmData.md#field_detail), [FarmAutomatedFarmSpec](vdi.resources.Farm.AutomatedFarmSpec.md#field_detail)

Since
> Horizon View 6.2


## Data Object Description

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**maxSessionsType**|  xsd:string| <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"UNLIMITED"</td><td>RDS Server has no limit on the number of supported sessions</td></tr><tr><td>"LIMITED"</td><td>RDS Server has a limit on the number of supported sessions</td></tr></table>
**maxSessions**|  xsd:int| [^1] [^8] [^9]


 


[^1]: This property need not be set.
[^8]: This property has a minimum value of 1.
[^9]: This property is required if maxSessionsType is set to 'LIMITED'.