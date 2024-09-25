---
layout: page
title: Data Object - FarmRDSServerMaxSessionsData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Farm.RDSServerMaxSessionsData
Property of
     [FarmAutomatedFarmData](vdi.resources.Farm.AutomatedFarmData.md#field_detail), [FarmAutomatedFarmSpec](vdi.resources.Farm.AutomatedFarmSpec.md#field_detail)
Since 
    Horizon View 6.2

## Data Object Description 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**maxSessionsType**|  xsd:string|    


  * This property will be one of:  
|  Value |  Description   
---|---  
"UNLIMITED"| RDS Server has no limit on the number of supported sessions  
"LIMITED"| RDS Server has a limit on the number of supported sessions  

  
**maxSessions**|  xsd:int|    


[^1]
  * This property has a minimum value of 1. 
  * This property is required if maxSessionsType is set to "LIMITED".

  
  

  

