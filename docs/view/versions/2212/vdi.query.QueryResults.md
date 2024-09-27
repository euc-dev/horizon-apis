---
layout: page
title: Data Object - QueryResults
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.query.QueryResults  
Returned by
     [GlobalSessionQueryService_GetNext](vdi.users.GlobalSessionQueryService.md#getNext), [GlobalSessionQueryService_QueryByBrokeringPod](vdi.users.GlobalSessionQueryService.md#queryByBrokeringPod), [GlobalSessionQueryService_QueryByDesktop](vdi.users.GlobalSessionQueryService.md#queryByDesktop), [GlobalSessionQueryService_QueryByPod](vdi.users.GlobalSessionQueryService.md#queryByPod), [GlobalSessionQueryService_QueryByUser](vdi.users.GlobalSessionQueryService.md#queryByUser), [GlobalSessionQueryService_QueryWithSpec](vdi.users.GlobalSessionQueryService.md#queryWithSpec), [PersistentDiskQueryService_QueryWithSpec](vdi.resources.PersistentDiskQueryService.md#queryWithSpec), [QueryService_Create](vdi.query.QueryService.md#create), [QueryService_GetNext](vdi.query.QueryService.md#getNext), [QueryService_Query](vdi.query.QueryService.md#query)  
See also
     [QueryId](vdi.entity.QueryId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Result of a query. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [QueryId](vdi.entity.QueryId.md)|  Query ID for this search, will be null for "virtual list"-style queries (i.e., the result of the [QueryService_Query](vdi.query.QueryService.md#query) method).   


* This property need not be set.

  
**startingOffset**|  xsd:int|  Offset of first result returned (0-based). If there are no matching results, this will still be set to the requested initial offset.   
  
**remainingCount**|  xsd:int|  Number of results remaining, or null if not supported. See documentation for specific query service.   


* This property need not be set.

  
**results**|  xsd:anyType[]|  Result set. Empty if no further results. The runtime type of the returned objects will match the type specified in [queryEntityType](vdi.query.QueryDefinition.md#queryEntityType).   


* This property need not be set.

  
  
  
  
  
  

