---
layout: page
title: Data Object - FarmCustomizationSettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Farm.CustomizationSettings
Property of
     [FarmAutomatedFarmData](vdi.resources.Farm.AutomatedFarmData.md#field_detail), [FarmAutomatedFarmSpec](vdi.resources.Farm.AutomatedFarmSpec.md#field_detail)
See also
     [ADContainerId](vdi.entity.ADContainerId.md), [FarmCloneprepCustomizationSettings](vdi.resources.Farm.CloneprepCustomizationSettings.md), [FarmSysprepCustomizationSettings](vdi.resources.Farm.SysprepCustomizationSettings.md), [ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)
Since 
    Horizon View 6.2

## Data Object Description 

Customization settings. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**customizationType**|  xsd:string|  Type of customization to use. For linked-clone RDS Servers, this cannot be changed after creation.   


[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"SYS_PREP"| Microsoft Sysprep is a tool to deploy the configured operating system installation from a base image. The machine can then be customized based on an answer script. Sysprep can modify a larger number of configurable parameters than QuickPrep. This is applicable only to RDS servers belonging to Automated Farms.  
"CLONE_PREP"| ClonePrep is a VMware system tool executed by Instant Clone Engine during an instant clone machine deployment. ClonePrep personalizes each machine created from the Master image. This is applicable only to instant clone farm.  

  
**domainAdministrator**| [ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)|  View Composer domain administrator. This is the administrator which will add the RDS Servers to its domain upon creation. This must be set for linked-clone RDS Servers.   


[^1]

  
**adContainer**| [ADContainerId](vdi.entity.ADContainerId.md)|  View Composer Active Directory container for QuickPrep. If unset, this will default to the AD container "CN=Computers".   


[^1]

  
**reusePreExistingAccounts**|  xsd:boolean|  Whether to allow the use of existing AD computer accounts when the VM names of newly created RDS Servers match the existing computer account names. This is applicable only for Automated Farms.   


  * This property has a default value of false.

  
**sysprepCustomizationSettings**| [FarmSysprepCustomizationSettings](vdi.resources.Farm.SysprepCustomizationSettings.md)|  Settings when Sysprep customization is requested.   


[^1]
  * This property is required if customizationType is set to "SYS_PREP".

  
**cloneprepCustomizationSettings**| [FarmCloneprepCustomizationSettings](vdi.resources.Farm.CloneprepCustomizationSettings.md)|  Settings when ClonePrep customization is requested.  **_Since_** Horizon 7.1  


[^1]
  * This property is required if customizationType is set to "CLONE_PREP".

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
