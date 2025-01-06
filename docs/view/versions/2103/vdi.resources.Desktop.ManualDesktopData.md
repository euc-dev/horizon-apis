---
layout: page
title: Data Object - DesktopManualDesktopData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.ManualDesktopData`

Property of
> [DesktopInfo](vdi.resources.Desktop.DesktopInfo.md#field_detail)

See also
> [DesktopUserAssignment](vdi.resources.Desktop.UserAssignment.md), [DesktopViewStorageAcceleratorSettings](vdi.resources.Desktop.ViewStorageAcceleratorSettings.md), [DesktopVirtualCenterManagedCommonSettings](vdi.resources.Desktop.VirtualCenterManagedCommonSettings.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon View 6.0


## Data Object Description

Data for a manual desktop. A manual desktop is a desktop of machine sources that is not provisioned automatically. Multiple users are mapped to multiple machines. However, only one user is active on a machine at a time.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**userAssignment**| [DesktopUserAssignment](vdi.resources.Desktop.UserAssignment.md)|  User assignment scheme.
**source**|  xsd:string|  The Source of machines. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>VIRTUAL_CENTER</td><td>Virtual center virtual machines managed as view machines. This option is valid for Automated and Manual Desktop. In case of Automated Desktop, these refer to Full Virtual Machines that are created from a vCenter Server template.</td></tr><tr><td>UNMANAGED</td><td>Non-vCenter Server virtual machines managed as view machines. These can include physical computers, non-vCenter Server virtual machines, and blade PCs. This option is only valid for Manual Desktops.</td></tr></table>
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  Virtual Center server. [^1] [^2] [^50]
**viewStorageAcceleratorSettings**| [DesktopViewStorageAcceleratorSettings](vdi.resources.Desktop.ViewStorageAcceleratorSettings.md)|  View Storage Accelerator settings.
**virtualCenterManagedCommonSettings**| [DesktopVirtualCenterManagedCommonSettings](vdi.resources.Desktop.VirtualCenterManagedCommonSettings.md)|  Common settings for Desktops managed by Virtual Center sources.  **_Since_** Horizon View 6.1 [^1] [^50]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^50]: This property is required if source is set to 'VIRTUAL_CENTER'.