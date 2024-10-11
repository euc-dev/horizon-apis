---
layout: page
title: Data Object - NetworkLabelData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.NetworkLabel.NetworkLabelData`

Property of  
> [NetworkLabelInfo](vdi.utils.virtualcenter.NetworkLabel.NetworkLabelInfo.md#field_detail)

See also  
> [NetworkLabelIncompatibleReasons](vdi.utils.virtualcenter.NetworkLabel.NetworkLabelIncompatibleReasons.md)

Since  
> Horizon View 6.0


## Data Object Description 

Set of attributes for a network label retrieved from the VC. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  The network label's VC display name.   


 * This property need not be set.
 * This property cannot be updated.

  
**switchType**|  xsd:string|  The network label's switch type.   


 * This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"STANDARD_SWITCH"| Standard Switch  
"DISTRIBUTED_VIRTUAL_SWITCH"| Distributed Virtual Switch  
"NSX_NETWORK_SWITCH"| NSX network switch  

  
**incompatibleReasons**| [NetworkLabelIncompatibleReasons](vdi.utils.virtualcenter.NetworkLabel.NetworkLabelIncompatibleReasons.md)|  Reasons that may preclude this NetworkLabel from being used in desktop configuration.   


 * This property cannot be updated.

  
**labelType**|  xsd:string|  The network label's type.  **_Since_** Horizon 7.1  


 * This property need not be set.
 * This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"earlyBinding"| A free DistributedVirtualPort will be selected and assigned to a Virtual Machine when the Virtual Machine is reconfigured to connect to the portgroup. NGVC Instant clones/farms only support earlyBinding port group type.  
"ephemeral"| A DistributedVirtualPort will be created and assigned to a Virtual Machine when the Virtual Machine is powered on, and will be deleted when the Virtual Machine is powered off. An ephemeral portgroup has no limit on the number of ports that can be a part of this portgroup. In cases where the vCenter Server is unavailable the host can create conflict ports in this portgroup to be used by a Virtual Machine at power on.  
"lateBinding"| deprecated as of vSphere API 5.0 A free DistributedVirtualPort will be selected and assigned to a Virtual Machine when the Virtual Machine is powered on.  

  
**maxNumOfPort**|  xsd:int|  The total number of ports present.  **_Since_** Horizon 7.1  


 * This property need not be set.
 * This property cannot be updated.

  
**availablePorts**|  xsd:int|  Available ports in network label.  **_Since_** Horizon 7.1  


 * This property need not be set.
 * This property cannot be updated.

  
  

  
