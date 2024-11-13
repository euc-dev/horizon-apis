---
layout: page
title: Data Object - NetworkLabelSpec
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.NetworkLabel.NetworkLabelSpec`

Parameter to
> [NetworkLabel_ListByNetworkLabelSpec](vdi.utils.virtualcenter.NetworkLabel.md#listByNetworkLabelSpec)

See also
> [HostOrClusterId](vdi.entity.HostOrClusterId.md)

Since
> Horizon 7.9


## Data Object Description

Specification to hold the cluster or host id and the type of network.
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**hostOrClusterId**| [HostOrClusterId](vdi.entity.HostOrClusterId.md)|  The host or cluster id, network label should belong to.
**networkType**|  xsd:string|  The type of network, network label should belong to. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"Network"</td><td>Standard network</td></tr><tr><td>"OpaqueNetwork"</td><td>Opaque network</td></tr><tr><td>"DistributedVirtualPortgroup"</td><td>DVS port group</td></tr></table>




 


[^1]: This property need not be set.
[^167]: This data object must be updated as a whole.