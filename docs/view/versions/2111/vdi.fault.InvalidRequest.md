---
layout: page
title: Fault - InvalidRequest
hide:
#- navigation
- toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.fault.InvalidRequest`

Thrown by
> [ADContainer_ListByViewComposerDomainAdministrator](vdi.utils.ADContainer.md#listByViewComposerDomainAdministrator), [EventDatabase_Update](vdi.infrastructure.EventDatabase.md#update), [GatewayAccessUserOrGroup_Create](vdi.users.GatewayAccessUserOrGroup.md#create), [GatewayAccessUserOrGroup_Delete](vdi.users.GatewayAccessUserOrGroup.md#delete), [GlobalApplicationEntitlement_Delete](vdi.federation.GlobalApplicationEntitlement.md#delete), [GlobalApplicationEntitlement_Update](vdi.federation.GlobalApplicationEntitlement.md#update), [GlobalEntitlement_Delete](vdi.federation.GlobalEntitlement.md#delete), [GlobalEntitlement_Update](vdi.federation.GlobalEntitlement.md#update), [GlobalSessionQueryService_GetCountWithSpec](vdi.users.GlobalSessionQueryService.md#getCountWithSpec), [GlobalSessionQueryService_QueryWithSpec](vdi.users.GlobalSessionQueryService.md#queryWithSpec), [Machine_Register](vdi.resources.Machine.md#register), [PersistentDiskQueryService_QueryWithSpec](vdi.resources.PersistentDiskQueryService.md#queryWithSpec), [Pod_Update](vdi.federation.Pod.md#update), [PodFederation_Update](vdi.federation.PodFederation.md#update), [Site_Update](vdi.federation.Site.md#update), [Syslog_Update](vdi.infrastructure.Syslog.md#update), [Task_Cancel](vdi.task.Task.md#cancel), [UnauthenticatedAccessUser_Create](vdi.users.UnauthenticatedAccessUser.md#create), [UnauthenticatedAccessUser_Delete](vdi.users.UnauthenticatedAccessUser.md#delete), [UnauthenticatedAccessUser_Update](vdi.users.UnauthenticatedAccessUser.md#update), [UserEntitlement_CreateUserEntitlements](vdi.users.UserEntitlement.md#createUserEntitlements), [UserHomeSite_Create](vdi.federation.UserHomeSite.md#create), [UserHomeSite_CreateOrUpdate](vdi.federation.UserHomeSite.md#createOrUpdate), [UserHomeSite_CreateOrUpdate](vdi.federation.UserHomeSite.md#createOrUpdate)

Extends
> [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)

Since
> Horizon View 6.0


## Fault Description

Represents an invalid request. Examples include: \- Only updating a subset of parameters which are required to be updated together. \- Performing an update that would leave the object in an invalid state. \- Including duplicate keys in an update map.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
None
Properties inherited from [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)
[errorMessage](vdi.fault.ViewRuntimeFault.md#errorMessage)
Properties inherited from [RuntimeFault](vmodl.RuntimeFault.md)
None
Properties inherited from [MethodFault](vmodl.MethodFault.md)
None


 
