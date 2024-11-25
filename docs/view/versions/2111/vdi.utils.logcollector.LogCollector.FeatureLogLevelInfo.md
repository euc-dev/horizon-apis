---
layout: page
title: Data Object - FeatureLogLevelInfo
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.logcollector.LogCollector.FeatureLogLevelInfo`

Property of
> [LogLevelInfo](vdi.utils.logcollector.LogCollector.LogLevelInfo.md#field_detail)

Since
> Horizon 8.4


## Data Object Description

Feature information along with the current log level.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**featureKey**|  xsd:string|  Unique short name of the feature.
**logLevel**|  xsd:string|  Current log level for this feature.
**featureDisplayName**|  xsd:string|  Feature display name.
**associatedFeatureList**|  xsd:string[]|  List of feature keys associated with this particular feature. [^1]
**supportedLogLevels**|  xsd:string[]|  List of log levels supported by this feature.


 


[^1]: This property need not be set.