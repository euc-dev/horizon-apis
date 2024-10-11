---
layout: page
title: Data Object - FarmRDSServerNamingSettings
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.RDSServerNamingSettings`

Property of  
> [FarmAutomatedFarmData](vdi.resources.Farm.AutomatedFarmData.md#field_detail)

See also  
> [FarmPatternNamingSettings](vdi.resources.Farm.PatternNamingSettings.md)

Since  
> Horizon View 6.2


## Data Object Description 

Settings related to the naming of RDS Servers in an automated farm. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**namingMethod**|  xsd:string|  Determines how the VMs in the farm are named.   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"PATTERN"| Naming pattern.  

  
**patternNamingSettings**| [FarmPatternNamingSettings](vdi.resources.Farm.PatternNamingSettings.md)|  Naming pattern settings.   


* This property need not be set.
  * This property is required if namingMethod is set to "PATTERN".

  
  
  

  
  
