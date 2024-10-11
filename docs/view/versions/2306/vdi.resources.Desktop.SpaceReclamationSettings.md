---
layout: page
title: Data Object - DesktopSpaceReclamationSettings
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.SpaceReclamationSettings`

Property of  
> [DesktopViewComposerStorageSettings](vdi.resources.Desktop.ViewComposerStorageSettings.md#field_detail)

Since  
> Horizon View 6.0


## Data Object Description 

Settings related to the Space Reclamation feature. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**reclaimVmDiskSpace**|  xsd:boolean|  With vSphere 5.x, virtual machines can be configured to use a space efficient disk format that supports reclamation of unused disk space (such as deleted files). This option reclaims unused disk space on each virtual machine. The operation is initiated when an estimate of used disk space exceeds the specified threshold. vSphere 5.1 Patch1 or later is required for this option. Note(s) :-  
  


  * This property has a default value of false.

  
**reclamationThresholdGB**|  xsd:long|  Initiate reclamation when unused space on VM exceeds the threshold.   


  * This property has a default value of 1.
* This property need not be set.
  * This property has a minimum value of 0. 
  * This property is required if reclaimVmDiskSpace is set to true.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
