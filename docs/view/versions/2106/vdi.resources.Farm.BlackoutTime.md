---
layout: page
title: Data Object - FarmBlackoutTime
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.BlackoutTime`

Property of  
> [FarmSpaceReclamationSettings](vdi.resources.Farm.SpaceReclamationSettings.md#field_detail)

Since  
> Horizon View 6.2


## Data Object Description 

Fields for specifying blackout time for space reclamation settings RDS server disk space reclamation do not occur during blackout times. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**days**|  xsd:string[]|  List of days for a given range of time.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"MONDAY"| Monday  
"TUESDAY"| Tuesday  
"WEDNESDAY"| Wednesday  
"THURSDAY"| Thursday  
"FRIDAY"| Friday  
"SATURDAY"| Saturday  
"SUNDAY"| Sunday  
"ALL"| All seven days of the week  

  
**startTime**|  xsd:string|  Starting time for the blackout.   


  * This property must be in the form hh:mm in 24 hours format. 

  
**endTime**|  xsd:string|  Ending time for the blackout.   


  * This property must be in the form hh:mm in 24 hours format. 

  
  
  

  
  
