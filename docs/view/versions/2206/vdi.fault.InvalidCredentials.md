---
layout: page
title: Fault - InvalidCredentials
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.fault.InvalidCredentials
Extends
     [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)
See also
     [MapEntry](vdi.util.MapEntry.md)
Since 
    Horizon 7.9

## Fault Description 

Thrown if the caller provides invalid credentials. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**errorCode**|  xsd:string|  An optional code associated with the underlying error.   


[^1]

  
**errorAttributes**| [MapEntry[]](vdi.util.MapEntry.md)|  An optional set of attributes associated with the underlying error.   


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
  
  
