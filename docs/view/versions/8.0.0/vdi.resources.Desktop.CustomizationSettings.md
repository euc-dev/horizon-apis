---
layout: page
title: Data Object - DesktopCustomizationSettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.CustomizationSettings
Property of
     [DesktopAutomatedDesktopData](vdi.resources.Desktop.AutomatedDesktopData.md#field_detail), [DesktopAutomatedDesktopSpec](vdi.resources.Desktop.AutomatedDesktopSpec.md#field_detail)
See also
     [ADContainerId](vdi.entity.ADContainerId.md), [DesktopCloneprepCustomizationSettings](vdi.resources.Desktop.CloneprepCustomizationSettings.md), [DesktopNoCustomizationSettings](vdi.resources.Desktop.NoCustomizationSettings.md), [DesktopQuickprepCustomizationSettings](vdi.resources.Desktop.QuickprepCustomizationSettings.md), [DesktopSysprepCustomizationSettings](vdi.resources.Desktop.SysprepCustomizationSettings.md), [ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)
Since 
    Horizon View 6.0

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
"SYS_PREP"| Microsoft Sysprep is a tool to deploy the configured operating system installation from a base image. The machine can then be customized based on an answer script. Sysprep can modify a larger number of configurable parameters than QuickPrep. This is applicable only to full clone and linked clone desktops.  
"CLONE_PREP"| ClonePrep is a VMware system tool executed by Instant Clone Engine during a instant clone machine deployment. ClonePrep personalizes each machine created from the Master image. This is applicable only to instant clone desktops.  

  
**domainAdministrator**| [ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)|  View Composer domain administrator. This is the administrator which will add the machines to its domain upon creation. This must be set for linked-clone automated desktops.   


[^1]

  
**adContainer**| [ADContainerId](vdi.entity.ADContainerId.md)|  View Composer and Instant Clone Engine Active Directory container for QuickPrep and ClonePrep. This must be set for Instant Clone Engine sourced desktops.   


[^1]

  
**reusePreExistingAccounts**|  xsd:boolean|  Whether to allow the use of existing AD computer accounts when the VM names of newly created clones match the existing computer account names. This is applicable only for Automated desktops.   


  * This property has a default value of false.

  
**noCustomizationSettings**| [DesktopNoCustomizationSettings](vdi.resources.Desktop.NoCustomizationSettings.md)|  Settings when customization will be done manually.   


[^1]
  * This property is required if customizationType is set to "NONE".

  
**sysprepCustomizationSettings**| [DesktopSysprepCustomizationSettings](vdi.resources.Desktop.SysprepCustomizationSettings.md)|  Settings when Sysprep customization is requested.   


[^1]
  * This property is required if customizationType is set to "SYS_PREP".

  
**quickprepCustomizationSettings**| [DesktopQuickprepCustomizationSettings](vdi.resources.Desktop.QuickprepCustomizationSettings.md)|  Settings when QuickPrep customization is requested.   


[^1]
  * This property is required if customizationType is set to "QUICK_PREP".

  
**cloneprepCustomizationSettings**| [DesktopCloneprepCustomizationSettings](vdi.resources.Desktop.CloneprepCustomizationSettings.md)|  Settings when ClonePrep customization is requested.  **_Since_** Horizon 7.0  


[^1]
  * This property is required if customizationType is set to "CLONE_PREP".

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
