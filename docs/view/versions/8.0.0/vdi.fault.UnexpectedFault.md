---
layout: page
title: Fault - UnexpectedFault
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.fault.UnexpectedFault
Extends
     [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)
See also
     [MapEntry](vdi.util.MapEntry.md)
Since 
    Horizon View 6.0

## Fault Description 

Indicated any internal failure during the method call. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**causeString**|  xsd:string|  The underlying cause of the fault.   


[^1]

  
**causeStackTrace**|  xsd:string[]|  The stack trace of the underlying error.   


[^1]

  
**errorCode**|  xsd:string|  An optional code associated with the underlying error. See [list of error codes](error-codes.md) for more information.   


[^1]

  
**errorAttributes**| [MapEntry[]](vdi.util.MapEntry.md)|  An optional set of attributes associated with the underlying error. See [list of error attributes](error-attributes.md) for more information.   


[^1]
  * This property is a set of entries with unique "key" members.

  
Properties inherited from [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)  
[errorMessage](vdi.fault.ViewRuntimeFault.md#errorMessage)  
Properties inherited from [RuntimeFault](vmodl.RuntimeFault.md)  
None  
Properties inherited from [MethodFault](vmodl.MethodFault.md)  
None  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
