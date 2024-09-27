---
layout: page
title: Data Object - FarmCloneprepCustomizationSettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Farm.CloneprepCustomizationSettings  
Property of
     [FarmCustomizationSettings](vdi.resources.Farm.CustomizationSettings.md#field_detail)  
See also
     [InstantCloneEngineDomainAdministratorId](vdi.entity.InstantCloneEngineDomainAdministratorId.md)  
Since 
    Horizon 7.1

## Data Object Description 

Settings for ClonePrep customization. This setting is only applicable to instant clone farms. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**instantCloneEngineDomainAdministrator**| [InstantCloneEngineDomainAdministratorId](vdi.entity.InstantCloneEngineDomainAdministratorId.md)|  Instant Clone Engine domain administrator. This is the administrator which will add the machines to its domain upon creation.   
  
**powerOffScriptName**|  xsd:string|  Power off script. ClonePrep can run a customization script on instant-clone machines before they are powered off. Provide the path to the script on the parent virtual machine.   


* This property need not be set.

  
**powerOffScriptParameters**|  xsd:string|  Power off script parameters. Example: p1 p2 p3   


* This property need not be set.

  
**postSynchronizationScriptName**|  xsd:string|  Post synchronization script. ClonePrep can run a customization script on instant-clone machines after they are created or recovered or a new image is pushed. Provide the path to the script on the parent virtual machine.   


* This property need not be set.

  
**postSynchronizationScriptParameters**|  xsd:string|  Post synchronization script parameters. Example: p1 p2 p3   


* This property need not be set.

  
**primingComputerAccount**|  xsd:string|  Instant Clone publishing needs an additional computer account in the same AD domain as the clones. This field accepts the pre-created computer accounts.This field is ignored when reusePreExistingAccounts is false.  **_Since_** Horizon 7.8  


* This property need not be set.

  
  
  

  
  

