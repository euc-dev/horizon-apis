---
layout: page
title: Data Object - CustomizationSpecIncompatibleReasons
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.CustomizationSpec.CustomizationSpecIncompatibleReasons
Property of
     [CustomizationSpecData](vdi.utils.virtualcenter.CustomizationSpec.CustomizationSpecData.md#field_detail)
Since 
    Horizon View 6.0

## Data Object Description 

Reasons that may preclude this CustomizationSpec from being used in desktop creation. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**dhcpNotConfigured**|  xsd:boolean|  Whether or not the customization spec has DHCP configured. If true, this customization spec cannot be used in desktop creation.   


[^2]

  
**notWindows**|  xsd:boolean| **Deprecated.**_Use[unSupportedOS](vdi.utils.virtualcenter.CustomizationSpec.CustomizationSpecIncompatibleReasons.md#unSupportedOS) instead. Whether or not the customization spec is for a Windows-based operating system. If true, this customization spec cannot be used in desktop creation. _   


[^2]

  
**unSupportedOS**|  xsd:boolean|  Whether or not customization spec contains unsupported operating system. Currently the supported operating systems are Windows and Linux. If true, this customization spec cannot be used in desktop creation.  **_Since_** Horizon 7.9  


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

