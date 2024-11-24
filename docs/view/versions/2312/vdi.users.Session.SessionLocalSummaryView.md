---
layout: page
title: Data Object - SessionLocalSummaryView
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.Session.SessionLocalSummaryView`

Returned by
> [Session_GetLocalSummaryView](vdi.users.Session.md#getLocalSummaryView)

See also
> [SessionData](vdi.users.Session.SessionData.md), [SessionId](vdi.entity.SessionId.md), [SessionLocalReferenceData](vdi.users.Session.SessionLocalReferenceData.md), [SessionNamesData](vdi.users.Session.SessionNamesData.md)

Since
> Horizon View 6.0


## Data Object Description

Summary view of a local session.

##  Queryable Data Object

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService").

The SessionLocalSummaryView query for locally resourced sessions. At least one of the specified privileges must be present.

Query **Privileges**

Privilege | Description
:---|:---
MACHINE_VIEW|  Results will be filtered with the corresponding access group permission.
FEDERATED_SESSIONS_VIEW|  All results can be returned.



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [SessionId](vdi.entity.SessionId.md)|  Session Id for this session.
**namesData**| [SessionNamesData](vdi.users.Session.SessionNamesData.md)|  Names of objects in this session.
**referenceData**| [SessionLocalReferenceData](vdi.users.Session.SessionLocalReferenceData.md)|  References in this session.
**sessionData**| [SessionData](vdi.users.Session.SessionData.md)|  Data about this session.
**refId**|  xsd:string|  Reference ID used for this session.  **_Since_** Horizon 8.4 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.