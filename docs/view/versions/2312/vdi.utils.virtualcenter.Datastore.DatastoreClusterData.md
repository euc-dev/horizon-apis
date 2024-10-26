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
**name**|  xsd:string|  Datastore Cluster name [^2]
**path**|  xsd:string|  Datastore Cluster path [^2]
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  VirtualCenter id for this datastore cluster [^2]
**datacenter**| [DatacenterId](vdi.entity.DatacenterId.md)|  Datacenter id for this datastore cluster [^1] [^2]
**hostOrCluster**| [HostOrClusterId](vdi.entity.HostOrClusterId.md)|  HostOrCluster id for this datastore cluster [^2]
**capacityMB**|  xsd:long|  Maximum capacity of this datastore cluster, in MB [^2]
**freeSpaceMB**|  xsd:long|  Available capacity of this datastore cluster, in MB [^2]
**datastores**| [DatastoreInfo[]](vdi.utils.virtualcenter.Datastore.DatastoreInfo.md)|  Datastores which are members of this datastore cluster [^1] [^2]


 
