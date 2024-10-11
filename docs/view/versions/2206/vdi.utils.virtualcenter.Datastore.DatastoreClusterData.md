---
layout: page
title: Data Object - DatastoreClusterData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.Datastore.DatastoreClusterData`

Property of  
> [DatastoreClusterInfo](vdi.utils.virtualcenter.Datastore.DatastoreClusterInfo.md#field_detail)

See also  
> [DatacenterId](vdi.entity.DatacenterId.md), [DatastoreInfo](vdi.utils.virtualcenter.Datastore.DatastoreInfo.md), [HostOrClusterId](vdi.entity.HostOrClusterId.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since  
> Horizon 7.2


## Data Object Description 

DatastoreClusterData is a set of Datastore cluster attributes retrieved from the VC. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  Datastore Cluster name   


* This property cannot be updated.

  
**path**|  xsd:string|  Datastore Cluster path   


* This property cannot be updated.

  
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  VirtualCenter id for this datastore cluster   


* This property cannot be updated.

  
**datacenter**| [DatacenterId](vdi.entity.DatacenterId.md)|  Datacenter id for this datastore cluster   


* This property need not be set.
* This property cannot be updated.

  
**hostOrCluster**| [HostOrClusterId](vdi.entity.HostOrClusterId.md)|  HostOrCluster id for this datastore cluster   


* This property cannot be updated.

  
**capacityMB**|  xsd:long|  Maximum capacity of this datastore cluster, in MB   


* This property cannot be updated.

  
**freeSpaceMB**|  xsd:long|  Available capacity of this datastore cluster, in MB   


* This property cannot be updated.

  
**datastores**| [DatastoreInfo[]](vdi.utils.virtualcenter.Datastore.DatastoreInfo.md)|  Datastores which are members of this datastore cluster   


* This property need not be set.
* This property cannot be updated.

  
  
  
 
  
  
