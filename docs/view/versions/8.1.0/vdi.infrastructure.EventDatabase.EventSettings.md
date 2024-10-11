---
layout: page
title: Data Object - EventDatabaseEventSettings
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.EventDatabase.EventSettings`

Property of  
> [EventDatabaseInfo](vdi.infrastructure.EventDatabase.EventDatabaseInfo.md#field_detail)

Since  
> Horizon View 6.0


## Data Object Description 

The EventSettings object. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**showEventsForTime**|  xsd:string|  Events will be shown in View Administrator for a time based on the value. Value is interpreted as longevity settings in EventsDatabase.EventLongevity   


  * This property will be one of:  
|  Value |  Description   
---|---  
"ONE_WEEK"| One week  
"TWO_WEEKS"| Two weeks  
"THREE_WEEKS"| Three weeks  
"ONE_MONTH"| One month  
"TWO_MONTHS"| Two months  
"THREE_MONTHS"| Three months  
"SIX_MONTHS"| Six months  

  
**classifyEventsAsNewForDays**|  xsd:int|  Events will be marked as new for a time based on the value. Must be between 1 and 3 days.   


  * This property has a minimum value of 1. 
  * This property has a maximum value of 3. 

  
**adminEventsCount**|  xsd:int|  Number of events administrator can see in admin console.  **_Since_** Horizon 7.9  


  * This property has a default value of 2000.
* This property need not be set.
  * This property has a minimum value of 1. 

  
  
  
  
  
  
