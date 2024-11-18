---
layout: page
title: Fault - UnexpectedFault
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.fault.UnexpectedFault`

Extends
> [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)

See also
> [MapEntry](vdi.util.MapEntry.md)

Since
> Horizon View 6.0


## Fault Description

Indicated any internal failure during the method call.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**causeString**|  xsd:string|  The underlying cause of the fault. [^1]
**causeStackTrace**|  xsd:string[]|  The stack trace of the underlying error. [^1]
**errorCode**|  xsd:string|  An optional code associated with the underlying error. See [list of error codes](error-codes.md) for more information. [^1]
**errorAttributes**| [MapEntry[]](vdi.util.MapEntry.md)|  An optional set of attributes associated with the underlying error. See [list of error attributes](error-attributes.md) for more information. [^1] [^227]
Properties inherited from [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md) @span
[errorMessage](vdi.fault.ViewRuntimeFault.md#errorMessage) @span
Properties inherited from [RuntimeFault](vmodl.RuntimeFault.md) @span
None @span
Properties inherited from [MethodFault](vmodl.MethodFault.md) @span
None @span


 


[^1]: This property need not be set.
[^227]: This property is a set of entries with unique "key" members.