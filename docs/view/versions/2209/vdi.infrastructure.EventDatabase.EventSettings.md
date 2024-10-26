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
**showEventsForTime**|  xsd:string|  Events will be shown in View Administrator for a time based on the value. Value is interpreted as longevity settings in EventsDatabase.EventLongevity<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"ONE_WEEK"</td><td>One week</td></tr><tr><td>"TWO_WEEKS"</td><td>Two weeks</td></tr><tr><td>"THREE_WEEKS"</td><td>Three weeks</td></tr><tr><td>"ONE_MONTH"</td><td>One month</td></tr><tr><td>"TWO_MONTHS"</td><td>Two months</td></tr><tr><td>"THREE_MONTHS"</td><td>Three months</td></tr><tr><td>"SIX_MONTHS"</td><td>Six months</td></tr></table>
**classifyEventsAsNewForDays**|  xsd:int|  Events will be marked as new for a time based on the value. Must be between 1 and 3 days. [^8] [^260]
**adminEventsCount**|  xsd:int|  Number of events administrator can see in admin console.  **_Since_** Horizon 7.9 [^261] [^1] [^8]
**timingProfilerDataLongevity**|  xsd:int|  Timing Profiler data will be kept in Database for a time based on the value. Must be between 1 and 7 days. Timing Profiler Data will not be stored in Event DB.  **_Since_** Horizon 8.2 [^93] [^1] [^8] [^262]


 
