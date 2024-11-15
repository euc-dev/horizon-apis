---
layout: page
title: Data Object - GlobalSessionPodSessionCounter
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.GlobalSessionQueryService.PodSessionCounter`

Returned by
> [GlobalSessionQueryService_GetCount](vdi.users.GlobalSessionQueryService.md#getCount), [GlobalSessionQueryService_GetCountWithSpec](vdi.users.GlobalSessionQueryService.md#getCountWithSpec)

See also
> [MethodFault](vmodl.MethodFault.md), [PodId](vdi.entity.PodId.md)

Since
> Horizon View 6.0


## Data Object Description

Session Counter for a pod
 [^167]



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [PodId](vdi.entity.PodId.md)|  PodId for which the session count is [^2]
**success**|  xsd:boolean|  Indicate whether the session count query is successful on the specified pod. [^2]
**fault**| [MethodFault](vmodl.MethodFault.md)|  The fault that caused the session count to fail. Only present if the success flag is false. [^1] [^2]
**count**|  xsd:int|  The session count. Only present when the success flag is true. [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.