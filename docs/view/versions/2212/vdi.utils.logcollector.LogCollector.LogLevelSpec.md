---
layout: page
title: Data Object - LogLevelSpec
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.logcollector.LogCollector.LogLevelSpec`

Parameter to
> [LogCollector_SetLogLevels](vdi.utils.logcollector.LogCollector.md#setLogLevels)

See also
> [LogCollectorComponentIdentifier](vdi.utils.logcollector.LogCollector.LogCollectorComponentIdentifier.md)

Since
> Horizon 8.4


## Data Object Description

Spec for updating feature-specific log level for a component.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**component**| [LogCollectorComponentIdentifier](vdi.utils.logcollector.LogCollector.LogCollectorComponentIdentifier.md)|  Represents a log component ID
**reset**|  xsd:boolean|  Indicates if the log level need to be reset to installation default. [^5] [^1]
**featureKey**|  xsd:string|  Short name of feature for which log level needs to be configured. Following is the component wise feature keys supported, currently. <br>* CONNECTION SERVER<br><table><tr><th>FeatureKey</th><th>Description</th></tr><tr><td>all</td><td>All Features</td></tr></table><br>* AGENT<br><table><tr><th>FeatureKey</th><th>Description</th></tr><tr><td>all</td><td>All Features</td></tr><tr><td>rtav</td><td>Real Time Audio Video</td></tr><tr><td>agentcore</td><td>Agent Core features</td></tr><tr><td>virtualchannel</td><td>Virtual Channel</td></tr><tr><td>blast</td><td>Blast</td></tr><tr><td>pcoip</td><td>PCOIP</td></tr><tr><td>cdr</td><td>Client Drive Redirection</td></tr><tr><td>clipboard</td><td>Clipboard Redirection</td></tr><tr><td>vdpservice</td><td>VDP Service</td></tr><tr><td>dnd</td><td>Drag and Drop</td></tr><tr><td>dpisync</td><td>DPI Synchronization</td></tr><tr><td>fa</td><td>File Type Association</td></tr><tr><td>perftracker</td><td>Performance Tracker</td></tr><tr><td>printredir</td><td>Printer Redirection</td></tr><tr><td>publishedapp</td><td>Published Applications</td></tr><tr><td>scannerredirection</td><td>Scanner Redirection</td></tr><tr><td>serialportredirection</td><td>Serial Port Redirection</td></tr><tr><td>smartcard</td><td>Smart Card Redirection</td></tr><tr><td>tsmmr</td><td>Multimedia Redirection</td></tr><tr><td>urlredirection</td><td>URL Content Redirection</td></tr><tr><td>usb</td><td>USB Redirection</td></tr><tr><td>watermark</td><td>Watermark</td></tr></table><br>Note: The supported feature list is subject to change as and when new features get added. Use getLogLevels(LogCollectorComponentIdentifier) to get list of installed features and its log levels. [^1] [^158]
**logLevel**|  xsd:string|  New log level for the provided feature. [^1] [^158] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"INFO"</td><td>Represents INFO log level.</td></tr><tr><td>"DEBUG"</td><td>Represents DEBUG log level.</td></tr><tr><td>"TRACE"</td><td>Represents TRACE log level.</td></tr><tr><td>"VERBOSE"</td><td>Represents VERBOSE log level.</td></tr></table>


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.
[^158]: This property is required if reset is set to false.