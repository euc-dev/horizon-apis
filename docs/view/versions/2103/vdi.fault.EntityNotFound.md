---
layout: page
title: Fault - EntityNotFound
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.fault.EntityNotFound`

Extends
> [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)

See also
> [EntityId](vdi.EntityId.md)

Since
> Horizon View 6.0


## Fault Description

Thrown if the method operates on an entity which never existed or no longer exists.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [EntityId](vdi.EntityId.md)|  The ID of the entity which could not be found.
Properties inherited from [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md) @span
[errorMessage](vdi.fault.ViewRuntimeFault.md#errorMessage) @span
Properties inherited from [RuntimeFault](vmodl.RuntimeFault.md) @span
None @span
Properties inherited from [MethodFault](vmodl.MethodFault.md) @span
None @span


 
