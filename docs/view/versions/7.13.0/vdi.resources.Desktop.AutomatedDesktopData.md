---
layout: page
title: Data Object - DesktopAutomatedDesktopData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.AutomatedDesktopData`

Property of
> [DesktopInfo](vdi.resources.Desktop.DesktopInfo.md#field_detail)

See also
> [DesktopCustomizationSettings](vdi.resources.Desktop.CustomizationSettings.md), [DesktopProvisioningStatusData](vdi.resources.Desktop.ProvisioningStatusData.md), [DesktopUserAssignment](vdi.resources.Desktop.UserAssignment.md), [DesktopVirtualCenterManagedCommonSettings](vdi.resources.Desktop.VirtualCenterManagedCommonSettings.md), [DesktopVirtualCenterNamesData](vdi.resources.Desktop.VirtualCenterNamesData.md), [DesktopVirtualCenterProvisioningSettings](vdi.resources.Desktop.VirtualCenterProvisioningSettings.md), [DesktopVirtualMachineNamingSettings](vdi.resources.Desktop.VirtualMachineNamingSettings.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon View 6.0


## Data Object Description

Data for an automated desktop. An automated desktop is a desktop that contains one or more dynamically generated virtual machines that are automatically created and customized by View Manager from a Virtual Center virtual machine template.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**provisioningType**|  xsd:string|  The Source or the Provisioning Type of machines. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>VIRTUAL_CENTER</td><td>Virtual center virtual machines managed as view machines. This option is valid for Automated and Manual Desktop. In case of Automated Desktop, these refer to Full Virtual Machines that are created from a vCenter Server template.</td></tr><tr><td>VIEW_COMPOSER</td><td>View composer linked clones managed as view machines. They share the same base image and use less storage space than full virtual machines. The user profile for linked clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes. This option is only valid for Automated Desktop.</td></tr><tr><td>INSTANT_CLONE_ENGINE</td><td>Instant clone engine created 'instant clones' managed as view machines. Instant clone engine uses vmfork technology to create the instant clones; these clones take very little time for provisioning. Instant clones have many similarities to linked clones. This option is only valid for Automated Desktop.</td></tr></table>
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  Virtual Center server. [^2]
**userAssignment**| [DesktopUserAssignment](vdi.resources.Desktop.UserAssignment.md)|  User assignment scheme.
**vmNamingSettings**| [DesktopVirtualMachineNamingSettings](vdi.resources.Desktop.VirtualMachineNamingSettings.md)|  Specifies the naming scheme for the VMs in the desktop.
**virtualCenterProvisioningSettings**| [DesktopVirtualCenterProvisioningSettings](vdi.resources.Desktop.VirtualCenterProvisioningSettings.md)|  Virtual Center provisioning settings for the automated desktop.
**virtualCenterManagedCommonSettings**| [DesktopVirtualCenterManagedCommonSettings](vdi.resources.Desktop.VirtualCenterManagedCommonSettings.md)|  Common settings for Desktops managed by Virtual Center sources.  **_Since_** Horizon View 6.1
**virtualCenterNamesData**| [DesktopVirtualCenterNamesData](vdi.resources.Desktop.VirtualCenterNamesData.md)|  Naming data for Virtual Center entities associated with this Desktop. [^2]
**provisioningStatusData**| [DesktopProvisioningStatusData](vdi.resources.Desktop.ProvisioningStatusData.md)|  Provisioning status data about this desktop. [^2]
**customizationSettings**| [DesktopCustomizationSettings](vdi.resources.Desktop.CustomizationSettings.md)|  Customization settings for this desktop.


 


[^2]: This property cannot be updated.