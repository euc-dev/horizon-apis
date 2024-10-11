---
layout: page
title: Data Object - CustomizationSpecData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.CustomizationSpec.CustomizationSpecData`

Property of  
> [CustomizationSpecInfo](vdi.utils.virtualcenter.CustomizationSpec.CustomizationSpecInfo.md#field_detail)

See also  
> [CustomizationSpecIncompatibleReasons](vdi.utils.virtualcenter.CustomizationSpec.CustomizationSpecIncompatibleReasons.md)

Since  
> Horizon View 6.0


## Data Object Description 

CustomizationSpecData is a set of attributes for a CustomizationSpec retrieved from the VC. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  Customization Spec name   


* This property cannot be updated.

  
**description**|  xsd:string|  Customization Spec description   


* This property need not be set.
* This property cannot be updated.

  
**guestOS**|  xsd:string|  Guest OS   


* This property need not be set.
* This property cannot be updated.

  
**incompatibleReasons**| [CustomizationSpecIncompatibleReasons](vdi.utils.virtualcenter.CustomizationSpec.CustomizationSpecIncompatibleReasons.md)|  Reasons that may preclude this CustomizationSpec from being used in desktop creation.   


* This property cannot be updated.

  
  
  

  
  
