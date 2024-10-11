---
layout: page
title: Fault - EntityNotFound
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.fault.EntityNotFound`

Extends  
> [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)

See also  
> [EntityId](vdi.EntityId.md)

Since  
> Horizon View 6.0


## Fault Description 

Thrown if the method operates on an entity which never existed or no longer exists. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [EntityId](vdi.EntityId.md)|  The ID of the entity which could not be found.   
  
Properties inherited from [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)  
[errorMessage](vdi.fault.ViewRuntimeFault.md#errorMessage)  
Properties inherited from [RuntimeFault](vmodl.RuntimeFault.md)  
None  
Properties inherited from [MethodFault](vmodl.MethodFault.md)  
None  
  
  

  
  
