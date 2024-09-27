---
layout: page
title: Data Object - DatastoreInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.Datastore.DatastoreInfo  
Property of
     [DatastoreClusterData](vdi.utils.virtualcenter.Datastore.DatastoreClusterData.md#field_detail)  
Returned by
     [Datastore_ListDatastoresByDesktopOrFarm](vdi.utils.virtualcenter.Datastore.md#listDatastoresByDesktopOrFarm), [Datastore_ListDatastoresByHostOrCluster](vdi.utils.virtualcenter.Datastore.md#listDatastoresByHostOrCluster)  
See also
     [DatastoreData](vdi.utils.virtualcenter.Datastore.DatastoreData.md), [DatastoreId](vdi.entity.DatastoreId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

DatastoreInfo aggregates DatastoreData with DatastoreId 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [DatastoreId](vdi.entity.DatastoreId.md)|  Datastore Id   


* This property cannot be updated.

  
**datastoreData**| [DatastoreData](vdi.utils.virtualcenter.Datastore.DatastoreData.md)|  Datastore data   


* This property cannot be updated.

  
**refId**|  xsd:string|  Reference ID used for this datastore.  **_Since_** Horizon 8.1  


* This property need not be set.
* This property cannot be updated.

  
  
  
   
  
  

