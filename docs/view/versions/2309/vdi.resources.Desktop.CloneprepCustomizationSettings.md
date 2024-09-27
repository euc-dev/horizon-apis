---
layout: page
title: Data Object - DesktopCloneprepCustomizationSettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.CloneprepCustomizationSettings  
Property of
     [DesktopCustomizationSettings](vdi.resources.Desktop.CustomizationSettings.md#field_detail)  
See also
     [InstantCloneEngineDomainAdministratorId](vdi.entity.InstantCloneEngineDomainAdministratorId.md)  
Since 
    Horizon 7.0

## Data Object Description 

Settings for ClonePrep customization. This setting is only applicable to instant clone desktops. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**instantCloneEngineDomainAdministrator**| [InstantCloneEngineDomainAdministratorId](vdi.entity.InstantCloneEngineDomainAdministratorId.md)| **Deprecated.**_use #CustomizationSettings.instantCloneEngineDomainAdministrator instead._ Instant Clone Engine domain administrator. This is the administrator which will add the machines to its domain upon creation.   


 * This property need not be set.

  
**powerOffScriptName**|  xsd:string| **Deprecated.**_since Horizon 2309. Use[powerOffScriptName](vdi.resources.Desktop.CustomizationScriptSettings.md#powerOffScriptName) _ Power off script. ClonePrep can run a customization script on instant-clone machines before they are powered off. Provide the path to the script on the parent virtual machine.   


 * This property need not be set.

  
**powerOffScriptParameters**|  xsd:string| **Deprecated.**_since Horizon 2309. Use[powerOffScriptParameters](vdi.resources.Desktop.CustomizationScriptSettings.md#powerOffScriptParameters) _ Power off script parameters. Example: p1 p2 p3   


 * This property need not be set.

  
**postSynchronizationScriptName**|  xsd:string| **Deprecated.**_since Horizon 2309. Use[postSynchronizationScriptName](vdi.resources.Desktop.CustomizationScriptSettings.md#postSynchronizationScriptName) _ Post synchronization script. ClonePrep can run a customization script on instant-clone machines after they are created or recovered or a new image is pushed. Provide the path to the script on the parent virtual machine.   


 * This property need not be set.

  
**postSynchronizationScriptParameters**|  xsd:string| **Deprecated.**_since Horizon 2309. Use[postSynchronizationScriptParameters](vdi.resources.Desktop.CustomizationScriptSettings.md#postSynchronizationScriptParameters) _ Post synchronization script parameters. Example: p1 p2 p3   


 * This property need not be set.

  
**primingComputerAccount**|  xsd:string|  Instant Clone publishing needs an additional computer account in the same AD domain as the clones. This field accepts the pre-created computer accounts. This field is ignored when reusePreExistingAccounts is false.  **_Since_** Horizon 7.8  


 * This property need not be set.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

