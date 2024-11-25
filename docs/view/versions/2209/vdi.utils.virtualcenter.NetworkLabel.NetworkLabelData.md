---
layout: page
title: Data Object - NetworkLabelData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.NetworkLabel.NetworkLabelData`

Property of
> [NetworkLabelInfo](vdi.utils.virtualcenter.NetworkLabel.NetworkLabelInfo.md#field_detail)

See also
> [NetworkLabelIncompatibleReasons](vdi.utils.virtualcenter.NetworkLabel.NetworkLabelIncompatibleReasons.md)

Since
> Horizon View 6.0


## Data Object Description

Set of attributes for a network label retrieved from the VC.
 [^167]



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**name**|  xsd:string|  The network label's VC display name. [^1] [^2]
**switchType**|  xsd:string|  The network label's switch type. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"STANDARD_SWITCH"</td><td>Standard Switch</td></tr><tr><td>"DISTRIBUTED_VIRTUAL_SWITCH"</td><td>Distributed Virtual Switch</td></tr><tr><td>"NSX_NETWORK_SWITCH"</td><td>NSX network switch</td></tr></table>
**incompatibleReasons**| [NetworkLabelIncompatibleReasons](vdi.utils.virtualcenter.NetworkLabel.NetworkLabelIncompatibleReasons.md)|  Reasons that may preclude this NetworkLabel from being used in desktop configuration. [^2]
**labelType**|  xsd:string|  The network label's type.  **_Since_** Horizon 7.1 [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"earlyBinding"</td><td>A free DistributedVirtualPort will be selected and assigned to a Virtual Machine when the Virtual Machine is reconfigured to connect to the portgroup. NGVC Instant clones/farms only support earlyBinding port group type.</td></tr><tr><td>"ephemeral"</td><td>A DistributedVirtualPort will be created and assigned to a Virtual Machine when the Virtual Machine is powered on, and will be deleted when the Virtual Machine is powered off. An ephemeral portgroup has no limit on the number of ports that can be a part of this portgroup. In cases where the vCenter Server is unavailable the host can create conflict ports in this portgroup to be used by a Virtual Machine at power on.</td></tr><tr><td>"lateBinding"</td><td>deprecated as of vSphere API 5.0 A free DistributedVirtualPort will be selected and assigned to a Virtual Machine when the Virtual Machine is powered on.</td></tr></table>
**maxNumOfPort**|  xsd:int|  The total number of ports present.  **_Since_** Horizon 7.1 [^1] [^2]
**availablePorts**|  xsd:int|  Available ports in network label.  **_Since_** Horizon 7.1 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.