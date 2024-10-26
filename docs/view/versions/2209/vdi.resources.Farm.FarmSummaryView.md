---
layout: page
title: Data Object - FarmSummaryView
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.FarmSummaryView`

Returned by
> [Farm_GetSummaryView](vdi.resources.Farm.md#getSummaryView)

See also
> [FarmId](vdi.entity.FarmId.md), [FarmSummaryData](vdi.resources.Farm.FarmSummaryData.md)

Since
> Horizon View 6.0


## Data Object Description

Farm summary View

##  Queryable Data Object

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService").

The fields which can be used in filters are:

* [data](vdi.resources.Farm.FarmSummaryView.md#data).[name](vdi.resources.Farm.FarmSummaryData.md#name)
* [data](vdi.resources.Farm.FarmSummaryView.md#data).[type](vdi.resources.Farm.FarmSummaryData.md#type)
* [data](vdi.resources.Farm.FarmSummaryView.md#data).[displayName](vdi.resources.Farm.FarmSummaryData.md#displayName)
* [data](vdi.resources.Farm.FarmSummaryView.md#data).[accessGroup](vdi.resources.Farm.FarmSummaryData.md#accessGroup)
* [data](vdi.resources.Farm.FarmSummaryView.md#data).[enabled](vdi.resources.Farm.FarmSummaryData.md#enabled)
* [data](vdi.resources.Farm.FarmSummaryView.md#data).[desktop](vdi.resources.Farm.FarmSummaryData.md#desktop) (Cannot use property to sort)



Query Privileges

Privilege |  Description
---|---
POOL_VIEW|  privilege is required to query Farm summary View.



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [FarmId](vdi.entity.FarmId.md)|  Farm entity ID [^2]
**data**| [FarmSummaryData](vdi.resources.Farm.FarmSummaryData.md)|  Farm summary Data [^2]
**refId**|  xsd:string|  Reference ID used for this farm.  **_Since_** Horizon 8.2 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.