---
layout: page
title: Data Object - UsageStatisticsLicensingCounters
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.statistics.UsageStatistics.LicensingCounters`

Property of  
> [UsageStatisticsLicensingCountersInfo](vdi.statistics.UsageStatistics.LicensingCountersInfo.md#field_detail)


## Data Object Description 

Statistics for the current and highest historical usage since the last reset. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**totalConcurrentConnections**|  xsd:int|  Concurrent connection user count.   


* This property cannot be updated.

  
**totalNamedUsers**|  xsd:int|  The number of unique users that have accessed the Horizon environment since the Horizon deployment was first configured or since the last Named Users Count reset. As highest count is not applicable, the value will be empty in [highestUsage](vdi.statistics.UsageStatistics.LicensingCountersInfo.md#highestUsage).   


* This property need not be set.
* This property cannot be updated.

  
**totalConcurrentSessions**|  xsd:int|  The number of connected sessions.   


* This property cannot be updated.

  
**concurrentFullVmSessions**|  xsd:int|  The number of concurrent sessions for full virtual machines.   


* This property cannot be updated.

  
**concurrentLinkedCloneSessions**|  xsd:int| **Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._ The number of concurrent linked clone sessions.   


* This property cannot be updated.

  
**concurrentUnmanagedVmSessions**|  xsd:int|  The number of concurrent sessions for unmanaged machines.   


* This property cannot be updated.

  
**concurrentApplicationSessions**|  xsd:int|  The number of concurrent application sessions.   


* This property cannot be updated.

  
**concurrentCollaborativeSessions**|  xsd:int|  The number of sessions where a session owner has invited one or more users for session collaboration.   


* This property cannot be updated.

  
**totalCollaborators**|  xsd:int|  The total number of users that are connected to a collaborative session, including the session owner and any collaborators.   


* This property cannot be updated.

  
  
  
   
  
  
