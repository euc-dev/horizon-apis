---
layout: page
title: Fault - InvalidType
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.fault.InvalidType`

Extends
> [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)

Since
> Horizon View 6.0


## Fault Description

An InvalidType is thrown if the arguments passed an invalid typed parameter to the function.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**parameterName**|  xsd:string|  The name of the invalid parameter [^1]
**expectedType**|  xsd:string|  The expected type of the parameter. [^1]
Properties inherited from [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)
[errorMessage](vdi.fault.ViewRuntimeFault.md#errorMessage)
Properties inherited from [RuntimeFault](vmodl.RuntimeFault.md)
None
Properties inherited from [MethodFault](vmodl.MethodFault.md)
None


 


[^1]: This property need not be set.