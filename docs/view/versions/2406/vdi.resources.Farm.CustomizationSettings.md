---
layout: page
title: Data Object - FarmCustomizationSettings
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.CustomizationSettings`

Property of  
> [FarmAutomatedFarmData](vdi.resources.Farm.AutomatedFarmData.md#field_detail), [FarmAutomatedFarmSpec](vdi.resources.Farm.AutomatedFarmSpec.md#field_detail)

See also  
> [ADContainerId](vdi.entity.ADContainerId.md), [FarmCloneprepCustomizationSettings](vdi.resources.Farm.CloneprepCustomizationSettings.md), [FarmCustomizationScriptSettings](vdi.resources.Farm.CustomizationScriptSettings.md), [FarmSysprepCustomizationSettings](vdi.resources.Farm.SysprepCustomizationSettings.md), [InstantCloneEngineDomainAdministratorId](vdi.entity.InstantCloneEngineDomainAdministratorId.md), [ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)

Since  
> Horizon View 6.2


## Data Object Description 

Customization settings. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**customizationType**|  xsd:string|  Type of customization to use. For linked-clone RDS Servers, this cannot be changed after creation.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"SYS_PREP"| Microsoft Sysprep is a tool to deploy the configured operating system installation from a base image. The machine can then be customized based on an answer script. Sysprep can modify a larger number of configurable parameters than QuickPrep. This is applicable only to RDS servers belonging to Automated Farms.  
"CLONE_PREP"| ClonePrep is a VMware system tool executed by Instant Clone Engine during an instant clone machine deployment. ClonePrep personalizes each machine created from the Master image. This is applicable only to instant clone farm.  

  
**domainAdministrator**| [ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)| **Deprecated.**_This property is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._ View Composer domain administrator. This is the administrator which will add the RDS Servers to its domain upon creation. This must be set for linked-clone RDS Servers.   


 * This property need not be set.

  
**instantCloneEngineDomainAdministrator**| [InstantCloneEngineDomainAdministratorId](vdi.entity.InstantCloneEngineDomainAdministratorId.md)|  Instant Clone Engine domain administrator. This is the administrator which will add the machines to its domain upon creation. This must be set for instant clone RDS Servers.  **_Since_** Horizon 8.3  


 * This property need not be set.

  
**adSiteName**|  xsd:string|  The AD Site, associated with [instantCloneEngineDomainAdministrator](vdi.resources.Farm.CustomizationSettings.md#instantCloneEngineDomainAdministrator), which will be used for instant clone pool provisioning. This attribute is valid for only instant clone automated farms.  **_Since_** Horizon 8.9  


 * This property need not be set.

  
**adContainer**| [ADContainerId](vdi.entity.ADContainerId.md)|  View Composer Active Directory container for QuickPrep. If unset, this will default to the AD container "CN=Computers".   


 * This property need not be set.

  
**reusePreExistingAccounts**|  xsd:boolean|  Whether to allow the use of existing AD computer accounts when the VM names of newly created RDS Servers match the existing computer account names. This is applicable only for Automated Farms.   


  * This property has a default value of false.

  
**enableSysprepDomainJoin**|  xsd:boolean|  Indicates whether Microsoft Sysprep process initiates domain join for instant clone virtual machines. When enabled, Microsoft SysPrep process creates computer accounts and perform domain join on instant clone VMs.  **_Since_** Horizon 8.11  


  * This property has a default value of false.
 * This property need not be set.

  
**customizationScriptSettings**| [FarmCustomizationScriptSettings](vdi.resources.Farm.CustomizationScriptSettings.md)|  Customization scripts to run on a cloned VM.  **_Since_** Horizon 8.11  


 * This property need not be set.

  
**sysprepCustomizationSettings**| [FarmSysprepCustomizationSettings](vdi.resources.Farm.SysprepCustomizationSettings.md)|  Settings when Sysprep customization is requested.   


 * This property need not be set.
  * This property is required if customizationType is set to "SYS_PREP".

  
**cloneprepCustomizationSettings**| [FarmCloneprepCustomizationSettings](vdi.resources.Farm.CloneprepCustomizationSettings.md)|  Settings when ClonePrep customization is requested.  **_Since_** Horizon 7.1  


 * This property need not be set.

  
  

  
