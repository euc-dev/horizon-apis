---
layout: page
title: Data Object - FarmScheduledMaintenanceData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Farm.ScheduledMaintenanceData`

Property of
> [FarmInstantCloneProvisioningStatusData](vdi.resources.Farm.InstantCloneProvisioningStatusData.md#field_detail)

See also
> [FarmRecurringMaintenanceSettings](vdi.resources.Farm.RecurringMaintenanceSettings.md)

Since
> Horizon 7.1


## Data Object Description

Data for scheduled maintenance operations.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**nextScheduledTime**|  xsd:dateTime|  Time when next scheduled maintenance would happen. [^1]
**immediateMaintenanceScheduled**|  xsd:boolean|  True if immediate maintenance is scheduled.  **_Since_** Horizon 7.4 [^5] [^1]
**logoffSetting**|  xsd:string|  Determines when to perform the operation on RDS servers which have an active session.  **_Since_** Horizon 7.4 <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"FORCE_LOGOFF"</td><td>Users will be forced to log off when the system is ready to operate on their RDS Servers. Before being forcibly logged off, users may have a grace period in which to save their work (Global Settings).</td></tr><tr><td>"WAIT_FOR_LOGOFF"</td><td>Wait for connected users to disconnect before the task starts. The operation starts immediately on RDS Servers without active sessions.</td></tr></table>
**stopOnFirstError**|  xsd:boolean|  Indicates that the operation should stop on first error.  **_Since_** Horizon 7.4 [^6]
**recurringMaintenanceSettings**| [FarmRecurringMaintenanceSettings](vdi.resources.Farm.RecurringMaintenanceSettings.md)|  Settings for recurring maintenance operations. [^1]
 


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.
[^6]: This property has a default value of true.