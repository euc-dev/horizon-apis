---
layout: page
title: Data Object - RemoteApplicationStatistics
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.helpdesk.Performance.RemoteApplicationStatistics`

Returned by
> [Performance_GetRemoteApplicationPerformanceData](vdi.helpdesk.Performance.md#getRemoteApplicationPerformanceData), [Performance_GetRemoteApplicationStatistics](vdi.helpdesk.Performance.md#getRemoteApplicationStatistics)

Since
> Horizon 7.3


## Data Object Description

The performance data for a remote application running on any virtual desktop.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**applicationId**|  xsd:string|  The identity of an application.  **_Since_** Horizon 7.6 [^2]
**processId**|  xsd:long|  The process Id. [^2]
**name**|  xsd:string|  The name of a remote application. [^2]
**status**|  xsd:string|  The status of a remote application. [^1] [^2] <br>* This property will be one of:<br><table><thead><tr><th>Value</th><th>Description</th></tr></thead><tbody><tr><td>"RUNNING"</td><td>The remote application is working properly.</td></tr><tr><td>"NOT_RESPONDING"</td><td>The remote application is not responding.</td></tr><tr><td>"UNKNOWN"</td><td>The status of the remote application is not known.</td></tr></tbody></table>
**description**|  xsd:string|  The description of a remote application. [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.