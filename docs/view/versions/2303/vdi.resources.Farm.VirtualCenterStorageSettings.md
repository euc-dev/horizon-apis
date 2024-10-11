---
layout: page
title: Data Object - FarmVirtualCenterStorageSettings
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.VirtualCenterStorageSettings`

Property of  
> [FarmVirtualCenterProvisioningSettings](vdi.resources.Farm.VirtualCenterProvisioningSettings.md#field_detail)

See also  
> [FarmViewComposerStorageSettings](vdi.resources.Farm.ViewComposerStorageSettings.md), [FarmViewStorageAcceleratorSettings](vdi.resources.Farm.ViewStorageAcceleratorSettings.md), [FarmVirtualCenterDatastoreSettings](vdi.resources.Farm.VirtualCenterDatastoreSettings.md)

Since  
> Horizon View 6.2


## Data Object Description 

Virtual Center storage settings. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**datastores**| [FarmVirtualCenterDatastoreSettings[]](vdi.resources.Farm.VirtualCenterDatastoreSettings.md)|  Datastore IDs to store the RDS Server (or the OS disk using other options for View Composer VM storage). Note(s) :-  


  * For Instant clone farms, this can be modified only if there are no current operations ( [operation](vdi.resources.Farm.InstantCloneProvisioningStatusData.md#operation) is NONE).

  
  
**useVSan**|  xsd:boolean|  Whether to use vSphere VSAN. This is applicable for vSphere 5.5 or later. [datastores](vdi.resources.Farm.VirtualCenterStorageSettings.md#datastores) must specify exactly one datastore of file system type VSAN. If this RDS Server is sourced from View Composer, [useSeparateDatastoresReplicaAndOSDisks](vdi.resources.Farm.ViewComposerStorageSettings.md#useSeparateDatastoresReplicaAndOSDisks) , and [reclaimVmDiskSpace](vdi.resources.Farm.SpaceReclamationSettings.md#reclaimVmDiskSpace) must be disabled.   


  * This property has a default value of false.

  
**viewComposerStorageSettings**| [FarmViewComposerStorageSettings](vdi.resources.Farm.ViewComposerStorageSettings.md)|  View Composer storage settings. This must be set for RDS servers in Automated Farms.   


* This property need not be set.

  
**viewStorageAcceleratorSettings**| [FarmViewStorageAcceleratorSettings](vdi.resources.Farm.ViewStorageAcceleratorSettings.md)|  View Storage Accelerator settings.  **_Since_** Horizon 7.2  


* This property need not be set.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
