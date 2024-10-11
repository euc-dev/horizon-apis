---
layout: page
title: Data Object - LogLevelSpec
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.logcollector.LogCollector.LogLevelSpec`

Parameter to  
> [LogCollector_SetLogLevels](vdi.utils.logcollector.LogCollector.md#setLogLevels)

See also  
> [LogCollectorComponentIdentifier](vdi.utils.logcollector.LogCollector.LogCollectorComponentIdentifier.md)

Since  
> Horizon 8.4


## Data Object Description 

Spec for updating feature-specific log level for a component. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**component**| [LogCollectorComponentIdentifier](vdi.utils.logcollector.LogCollector.LogCollectorComponentIdentifier.md)|  Represents a log component ID   
  
**reset**|  xsd:boolean|  Indicates if the log level need to be reset to installation default.   


  * This property has a default value of false.
* This property need not be set.

  
**featureKey**|  xsd:string|  Short name of feature for which log level needs to be configured. Following is the component wise feature keys supported, currently. 

  * CONNECTION SERVER
| FeatureKey | Description  
---|---  
all | All Features  


  * AGENT
FeatureKey | Description  
---|---  
all | All Features  
rtav | Real Time Audio Video  
agentcore | Agent Core features  
virtualchannel | Virtual Channel  
blast | Blast  
pcoip | PCOIP  
cdr | Client Drive Redirection  
clipboard | Clipboard Redirection  
vdpservice | VDP Service  
dnd | Drag and Drop  
dpisync | DPI Synchronization  
fa | File Type Association  
perftracker | Performance Tracker  
printredir | Printer Redirection  
publishedapp | Published Applications  
scannerredirection | Scanner Redirection  
serialportredirection | Serial Port Redirection  
smartcard | Smart Card Redirection  
tsmmr | Multimedia Redirection  
urlredirection | URL Content Redirection  
usb | USB Redirection  
watermark | Watermark  

Note: The supported feature list is subject to change as and when new features get added. Use getLogLevels(LogCollectorComponentIdentifier) to get list of installed features and its log levels.   


* This property need not be set.
  * This property is required if reset is set to false.

  
**logLevel**|  xsd:string|  New log level for the provided feature.   


* This property need not be set.
  * This property is required if reset is set to false.
  * This property will be one of:  
|  Value |  Description   
---|---  
"INFO"| Represents INFO log level.  
"DEBUG"| Represents DEBUG log level.  
"TRACE"| Represents TRACE log level.  
"VERBOSE"| Represents VERBOSE log level.  

  
  
  
  
  
  
