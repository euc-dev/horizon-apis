---
layout: page
title: Data Object - HostOrClusterTreeContainer
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.HostOrCluster.HostOrClusterTreeContainer`

Property of
> [HostOrClusterTreeNode](vdi.utils.virtualcenter.HostOrCluster.HostOrClusterTreeNode.md#field_detail)

See also
> [HostOrClusterTreeNode](vdi.utils.virtualcenter.HostOrCluster.HostOrClusterTreeNode.md)

Since
> Horizon View 6.0


## Data Object Description

Information about a host or cluster container.
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**name**|  xsd:string|  Host or cluster container node display name. [^2]
**path**|  xsd:string|  Host or cluster container node path. [^2]
**type**|  xsd:string|  Type of container. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"DATACENTER"</td><td>A datacenter container, which is usually the root of the host or cluster tree.</td></tr><tr><td>"FOLDER"</td><td>A folder container.</td></tr><tr><td>"OTHER"</td><td>Some other container type.</td></tr></table>
**children**| [HostOrClusterTreeNode[]](vdi.utils.virtualcenter.HostOrCluster.HostOrClusterTreeNode.md)|  Contents of the container. These may be hosts or clusters or further nested containers. [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.