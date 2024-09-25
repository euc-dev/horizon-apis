---
layout: page
title: Data Object - DesktopVirtualMachineNamingSpec
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.VirtualMachineNamingSpec
Property of
     [DesktopAutomatedDesktopSpec](vdi.resources.Desktop.AutomatedDesktopSpec.md#field_detail)
See also
     [DesktopPatternNamingSettings](vdi.resources.Desktop.PatternNamingSettings.md), [DesktopSpecificNamingSpec](vdi.resources.Desktop.SpecificNamingSpec.md)
Since 
    Horizon View 6.0

## Data Object Description 

Settings related to the naming of the VMs in the desktop for creation. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**namingMethod**|  xsd:string|  Determines how the VMs in the desktop are named. Note(s) :-  


  * For Instant clone desktops, this setting can only be set to PATTERN.

  


  * This property will be one of:  
|  Value |  Description   
---|---  
"SPECIFIED"| List of specified names. All provisioning is done up-front.  
"PATTERN"| Naming pattern.  

  
**patternNamingSettings**| [DesktopPatternNamingSettings](vdi.resources.Desktop.PatternNamingSettings.md)|  Naming pattern settings.   


[^1]
  * This property is required if namingMethod is set to "PATTERN".

  
**specificNamingSpec**| [DesktopSpecificNamingSpec](vdi.resources.Desktop.SpecificNamingSpec.md)|  Specified name settings.   


[^1]
  * This property is required if namingMethod is set to "SPECIFIED".

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
