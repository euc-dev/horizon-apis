---
layout: page
title: Data Object - DesktopCustomizationSettings
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.CustomizationSettings`

Property of  
> [DesktopAutomatedDesktopData](vdi.resources.Desktop.AutomatedDesktopData.md#field_detail), [DesktopAutomatedDesktopSpec](vdi.resources.Desktop.AutomatedDesktopSpec.md#field_detail)

See also  
> [ADContainerId](vdi.entity.ADContainerId.md), [DesktopCloneprepCustomizationSettings](vdi.resources.Desktop.CloneprepCustomizationSettings.md), [DesktopNoCustomizationSettings](vdi.resources.Desktop.NoCustomizationSettings.md), [DesktopQuickprepCustomizationSettings](vdi.resources.Desktop.QuickprepCustomizationSettings.md), [DesktopSysprepCustomizationSettings](vdi.resources.Desktop.SysprepCustomizationSettings.md), [InstantCloneEngineDomainAdministratorId](vdi.entity.InstantCloneEngineDomainAdministratorId.md), [ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)

Since  
> Horizon View 6.0


## Data Object Description 

Customization settings. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**customizationType**|  xsd:string|  Type of customization to use. For View Composer and Instant clone engine sourced desktops, this cannot be changed after creation.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"NONE"| No customization. This is applicable only to full clone desktops.  
"QUICK_PREP"| QuickPrep is a VMware system tool executed by View Composer during a linked-clone machine deployment. QuickPrep personalizes each machine created from the Master image. This is applicable only to linked clone desktops.  
"SYS_PREP"| Microsoft Sysprep is a tool to deploy the configured operating system installation from a base image. The machine can then be customized based on an answer script. Sysprep can modify a larger number of configurable parameters than QuickPrep.  
"CLONE_PREP"| ClonePrep is a VMware system tool executed by Instant Clone Engine during a instant clone machine deployment. ClonePrep personalizes each machine created from the Master image. This is applicable only to instant clone desktops.  

  
**domainAdministrator**| [ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)| **Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._ View Composer domain administrator. This is the administrator which will add the machines to its domain upon creation. This must be set for linked-clone automated desktops.   


* This property need not be set.

  
**instantCloneEngineDomainAdministrator**| [InstantCloneEngineDomainAdministratorId](vdi.entity.InstantCloneEngineDomainAdministratorId.md)|  Instant Clone Engine/Full Clone domain administrator. This is the administrator which will add the machines to its domain upon creation. This must be set for instant clone automated desktops.  **_Since_** Horizon 8.3  


* This property need not be set.

  
**adContainer**| [ADContainerId](vdi.entity.ADContainerId.md)|  Instant Clone Engine and Full Clone Active Directory container for ClonePrep and SysPrep. This must be set for Instant Clone Engine sourced desktops.   


* This property need not be set.

  
**reusePreExistingAccounts**|  xsd:boolean|  Whether to allow the use of existing AD computer accounts when the VM names of newly created clones match the existing computer account names. This is applicable only for Automated desktops.   


  * This property has a default value of false.

  
**noCustomizationSettings**| [DesktopNoCustomizationSettings](vdi.resources.Desktop.NoCustomizationSettings.md)|  Settings when customization will be done manually.   


* This property need not be set.
  * This property is required if customizationType is set to "NONE".

  
**sysprepCustomizationSettings**| [DesktopSysprepCustomizationSettings](vdi.resources.Desktop.SysprepCustomizationSettings.md)|  Settings when Sysprep customization is requested.   


* This property need not be set.
  * This property is required if customizationType is set to "SYS_PREP".

  
**quickprepCustomizationSettings**| [DesktopQuickprepCustomizationSettings](vdi.resources.Desktop.QuickprepCustomizationSettings.md)|  Settings when QuickPrep customization is requested.   


* This property need not be set.
  * This property is required if customizationType is set to "QUICK_PREP".

  
**cloneprepCustomizationSettings**| [DesktopCloneprepCustomizationSettings](vdi.resources.Desktop.CloneprepCustomizationSettings.md)|  Settings when ClonePrep customization is requested.  **_Since_** Horizon 7.0  


* This property need not be set.

  
  
  
  
  
  
