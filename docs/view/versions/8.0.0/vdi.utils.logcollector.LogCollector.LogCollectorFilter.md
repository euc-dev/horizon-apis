---
layout: page
title: Data Object - LogCollectorFilter
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.logcollector.LogCollector.LogCollectorFilter
Property of
     [LogCollectorSpec](vdi.utils.logcollector.LogCollector.LogCollectorSpec.md#field_detail)
Since 
    Horizon 7.10

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
"ALL_DUMP"| Collects all dumps.  
"ALL_PROCESS_DUMP"| All process dumps with user session information included.  
"PROCESS_DUMP"| Process dumps without user session information included.  
"PRODUCT_DUMP"| Collect the product dumps, if present.  
"WINDOWS_DUMP"| Collects the windows dumps, if present.  

  
**stickyLogCollection**|  xsd:boolean|  Indicates the connection server processing the [LogCollectorSpec](vdi.utils.logcollector.LogCollector.LogCollectorSpec.md) becomes the download owner.  **_Since_** Horizon 7.12  


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

