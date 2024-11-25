---
layout: page
title: Service - GlobalSessionQueryService
hide:
#  - navigation
  - toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.GlobalSessionQueryService`

See also
> [DesktopId](vdi.entity.DesktopId.md), [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md), [GlobalSessionPodSessionCounter](vdi.users.GlobalSessionQueryService.PodSessionCounter.md), [GlobalSessionQueryServiceCountSpec](vdi.users.GlobalSessionQueryService.CountSpec.md), [GlobalSessionQueryServiceQuerySpec](vdi.users.GlobalSessionQueryService.QuerySpec.md), [PodId](vdi.entity.PodId.md), [QueryId](vdi.entity.QueryId.md), [QueryResults](vdi.query.QueryResults.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0





## Service Description

Service that supports a pre-defined set of global session queries.

**Methods**

Methods defined in this Service:
GlobalSessionQueryService_Delete, GlobalSessionQueryService_GetCount, GlobalSessionQueryService_GetCountWithSpec, GlobalSessionQueryService_GetNext, GlobalSessionQueryService_QueryByBrokeringPod, GlobalSessionQueryService_QueryByDesktop, GlobalSessionQueryService_QueryByPod, GlobalSessionQueryService_QueryByUser, GlobalSessionQueryService_QueryWithSpec




Deletes the server-side state associated with query. To be used after queryByuser, queryByPod, queryByBrokeringPod, queryByDesktop and queryBySpec.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalSessionQueryService](vdi.users.GlobalSessionQueryService.md) used to make the method call.
**id**| [QueryId](vdi.entity.QueryId.md)|  from a result set.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







**Deprecated.**_use #getCountWithSpec(CountSpec) instead_

Returns global session count for combination of parameters. All criteria are optional, though at least one must be specified.

**Privileges**

Privilege | Description
:---|:---
FEDERATED_SESSIONS_VIEW|  Global session read is required to return a count of query results.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalSessionQueryService](vdi.users.GlobalSessionQueryService.md) used to make the method call.
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  unique identifier for user or group [^135]
**pod**| [PodId](vdi.entity.PodId.md)|  unique identifier for pod [^135]
**brokeringPod**| [PodId](vdi.entity.PodId.md)|  unique identifier for brokering pod [^135]
**globalEntitlement**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  unique identifier for global entitlement [^135]





**Return Value**

Type | Description
:---|:---
[GlobalSessionPodSessionCounter[]](vdi.users.GlobalSessionQueryService.PodSessionCounter.md)| PodSessionCounter with session counts broken down by pods



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Returns global session count for combination of parameters. All criteria are optional, though at least one must be specified.

**Privileges**

Privilege | Description
:---|:---
FEDERATED_SESSIONS_VIEW|  Global session read is required to return a count of query results.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalSessionQueryService](vdi.users.GlobalSessionQueryService.md) used to make the method call.
**countSpec**| [GlobalSessionQueryServiceCountSpec](vdi.users.GlobalSessionQueryService.CountSpec.md)|




**Return Value**

Type | Description
:---|:---
[GlobalSessionPodSessionCounter[]](vdi.users.GlobalSessionQueryService.PodSessionCounter.md)| PodSessionCounter with session counts broken down by pods



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if both [globalEntitlement](vdi.users.GlobalSessionQueryService.CountSpec.md#globalEntitlement) and [globalApplicationEntitlement](vdi.users.GlobalSessionQueryService.CountSpec.md#globalApplicationEntitlement) are set to non null values. <br>If any two or more fields of [user](vdi.users.GlobalSessionQueryService.CountSpec.md#user), [pod](vdi.users.GlobalSessionQueryService.CountSpec.md#pod), [brokeringPod](vdi.users.GlobalSessionQueryService.CountSpec.md#brokeringPod), [desktop](vdi.users.GlobalSessionQueryService.CountSpec.md#desktop), [clientName](vdi.users.GlobalSessionQueryService.CountSpec.md#clientName) are set to non null values.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets next page from query. To be used with queryByUser, queryByPod, queryByBrokeringPod, queryByDesktop and queryBySpec.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalSessionQueryService](vdi.users.GlobalSessionQueryService.md) used to make the method call.
**id**| [QueryId](vdi.entity.QueryId.md)|  from a result set.




**Return Value**

Type | Description
:---|:---
[QueryResults](vdi.query.QueryResults.md)| next page of results.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







**Deprecated.**_use #queryWithSpec(QuerySpec) instead_

Queries global sessions by brokering pod. Create a cursor for iterating though query results efficiently, and return the first set of results. Creates server-side state which should be explicitly deleted. Server side state will also time out eventually.

**Privileges**

Privilege | Description
:---|:---
FEDERATED_SESSIONS_VIEW|  Global session read is required to query by brokering pod.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalSessionQueryService](vdi.users.GlobalSessionQueryService.md) used to make the method call.
**pod**| [PodId](vdi.entity.PodId.md)|  unique identifier for brokering pod
**globalEntitlement**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  unique identifier for global entitlement [^135]
**sortBy**|  xsd:string|  Member name to sort results by. [^135]
**sortDescending**|  xsd:boolean|  Sort order: false (ascending) by default. [^135]
**maxPageSize**|  xsd:int|  Maximum page size to return (the server may use a smaller size). [^135]





**Return Value**

Type | Description
:---|:---
[QueryResults](vdi.query.QueryResults.md)| one page of results.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







**Deprecated.**_use #queryWithSpec(QuerySpec) instead_

Queries global sessions by desktop and GE for local pod. Create a cursor for iterating though query results efficiently, and return the first set of results. Creates server-side state which should be explicitly deleted. Server side state will also time out eventually.

**Privileges**

Privilege | Description
:---|:---
FEDERATED_SESSIONS_VIEW|  Global session read is required to query by desktop.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalSessionQueryService](vdi.users.GlobalSessionQueryService.md) used to make the method call.
**desktop**| [DesktopId](vdi.entity.DesktopId.md)|  unique identifier for desktop
**globalEntitlement**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  unique identifier for global entitlement [^135]
**sortBy**|  xsd:string|  Member name to sort results by. [^135]
**sortDescending**|  xsd:boolean|  Sort order: false (ascending) by default. [^135]
**maxPageSize**|  xsd:int|  Maximum page size to return (the server may use a smaller size). [^135]





**Return Value**

Type | Description
:---|:---
[QueryResults](vdi.query.QueryResults.md)| one page of results.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







**Deprecated.**_use #queryWithSpec(QuerySpec) instead_

Queries sessions by resource/destination pod. Create a cursor for iterating though query results efficiently, and return the first set of results. Creates server-side state which should be explicitly deleted. Server side state will also time out eventually.

**Privileges**

Privilege | Description
:---|:---
FEDERATED_SESSIONS_VIEW|  Global session read is required to query by resource/destination pod.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalSessionQueryService](vdi.users.GlobalSessionQueryService.md) used to make the method call.
**pod**| [PodId](vdi.entity.PodId.md)|  unique identifier for pod
**globalEntitlement**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  unique identifier for global entitlement [^135]
**sortBy**|  xsd:string|  Member name to sort results by. [^135]
**sortDescending**|  xsd:boolean|  Sort order: false (ascending) by default. [^135]
**maxPageSize**|  xsd:int|  Maximum page size to return (the server may use a smaller size). [^135]





**Return Value**

Type | Description
:---|:---
[QueryResults](vdi.query.QueryResults.md)| one page of results.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







**Deprecated.**_use #queryWithSpec(QuerySpec) instead_

Queries global sessions by user. Create a cursor for iterating though query results efficiently, and return the first set of results. Creates server-side state which should be explicitly deleted. Server side state will also time out eventually.

**Privileges**

Privilege | Description
:---|:---
FEDERATED_SESSIONS_VIEW|  Global session read is required to query by user.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalSessionQueryService](vdi.users.GlobalSessionQueryService.md) used to make the method call.
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  unique identifier for user
**globalEntitlement**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  unique identifier for global entitlement [^135]
**sortBy**|  xsd:string|  Member name to sort results by. [^135]
**sortDescending**|  xsd:boolean|  Sort order: false (ascending) by default. [^135]
**maxPageSize**|  xsd:int|  Maximum page size to return (the server may use a smaller size). [^135]





**Return Value**

Type | Description
:---|:---
[QueryResults](vdi.query.QueryResults.md)| one page of results.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Queries global sessions based on QuerySpec . Creates a cursor for iterating though query results efficiently, and return the first set of results. Creates server-side state which should be explicitly deleted. Server side state will also time out eventually.

**Privileges**

Privilege | Description
:---|:---
FEDERATED_SESSIONS_VIEW|  Global session read is required to query by user.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalSessionQueryService](vdi.users.GlobalSessionQueryService.md) used to make the method call.
**querySpec**| [GlobalSessionQueryServiceQuerySpec](vdi.users.GlobalSessionQueryService.QuerySpec.md)|  querySpec to filter the results




**Return Value**

Type | Description
:---|:---
[QueryResults](vdi.query.QueryResults.md)| one page of results.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if both [globalEntitlement](vdi.users.GlobalSessionQueryService.QuerySpec.md#globalEntitlement) and [globalApplicationEntitlement](vdi.users.GlobalSessionQueryService.QuerySpec.md#globalApplicationEntitlement) are set to non null values.
If any two or more fields of [user](vdi.users.GlobalSessionQueryService.QuerySpec.md#user), [pod](vdi.users.GlobalSessionQueryService.QuerySpec.md#pod), [brokeringPod](vdi.users.GlobalSessionQueryService.QuerySpec.md#brokeringPod), [desktop](vdi.users.GlobalSessionQueryService.QuerySpec.md#desktop), [clientName](vdi.users.GlobalSessionQueryService.QuerySpec.md#clientName) are set to non null values.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 


[^135]: This parameter need not be set.