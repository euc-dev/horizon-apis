---
layout: page
title: Data Object - DesktopSpecifiedName
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.SpecifiedName`

Property of
> [DesktopSpecificNamingSettings](vdi.resources.Desktop.SpecificNamingSettings.md#field_detail), [DesktopSpecificNamingSpec](vdi.resources.Desktop.SpecificNamingSpec.md#field_detail)

Parameter to
> [Desktop_AddMachinesToSpecifiedNamingDesktop](vdi.resources.Desktop.md#addMachinesToSpecifiedNamingDesktop), [Desktop_AddMachineToSpecifiedNamingDesktop](vdi.resources.Desktop.md#addMachineToSpecifiedNamingDesktop)

See also
> [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0


## Data Object Description

Fields for specifying a VM name and optional user id to entitle the user to the VM in case of dedicated desktops.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**vmName**|  xsd:string|  The name of the machine. [^80]
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User to assign to the machine in case of dedicated desktops. [^1]


 


[^1]: This property need not be set.
[^80]: This property must contain only alphanumerics and dashes. It must contain at least one alpha character. The maximum length is 15 characters.