---
layout: page
title: Data Object - GlobalSessionQueryServiceQuerySpec
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.GlobalSessionQueryService.QuerySpec`

Parameter to
> [GlobalSessionQueryService_QueryWithSpec](vdi.users.GlobalSessionQueryService.md#queryWithSpec)

See also
> [DesktopId](vdi.entity.DesktopId.md), [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md), [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md), [PodId](vdi.entity.PodId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.2


## Data Object Description

QuerySpec for filtering the sessions
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  Unique identifier for user. <br>Exactly one of the [user](vdi.users.GlobalSessionQueryService.QuerySpec.md#user), [pod](vdi.users.GlobalSessionQueryService.QuerySpec.md#pod), [brokeringPod](vdi.users.GlobalSessionQueryService.QuerySpec.md#brokeringPod), [desktop](vdi.users.GlobalSessionQueryService.QuerySpec.md#desktop), [clientName](vdi.users.GlobalSessionQueryService.QuerySpec.md#clientName) values must be set to non null value, querying can be done with exactly one of these fields. [^1]
**pod**| [PodId](vdi.entity.PodId.md)|  ID of the pod hosting the session. <br>Exactly one of the [user](vdi.users.GlobalSessionQueryService.QuerySpec.md#user), [pod](vdi.users.GlobalSessionQueryService.QuerySpec.md#pod), [brokeringPod](vdi.users.GlobalSessionQueryService.QuerySpec.md#brokeringPod), [desktop](vdi.users.GlobalSessionQueryService.QuerySpec.md#desktop), [clientName](vdi.users.GlobalSessionQueryService.QuerySpec.md#clientName) values must be set to non null value, querying can be done with exactly one of these fields. [^1]
**brokeringPod**| [PodId](vdi.entity.PodId.md)|  ID of pod that brokered the session. <br>Exactly one of the [user](vdi.users.GlobalSessionQueryService.QuerySpec.md#user), [pod](vdi.users.GlobalSessionQueryService.QuerySpec.md#pod), [brokeringPod](vdi.users.GlobalSessionQueryService.QuerySpec.md#brokeringPod), [desktop](vdi.users.GlobalSessionQueryService.QuerySpec.md#desktop), [clientName](vdi.users.GlobalSessionQueryService.QuerySpec.md#clientName) values must be set to non null value, querying can be done with exactly one of these fields. [^1]
**desktop**| [DesktopId](vdi.entity.DesktopId.md)|  Desktop pool id. <br>Exactly one of the [user](vdi.users.GlobalSessionQueryService.QuerySpec.md#user), [pod](vdi.users.GlobalSessionQueryService.QuerySpec.md#pod), [brokeringPod](vdi.users.GlobalSessionQueryService.QuerySpec.md#brokeringPod), [desktop](vdi.users.GlobalSessionQueryService.QuerySpec.md#desktop), [clientName](vdi.users.GlobalSessionQueryService.QuerySpec.md#clientName) values must be set to non null value, querying can be done with exactly one of these fields. [^1]
**clientName**|  xsd:string|  Client machine name. <br>Exactly one of the [user](vdi.users.GlobalSessionQueryService.QuerySpec.md#user), [pod](vdi.users.GlobalSessionQueryService.QuerySpec.md#pod), [brokeringPod](vdi.users.GlobalSessionQueryService.QuerySpec.md#brokeringPod), [desktop](vdi.users.GlobalSessionQueryService.QuerySpec.md#desktop), [clientName](vdi.users.GlobalSessionQueryService.QuerySpec.md#clientName) values must be set to non null value, querying can be done with exactly one of these fields.  **_Since_** Horizon 7.2 [^1]
**globalEntitlement**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  GlobalEntitlement unique identifier for global entitlement. <br>Either [globalEntitlement](vdi.users.GlobalSessionQueryService.QuerySpec.md#globalEntitlement) or [globalApplicationEntitlement](vdi.users.GlobalSessionQueryService.QuerySpec.md#globalApplicationEntitlement) can be set. At most one of these fields can be set. [^1]
**globalApplicationEntitlement**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  GlobalEntitlement unique identifier for global application entitlement. <br>Either [globalEntitlement](vdi.users.GlobalSessionQueryService.QuerySpec.md#globalEntitlement) or [globalApplicationEntitlement](vdi.users.GlobalSessionQueryService.QuerySpec.md#globalApplicationEntitlement) can be set. At most one of these fields can be set. [^1]
**sortBy**|  xsd:string|  sortBy Member name to sort results by. [^1]
**sortDescending**|  xsd:boolean|  sortDescending Sort order: false (ascending) by default. [^1]
**maxPageSize**|  xsd:int|  maxPageSize Maximum page size to return (the server may use a smaller size). [^1]


 


[^1]: This property need not be set.
[^167]: This data object must be updated as a whole.