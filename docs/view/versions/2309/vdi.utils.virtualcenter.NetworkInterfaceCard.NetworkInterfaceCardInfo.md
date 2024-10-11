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
> [NetworkInterfaceCard_ListByBaseImageVm](vdi.utils.virtualcenter.NetworkInterfaceCard.md#listByBaseImageVm), [NetworkInterfaceCard_ListBySnapshot](vdi.utils.virtualcenter.NetworkInterfaceCard.md#listBySnapshot), [NetworkInterfaceCard_ListByTemplate](vdi.utils.virtualcenter.NetworkInterfaceCard.md#listByTemplate)

See also  
> [NetworkInterfaceCardData](vdi.utils.virtualcenter.NetworkInterfaceCard.NetworkInterfaceCardData.md), [NetworkInterfaceCardId](vdi.entity.NetworkInterfaceCardId.md)

Since  
> Horizon View 6.0


## Data Object Description 

Network interface card (NIC) information from VC. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [NetworkInterfaceCardId](vdi.entity.NetworkInterfaceCardId.md)|  Network interface card id.   


 * This property cannot be updated.

  
**data**| [NetworkInterfaceCardData](vdi.utils.virtualcenter.NetworkInterfaceCard.NetworkInterfaceCardData.md)|  Network interface card data.   


 * This property cannot be updated.

  
**refId**|  xsd:string|  Reference ID used for this network interface card.  **_Since_** Horizon 8.1  


 * This property need not be set.
 * This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
