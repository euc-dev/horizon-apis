---
layout: page
title: Data Object - UsageStatisticsLicensingCounters
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.statistics.UsageStatistics.LicensingCounters`

Property of
> [UsageStatisticsLicensingCountersInfo](vdi.statistics.UsageStatistics.LicensingCountersInfo.md#field_detail)


## Data Object Description

Statistics for the current and highest historical usage since the last reset.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**totalConcurrentConnections**|  xsd:int|  Concurrent connection user count. [^2]
**totalNamedUsers**|  xsd:int|  The number of unique users that have accessed the Horizon environment since the Horizon deployment was first configured or since the last Named Users Count reset. As highest count is not applicable, the value will be empty in [highestUsage](vdi.statistics.UsageStatistics.LicensingCountersInfo.md#highestUsage). [^1] [^2]
**totalConcurrentSessions**|  xsd:int|  The number of connected sessions. [^2]
**concurrentFullVmSessions**|  xsd:int|  The number of concurrent sessions for full virtual machines. [^2]
**concurrentLinkedCloneSessions**|  xsd:int| **Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._ The number of concurrent linked clone sessions. [^2]
**concurrentUnmanagedVmSessions**|  xsd:int|  The number of concurrent sessions for unmanaged machines. [^2]
**concurrentApplicationSessions**|  xsd:int|  The number of concurrent application sessions. [^2]
**concurrentCollaborativeSessions**|  xsd:int|  The number of sessions where a session owner has invited one or more users for session collaboration. [^2]
**totalCollaborators**|  xsd:int|  The total number of users that are connected to a collaborative session, including the session owner and any collaborators. [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.