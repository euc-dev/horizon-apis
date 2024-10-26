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
**logCollectorFilterType**|  xsd:string[]|  Filter type to be used while collecting the logs bundle. Filter is set to DEFAULT if none specified. [^157] [^14] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>DEFAULT</td><td>No dumps included with DEFAULT filter.</td></tr><tr><td>ALL_DUMP</td><td>Collects all dumps.</td></tr><tr><td>ALL_PROCESS_DUMP</td><td>All process dumps with user session information included.</td></tr><tr><td>PROCESS_DUMP</td><td>Process dumps without user session information included.</td></tr><tr><td>PRODUCT_DUMP</td><td>Collect the product dumps, if present.</td></tr><tr><td>WINDOWS_DUMP</td><td>Collects the windows dumps, if present.</td></tr></table>
**stickyLogCollection**|  xsd:boolean|  Indicates the connection server processing the [LogCollectorSpec](vdi.utils.logcollector.LogCollector.LogCollectorSpec.md) becomes the download owner.  **_Since_** Horizon 7.12 [^1] [^2]


 
