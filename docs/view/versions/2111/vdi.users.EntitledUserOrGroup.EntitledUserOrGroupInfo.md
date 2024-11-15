---
layout: page
title: Data Object - EntitledUserOrGroupInfo
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.users.EntitledUserOrGroup.EntitledUserOrGroupInfo`

Returned by
> [EntitledUserOrGroup_Get](vdi.users.EntitledUserOrGroup.md#get), [EntitledUserOrGroup_GetInfos](vdi.users.EntitledUserOrGroup.md#getInfos)

See also
> [ADUserOrGroupBase](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md), [EntitledUserOrGroupGloballyEntitledData](vdi.users.EntitledUserOrGroup.GloballyEntitledData.md), [EntitledUserOrGroupLocallyEntitledData](vdi.users.EntitledUserOrGroup.LocallyEntitledData.md), [EntitledUserOrGroupUserSessionData](vdi.users.EntitledUserOrGroup.UserSessionData.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0


## Data Object Description

The root entitled user or group information.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User or group ID of this entity. [^2]
**base**| [ADUserOrGroupBase](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md)|  Basic active directory data for a user or group. [^2]
**localData**| [EntitledUserOrGroupLocallyEntitledData](vdi.users.EntitledUserOrGroup.LocallyEntitledData.md)|  Data relevant to locally entitled users. If no local data exists or is not permitted, this will contain only null members. [^1] [^2]
**sessionData**| [EntitledUserOrGroupUserSessionData](vdi.users.EntitledUserOrGroup.UserSessionData.md)|  Data relevant to sessions for this user or group. [^1] [^2]
**globalData**| [EntitledUserOrGroupGloballyEntitledData](vdi.users.EntitledUserOrGroup.GloballyEntitledData.md)|  Data relevant to globally entitled users. If Multi-Data Center View is not enabled, this is null. If no global data exists or is not permitted, this will contain only null members. [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.