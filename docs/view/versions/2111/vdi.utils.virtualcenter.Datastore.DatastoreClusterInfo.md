---
layout: page
title: Data Object - DatastoreClusterInfo
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.Datastore.DatastoreClusterInfo`

Returned by
> [Datastore_ListDatastoreClustersByHostOrCluster](vdi.utils.virtualcenter.Datastore.md#listDatastoreClustersByHostOrCluster)

See also
> [DatastoreClusterData](vdi.utils.virtualcenter.Datastore.DatastoreClusterData.md), [DatastoreId](vdi.entity.DatastoreId.md)

Since
> Horizon 7.2


## Data Object Description

DatastoreClusterInfo aggregates DatastoreClusterData with DatastoreId

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [DatastoreId](vdi.entity.DatastoreId.md)|  Datastore Id [^2]
**datastoreClusterData**| [DatastoreClusterData](vdi.utils.virtualcenter.Datastore.DatastoreClusterData.md)|  Datastore cluster data [^2]
**refId**|  xsd:string|  Reference ID used for this datastore cluster.  **_Since_** Horizon 8.1 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.