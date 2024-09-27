---
layout: page
title: Data Object - NetworkInterfaceCardData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.NetworkInterfaceCard.NetworkInterfaceCardData  
Property of
     [NetworkInterfaceCardInfo](vdi.utils.virtualcenter.NetworkInterfaceCard.NetworkInterfaceCardInfo.md#field_detail)  
Since 
    Horizon View 6.0

## Data Object Description 

Set of attributes for a network interface card retrieved from the VC. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  The network interface card's VC display name.   


* This property need not be set.
* This property cannot be updated.

  
**macAddress**|  xsd:string|  The network interface card's MAC address.   


* This property need not be set.
* This property cannot be updated.

  
**networkType**|  xsd:string|  Type of network interface card.  **_Since_** Horizon 8.4  


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"Network"| Standard network  
"OpaqueNetwork"| Opaque network  
"DistributedVirtualPortgroup"| DVS port group  

  
  
  
   
  
  

