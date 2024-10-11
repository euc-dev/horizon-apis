---
layout: page
title: Data Object - LogCollectorFilter
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.logcollector.LogCollector.LogCollectorFilter`

Property of  
> [LogCollectorSpec](vdi.utils.logcollector.LogCollector.LogCollectorSpec.md#field_detail)

Since  
> Horizon 7.10


## Data Object Description 

Filter to specify the type of information to be collected while requesting for logs bundle collection. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**logCollectorFilterType**|  xsd:string[]|  Filter type to be used while collecting the logs bundle. Filter is set to DEFAULT if none specified.   


  * This property has a default value of ["DEFAULT"].
  * This property is an unordered array of unique values.
  * This property will be one of:  
|  Value |  Description   
---|---  
"DEFAULT"| No dumps included with DEFAULT filter.  
"PRODUCT_DUMP"| Collect the product dumps, if present.  
"WINDOWS_DUMP"| Collects the windows dumps, if present.  

  
**stickyLogCollection**|  xsd:boolean|  Indicates the connection server processing the [LogCollectorSpec](vdi.utils.logcollector.LogCollector.LogCollectorSpec.md) becomes the download owner.  **_Since_** Horizon 7.12  


* This property need not be set.
* This property cannot be updated.

  
**featureList**|  xsd:string[]|  List of features for which the logs need to be collected. Feature wise log collection is supported only for AGENT and AGENT_RDS. Following is the list of currently supported features. 

| FeatureKey | Description  
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

**_Since_** Horizon 8.4  


* This property need not be set.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
