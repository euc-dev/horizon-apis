---
layout: page
title: Data Object - FarmMaintenanceSpec
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Farm.MaintenanceSpec
Parameter to
     [Farm_ImageManagementScheduleMaintenance](vdi.resources.Farm.md#imageManagementScheduleMaintenance), [Farm_ScheduleMaintenance](vdi.resources.Farm.md#scheduleMaintenance)
See also
     [FarmImageMaintenanceSettings](vdi.resources.Farm.ImageMaintenanceSettings.md), [FarmImageManagementMaintenanceSettings](vdi.resources.Farm.ImageManagementMaintenanceSettings.md), [FarmRecurringMaintenanceSettings](vdi.resources.Farm.RecurringMaintenanceSettings.md), [RDSServerId](vdi.entity.RDSServerId.md)
Since 
    Horizon 7.1

## Data Object Description 

Settings for maintenance operations. This is applicable only for RDSH Instant Clone Farm 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**maintenanceMode**|  xsd:string|  The mode of schedule maintenance for Instant Clone Farm   


  * This property will be one of:  
|  Value |  Description   
---|---  
"IMMEDIATE"| All server VMs will be refreshed once, immediately or at user scheduled time.  
"RECURRING"| All server VMs will be periodically refreshed based on FarmInstantCloneRecurringMaintenancePeriod and StartTime  

  
**scheduledTime**|  xsd:dateTime|  When to actually perform the next maintenance. For IMMEDIATE if unset, maintenance will begin immediately. For RECURRING If unset, will be calculated based on current recurring maintenance configuration. If in the past, maintenance will begin immediately.   


[^1]

  
**logoffSetting**|  xsd:string|  Determines when to perform the operation on machines which have an active session.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"FORCE_LOGOFF"| Users will be forced to log off when the system is ready to operate on their RDS Servers. Before being forcibly logged off, users may have a grace period in which to save their work (Global Settings).  
"WAIT_FOR_LOGOFF"| Wait for connected users to disconnect before the task starts. The operation starts immediately on RDS Servers without active sessions.  

  
**stopOnFirstError**|  xsd:boolean|  Indicates that the operation should stop on first error.   


  * This property has a default value of true.
[^1]

  
**recurringMaintenanceSettings**| [FarmRecurringMaintenanceSettings](vdi.resources.Farm.RecurringMaintenanceSettings.md)|  Recurring maintenance configuration settings. Required only if maintenanceMode == RECURRING   


[^1]
  * This property is required if maintenanceMode is set to "RECURRING".

  
**imageMaintenanceSettings**| [FarmImageMaintenanceSettings](vdi.resources.Farm.ImageMaintenanceSettings.md)|  Settings for the Image maintenance. This is required only if maintenance is triggered using [Farm_ScheduleMaintenance](vdi.resources.Farm.md#scheduleMaintenance) API.   


[^1]

  
**imageManagementMaintenanceSettings**| [FarmImageManagementMaintenanceSettings](vdi.resources.Farm.ImageManagementMaintenanceSettings.md)|  Settings for the Image maintenance if farm is created using image catalog. This is required only if maintenance is triggered using [Farm_ImageManagementScheduleMaintenance](vdi.resources.Farm.md#imageManagementScheduleMaintenance) API.  **_Since_** Horizon 7.10  


[^1]

  
**selectiveScheduleMaintenance**|  xsd:boolean|  Set to true for selective schedule maintenance. Indicates if the new image should be applied to a subset of the rds servers in the farm. The image published with this option, will be held as a pending Image, unless it is either promoted canceled.  **_Since_** Horizon 8.4  


  * This property has a default value of false.
[^1]

  
**rdsServers**| [RDSServerId[]](vdi.entity.RDSServerId.md)|  The list of rds servers from the farm on which new image is to be applied  **_Since_** Horizon 8.4  


[^1]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

