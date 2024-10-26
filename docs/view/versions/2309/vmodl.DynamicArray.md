---
layout: page
title: Data Object - DynamicArray
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vim.binding.vmodl.DynamicArray`

Since
> vmodl.version.version0


## Data Object Description

DynamicArray is a data object type that represents an array of dynamically-typed objects. A client should only see a DynamicArray object when the element type is unknown (meaning the type is newer than the client). Otherwise, a client would see the type as T[] where T is known.
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**val**|  xsd:anyType[]|  Array of dynamic values.
 


 


[^167]: This data object must be updated as a whole.