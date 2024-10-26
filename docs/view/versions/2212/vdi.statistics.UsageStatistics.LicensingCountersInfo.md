---
layout: page
title: Data Object - UsageStatisticsLicensingCountersInfo
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.statistics.UsageStatistics.LicensingCountersInfo`

Returned by
> [UsageStatistics_GetLicensingCounters](vdi.statistics.UsageStatistics.md#getLicensingCounters)

See also
> [UsageStatisticsLicensingCounters](vdi.statistics.UsageStatistics.LicensingCounters.md)


## Data Object Description

Statistics for the current and highest historical usage since the last reset.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**currentUsage**| [UsageStatisticsLicensingCounters](vdi.statistics.UsageStatistics.LicensingCounters.md)|  Current usage numbers. [^2]
**highestUsage**| [UsageStatisticsLicensingCounters](vdi.statistics.UsageStatistics.LicensingCounters.md)|  The highest usage numbers since the Horizon deployment was first configured or since the last reset. [^2]


 


[^2]: This property cannot be updated.