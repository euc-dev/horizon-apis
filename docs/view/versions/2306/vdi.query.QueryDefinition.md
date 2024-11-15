---
layout: page
title: Data Object - QueryDefinition
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.query.QueryDefinition`

Parameter to
> [QueryService_Create](vdi.query.QueryService.md#create), [QueryService_GetCount](vdi.query.QueryService.md#getCount), [QueryService_Query](vdi.query.QueryService.md#query)

See also
> [QueryFilter](vdi.query.QueryFilter.Filter.md)

Since
> Horizon View 6.0


## Data Object Description

Simple, general purpose query definition. (More complex, hard-coded queries may be offered for specific entities by their respective interfaces.) Not all entities are queryable.
 [^167]



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**queryEntityType**|  xsd:string|  Name of the type of object to be returned. The exact list of queryable data objects is defined here: [Queryable Data Objects](index-queries.md)
**filter**| [QueryFilter](vdi.query.QueryFilter.Filter.md)|  Any filter criteria for this query. [^1]
**sortBy**|  xsd:string|  Member names to sort by, if any. This attribute must be able to be filtered upon and be one of these types:<br>* xsd:boolean<br>* xsd:int<br>* xsd:long<br>* xsd:string<br>* xsd:dateTime<br>* [EntityId](vdi.EntityId.md) [^1]
**sortDescending**|  xsd:boolean|  Sort order: false (ascending) by default. [^1]
**startingOffset**|  xsd:int|  0-based starting offset for returned results, defaults to 0. [^1]
**limit**|  xsd:int|  Maximum count of items this query should produce, defaults to all. [^1]
**maxPageSize**|  xsd:int|  Maximum page size to return (the server may use a smaller size). [^1]
 


 


[^1]: This property need not be set.
[^167]: This data object must be updated as a whole.