---
layout: page
title: Data Object - FarmRDSServerNamingSpec
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.resources.Farm.RDSServerNamingSpec`

Property of
> [FarmAutomatedFarmSpec](vdi.resources.Farm.AutomatedFarmSpec.md#field_detail)

See also
> [FarmPatternNamingSettings](vdi.resources.Farm.PatternNamingSettings.md)

Since
> Horizon View 6.2


## Data Object Description

Settings related to the naming of RDS Servers in an automated farm for creation.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**namingMethod**|  xsd:string|  Determines how the VMs in the farm are named. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"PATTERN"</td><td>Naming pattern.</td></tr></table>
**patternNamingSettings**| [FarmPatternNamingSettings](vdi.resources.Farm.PatternNamingSettings.md)|  Naming pattern settings. [^1] [^102]


 


[^1]: This property need not be set.
[^102]: This property is required if namingMethod is set to 'PATTERN'.