---
layout: page
title: Data Object - CustomizationSpecData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.CustomizationSpec.CustomizationSpecData`

Property of
> [CustomizationSpecInfo](vdi.utils.virtualcenter.CustomizationSpec.CustomizationSpecInfo.md#field_detail)

See also
> [CustomizationSpecIncompatibleReasons](vdi.utils.virtualcenter.CustomizationSpec.CustomizationSpecIncompatibleReasons.md)

Since
> Horizon View 6.0


## Data Object Description

CustomizationSpecData is a set of attributes for a CustomizationSpec retrieved from the VC.
 [^167]



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**name**|  xsd:string|  Customization Spec name [^2]
**description**|  xsd:string|  Customization Spec description [^1] [^2]
**guestOS**|  xsd:string|  Guest OS [^1] [^2]
**incompatibleReasons**| [CustomizationSpecIncompatibleReasons](vdi.utils.virtualcenter.CustomizationSpec.CustomizationSpecIncompatibleReasons.md)|  Reasons that may preclude this CustomizationSpec from being used in desktop creation. [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.