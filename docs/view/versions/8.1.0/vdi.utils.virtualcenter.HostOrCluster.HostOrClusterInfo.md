---
layout: page
title: Data Object - HostOrClusterInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.HostOrCluster.HostOrClusterInfo`

Property of  
> [HostOrClusterTreeNode](vdi.utils.virtualcenter.HostOrCluster.HostOrClusterTreeNode.md#field_detail)

See also  
> [DatacenterId](vdi.entity.DatacenterId.md), [HostOrClusterId](vdi.entity.HostOrClusterId.md), [HostOrClusterIncompatibleReasons](vdi.utils.virtualcenter.HostOrCluster.HostOrClusterIncompatibleReasons.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since  
> Horizon View 6.0


## Data Object Description 

Information about a host or cluster. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [HostOrClusterId](vdi.entity.HostOrClusterId.md)|  Host or Cluster Id   


* This property cannot be updated.

  
**cluster**|  xsd:boolean|  Whether or not this is a cluster or a host.   


* This property cannot be updated.

  
**name**|  xsd:string|  Host or cluster display name   


* This property cannot be updated.

  
**path**|  xsd:string|  Host or cluster path   


* This property cannot be updated.

  
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  VirtualCenter id for this host or cluster.   


* This property cannot be updated.

  
**datacenter**| [DatacenterId](vdi.entity.DatacenterId.md)|  Datacenter id for this host or cluster.   


* This property need not be set.
* This property cannot be updated.

  
**vGPUTypes**|  xsd:string[]|  Types of NVIDIA GRID vGPUs supported by this host or at least one host on this cluster. If unset, this host or cluster does not support NVIDIA GRID vGPUs and cannot be used for desktop creation with NVIDIA GRID vGPU support enabled.  **_Since_** Horizon View 6.1  


* This property need not be set.
  * This property is an unordered array of unique values.
* This property cannot be updated.

  
**incompatibleReasons**| [HostOrClusterIncompatibleReasons](vdi.utils.virtualcenter.HostOrCluster.HostOrClusterIncompatibleReasons.md)|  Reasons that may preclude this HostOrCluster from being used in desktop creation.   


* This property cannot be updated.

  
**refId**|  xsd:string|  Reference ID used for this host or cluster.  **_Since_** Horizon 8.1  


* This property need not be set.
* This property cannot be updated.

  
  
  
  
  
  
