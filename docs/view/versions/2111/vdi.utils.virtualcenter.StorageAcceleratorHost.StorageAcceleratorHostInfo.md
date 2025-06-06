---
layout: page
title: Data Object - StorageAcceleratorHostInfo
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.StorageAcceleratorHost.StorageAcceleratorHostInfo`

Returned by
> [StorageAcceleratorHost_ListByServerDefinition](vdi.utils.virtualcenter.StorageAcceleratorHost.md#listByServerDefinition), [StorageAcceleratorHost_ListByVirtualCenter](vdi.utils.virtualcenter.StorageAcceleratorHost.md#listByVirtualCenter)

Since
> Horizon View 6.0


## Data Object Description

Information on a host which supports View Storage Accelerator.
 [^167]



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**name**|  xsd:string|  Host or cluster display name
**path**|  xsd:string|  Host or cluster path
**hostVersion**|  xsd:string|  Version of the host.  **_Since_** Horizon 8.0 [^2]


 


[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.