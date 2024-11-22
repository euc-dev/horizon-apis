---
layout: page
title: Data Object - QueryFilterStartsWith
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.query.QueryFilter.StartsWith`

Extends
> [QueryFilter](vdi.query.QueryFilter.Filter.md)

Since
> Horizon View 6.0


## Data Object Description

Specify that the named member must start with the specified value, ignores case. The supported types are:

* xsd:string: The value in the resulting data object must start with the specified [value](vdi.query.QueryFilter.StartsWith.md#value).

 [^167]



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**memberName**|  xsd:string|  The name of the member to compare.
**value**|  xsd:anyType|  The value that the member must start with. [^1]
Properties inherited from [QueryFilter](vdi.query.QueryFilter.Filter.md)
None


 


[^1]: This property need not be set.
[^167]: This data object must be updated as a whole.