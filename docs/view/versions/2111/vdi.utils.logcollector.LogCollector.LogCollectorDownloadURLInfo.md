---
layout: page
title: Data Object - LogCollectorDownloadURLInfo
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.utils.logcollector.LogCollector.LogCollectorDownloadURLInfo`

Returned by
> [LogCollector_GetDownloadURL](vdi.utils.logcollector.LogCollector.md#getDownloadURL)

See also
> [LogCollectorTaskId](vdi.entity.LogCollectorTaskId.md)

Since
> Horizon 7.10


## Data Object Description

Represents download URL for a log collector component.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**logcollectorTaskId**| [LogCollectorTaskId](vdi.entity.LogCollectorTaskId.md)|  Log collection task identifier
**url**|  xsd:string|  Short lived URL
**logCollectorBundleProfile**|  xsd:string[]|  Provides additional information about the log collection bundle.  **_Since_** Horizon 7.12 [^1] [^14] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>LOG_FILTER_NOT_HONORED</td><td>Indicates only default log collection filter is applied on the logs bundle.</td></tr></table>


 


[^1]: This property need not be set.
[^14]: This property is an unordered array of unique values.