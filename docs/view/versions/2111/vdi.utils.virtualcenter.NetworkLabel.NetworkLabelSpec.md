---
layout: page
title: Data Object - NetworkLabelSpec
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.NetworkLabel.NetworkLabelSpec`

Parameter to  
> [NetworkLabel_ListByNetworkLabelSpec](vdi.utils.virtualcenter.NetworkLabel.md#listByNetworkLabelSpec)

See also  
> [HostOrClusterId](vdi.entity.HostOrClusterId.md)

Since  
> Horizon 7.9


## Data Object Description 

Specification to hold the cluster or host id and the type of network. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**hostOrClusterId**| [HostOrClusterId](vdi.entity.HostOrClusterId.md)|  The host or cluster id, network label should belong to.   
  
**networkType**|  xsd:string|  The type of network, network label should belong to.   


* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"Network"| Standard network  
"OpaqueNetwork"| Opaque network  
"DistributedVirtualPortgroup"| DVS port group  

  
  
  
   
  
  
