---
layout: page
title: Data Object - LogCollectorFilter
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.logcollector.LogCollector.LogCollectorFilter`

Property of
> [LogCollectorSpec](vdi.utils.logcollector.LogCollector.LogCollectorSpec.md#field_detail)

Since
> Horizon 7.10


## Data Object Description

Filter to specify the type of information to be collected while requesting for logs bundle collection.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**logCollectorFilterType**|  xsd:string[]|  Filter type to be used while collecting the logs bundle. Filter is set to DEFAULT if none specified. [^157] [^14] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>DEFAULT</td><td>No dumps included with DEFAULT filter.</td></tr><tr><td>PRODUCT_DUMP</td><td>Collect the product dumps, if present.</td></tr><tr><td>WINDOWS_DUMP</td><td>Collects the windows dumps, if present.</td></tr></table>
**stickyLogCollection**|  xsd:boolean|  Indicates the connection server processing the [LogCollectorSpec](vdi.utils.logcollector.LogCollector.LogCollectorSpec.md) becomes the download owner.  **_Since_** Horizon 7.12 [^1] [^2]
**featureList**|  xsd:string[]|  List of features for which the logs need to be collected. Feature wise log collection is supported only for AGENT and AGENT_RDS. Following is the list of currently supported features.<br><table><tr><th>FeatureKey</th><th>Description</th></tr><tr><td>all</td><td>All Features</td></tr><tr><td>rtav</td><td>Real Time Audio Video</td></tr><tr><td>agentcore</td><td>Agent Core features</td></tr><tr><td>virtualchannel</td><td>Virtual Channel</td></tr><tr><td>blast</td><td>Blast</td></tr><tr><td>pcoip</td><td>PCOIP</td></tr><tr><td>cdr</td><td>Client Drive Redirection</td></tr><tr><td>clipboard</td><td>Clipboard Redirection</td></tr><tr><td>vdpservice</td><td>VDP Service</td></tr><tr><td>dnd</td><td>Drag and Drop</td></tr><tr><td>dpisync</td><td>DPI Synchronization</td></tr><tr><td>fa</td><td>File Type Association</td></tr><tr><td>perftracker</td><td>Performance Tracker</td></tr><tr><td>printredir</td><td>Printer Redirection</td></tr><tr><td>publishedapp</td><td>Published Applications</td></tr><tr><td>scannerredirection</td><td>Scanner Redirection</td></tr><tr><td>serialportredirection</td><td>Serial Port Redirection</td></tr><tr><td>smartcard</td><td>Smart Card Redirection</td></tr><tr><td>tsmmr</td><td>Multimedia Redirection</td></tr><tr><td>urlredirection</td><td>URL Content Redirection</td></tr><tr><td>usb</td><td>USB Redirection</td></tr><tr><td>watermark</td><td>Watermark</td></tr><tr><td colspan="2">Note: The supported feature list is subject to change as and when new features get added. Use getLogLevels(LogCollectorComponentIdentifier) to get list of installed features and its log levels. <strong>Since</strong> Horizon 8.4 [^1]</td></tr></table>


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^14]: This property is an unordered array of unique values.
[^157]: This property has a default value of ["DEFAULT"].