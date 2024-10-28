---
layout: page
title: Data Object - CustomizationSpecInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.CustomizationSpec.CustomizationSpecInfo`

Returned by
> [CustomizationSpec_List](vdi.utils.virtualcenter.CustomizationSpec.md#list)

See also
> [CustomizationSpecData](vdi.utils.virtualcenter.CustomizationSpec.CustomizationSpecData.md), [CustomizationSpecId](vdi.entity.CustomizationSpecId.md)

Since
> Horizon View 6.0


## Data Object Description

CustomizationSpecInfo aggregates CustomizationSpecData with CustomizationSpecId for Customization specs retrieved from the VC.
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [CustomizationSpecId](vdi.entity.CustomizationSpecId.md)|  CustomizationSpec Id [^2]
**customizationSpecData**| [CustomizationSpecData](vdi.utils.virtualcenter.CustomizationSpec.CustomizationSpecData.md)|  CustomizationSpecInfo data [^2]


 


[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.