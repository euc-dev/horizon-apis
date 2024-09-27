---
layout: page
title: Data Object - FarmVirtualCenterNetworkingSettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Farm.VirtualCenterNetworkingSettings  
Property of
     [FarmVirtualCenterProvisioningSettings](vdi.resources.Farm.VirtualCenterProvisioningSettings.md#field_detail)  
See also
     [FarmNetworkInterfaceCardSettings](vdi.resources.Farm.NetworkInterfaceCardSettings.md)  
Since 
    Horizon View 6.2

## Data Object Description 

Virtual Center networking settings. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**nics**| [FarmNetworkInterfaceCardSettings[]](vdi.resources.Farm.NetworkInterfaceCardSettings.md)|  Network interface card settings for RDS Servers provisioned for this farm. A NIC may appear at most once in these settings and must be present on this RDS Server's parent's snapshot. Not all NICs need be configured. Any that are not will use default settings.   


* This property need not be set.
  * This property is an unordered array of unique values.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

