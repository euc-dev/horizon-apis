---
layout: page
title: Data Object - DesktopVirtualCenterNetworkingSettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.VirtualCenterNetworkingSettings  
Property of
     [DesktopVirtualCenterProvisioningSettings](vdi.resources.Desktop.VirtualCenterProvisioningSettings.md#field_detail)  
See also
     [DesktopNetworkInterfaceCardSettings](vdi.resources.Desktop.NetworkInterfaceCardSettings.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Virtual Center networking settings. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**nics**| [DesktopNetworkInterfaceCardSettings[]](vdi.resources.Desktop.NetworkInterfaceCardSettings.md)|  Network interface card settings for machines provisioned for this desktop. A NIC may appear at most once in these settings and must be present on this desktop's parent's snapshot or template. Not all NICs need be configured. Any that are not will use default settings.   


* This property need not be set.
  * This property is an unordered array of unique values.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

