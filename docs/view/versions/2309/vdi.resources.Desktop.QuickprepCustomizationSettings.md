---
layout: page
title: Data Object - DesktopQuickprepCustomizationSettings
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.QuickprepCustomizationSettings  
Property of
     [DesktopCustomizationSettings](vdi.resources.Desktop.CustomizationSettings.md#field_detail)  
Since 
    Horizon View 6.0

## Data Object Description 

Settings for QuickPrep customization. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**powerOffScriptName**|  xsd:string|  Power off script. QuickPrep can run a customization script on linked-clone machines before they are powered off. Provide the path to the script on the parent virtual machine.   


 * This property need not be set.

  
**powerOffScriptParameters**|  xsd:string|  Power off script parameters. Example: p1 p2 p3   


 * This property need not be set.

  
**postSynchronizationScriptName**|  xsd:string|  Post synchronization script. QuickPrep can run a customization script on linked-clone machines after they are created, recomposed, and refreshed. Provide the path to the script on the parent virtual machine.   


 * This property need not be set.

  
**postSynchronizationScriptParameters**|  xsd:string|  Post synchronization script parameters. Example: p1 p2 p3   


 * This property need not be set.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

