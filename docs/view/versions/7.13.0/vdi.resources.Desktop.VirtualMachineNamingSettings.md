---
layout: page
title: Data Object - DesktopVirtualMachineNamingSettings
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.VirtualMachineNamingSettings`

Property of
> [DesktopAutomatedDesktopData](vdi.resources.Desktop.AutomatedDesktopData.md#field_detail)

See also
> [DesktopPatternNamingSettings](vdi.resources.Desktop.PatternNamingSettings.md), [DesktopSpecificNamingSettings](vdi.resources.Desktop.SpecificNamingSettings.md)

Since
> Horizon View 6.0


## Data Object Description

Settings related to the naming of the VMs in the desktop.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**namingMethod**|  xsd:string|  Determines how the VMs in the desktop are named. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>SPECIFIED</td><td>List of specified names. All provisioning is done up-front.</td></tr><tr><td>PATTERN</td><td>Naming pattern.</td></tr></table>
**patternNamingSettings**| [DesktopPatternNamingSettings](vdi.resources.Desktop.PatternNamingSettings.md)|  Naming pattern settings. [^1] [^102]
**specificNamingSettings**| [DesktopSpecificNamingSettings](vdi.resources.Desktop.SpecificNamingSettings.md)|  Specified name settings. [^1] [^103]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^102]: This property is required if namingMethod is set to 'PATTERN'.
[^103]: This property is required if namingMethod is set to 'SPECIFIED'.