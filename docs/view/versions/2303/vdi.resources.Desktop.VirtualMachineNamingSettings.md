---
layout: page
title: Data Object - DesktopVirtualMachineNamingSettings
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.VirtualMachineNamingSettings`

Property of  
> [DesktopAutomatedDesktopData](vdi.resources.Desktop.AutomatedDesktopData.md#field_detail)

See also  
> [DesktopPatternNamingSettings](vdi.resources.Desktop.PatternNamingSettings.md), [DesktopSpecificNamingSettings](vdi.resources.Desktop.SpecificNamingSettings.md)

Since  
> Horizon View 6.0


## Data Object Description 

Settings related to the naming of the VMs in the desktop. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**namingMethod**|  xsd:string|  Determines how the VMs in the desktop are named.   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"SPECIFIED"| List of specified names. All provisioning is done up-front.  
"PATTERN"| Naming pattern.  

  
**patternNamingSettings**| [DesktopPatternNamingSettings](vdi.resources.Desktop.PatternNamingSettings.md)|  Naming pattern settings.   


* This property need not be set.
  * This property is required if namingMethod is set to "PATTERN".

  
**specificNamingSettings**| [DesktopSpecificNamingSettings](vdi.resources.Desktop.SpecificNamingSettings.md)|  Specified name settings.   


* This property need not be set.
  * This property is required if namingMethod is set to "SPECIFIED".

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
