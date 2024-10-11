---
layout: page
title: Data Object - FarmRecurringMaintenanceSettings
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.RecurringMaintenanceSettings`

Property of  
> [FarmMaintenanceSpec](vdi.resources.Farm.MaintenanceSpec.md#field_detail), [FarmScheduledMaintenanceData](vdi.resources.Farm.ScheduledMaintenanceData.md#field_detail)

Since  
> Horizon 7.1


## Data Object Description 

Settings for recurring maintenance operations. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**startTime**|  xsd:string|  Configured start time for the recurring maintenance.   


  * This property must be in the form hh:mm in 24 hours format. 

  
**maintenancePeriod**|  xsd:string|  This represents the frequency at which to perform recurring maintenance.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"DAILY"| Daily recurring maintenance  
"WEEKLY"| Weekly recurring maintenance  
"MONTHLY"| Monthly recurring maintenance  

  
**startInt**|  xsd:int|  Start index for weekly or monthly maintenance. Weekly: 1-7 (Sun-Sat), Monthly: 1-31   


* This property need not be set.
  * This property has a minimum value of 1. 
  * This property has a maximum value of 31. 
  * This property is required if maintenancePeriod is set to "WEEKLY"or "MONTHLY".

  
**everyInt**|  xsd:int|  How frequently to repeat maintenance, expressed as a multiple of the maintenance period. e.g. Every 2 weeks.   


  * This property has a default value of 1.
* This property need not be set.
  * This property has a minimum value of 1. 
  * This property has a maximum value of 100. 

  
  
  
   
  
  
