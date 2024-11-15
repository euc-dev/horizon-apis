---
layout: page
title: Data Object - EntitledUserOrGroupGlobalSummaryView
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.users.EntitledUserOrGroup.EntitledUserOrGroupGlobalSummaryView`

Returned by
> [EntitledUserOrGroup_GetGlobalSummaryView](vdi.users.EntitledUserOrGroup.md#getGlobalSummaryView), [EntitledUserOrGroup_GetGlobalSummaryViews](vdi.users.EntitledUserOrGroup.md#getGlobalSummaryViews)

See also
> [ADUserOrGroupBase](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md), [EntitledUserOrGroupGloballyEntitledData](vdi.users.EntitledUserOrGroup.GloballyEntitledData.md), [EntitledUserOrGroupUserSessionData](vdi.users.EntitledUserOrGroup.UserSessionData.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0


## Data Object Description

Summary view of a globally entitled user or group.

##  Queryable Data Object

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService").

Only results associated with at least one Global Entitlement or Global Application Entitlement are returned.
[sessionData](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupGlobalSummaryView.md#sessionData) members are populated when results are returned, not when results are originally created.
[globalData](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupGlobalSummaryView.md#globalData).[globalEntitlements](vdi.users.EntitledUserOrGroup.GloballyEntitledData.md#globalEntitlements) field only supports the [QueryFilterContains](vdi.query.QueryFilter.Contains.md) filter.
[sessionData](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupGlobalSummaryView.md#sessionData) and all other [globalData](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupGlobalSummaryView.md#globalData) fields are not allowed members in filters.
[base](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupGlobalSummaryView.md#base).[inFolder](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md#inFolder), [base](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupGlobalSummaryView.md#base).[phone](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md#phone), and [base](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupGlobalSummaryView.md#base).[description](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md#description) are not allowed member in filters.

Query **Privileges**

Privilege | Description
:---|:---
FEDERATED_LDAP_VIEW|  Global LDAP read is required for this query. The pod federation must also be initialized.



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User or group ID of this entity.
**base**| [ADUserOrGroupBase](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md)|  Basic active directory data for a user or group, from a global cache. [^2]
**globalData**| [EntitledUserOrGroupGloballyEntitledData](vdi.users.EntitledUserOrGroup.GloballyEntitledData.md)|  Global entitlement data. [^2]
**sessionData**| [EntitledUserOrGroupUserSessionData](vdi.users.EntitledUserOrGroup.UserSessionData.md)|  Data relevant to sessions for this user or group. [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.