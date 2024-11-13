---
layout: page
title: Data Object - HostOrClusterInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.HostOrCluster.HostOrClusterInfo`

Property of
> [HostOrClusterTreeNode](vdi.utils.virtualcenter.HostOrCluster.HostOrClusterTreeNode.md#field_detail)

See also
> [DatacenterId](vdi.entity.DatacenterId.md), [HostOrClusterId](vdi.entity.HostOrClusterId.md), [HostOrClusterIncompatibleReasons](vdi.utils.virtualcenter.HostOrCluster.HostOrClusterIncompatibleReasons.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon View 6.0


## Data Object Description

Information about a host or cluster.
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [HostOrClusterId](vdi.entity.HostOrClusterId.md)|  Host or Cluster Id [^2]
**cluster**|  xsd:boolean|  Whether or not this is a cluster or a host. [^2]
**name**|  xsd:string|  Host or cluster display name [^2]
**path**|  xsd:string|  Host or cluster path [^2]
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  VirtualCenter id for this host or cluster. [^2]
**datacenter**| [DatacenterId](vdi.entity.DatacenterId.md)|  Datacenter id for this host or cluster. [^1] [^2]
**vGPUTypes**|  xsd:string[]|  Types of NVIDIA GRID vGPUs supported by this host or at least one host on this cluster. If unset, this host or cluster does not support NVIDIA GRID vGPUs and cannot be used for desktop creation with NVIDIA GRID vGPU support enabled.  **_Since_** Horizon View 6.1 [^1] [^14] [^2]
**incompatibleReasons**| [HostOrClusterIncompatibleReasons](vdi.utils.virtualcenter.HostOrCluster.HostOrClusterIncompatibleReasons.md)|  Reasons that may preclude this HostOrCluster from being used in desktop creation. [^2]
**refId**|  xsd:string|  Reference ID used for this host or cluster.  **_Since_** Horizon 8.1 [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^14]: This property is an unordered array of unique values.
[^167]: This data object must be updated as a whole.