---
layout: page
title: Data Object - LogCollectorDownloadURLInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.logcollector.LogCollector.LogCollectorDownloadURLInfo
Returned by
     [LogCollector_GetDownloadURL](vdi.utils.logcollector.LogCollector.md#getDownloadURL)
See also
     [LogCollectorTaskId](vdi.entity.LogCollectorTaskId.md)
Since 
    Horizon 7.10

## Data Object Description 

Represents download URL for a log collector component. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**logcollectorTaskId**| [LogCollectorTaskId](vdi.entity.LogCollectorTaskId.md)|  Log collection task identifier   
  
**url**|  xsd:string|  Short lived URL   
  
**logCollectorBundleProfile**|  xsd:string[]|  Provides additional information about the log collection bundle.  **_Since_** Horizon 7.12  


[^1]
  * This property is an unordered array of unique values.
  * This property will be one of:  
|  Value |  Description   
---|---  
"LOG_FILTER_NOT_HONORED"| Indicates only default log collection filter is applied on the logs bundle.  

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
