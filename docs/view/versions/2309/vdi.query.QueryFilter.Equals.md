---
layout: page
title: Data Object - QueryFilterEquals
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.query.QueryFilter.Equals`

Extends  
> [QueryFilter](vdi.query.QueryFilter.Filter.md)

Since  
> Horizon View 6.0


## Data Object Description 

Specify that the named member must be equal to the specified value. The supported types are: 

  * xsd:string: The value in the resulting data object must be equal to the specified [value](vdi.query.QueryFilter.Equals.md#value), ignores case.
  * xsd:ArrayOfString: The values in the resulting data object must be equal to the specified [value](vdi.query.QueryFilter.Equals.md#value), ignores case.
  * Object: The values in the resulting data object must be equal to the specified [value](vdi.query.QueryFilter.Equals.md#value). This equality is based on object's equals method implementation


  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**memberName**|  xsd:string|  The name of the member to compare.   
  
**value**|  xsd:anyType|  The value to be compared against.   


 * This property need not be set.

  
Properties inherited from [QueryFilter](vdi.query.QueryFilter.Filter.md)  
None  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
