---
layout: page
title: Data Object - ResourcePoolData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.ResourcePool.ResourcePoolData`

Property of
> [ResourcePoolInfo](vdi.utils.virtualcenter.ResourcePool.ResourcePoolInfo.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

ResourcePoolData is a set of attributes for a ResourcePool retrieved from the VC.
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**name**|  xsd:string|  ResourcePool display name [^2]
**path**|  xsd:string|  ResourcePool path [^2]
**type**|  xsd:string|  The type of this resource pool node. Some types may not be suitable for desktop creation. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"HOST_OR_CLUSTER"</td><td>A host or cluster used as a resource pool suitable for use in desktop creation.</td></tr><tr><td>"RESOURCE_POOL"</td><td>A regular resource pool suitable for use in desktop creation.</td></tr><tr><td>"OTHER"</td><td>Some other resource type that cannot be used in desktop creation.</td></tr></table>
**isCluster**|  xsd:boolean|  Whether the Resource Pool is a Cluster Node.  **_Since_** Horizon 7.9 [^2]
 


 


[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.