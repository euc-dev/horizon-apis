---
layout: page
title: Data Object - UserOrGroupId
hide:
#- navigation
- toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.entity.UserOrGroupId`

Property of
> [AdminUserOrGroupInfo](vdi.users.AdminUserOrGroup.AdminUserOrGroupInfo.md#field_detail), [AdminUserOrGroupLoginView](vdi.users.AdminUserOrGroup.AdminUserOrGroupLoginView.md#field_detail), [AdminUserOrGroupView](vdi.users.AdminUserOrGroup.AdminUserOrGroupView.md#field_detail), [ADUserOrGroupExtendedData](vdi.users.ADUserOrGroup.ADUserOrGroupExtendedData.md#field_detail), [ADUserOrGroupInfo](vdi.users.ADUserOrGroup.ADUserOrGroupInfo.md#field_detail), [ADUserOrGroupSummaryView](vdi.users.ADUserOrGroup.ADUserOrGroupSummaryView.md#field_detail), [ADUserOrGroupView](vdi.users.ADUserOrGroup.ADUserOrGroupView.md#field_detail), [DesktopSpecifiedName](vdi.resources.Desktop.SpecifiedName.md#field_detail), [EntitledUserOrGroupGlobalSummaryView](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupGlobalSummaryView.md#field_detail), [EntitledUserOrGroupInfo](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupInfo.md#field_detail), [EntitledUserOrGroupLocalSummaryView](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupLocalSummaryView.md#field_detail), [EventData](vdi.infrastructure.EventDatabase.EventData.md#field_detail), [GatewayAccessUserOrGroupInfo](vdi.users.GatewayAccessUserOrGroup.GatewayAccessUserOrGroupInfo.md#field_detail), [GlobalSessionQueryServiceCountSpec](vdi.users.GlobalSessionQueryService.CountSpec.md#field_detail), [GlobalSessionQueryServiceQuerySpec](vdi.users.GlobalSessionQueryService.QuerySpec.md#field_detail), [LogCollectorFault](vdi.fault.LogCollectorFault.md#field_detail), [LogCollectorTaskInfo](vdi.utils.logcollector.LogCollector.LogCollectorTaskInfo.md#field_detail), [MachineBase](vdi.resources.Machine.MachineBase.md#field_detail), [MachineData](vdi.resources.Machine.MachineData.md#field_detail), [MachineDetailsView](vdi.resources.Machine.MachineDetailsView.md#field_detail), [MachineSessionData](vdi.resources.Machine.MachineSessionData.md#field_detail), [PermissionBase](vdi.users.Permission.PermissionBase.md#field_detail), [PersistentDiskGeneralData](vdi.resources.PersistentDisk.PersistentDiskGeneralData.md#field_detail), [PersistentDiskSpec](vdi.resources.PersistentDisk.PersistentDiskSpec.md#field_detail), [PodAssignmentData](vdi.federation.PodAssignment.PodAssignmentData.md#field_detail), [PoliciesInfo](vdi.users.Policies.PoliciesInfo.md#field_detail), [SecondaryCredentialsData](vdi.users.SecondaryCredentials.SecondaryCredentialsData.md#field_detail), [SecondaryCredentialsDeleteSpec](vdi.users.SecondaryCredentials.DeleteSpec.md#field_detail), [SecondaryCredentialsSpec](vdi.users.SecondaryCredentials.SecondaryCredentialsSpec.md#field_detail), [SessionGlobalReferenceData](vdi.users.Session.SessionGlobalReferenceData.md#field_detail), [SessionLocalReferenceData](vdi.users.Session.SessionLocalReferenceData.md#field_detail), [UnauthenticatedAccessConfig](vdi.infrastructure.ConnectionServer.UnauthenticatedAccessConfig.md#field_detail), [UnauthenticatedAccessUserData](vdi.users.UnauthenticatedAccessUser.UnauthenticatedAccessUserData.md#field_detail), [UserEntitlementBase](vdi.users.UserEntitlement.UserEntitlementBase.md#field_detail), [UserHomeSiteBase](vdi.federation.UserHomeSite.UserHomeSiteBase.md#field_detail), [UserHomeSiteResolutionData](vdi.federation.UserHomeSite.UserHomeSiteResolutionData.md#field_detail)

Parameter to
> [AdminUserOrGroup_Get](vdi.users.AdminUserOrGroup.md#get), [AdminUserOrGroup_GetLoginViewById](vdi.users.AdminUserOrGroup.md#getLoginViewById), [AdminUserOrGroup_GetView](vdi.users.AdminUserOrGroup.md#getView), [ADUserOrGroup_Get](vdi.users.ADUserOrGroup.md#get), [ADUserOrGroup_GetEntitlementGroups](vdi.users.ADUserOrGroup.md#getEntitlementGroups), [ADUserOrGroup_GetInfos](vdi.users.ADUserOrGroup.md#getInfos), [ADUserOrGroup_GetSummaryView](vdi.users.ADUserOrGroup.md#getSummaryView), [ADUserOrGroup_GetSummaryViews](vdi.users.ADUserOrGroup.md#getSummaryViews), [ADUserOrGroup_GetView](vdi.users.ADUserOrGroup.md#getView), [ADUserOrGroup_GetViews](vdi.users.ADUserOrGroup.md#getViews), [ADUserOrGroup_Refresh](vdi.users.ADUserOrGroup.md#refresh), [ADUserOrGroup_RefreshUsersOrGroups](vdi.users.ADUserOrGroup.md#refreshUsersOrGroups), [EntitledUserOrGroup_Get](vdi.users.EntitledUserOrGroup.md#get), [EntitledUserOrGroup_GetGlobalSummaryView](vdi.users.EntitledUserOrGroup.md#getGlobalSummaryView), [EntitledUserOrGroup_GetGlobalSummaryViews](vdi.users.EntitledUserOrGroup.md#getGlobalSummaryViews), [EntitledUserOrGroup_GetInfos](vdi.users.EntitledUserOrGroup.md#getInfos), [EntitledUserOrGroup_GetLocalSummaryView](vdi.users.EntitledUserOrGroup.md#getLocalSummaryView), [EntitledUserOrGroup_GetLocalSummaryViews](vdi.users.EntitledUserOrGroup.md#getLocalSummaryViews), [GatewayAccessUserOrGroup_Delete](vdi.users.GatewayAccessUserOrGroup.md#delete), [GatewayAccessUserOrGroup_Get](vdi.users.GatewayAccessUserOrGroup.md#get), [GlobalSessionQueryService_GetCount](vdi.users.GlobalSessionQueryService.md#getCount), [GlobalSessionQueryService_QueryByUser](vdi.users.GlobalSessionQueryService.md#queryByUser), [LogCollector_List](vdi.utils.logcollector.LogCollector.md#list), [Machine_assignUsers](vdi.resources.Machine.md#assignUsers), [Machine_unassignUsers](vdi.resources.Machine.md#unassignUsers), [Policies_Clear](vdi.users.Policies.md#clear), [Policies_Get](vdi.users.Policies.md#get), [Policies_Set](vdi.users.Policies.md#set), [Policies_Update](vdi.users.Policies.md#update), [SecondaryCredentials_List](vdi.users.SecondaryCredentials.md#list), [UnauthenticatedAccessUser_Delete](vdi.users.UnauthenticatedAccessUser.md#delete), [UnauthenticatedAccessUser_Get](vdi.users.UnauthenticatedAccessUser.md#get), [UnauthenticatedAccessUser_IsUnauthenticatedAccessUser](vdi.users.UnauthenticatedAccessUser.md#isUnauthenticatedAccessUser), [UserHomeSite_List](vdi.federation.UserHomeSite.md#list), [UserHomeSite_Resolve](vdi.federation.UserHomeSite.md#resolve), [UserHomeSite_ResolveForGAE](vdi.federation.UserHomeSite.md#resolveForGAE), [UserHomeSite_ResolveHomeSites](vdi.federation.UserHomeSite.md#resolveHomeSites)

Returned by
> [GatewayAccessUserOrGroup_Create](vdi.users.GatewayAccessUserOrGroup.md#create), [UnauthenticatedAccessUser_Create](vdi.users.UnauthenticatedAccessUser.md#create), [UnauthenticatedAccessUser_Update](vdi.users.UnauthenticatedAccessUser.md#update)

Extends
> [EntityId](vdi.EntityId.md)

Since
> Horizon View 6.0


## Data Object Description

Representation of a user or group ID.
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
None
Properties inherited from [EntityId](vdi.EntityId.md)
[id](vdi.EntityId.md#id)


 


[^167]: This data object must be updated as a whole.