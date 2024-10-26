---
layout: page
title: Data Object - LogLevelInfo
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.utils.logcollector.LogCollector.LogLevelInfo`

Returned by
> [LogCollector_GetLogLevels](vdi.utils.logcollector.LogCollector.md#getLogLevels), [LogCollector_SetLogLevels](vdi.utils.logcollector.LogCollector.md#setLogLevels)

See also
> [FeatureLogLevelInfo](vdi.utils.logcollector.LogCollector.FeatureLogLevelInfo.md), [LogCollectorComponentIdentifier](vdi.utils.logcollector.LogCollector.LogCollectorComponentIdentifier.md)

Since
> Horizon 8.4


## Data Object Description

Log level information for a component.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**logCollectorComponentId**| [LogCollectorComponentIdentifier](vdi.utils.logcollector.LogCollector.LogCollectorComponentIdentifier.md)|  Represents a log component ID
**featurewiseLogLevelsList**| [FeatureLogLevelInfo[]](vdi.utils.logcollector.LogCollector.FeatureLogLevelInfo.md)|  List of log level info where each object in the list represents the log levels for a feature. [^14]
**lastModifiedTime**|  xsd:long|  The duration in seconds since the last log level modification. [^19] [^1] [^72]
 


 
