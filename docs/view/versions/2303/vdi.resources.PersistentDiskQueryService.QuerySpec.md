---
layout: page
title: Data Object - PersistentDiskQueryServiceQuerySpec
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.PersistentDiskQueryService.QuerySpec`

Parameter to
> [PersistentDiskQueryService_QueryWithSpec](vdi.resources.PersistentDiskQueryService.md#queryWithSpec)

See also
> [PersistentDiskId](vdi.entity.PersistentDiskId.md)


## Data Object Description

**Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

deprecated This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [PersistentDiskId](vdi.entity.PersistentDiskId.md)|  The ID of the persistent disk.
**sortBy**|  xsd:string|  sortBy Member name to sort results by. [^1]
**sortDescending**|  xsd:boolean|  sortDescending Sort order: false (ascending) by default. [^1]
**maxPageSize**|  xsd:int|  maxPageSize Maximum page size to return. [^197] [^1]
 


 


[^1]: This property need not be set.
[^197]: This property has a default value of 1000.