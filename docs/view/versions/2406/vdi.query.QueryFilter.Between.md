---
layout: page
title: Data Object - QueryFilterBetween
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.query.QueryFilter.Between
Extends
     [QueryFilter](vdi.query.QueryFilter.Filter.md)
Since 
    Horizon 7.3

## Data Object Description 

Specify that the named member must be in between the range [fromValue](vdi.query.QueryFilter.Between.md#fromValue) to [toValue](vdi.query.QueryFilter.Between.md#toValue). The supported types are: 

  * xsd:dateTime: The value in the resulting data object must be between the range [fromValue](vdi.query.QueryFilter.Between.md#fromValue) to [toValue](vdi.query.QueryFilter.Between.md#toValue).


  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**memberName**|  xsd:string|  The name of the member to compare.   
  
**fromValue**|  xsd:anyType|  Start value of the range.   


[^1]

  
**toValue**|  xsd:anyType|  End value of the range.   


[^1]

  
Properties inherited from [QueryFilter](vdi.query.QueryFilter.Filter.md)  
None  
  

  

