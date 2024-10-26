---
layout: page
title: Data Object - FarmVirtualCenterNetworkingSettings
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.VirtualCenterNetworkingSettings`

Property of
> [FarmVirtualCenterProvisioningSettings](vdi.resources.Farm.VirtualCenterProvisioningSettings.md#field_detail)

See also
> [FarmNetworkInterfaceCardSettings](vdi.resources.Farm.NetworkInterfaceCardSettings.md)

Since
> Horizon View 6.2


## Data Object Description

Virtual Center networking settings.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**nics**| [FarmNetworkInterfaceCardSettings[]](vdi.resources.Farm.NetworkInterfaceCardSettings.md)|  Network interface card settings for RDS Servers provisioned for this farm. A NIC may appear at most once in these settings and must be present on this RDS Server's parent's snapshot. Not all NICs need be configured. Any that are not will use default settings. [^1] [^14]


 


[^1]: This property need not be set.
[^14]: This property is an unordered array of unique values.