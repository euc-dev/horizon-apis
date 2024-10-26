---
layout: page
title: Data Object - NetworkInterfaceCardInfo
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.NetworkInterfaceCard.NetworkInterfaceCardInfo`

Returned by
> [NetworkInterfaceCard_ListBySnapshot](vdi.utils.virtualcenter.NetworkInterfaceCard.md#listBySnapshot), [NetworkInterfaceCard_ListByTemplate](vdi.utils.virtualcenter.NetworkInterfaceCard.md#listByTemplate)

See also
> [NetworkInterfaceCardData](vdi.utils.virtualcenter.NetworkInterfaceCard.NetworkInterfaceCardData.md), [NetworkInterfaceCardId](vdi.entity.NetworkInterfaceCardId.md)

Since
> Horizon View 6.0


## Data Object Description

Network interface card (NIC) information from VC.
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [NetworkInterfaceCardId](vdi.entity.NetworkInterfaceCardId.md)|  Network interface card id. [^2]
**data**| [NetworkInterfaceCardData](vdi.utils.virtualcenter.NetworkInterfaceCard.NetworkInterfaceCardData.md)|  Network interface card data. [^2]


 


[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.