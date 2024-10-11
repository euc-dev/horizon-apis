---
layout: page
title: Data Object - VmTemplateIncompatibleReasons
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.VmTemplate.VmTemplateIncompatibleReasons`

Property of  
> [VmTemplateInfo](vdi.utils.virtualcenter.VmTemplate.VmTemplateInfo.md#field_detail)

Since  
> Horizon View 6.0


## Data Object Description 

Reasons that may preclude this VmTemplate from being used in full clone desktop creation. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**unsupportedOS**|  xsd:boolean|  This VmTemplate has an unsupported operating system. Certain server operating systems are only supported when [enableServerInSingleUserMode](vdi.infrastructure.GlobalSettings.GeneralData.md#enableServerInSingleUserMode) is enabled. If true, this cannot be used in desktop creation.   


 * This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
