---
layout: page
title: Data Object - NetworkInterfaceCardData
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.NetworkInterfaceCard.NetworkInterfaceCardData`

Property of
> [NetworkInterfaceCardInfo](vdi.utils.virtualcenter.NetworkInterfaceCard.NetworkInterfaceCardInfo.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Set of attributes for a network interface card retrieved from the VC.
 [^167]



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**name**|  xsd:string|  The network interface card's VC display name. [^1] [^2]
**macAddress**|  xsd:string|  The network interface card's MAC address. [^1] [^2]
**networkType**|  xsd:string|  Type of network interface card.  **_Since_** Horizon 8.4 [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"Network"</td><td>Standard network</td></tr><tr><td>"OpaqueNetwork"</td><td>Opaque network</td></tr><tr><td>"DistributedVirtualPortgroup"</td><td>DVS port group</td></tr></table>


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.