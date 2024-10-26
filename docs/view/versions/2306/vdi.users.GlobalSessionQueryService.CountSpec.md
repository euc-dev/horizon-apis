---
layout: page
title: Data Object - GlobalSessionQueryServiceCountSpec
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.users.GlobalSessionQueryService.CountSpec`

Parameter to
> [GlobalSessionQueryService_GetCountWithSpec](vdi.users.GlobalSessionQueryService.md#getCountWithSpec)

See also
> [DesktopId](vdi.entity.DesktopId.md), [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md), [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md), [PodId](vdi.entity.PodId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.2


## Data Object Description

CountSpec to filter & count the sessions
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  Unique identifier for user. <br>At most one of the [user](vdi.users.GlobalSessionQueryService.CountSpec.md#user), [pod](vdi.users.GlobalSessionQueryService.CountSpec.md#pod), [brokeringPod](vdi.users.GlobalSessionQueryService.CountSpec.md#brokeringPod), [desktop](vdi.users.GlobalSessionQueryService.CountSpec.md#desktop), [clientName](vdi.users.GlobalSessionQueryService.CountSpec.md#clientName) values can be set to non null value. [^1]
**pod**| [PodId](vdi.entity.PodId.md)|  ID of the pod hosting the session. <br>At most one of the [user](vdi.users.GlobalSessionQueryService.CountSpec.md#user), [pod](vdi.users.GlobalSessionQueryService.CountSpec.md#pod), [brokeringPod](vdi.users.GlobalSessionQueryService.CountSpec.md#brokeringPod), [desktop](vdi.users.GlobalSessionQueryService.CountSpec.md#desktop), [clientName](vdi.users.GlobalSessionQueryService.CountSpec.md#clientName) values can be set to non null value. [^1]
**brokeringPod**| [PodId](vdi.entity.PodId.md)|  ID of pod that brokered the session. <br>At most one of the [user](vdi.users.GlobalSessionQueryService.CountSpec.md#user), [pod](vdi.users.GlobalSessionQueryService.CountSpec.md#pod), [brokeringPod](vdi.users.GlobalSessionQueryService.CountSpec.md#brokeringPod), [desktop](vdi.users.GlobalSessionQueryService.CountSpec.md#desktop), [clientName](vdi.users.GlobalSessionQueryService.CountSpec.md#clientName) values can be set to non null value. [^1]
**desktop**| [DesktopId](vdi.entity.DesktopId.md)|  Desktop pool id. <br>At most one of the [user](vdi.users.GlobalSessionQueryService.CountSpec.md#user), [pod](vdi.users.GlobalSessionQueryService.CountSpec.md#pod), [brokeringPod](vdi.users.GlobalSessionQueryService.CountSpec.md#brokeringPod), [desktop](vdi.users.GlobalSessionQueryService.CountSpec.md#desktop), [clientName](vdi.users.GlobalSessionQueryService.CountSpec.md#clientName) values can be set to non null value. [^1]
**clientName**|  xsd:string|  Client machine name. <br>At most one of the [user](vdi.users.GlobalSessionQueryService.CountSpec.md#user), [pod](vdi.users.GlobalSessionQueryService.CountSpec.md#pod), [brokeringPod](vdi.users.GlobalSessionQueryService.CountSpec.md#brokeringPod), [desktop](vdi.users.GlobalSessionQueryService.CountSpec.md#desktop), [clientName](vdi.users.GlobalSessionQueryService.CountSpec.md#clientName) values must be set to non null value.  **_Since_** Horizon 7.2 [^1]
**globalEntitlement**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  GlobalEntitlement unique identifier for global entitlement. Either [globalEntitlement](vdi.users.GlobalSessionQueryService.CountSpec.md#globalEntitlement) or [globalApplicationEntitlement](vdi.users.GlobalSessionQueryService.CountSpec.md#globalApplicationEntitlement) can be set. At most one of these fields can be set. [^1]
**globalApplicationEntitlement**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  GlobalEntitlement unique identifier for global application entitlement. Either [globalEntitlement](vdi.users.GlobalSessionQueryService.CountSpec.md#globalEntitlement) or [globalApplicationEntitlement](vdi.users.GlobalSessionQueryService.CountSpec.md#globalApplicationEntitlement) can be set. At most one of these fields can be set. [^1]
 


 
