---
layout: page
title: Data Object - SessionRemoteApplicationStatistics
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.helpdesk.Performance.SessionRemoteApplicationStatistics`

See also
> [RemoteApplicationStatistics](vdi.helpdesk.Performance.RemoteApplicationStatistics.md), [SessionId](vdi.entity.SessionId.md)

Since
> Horizon 8.1


## Data Object Description

The performance data for a remote application running on any virtual desktop.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**sessionId**| [SessionId](vdi.entity.SessionId.md)|  Session Id
**applicationStatistics**| [RemoteApplicationStatistics[]](vdi.helpdesk.Performance.RemoteApplicationStatistics.md)|  The performance data for a remote application running during the session on virtual desktop. The value will be null if error occurs while retrieving the data. [^1]
**errorMsg**|  xsd:string|  The error encoutered if any in fetching session info for each session. This value will be populated only if an error has occured and will be null otherwise.  **_Since_** Horizon 8.2 [^1]


 


[^1]: This property need not be set.