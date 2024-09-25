---
layout: page
title: Fault - EntityInUse
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.fault.EntityInUse
Thrown by
     [Farm_Create](vdi.resources.Farm.md#create), [ImageManagementAsset_Delete](vdi.utils.imagemanagement.ImageManagementAsset.md#delete), [ImageManagementStream_Delete](vdi.utils.imagemanagement.ImageManagementStream.md#delete), [ImageManagementTag_Delete](vdi.utils.imagemanagement.ImageManagementTag.md#delete), [InstantCloneEngineDomainAdministrator_Delete](vdi.utils.InstantCloneEngineDomainAdministrator.md#delete), [RADIUSAuthenticator_Delete](vdi.infrastructure.RADIUSAuthenticator.md#delete), [SAMLAuthenticator_Delete](vdi.infrastructure.SAMLAuthenticator.md#delete)
Extends
     [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)
See also
     [EntityId](vdi.EntityId.md)
Since 
    Horizon View 6.0

## Fault Description 

Thrown if the method tries to perform operation on an entity which is in use. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [EntityId](vdi.EntityId.md)|  The ID of the entity which is in use.   
  
**usedBy**| [EntityId[]](vdi.EntityId.md)|  An array of entity IDs that entityId is used by.   
  
Properties inherited from [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)  
[errorMessage](vdi.fault.ViewRuntimeFault.md#errorMessage)  
Properties inherited from [RuntimeFault](vmodl.RuntimeFault.md)  
None  
Properties inherited from [MethodFault](vmodl.MethodFault.md)  
None  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

