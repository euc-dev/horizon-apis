---
layout: page
title: Data Object - DesktopCustomizationSettings
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.CustomizationSettings`

Property of
> [DesktopAutomatedDesktopData](vdi.resources.Desktop.AutomatedDesktopData.md#field_detail), [DesktopAutomatedDesktopSpec](vdi.resources.Desktop.AutomatedDesktopSpec.md#field_detail)

See also
> [ADContainerId](vdi.entity.ADContainerId.md), [DesktopCloneprepCustomizationSettings](vdi.resources.Desktop.CloneprepCustomizationSettings.md), [DesktopCustomizationScriptSettings](vdi.resources.Desktop.CustomizationScriptSettings.md), [DesktopNoCustomizationSettings](vdi.resources.Desktop.NoCustomizationSettings.md), [DesktopQuickprepCustomizationSettings](vdi.resources.Desktop.QuickprepCustomizationSettings.md), [DesktopSysprepCustomizationSettings](vdi.resources.Desktop.SysprepCustomizationSettings.md), [InstantCloneEngineDomainAdministratorId](vdi.entity.InstantCloneEngineDomainAdministratorId.md), [ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)

Since
> Horizon View 6.0


## Data Object Description

Customization settings.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**customizationType**|  xsd:string|  Type of customization to use. For View Composer and Instant clone engine sourced desktops, this cannot be changed after creation.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>NONE</td><td>No customization. This is applicable only to full clone desktops.</td></tr><tr><td>QUICK_PREP</td><td>QuickPrep is a VMware system tool executed by View Composer during a linked-clone machine deployment. QuickPrep personalizes each machine created from the Master image. This is applicable only to linked clone desktops.</td></tr><tr><td>SYS_PREP</td><td>Microsoft Sysprep is a tool to deploy the configured operating system installation from a base image. The machine can then be customized based on an answer script. Sysprep can modify a larger number of configurable parameters than QuickPrep.</td></tr><tr><td>CLONE_PREP</td><td>ClonePrep is a VMware system tool executed by Instant Clone Engine during an instant clone machine deployment. ClonePrep personalizes each machine created from the Master image. This is applicable only to instant clone desktops.</td></tr></table>
**domainAdministrator**| [ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)| **Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._ View Composer domain administrator. This is the administrator which will add the machines to its domain upon creation. This must be set for linked-clone automated desktops. [^1]
**instantCloneEngineDomainAdministrator**| [InstantCloneEngineDomainAdministratorId](vdi.entity.InstantCloneEngineDomainAdministratorId.md)|  Instant Clone Engine/Full Clone domain administrator. This is the administrator which will add the machines to its domain upon creation. This must be set for instant clone automated desktops.  **_Since_** Horizon 8.3 [^1]
**adSiteName**|  xsd:string|  The AD Site, associated with [instantCloneEngineDomainAdministrator](vdi.resources.Desktop.CustomizationSettings.md#instantCloneEngineDomainAdministrator), which will be used for instant clone pool provisioning. This attribute is valid for only instant clone automated desktops.  **_Since_** Horizon 8.9 [^1]
**adContainer**| [ADContainerId](vdi.entity.ADContainerId.md)|  Instant Clone Engine and Full Clone Active Directory container for ClonePrep and SysPrep. This must be set for Instant Clone Engine sourced desktops. [^1]
**reusePreExistingAccounts**|  xsd:boolean|  Whether to allow the use of existing AD computer accounts when the VM names of newly created clones match the existing computer account names. This is applicable only for Automated desktops. [^5]
**enableSysprepDomainJoin**|  xsd:boolean|  Indicates whether Microsoft Sysprep process initiates domain join for instant clone virtual machines. When enabled, Microsoft SysPrep process creates computer accounts and perform domain join on instant clone VMs.  **_Since_** Horizon 8.11 [^5] [^1]
**customizationScriptSettings**| [DesktopCustomizationScriptSettings](vdi.resources.Desktop.CustomizationScriptSettings.md)|  Customization scripts to run on a cloned VM.  **_Since_** Horizon 8.11 [^1]
**noCustomizationSettings**| [DesktopNoCustomizationSettings](vdi.resources.Desktop.NoCustomizationSettings.md)|  Settings when customization will be done manually. [^1] [^23]
**sysprepCustomizationSettings**| [DesktopSysprepCustomizationSettings](vdi.resources.Desktop.SysprepCustomizationSettings.md)|  Settings when Sysprep customization is requested. [^1] [^24]
**quickprepCustomizationSettings**| [DesktopQuickprepCustomizationSettings](vdi.resources.Desktop.QuickprepCustomizationSettings.md)|  Settings when QuickPrep customization is requested. [^1] [^25]
**cloneprepCustomizationSettings**| [DesktopCloneprepCustomizationSettings](vdi.resources.Desktop.CloneprepCustomizationSettings.md)|  Settings when ClonePrep customization is requested.  **_Since_** Horizon 7.0 [^1]


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.
[^23]: This property is required if customizationType is set to 'NONE'.
[^24]: This property is required if customizationType is set to 'SYS_PREP'.
[^25]: This property is required if customizationType is set to 'QUICK_PREP'.