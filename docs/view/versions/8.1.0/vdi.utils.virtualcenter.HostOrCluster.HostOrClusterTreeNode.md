---
layout: page
title: Data Object - HostOrClusterTreeNode
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.HostOrCluster.HostOrClusterTreeNode  
Property of
     [HostOrClusterTreeContainer](vdi.utils.virtualcenter.HostOrCluster.HostOrClusterTreeContainer.md#field_detail)  
Returned by
     [HostOrCluster_GetHostOrClusterTree](vdi.utils.virtualcenter.HostOrCluster.md#getHostOrClusterTree)  
See also
     [HostOrClusterInfo](vdi.utils.virtualcenter.HostOrCluster.HostOrClusterInfo.md), [HostOrClusterTreeContainer](vdi.utils.virtualcenter.HostOrCluster.HostOrClusterTreeContainer.md)  
Since 
    Horizon View 6.0

## Data Object Description 

A generic tree node that either represents a host or cluster or a container which can contain host or clusters or further nested containers. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**container**|  xsd:boolean|  Whether or not this node is a container or a legitimate host or cluster.   


* This property cannot be updated.

  
**treeContainer**| [HostOrClusterTreeContainer](vdi.utils.virtualcenter.HostOrCluster.HostOrClusterTreeContainer.md)|  Set only if this node represents a container.   


* This property need not be set.
* This property cannot be updated.

  
**info**| [HostOrClusterInfo](vdi.utils.virtualcenter.HostOrCluster.HostOrClusterInfo.md)|  Set only if this node represents a host or cluster.   


* This property need not be set.
* This property cannot be updated.

  
  
  
  
  
  

