---
layout: page
title: Data Object - PodAssignmentInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.federation.PodAssignment.PodAssignmentInfo`

Returned by
> [PodAssignment_Get](vdi.federation.PodAssignment.md#get), [PodAssignment_GetInfos](vdi.federation.PodAssignment.md#getInfos)

See also
> [PodAssignmentData](vdi.federation.PodAssignment.PodAssignmentData.md), [PodAssignmentId](vdi.entity.PodAssignmentId.md)

Since
> Horizon View 6.0


## Data Object Description

The pod assignment info class.

##  Queryable Data Object

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService").

The query for Pod assignments.

Query Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_VIEW|  Global LDAP read access is required to query for Pod assignments.



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [PodAssignmentId](vdi.entity.PodAssignmentId.md)|  Id of the pod assignment configuration [^2]
**data**| [PodAssignmentData](vdi.federation.PodAssignment.PodAssignmentData.md)|  Data for the pod assignment configuration. [^2]
**refId**|  xsd:string|  Reference ID used for this pod assignment.  **_Since_** Horizon 8.1 [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.