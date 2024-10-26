---
layout: page
title: Data Object - NetworkLabelInfo
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.NetworkLabel.NetworkLabelInfo`

Returned by
> [NetworkLabel_ListByHostOrCluster](vdi.utils.virtualcenter.NetworkLabel.md#listByHostOrCluster), [NetworkLabel_ListByNetworkLabelSpec](vdi.utils.virtualcenter.NetworkLabel.md#listByNetworkLabelSpec)

See also
> [NetworkLabelData](vdi.utils.virtualcenter.NetworkLabel.NetworkLabelData.md), [NetworkLabelId](vdi.entity.NetworkLabelId.md)

Since
> Horizon View 6.0


## Data Object Description

Network label information from VC.
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [NetworkLabelId](vdi.entity.NetworkLabelId.md)|  Network label id. [^2]
**data**| [NetworkLabelData](vdi.utils.virtualcenter.NetworkLabel.NetworkLabelData.md)|  Network label data. [^2]


 


[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.