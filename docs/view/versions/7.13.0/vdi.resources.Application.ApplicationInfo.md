---
layout: page
title: Data Object - ApplicationInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Application.ApplicationInfo`

Returned by
> [Application_Get](vdi.resources.Application.md#get)

See also
> [AccessGroupId](vdi.entity.AccessGroupId.md), [ApplicationData](vdi.resources.Application.ApplicationData.md), [ApplicationExecutionData](vdi.resources.Application.ApplicationExecutionData.md), [ApplicationIconId](vdi.entity.ApplicationIconId.md), [ApplicationId](vdi.entity.ApplicationId.md), [ApplicationRuntimeData](vdi.resources.Application.ApplicationRuntimeData.md)

Since
> Horizon View 6.0


## Data Object Description

ApplicationInfo used in Application get()/update().

##  Queryable Data Object

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService").

Only fields in [data](vdi.resources.Application.ApplicationInfo.md#data) support filtering.

Query Privileges

Privilege |  Description
---|---
POOL_VIEW|  privilege is required to query ApplicationInfo.



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [ApplicationId](vdi.entity.ApplicationId.md)|  Application Entity ID [^2]
**data**| [ApplicationData](vdi.resources.Application.ApplicationData.md)|  Application Data to read/update an Application entry.
**executionData**| [ApplicationExecutionData](vdi.resources.Application.ApplicationExecutionData.md)|  Application execution data to read/update an Application entry.
**icons**| [ApplicationIconId[]](vdi.entity.ApplicationIconId.md)|  Array of icon entityIds associated with the Application [^1] [^14] [^2]
**customizedIcons**| [ApplicationIconId[]](vdi.entity.ApplicationIconId.md)|  Array of customized icon entityIds associated with the Application  **_Since_** Horizon 7.9 [^1] [^14] [^2]
**accessGroup**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  View access groups can organize the Applications in your organization. They can also be used for delegated administration. For Application, this is the same as that of the Farm that the Application belongs to. [^2]
**runtimeData**| [ApplicationRuntimeData](vdi.resources.Application.ApplicationRuntimeData.md)|  Application runtime information  **_Since_** Horizon 7.12 [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^14]: This property is an unordered array of unique values.