---
layout: page
title: Fault - EntityInUse
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.fault.EntityInUse`

Thrown by
> [Farm_Create](vdi.resources.Farm.md#create), [GSSAPIAuthenticator_Delete](vdi.infrastructure.GSSAPIAuthenticator.md#delete), [ImageManagementAsset_Delete](vdi.utils.imagemanagement.ImageManagementAsset.md#delete), [ImageManagementStream_Delete](vdi.utils.imagemanagement.ImageManagementStream.md#delete), [ImageManagementTag_Delete](vdi.utils.imagemanagement.ImageManagementTag.md#delete), [InstantCloneEngineDomainAdministrator_Delete](vdi.utils.InstantCloneEngineDomainAdministrator.md#delete), [RADIUSAuthenticator_Delete](vdi.infrastructure.RADIUSAuthenticator.md#delete), [SAMLAuthenticator_Delete](vdi.infrastructure.SAMLAuthenticator.md#delete)

Extends
> [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)

See also
> [EntityId](vdi.EntityId.md)

Since
> Horizon View 6.0


## Fault Description

Thrown if the method tries to perform operation on an entity which is in use.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [EntityId](vdi.EntityId.md)|  The ID of the entity which is in use.
**usedBy**| [EntityId[]](vdi.EntityId.md)|  An array of entity IDs that entityId is used by.
Properties inherited from [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)
[errorMessage](vdi.fault.ViewRuntimeFault.md#errorMessage)
Properties inherited from [RuntimeFault](vmodl.RuntimeFault.md)
None
Properties inherited from [MethodFault](vmodl.MethodFault.md)
None


 
