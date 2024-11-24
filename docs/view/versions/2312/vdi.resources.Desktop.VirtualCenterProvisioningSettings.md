---
layout: page
title: Data Object - DesktopVirtualCenterProvisioningSettings
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.VirtualCenterProvisioningSettings`

Property of
> [DesktopAutomatedDesktopData](vdi.resources.Desktop.AutomatedDesktopData.md#field_detail), [DesktopAutomatedDesktopSpec](vdi.resources.Desktop.AutomatedDesktopSpec.md#field_detail)

See also
> [DesktopVirtualCenterNetworkingSettings](vdi.resources.Desktop.VirtualCenterNetworkingSettings.md), [DesktopVirtualCenterProvisioningData](vdi.resources.Desktop.VirtualCenterProvisioningData.md), [DesktopVirtualCenterStorageSettings](vdi.resources.Desktop.VirtualCenterStorageSettings.md)

Since
> Horizon View 6.0


## Data Object Description

Virtual Center entities associated with this Desktop.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**enableProvisioning**|  xsd:boolean|  Whether to enable provisioning immediately. [^6]
**stopProvisioningOnError**|  xsd:boolean|  Whether provisioning on all VMs stops on error. [^6]
**minReadyVMsOnVComposerMaintenance**|  xsd:int| **Deprecated.**_This property is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._ Minimum number of ready (provisioned) machines during View Composer maintenance operations. Use this setting to perform machine maintenance operations in a rolling fashion. Increasing this count may decrease the concurrency for View Composer operations for the machine desktop. This is applicable only in the case of linked-clone Automated Desktops. <br>If the naming method is PATTERN, this value must be less than [minNumberOfMachines](vdi.resources.Desktop.PatternNamingSettings.md#minNumberOfMachines). If the naming method is SPECIFIED and this is a create, this value must be less than the number of specified names. If the naming method is SPECIFIED and this value is updated, it must be less than the total number of existing machines in the desktop. The above checks are not done if this value is 0. [^19] [^72]
**virtualCenterProvisioningData**| [DesktopVirtualCenterProvisioningData](vdi.resources.Desktop.VirtualCenterProvisioningData.md)|  Virtual center entities used for provisioning.
**virtualCenterStorageSettings**| [DesktopVirtualCenterStorageSettings](vdi.resources.Desktop.VirtualCenterStorageSettings.md)|  Virtual Center storage settings.
**virtualCenterNetworkingSettings**| [DesktopVirtualCenterNetworkingSettings](vdi.resources.Desktop.VirtualCenterNetworkingSettings.md)|  Virtual Center networking settings.
**addVirtualTPM**|  xsd:boolean|  Whether to add Virtual TPM device.  **_Since_** Horizon 7.6 [^5] [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^5]: This property has a default value of false.
[^6]: This property has a default value of true.
[^19]: This property has a default value of 0.
[^72]: This property has a minimum value of 0.