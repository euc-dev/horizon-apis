---
layout: page
title: Data Object - DatastoreInfo
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.Datastore.DatastoreInfo`

Property of
> [DatastoreClusterData](vdi.utils.virtualcenter.Datastore.DatastoreClusterData.md#field_detail)

Returned by
> [Datastore_ListDatastoresByDesktopOrFarm](vdi.utils.virtualcenter.Datastore.md#listDatastoresByDesktopOrFarm), [Datastore_ListDatastoresByHostOrCluster](vdi.utils.virtualcenter.Datastore.md#listDatastoresByHostOrCluster)

See also
> [DatastoreData](vdi.utils.virtualcenter.Datastore.DatastoreData.md), [DatastoreId](vdi.entity.DatastoreId.md)

Since
> Horizon View 6.0


## Data Object Description

DatastoreInfo aggregates DatastoreData with DatastoreId

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [DatastoreId](vdi.entity.DatastoreId.md)|  Datastore Id [^2]
**datastoreData**| [DatastoreData](vdi.utils.virtualcenter.Datastore.DatastoreData.md)|  Datastore data [^2]
**refId**|  xsd:string|  Reference ID used for this datastore.  **_Since_** Horizon 8.1 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.