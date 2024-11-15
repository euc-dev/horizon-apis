---
layout: page
title: Data Object - QueryFilterContains
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.query.QueryFilter.Contains`

Extends
> [QueryFilter](vdi.query.QueryFilter.Filter.md)

Since
> Horizon View 6.0


## Data Object Description

Specify that the named member must contain the specified value. The supported types are:

* xsd:string: The value in the resulting data object must contain (as a substring) the specified [value](vdi.query.QueryFilter.Contains.md#value), ignores case.
* xsd:ArrayOfString: The value in the resulting data object must contain all values specified in [value](vdi.query.QueryFilter.Contains.md#value), ignores case.
* array: The values in the resulting data object must contain all values specified in [value](vdi.query.QueryFilter.Contains.md#value).

 [^167]



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**memberName**|  xsd:string|  The name of the member to compare.
**value**|  xsd:anyType|  The value that the member must contain. [^1]
Properties inherited from [QueryFilter](vdi.query.QueryFilter.Filter.md)
None


 


[^1]: This property need not be set.
[^167]: This data object must be updated as a whole.