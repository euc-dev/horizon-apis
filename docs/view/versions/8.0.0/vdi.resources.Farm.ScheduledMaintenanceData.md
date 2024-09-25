---
layout: page
title: Data Object - FarmScheduledMaintenanceData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Farm.ScheduledMaintenanceData
Property of
     [FarmInstantCloneProvisioningStatusData](vdi.resources.Farm.InstantCloneProvisioningStatusData.md#field_detail)
See also
     [FarmRecurringMaintenanceSettings](vdi.resources.Farm.RecurringMaintenanceSettings.md)
Since 
    Horizon 7.1

## Data Object Description 

Data for scheduled maintenance operations. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**nextScheduledTime**|  xsd:dateTime|  Time when next scheduled maintenance would happen.   


[^1]

  
**immediateMaintenanceScheduled**|  xsd:boolean|  True if immediate maintenance is scheduled.  **_Since_** Horizon 7.4  


  * This property has a default value of false.
[^1]

  
**logoffSetting**|  xsd:string|  Determines when to perform the operation on RDS servers which have an active session.  **_Since_** Horizon 7.4  


  * This property will be one of:  
|  Value |  Description   
---|---  
"FORCE_LOGOFF"| Users will be forced to log off when the system is ready to operate on their RDS Servers. Before being forcibly logged off, users may have a grace period in which to save their work (Global Settings).  
"WAIT_FOR_LOGOFF"| Wait for connected users to disconnect before the task starts. The operation starts immediately on RDS Servers without active sessions.  

  
**stopOnFirstError**|  xsd:boolean|  Indicates that the operation should stop on first error.  **_Since_** Horizon 7.4  


  * This property has a default value of true.

  
**recurringMaintenanceSettings**| [FarmRecurringMaintenanceSettings](vdi.resources.Farm.RecurringMaintenanceSettings.md)|  Settings for recurring maintenance operations.   


[^1]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
