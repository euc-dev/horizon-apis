---
layout: page
title: Data Object - PartialFailureFaultResult
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.fault.PartialFailureFault.PartialFailureFaultResult`

Property of
> [PartialFailureFault](vdi.fault.PartialFailureFault.md#field_detail)

See also
> [MethodFault](vmodl.MethodFault.md)

Since
> Horizon View 6.0


## Data Object Description

The result of one individual operation. This will contain either a fault in the event that the operation failed or a result (if one exists) of the operation on success. At most one of these fields will be populated.
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**fault**| [MethodFault](vmodl.MethodFault.md)|  The error if the individual operation failed. [^1]
**result**|  xsd:anyType|  The result (if any) of the function if the individual operation succeeded. [^1]


 


[^1]: This property need not be set.
[^167]: This data object must be updated as a whole.