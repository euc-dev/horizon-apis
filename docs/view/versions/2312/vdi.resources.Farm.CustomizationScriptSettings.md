---
layout: page
title: Data Object - FarmCustomizationScriptSettings
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.CustomizationScriptSettings`

Property of  
> [FarmCustomizationSettings](vdi.resources.Farm.CustomizationSettings.md#field_detail)

Since  
> Horizon 8.11


## Data Object Description 

Customization scripts to run on a cloned VM. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**powerOffScriptName**|  xsd:string|  Power off script. Allows to run a customization script on cloned machines before they are powered off. Provide the path to the script on the parent virtual machine.   


 * This property need not be set.

  
**powerOffScriptParameters**|  xsd:string|  Power off script parameters. Example: p1 p2 p3   


 * This property need not be set.

  
**postSynchronizationScriptName**|  xsd:string|  Post synchronization script. Allows to run a customization script on cloned machines after they are created, recomposed, or refreshed. Provide the path to the script on the parent virtual machine.   


 * This property need not be set.

  
**postSynchronizationScriptParameters**|  xsd:string|  Post synchronization script parameters. Example: p1 p2 p3   


 * This property need not be set.

  
  
  
   
  
  
