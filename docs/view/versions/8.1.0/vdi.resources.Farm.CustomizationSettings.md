---
layout: page
title: Data Object - FarmCustomizationSettings
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Farm.CustomizationSettings`

Property of
> [FarmAutomatedFarmData](vdi.resources.Farm.AutomatedFarmData.md#field_detail), [FarmAutomatedFarmSpec](vdi.resources.Farm.AutomatedFarmSpec.md#field_detail)

See also
> [ADContainerId](vdi.entity.ADContainerId.md), [FarmCloneprepCustomizationSettings](vdi.resources.Farm.CloneprepCustomizationSettings.md), [FarmSysprepCustomizationSettings](vdi.resources.Farm.SysprepCustomizationSettings.md), [ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)

Since
> Horizon View 6.2


## Data Object Description

Customization settings.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**customizationType**|  xsd:string|  Type of customization to use. For linked-clone RDS Servers, this cannot be changed after creation. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"SYS_PREP"</td><td>Microsoft Sysprep is a tool to deploy the configured operating system installation from a base image. The machine can then be customized based on an answer script. Sysprep can modify a larger number of configurable parameters than QuickPrep. This is applicable only to RDS servers belonging to Automated Farms.</td></tr><tr><td>"CLONE_PREP"</td><td>ClonePrep is a VMware system tool executed by Instant Clone Engine during an instant clone machine deployment. ClonePrep personalizes each machine created from the Master image. This is applicable only to instant clone farm.</td></tr></table>
**domainAdministrator**| [ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)| **Deprecated.**_This property is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._ View Composer domain administrator. This is the administrator which will add the RDS Servers to its domain upon creation. This must be set for linked-clone RDS Servers. [^1]
**adContainer**| [ADContainerId](vdi.entity.ADContainerId.md)|  View Composer Active Directory container for QuickPrep. If unset, this will default to the AD container "CN=Computers". [^1]
**reusePreExistingAccounts**|  xsd:boolean|  Whether to allow the use of existing AD computer accounts when the VM names of newly created RDS Servers match the existing computer account names. This is applicable only for Automated Farms. [^5]
**sysprepCustomizationSettings**| [FarmSysprepCustomizationSettings](vdi.resources.Farm.SysprepCustomizationSettings.md)|  Settings when Sysprep customization is requested. [^1] [^24]
**cloneprepCustomizationSettings**| [FarmCloneprepCustomizationSettings](vdi.resources.Farm.CloneprepCustomizationSettings.md)|  Settings when ClonePrep customization is requested.  **_Since_** Horizon 7.1 [^1] <br>* This property is required if customizationType is set to "CLONE_PREP".


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^5]: This property has a default value of false.
[^24]: This property is required if customizationType is set to 'SYS_PREP'.