---
layout: page
title: Data Object - DataStoreSummaryStatistics
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.statistics.VirtualCenterStatistics.DataStoreSummaryStatistics`

Property of
> [VirtualCenterSummaryStatistics](vdi.statistics.VirtualCenterStatistics.VirtualCenterSummaryStatistics.md#field_detail)

Since
> Horizon 7.8


## Data Object Description

Statistics about a Virtual Center datastore.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**name**|  xsd:string|  The name of the data store. [^2]
**accessible**|  xsd:boolean|  Whether or not this data store is accessible [^1] [^2]
**path**|  xsd:string|  The path to the data store. [^1] [^2]
**dataStoreType**|  xsd:string|  The type of the data store. [^1] [^2]
**capacityMB**|  xsd:long|  The capacity of the data store, in MBs. [^1] [^2]
**freeSpaceMB**|  xsd:long|  The free space on the data store, in MBs. [^1] [^2]
**url**|  xsd:string|  The unique locator for the data store. [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.