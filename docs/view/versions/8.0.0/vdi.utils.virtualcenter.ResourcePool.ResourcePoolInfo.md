---
layout: page
title: Data Object - ResourcePoolInfo
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.ResourcePool.ResourcePoolInfo`

Property of
> [ResourcePoolInfo](vdi.utils.virtualcenter.ResourcePool.ResourcePoolInfo.md#field_detail)

Returned by
> [ResourcePool_GetResourcePoolTree](vdi.utils.virtualcenter.ResourcePool.md#getResourcePoolTree)

See also
> [ResourcePoolData](vdi.utils.virtualcenter.ResourcePool.ResourcePoolData.md), [ResourcePoolId](vdi.entity.ResourcePoolId.md),

Since
> Horizon View 6.0


## Data Object Description

ResourcePoolInfo aggregates ResourcePoolData retrieved from the VC. It is a tree-structure.
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [ResourcePoolId](vdi.entity.ResourcePoolId.md)|  ResourcePool Id [^2]
**resourcePoolData**| [ResourcePoolData](vdi.utils.virtualcenter.ResourcePool.ResourcePoolData.md)|  ResourcePool display data [^2]
**children**| [ResourcePoolInfo[]](vdi.utils.virtualcenter.ResourcePool.ResourcePoolInfo.md)|  Children nodes of the tree-structure [^1] [^2]


 
