---
layout: page
title: Data Object - DesktopAutomatedDesktopSpec
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.AutomatedDesktopSpec`

Property of
> [DesktopSpec](vdi.resources.Desktop.DesktopSpec.md#field_detail)

See also
> [DesktopCustomizationSettings](vdi.resources.Desktop.CustomizationSettings.md), [DesktopUserAssignment](vdi.resources.Desktop.UserAssignment.md), [DesktopVirtualCenterManagedCommonSettings](vdi.resources.Desktop.VirtualCenterManagedCommonSettings.md), [DesktopVirtualCenterProvisioningSettings](vdi.resources.Desktop.VirtualCenterProvisioningSettings.md), [DesktopVirtualMachineNamingSpec](vdi.resources.Desktop.VirtualMachineNamingSpec.md), [PartnerDesktopSettings](vdi.resources.Desktop.PartnerDesktopSettings.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon View 6.0


## Data Object Description

Specification for an automated desktop. An automated desktop is a desktop that contains one or more dynamically generated virtual machines that are automatically created and customized by View Manager from a Virtual Center virtual machine template.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**provisioningType**|  xsd:string|  The Source or the Provisioning Type of machines. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"VIRTUAL_CENTER"</td><td>Virtual center virtual machines managed as view machines. This option is valid for Automated and Manual Desktop. In case of Automated Desktop, these refer to Full Virtual Machines that are created from a vCenter Server template.</td></tr><tr><td>"VIEW_COMPOSER"</td><td>View composer linked clones managed as view machines. They share the same base image and use less storage space than full virtual machines. The user profile for linked clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes. This option is only valid for Automated Desktop.</td></tr><tr><td>"INSTANT_CLONE_ENGINE"</td><td>Instant clone engine created 'instant clones' managed as view machines. Instant clone engine uses vmfork technology to create the instant clones, these clones take very less time for provisioning. Instant clones have many similarities to linked clones. This option is only valid for Automated Desktop.</td></tr><tr><td>"AWS_CORE"</td><td>AWS-core workspaces managed as view machines. This option is valid for automated desktop.</td></tr></table>
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  Virtual Center server. For instant clone engine desktops the Virtual Center server version should be at least 6.0 or above.
**userAssignment**| [DesktopUserAssignment](vdi.resources.Desktop.UserAssignment.md)|  User assignment scheme.
**vmNamingSpec**| [DesktopVirtualMachineNamingSpec](vdi.resources.Desktop.VirtualMachineNamingSpec.md)|  Specifies the naming scheme for the VMs in the desktop.
**virtualCenterProvisioningSettings**| [DesktopVirtualCenterProvisioningSettings](vdi.resources.Desktop.VirtualCenterProvisioningSettings.md)|  Virtual Center provisioning settings for the automated desktop.
**virtualCenterManagedCommonSettings**| [DesktopVirtualCenterManagedCommonSettings](vdi.resources.Desktop.VirtualCenterManagedCommonSettings.md)|  Common settings for Desktops managed by Virtual Center sources.  **_Since_** Horizon View 6.1
**customizationSettings**| [DesktopCustomizationSettings](vdi.resources.Desktop.CustomizationSettings.md)|  Customization settings.
**partnerDesktopSetting**| [PartnerDesktopSettings](vdi.resources.Desktop.PartnerDesktopSettings.md)|  Partner desktop settings.  **_Since_** Horizon 8.13 [^1]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.