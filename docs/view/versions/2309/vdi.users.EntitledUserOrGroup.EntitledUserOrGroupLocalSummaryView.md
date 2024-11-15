---
layout: page
title: Data Object - EntitledUserOrGroupLocalSummaryView
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.EntitledUserOrGroup.EntitledUserOrGroupLocalSummaryView`

Returned by
> [EntitledUserOrGroup_GetLocalSummaryView](vdi.users.EntitledUserOrGroup.md#getLocalSummaryView), [EntitledUserOrGroup_GetLocalSummaryViews](vdi.users.EntitledUserOrGroup.md#getLocalSummaryViews)

See also
> [ADUserOrGroupBase](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md), [EntitledUserOrGroupLocallyEntitledData](vdi.users.EntitledUserOrGroup.LocallyEntitledData.md), [EntitledUserOrGroupUserSessionData](vdi.users.EntitledUserOrGroup.UserSessionData.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0


## Data Object Description

Summary view of a locally entitled user or group.

##  Queryable Data Object

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService").

Results returned omit data on desktops, applications, machines,persistent disks and urlredirection settings the current administrator is not permitted to access based on access group privileges.
If the current administrator does not have root access group access, some machine and persistent disk information may be omitted from results if that user is not entitled to that machine's desktop or persistent disk.
Results are only returned for users entitled to at least one desktop or application, even if that user has machine or persistent disk assignments.
[sessionData](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupLocalSummaryView.md#sessionData) members are populated when results are returned, not when results are originally created.
[localData](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupLocalSummaryView.md#localData) fields only support the [QueryFilterContains](vdi.query.QueryFilter.Contains.md) filter.
[sessionData](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupLocalSummaryView.md#sessionData), [localData](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupLocalSummaryView.md#localData).[desktopUserEntitlements](vdi.users.EntitledUserOrGroup.LocallyEntitledData.md#desktopUserEntitlements), [localData](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupLocalSummaryView.md#localData).[applicationUserEntitlements](vdi.users.EntitledUserOrGroup.LocallyEntitledData.md#applicationUserEntitlements), [base](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupLocalSummaryView.md#base).[inFolder](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md#inFolder), [base](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupLocalSummaryView.md#base).[phone](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md#phone), and [base](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupLocalSummaryView.md#base).[description](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md#description) are not allowed member in filters.

Query **Privileges**

Privilege | Description
:---|:---
POOL_VIEW|  Desktop or application read privileges in the corresponding access group are required to filter by or include results for those desktops or applications.
MACHINE_VIEW|  Machine read privileges in the corresponding access group are required to filter by or include results for those machines.
FEDERATED_SESSIONS_VIEW|  Federated session read privilege or one of the above on the corresponding folder is required to include session information for a machine.



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User or group ID of this entity.
**base**| [ADUserOrGroupBase](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md)|  Basic active directory data for a user or group, from a local cache. [^2]
**localData**| [EntitledUserOrGroupLocallyEntitledData](vdi.users.EntitledUserOrGroup.LocallyEntitledData.md)|  Local entitlement data. [^2]
**sessionData**| [EntitledUserOrGroupUserSessionData](vdi.users.EntitledUserOrGroup.UserSessionData.md)|  Data relevant to sessions for this user or group. [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.