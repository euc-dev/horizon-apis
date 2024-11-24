---
layout: page
title: Data Object - EntitledUserOrGroupUserSessionData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.EntitledUserOrGroup.UserSessionData`

Property of
> [EntitledUserOrGroupGlobalSummaryView](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupGlobalSummaryView.md#field_detail), [EntitledUserOrGroupInfo](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupInfo.md#field_detail), [EntitledUserOrGroupLocalSummaryView](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupLocalSummaryView.md#field_detail)

See also
> [SessionId](vdi.entity.SessionId.md)

Since
> Horizon View 6.0


## Data Object Description

Data relevant to sessions for this user or group.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**desktopLocalSessionCount**|  xsd:int|  Count of local desktop sessions for this user or group. [^2]
**desktopLocalSessions**| [SessionId[]](vdi.entity.SessionId.md)|  Ids for local desktop sessions for this user. This will be null if this is a group. [^1] [^2]
**applicationLocalSessionCount**|  xsd:int|  Count of local application sessions for this user or group. [^2]
**applicationLocalSessions**| [SessionId[]](vdi.entity.SessionId.md)|  Ids for local application sessions for this user. This will be null if this is a group. [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.