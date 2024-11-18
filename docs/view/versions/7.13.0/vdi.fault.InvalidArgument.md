---
layout: page
title: Fault - InvalidArgument
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.fault.InvalidArgument`

Extends
> [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)

Since
> Horizon View 6.0


## Fault Description

An InvalidArgument is thrown if the set of arguments passed to the function is not specified correctly.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**parameterName**|  xsd:string|  The name of the invalid parameter [^1]
Properties inherited from [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md) @span
[errorMessage](vdi.fault.ViewRuntimeFault.md#errorMessage) @span
Properties inherited from [RuntimeFault](vmodl.RuntimeFault.md) @span
None @span
Properties inherited from [MethodFault](vmodl.MethodFault.md) @span
None @span


 


[^1]: This property need not be set.