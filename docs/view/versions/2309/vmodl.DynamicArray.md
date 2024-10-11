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

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**val**|  xsd:anyType[]|  Array of dynamic values.   
  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
