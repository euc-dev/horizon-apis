---
layout: page
title: Data Object - DesktopVirtualMachineNamingSpec
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.VirtualMachineNamingSpec`

Property of
> [DesktopAutomatedDesktopSpec](vdi.resources.Desktop.AutomatedDesktopSpec.md#field_detail)

See also
> [DesktopPatternNamingSettings](vdi.resources.Desktop.PatternNamingSettings.md), [DesktopSpecificNamingSpec](vdi.resources.Desktop.SpecificNamingSpec.md)

Since
> Horizon View 6.0


## Data Object Description

Settings related to the naming of the VMs in the desktop for creation.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**namingMethod**|  xsd:string|  Determines how the VMs in the desktop are named. Note(s) :- [^104] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>SPECIFIED</td><td>List of specified names. All provisioning is done up-front.</td></tr><tr><td>PATTERN</td><td>Naming pattern.</td></tr></table>
**patternNamingSettings**| [DesktopPatternNamingSettings](vdi.resources.Desktop.PatternNamingSettings.md)|  Naming pattern settings. [^1] [^102]
**specificNamingSpec**| [DesktopSpecificNamingSpec](vdi.resources.Desktop.SpecificNamingSpec.md)|  Specified name settings. [^1] [^103]


 
