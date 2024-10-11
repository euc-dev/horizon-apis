---
layout: page
title: Data Object - DatastoreClusterInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.Datastore.DatastoreClusterInfo`

Returned by  
> [Datastore_ListDatastoreClustersByHostOrCluster](vdi.utils.virtualcenter.Datastore.md#listDatastoreClustersByHostOrCluster)

See also  
> [DatastoreClusterData](vdi.utils.virtualcenter.Datastore.DatastoreClusterData.md), [DatastoreId](vdi.entity.DatastoreId.md)

Since  
> Horizon 7.2


## Data Object Description 

DatastoreClusterInfo aggregates DatastoreClusterData with DatastoreId 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [DatastoreId](vdi.entity.DatastoreId.md)|  Datastore Id   


* This property cannot be updated.

  
**datastoreClusterData**| [DatastoreClusterData](vdi.utils.virtualcenter.Datastore.DatastoreClusterData.md)|  Datastore cluster data   


* This property cannot be updated.

  
**refId**|  xsd:string|  Reference ID used for this datastore cluster.  **_Since_** Horizon 8.1  


* This property need not be set.
* This property cannot be updated.

  
  
  
  
  
  
