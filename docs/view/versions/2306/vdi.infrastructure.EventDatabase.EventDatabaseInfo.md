---
layout: page
title: Data Object - EventDatabaseInfo
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.EventDatabase.EventDatabaseInfo`

Returned by
> [EventDatabase_Get](vdi.infrastructure.EventDatabase.md#get)

See also
> [EventDatabaseEventSettings](vdi.infrastructure.EventDatabase.EventSettings.md), [EventDatabaseSettings](vdi.infrastructure.EventDatabase.EventDatabaseSettings.md)

Since
> Horizon View 6.0


## Data Object Description

The EventDatabase info object.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**eventDatabaseSet**|  xsd:boolean|  Whether or not the event database has been set in the backend. This should be effectively treated as read-only, as it will be ignored on update.
**database**| [EventDatabaseSettings](vdi.infrastructure.EventDatabase.EventDatabaseSettings.md)|  How to reach and log into the database server, plus database settings to use [^1] [^258]
**settings**| [EventDatabaseEventSettings](vdi.infrastructure.EventDatabase.EventSettings.md)|  Event persistence settings [^1] [^258]
 


 


[^1]: This property need not be set.
[^258]: This property is required if eventDatabaseSet is set to true.