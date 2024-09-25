---
layout: page
title: Data Object - HostOrClusterIncompatibleReasons
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.HostOrCluster.HostOrClusterIncompatibleReasons
Property of
     [HostOrClusterInfo](vdi.utils.virtualcenter.HostOrCluster.HostOrClusterInfo.md#field_detail)
Since 
    Horizon View 6.0

## Data Object Description 

Reasons that may preclude this HostOrCluster from being used in desktop creation. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**unsupportedESXVersion**|  xsd:boolean|  Whether or not the host or at least one host in the cluster has an ESX version unsupported by View. If true, this host or cluster cannot be used in desktop creation.   


[^2]

  
**allHostsDisconnected**|  xsd:boolean|  Whether or not the host or at least one host in the cluster is disconnected. If true, this host or cluster cannot be used in desktop creation.   


[^2]

  
**noHostsInCluster**|  xsd:boolean|  If this is a cluster, whether or not it contains no hosts. If true, this host or cluster cannot be used in desktop creation.   


[^2]

  
**incompatibleVSAN**|  xsd:boolean|  Whether or not the host or at least one host in the cluster is incompatible with VSAN. This validates against the host or cluster's VC version, the host or cluster's own version, and whether or not at least one datastore in the host or cluster has a VSAN filesystem. If true, this host or cluster cannot be used in desktop creation with VSAN enabled.   


[^2]

  
**incompatibleStorageAccelerator**|  xsd:boolean|  Whether or not the host or at least one host in the cluster is incompatible with the storage accelerator feature. This validates against the host or cluster's version. If true, this host or cluster cannot be used in desktop creation with storage accelerator enabled.   


[^2]

  
**incompatibleNativeSnapshots**|  xsd:boolean|  Whether or not the host or at least one host in the cluster is incompatible with the native snapshot feature. This validates against the host or cluster's VC version and the host or cluster's own version. This does not validate whether or not all datastores in the host or cluster support native snapshots. If true, this host or cluster cannot be used in desktop creation with native snapshots enabled.   


[^2]

  
**incompatibleInstantCloneDesktops**|  xsd:boolean|  Whether or not this cluster and all the hosts in this cluster support instant clone feature. This check validates that the Cluster's version and version of all the hosts in this cluster are at least 6.0 or above. If true, this cluster cannot be used in instant clone desktop creation. Note that only clusters can be selected for instant clone desktops.  **_Since_** Horizon 7.0  


[^2]

  
**incompatibleStandaloneHostForInstantClone**|  xsd:boolean|  Whether or not this host is part of a cluster. Standalone hosts can not be used for Instant clones. This will be false if [cluster](vdi.utils.virtualcenter.HostOrCluster.HostOrClusterInfo.md#cluster) is set to true.  **_Since_** Horizon 7.7  


[^1]
[^2]

  
**incompatiblevGPUType**|  xsd:boolean|  Whether or not this host or at least one host on this cluster supports NVIDIA GRID vGPUs.  **_Since_** Horizon 7.7  


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

