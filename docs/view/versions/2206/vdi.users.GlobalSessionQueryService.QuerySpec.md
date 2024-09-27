---
layout: page
title: Data Object - GlobalSessionQueryServiceQuerySpec
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.GlobalSessionQueryService.QuerySpec  
Parameter to
     [GlobalSessionQueryService_QueryWithSpec](vdi.users.GlobalSessionQueryService.md#queryWithSpec)  
See also
     [DesktopId](vdi.entity.DesktopId.md), [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md), [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md), [PodId](vdi.entity.PodId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)  
Since 
    Horizon View 6.2

## Data Object Description 

QuerySpec for filtering the sessions 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  Unique identifier for user.  
Exactly one of the [user](vdi.users.GlobalSessionQueryService.QuerySpec.md#user), [pod](vdi.users.GlobalSessionQueryService.QuerySpec.md#pod), [brokeringPod](vdi.users.GlobalSessionQueryService.QuerySpec.md#brokeringPod), [desktop](vdi.users.GlobalSessionQueryService.QuerySpec.md#desktop), [clientName](vdi.users.GlobalSessionQueryService.QuerySpec.md#clientName) values must be set to non null value, querying can be done with exactly one of these fields.   


* This property need not be set.

  
**pod**| [PodId](vdi.entity.PodId.md)|  ID of the pod hosting the session.  
Exactly one of the [user](vdi.users.GlobalSessionQueryService.QuerySpec.md#user), [pod](vdi.users.GlobalSessionQueryService.QuerySpec.md#pod), [brokeringPod](vdi.users.GlobalSessionQueryService.QuerySpec.md#brokeringPod), [desktop](vdi.users.GlobalSessionQueryService.QuerySpec.md#desktop), [clientName](vdi.users.GlobalSessionQueryService.QuerySpec.md#clientName) values must be set to non null value, querying can be done with exactly one of these fields.   


* This property need not be set.

  
**brokeringPod**| [PodId](vdi.entity.PodId.md)|  ID of pod that brokered the session.  
Exactly one of the [user](vdi.users.GlobalSessionQueryService.QuerySpec.md#user), [pod](vdi.users.GlobalSessionQueryService.QuerySpec.md#pod), [brokeringPod](vdi.users.GlobalSessionQueryService.QuerySpec.md#brokeringPod), [desktop](vdi.users.GlobalSessionQueryService.QuerySpec.md#desktop), [clientName](vdi.users.GlobalSessionQueryService.QuerySpec.md#clientName) values must be set to non null value, querying can be done with exactly one of these fields.   


* This property need not be set.

  
**desktop**| [DesktopId](vdi.entity.DesktopId.md)|  Desktop pool id.  
Exactly one of the [user](vdi.users.GlobalSessionQueryService.QuerySpec.md#user), [pod](vdi.users.GlobalSessionQueryService.QuerySpec.md#pod), [brokeringPod](vdi.users.GlobalSessionQueryService.QuerySpec.md#brokeringPod), [desktop](vdi.users.GlobalSessionQueryService.QuerySpec.md#desktop), [clientName](vdi.users.GlobalSessionQueryService.QuerySpec.md#clientName) values must be set to non null value, querying can be done with exactly one of these fields.   


* This property need not be set.

  
**clientName**|  xsd:string|  Client machine name.  
Exactly one of the [user](vdi.users.GlobalSessionQueryService.QuerySpec.md#user), [pod](vdi.users.GlobalSessionQueryService.QuerySpec.md#pod), [brokeringPod](vdi.users.GlobalSessionQueryService.QuerySpec.md#brokeringPod), [desktop](vdi.users.GlobalSessionQueryService.QuerySpec.md#desktop), [clientName](vdi.users.GlobalSessionQueryService.QuerySpec.md#clientName) values must be set to non null value, querying can be done with exactly one of these fields.  **_Since_** Horizon 7.2  


* This property need not be set.

  
**globalEntitlement**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  GlobalEntitlement unique identifier for global entitlement.  
Either [globalEntitlement](vdi.users.GlobalSessionQueryService.QuerySpec.md#globalEntitlement) or [globalApplicationEntitlement](vdi.users.GlobalSessionQueryService.QuerySpec.md#globalApplicationEntitlement) can be set. At most one of these fields can be set.   


* This property need not be set.

  
**globalApplicationEntitlement**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  GlobalEntitlement unique identifier for global application entitlement.  
Either [globalEntitlement](vdi.users.GlobalSessionQueryService.QuerySpec.md#globalEntitlement) or [globalApplicationEntitlement](vdi.users.GlobalSessionQueryService.QuerySpec.md#globalApplicationEntitlement) can be set. At most one of these fields can be set.   


* This property need not be set.

  
**sortBy**|  xsd:string|  sortBy Member name to sort results by.   


* This property need not be set.

  
**sortDescending**|  xsd:boolean|  sortDescending Sort order: false (ascending) by default.   


* This property need not be set.

  
**maxPageSize**|  xsd:int|  maxPageSize Maximum page size to return (the server may use a smaller size).   


* This property need not be set.

  
  
  
 
  
  

