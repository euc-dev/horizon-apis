---
layout: page
title: Data Object - CustomizationSpecData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.CustomizationSpec.CustomizationSpecData
Property of
     [CustomizationSpecInfo](vdi.utils.virtualcenter.CustomizationSpec.CustomizationSpecInfo.md#field_detail)
See also
     [CustomizationSpecIncompatibleReasons](vdi.utils.virtualcenter.CustomizationSpec.CustomizationSpecIncompatibleReasons.md)
Since 
    Horizon View 6.0

## Data Object Description 

CustomizationSpecData is a set of attributes for a CustomizationSpec retrieved from the VC. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  Customization Spec name   


[^2]

  
**description**|  xsd:string|  Customization Spec description   


[^1]
[^2]

  
**guestOS**|  xsd:string|  Guest OS   


[^1]
[^2]

  
**incompatibleReasons**| [CustomizationSpecIncompatibleReasons](vdi.utils.virtualcenter.CustomizationSpec.CustomizationSpecIncompatibleReasons.md)|  Reasons that may preclude this CustomizationSpec from being used in desktop creation.   


[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

