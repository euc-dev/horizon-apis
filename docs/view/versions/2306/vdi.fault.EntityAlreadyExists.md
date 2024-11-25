---
layout: page
title: Fault - EntityAlreadyExists
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.fault.EntityAlreadyExists`

Thrown by
> [Farm_Create](vdi.resources.Farm.md#create)

Extends
> [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)

See also
> [EntityId](vdi.EntityId.md)

Since
> Horizon View 6.0


## Fault Description

Thrown if the method tries to create an entity which already exists.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [EntityId](vdi.EntityId.md)|  The ID of the entity which already exists.
Properties inherited from [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)
[errorMessage](vdi.fault.ViewRuntimeFault.md#errorMessage)
Properties inherited from [RuntimeFault](vmodl.RuntimeFault.md)
None
Properties inherited from [MethodFault](vmodl.MethodFault.md)
None
 


 
