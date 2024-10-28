---
layout: page
title: Data Object - VmTemplateIncompatibleReasons
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.VmTemplate.VmTemplateIncompatibleReasons`

Property of
> [VmTemplateInfo](vdi.utils.virtualcenter.VmTemplate.VmTemplateInfo.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Reasons that may preclude this VmTemplate from being used in full clone desktop creation.
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**unsupportedOS**|  xsd:boolean|  This VmTemplate has an unsupported operating system. Certain server operating systems are only supported when [enableServerInSingleUserMode](vdi.infrastructure.GlobalSettings.GeneralData.md#enableServerInSingleUserMode) is enabled. If true, this cannot be used in desktop creation. [^2]


 


[^2]: This property cannot be updated.
[^167]: This data object must be updated as a whole.