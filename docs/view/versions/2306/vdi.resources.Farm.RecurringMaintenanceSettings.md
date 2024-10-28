---
layout: page
title: Data Object - FarmRecurringMaintenanceSettings
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Farm.RecurringMaintenanceSettings`

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
**startTime**|  xsd:string|  Configured start time for the recurring maintenance. [^22]
**maintenancePeriod**|  xsd:string|  This represents the frequency at which to perform recurring maintenance. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"DAILY"</td><td>Daily recurring maintenance</td></tr><tr><td>"WEEKLY"</td><td>Weekly recurring maintenance</td></tr><tr><td>"MONTHLY"</td><td>Monthly recurring maintenance</td></tr></table>
**startInt**|  xsd:int|  Start index for weekly or monthly maintenance. Weekly: 1-7 (Sun-Sat), Monthly: 1-31 [^1] [^8] [^119] [^120]
**everyInt**|  xsd:int|  How frequently to repeat maintenance, expressed as a multiple of the maintenance period. e.g. Every 2 weeks. [^10] [^1] [^8] [^115]
 


 


[^1]: This property need not be set.
[^8]: This property has a minimum value of 1.
[^10]: This property has a default value of 1.
[^22]: This property must be in the form hh:mm in 24 hours format.
[^115]: This property has a maximum value of 100.
[^119]: This property has a maximum value of 31.
[^120]: This property is required if maintenancePeriod is set to 'WEEKLY' or 'MONTHLY'.