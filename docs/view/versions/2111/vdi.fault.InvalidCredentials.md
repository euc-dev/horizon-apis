---
layout: page
title: Fault - InvalidCredentials
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.fault.InvalidCredentials`

Extends
> [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)

See also
> [MapEntry](vdi.util.MapEntry.md)

Since
> Horizon 7.9


## Fault Description

Thrown if the caller provides invalid credentials.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**errorCode**|  xsd:string|  An optional code associated with the underlying error. [^1]
**errorAttributes**| [MapEntry[]](vdi.util.MapEntry.md)|  An optional set of attributes associated with the underlying error. [^1] [^227]
Properties inherited from [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)
[errorMessage](vdi.fault.ViewRuntimeFault.md#errorMessage)
Properties inherited from [RuntimeFault](vmodl.RuntimeFault.md)
None
Properties inherited from [MethodFault](vmodl.MethodFault.md)
None


 


[^1]: This property need not be set.
[^227]: This property is a set of entries with unique "key" members.