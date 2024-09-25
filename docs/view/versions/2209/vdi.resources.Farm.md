---
layout: page
title: Service - Farm
hide:
 #- navigation
 - toc
---

  
| | | Local Methods  
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Farm
See also
     [ApplicationDiscoveryData](vdi.resources.Application.ApplicationDiscoveryData.md), [FarmId](vdi.entity.FarmId.md), [FarmInfo](vdi.resources.Farm.FarmInfo.md), [FarmMaintenanceSpec](vdi.resources.Farm.MaintenanceSpec.md), [FarmMissingApplicationInstallationData](vdi.resources.Farm.MissingApplicationInstallationData.md), [FarmRecomposeSpec](vdi.resources.Farm.RecomposeSpec.md), [FarmSpec](vdi.resources.Farm.FarmSpec.md), [FarmSummaryView](vdi.resources.Farm.FarmSummaryView.md), [MapEntry](vdi.util.MapEntry.md), [RDSServerId](vdi.entity.RDSServerId.md)
Since 
    Horizon View 6.0

  


## Service Description

Service that represents Farm 

Methods

Methods defined in this Service   
---  
Farm_AddRDSServers, Farm_ApplyImage, Farm_CancelScheduleMaintenance, Farm_Create, Farm_Delete, Farm_DiscoverInstalledApplications, Farm_Get, Farm_GetByNamingPattern, Farm_GetSummaryView, Farm_ImageManagementScheduleMaintenance, Farm_PromotePendingImage, Farm_Recompose, Farm_RemoveRDSServers, Farm_ScheduleMaintenance, Farm_Update, Farm_ValidateInstalledApplications  
  



Adds a set of RDS servers to the Farm. This operation is only applicable for manual farms. 

Privileges 

Privilege |  Description   
---|---  
POOL_MANAGEMENT|  privilege is required to add RDSServers to the Farm.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Farm](vdi.resources.Farm.md) used to make the method call.   
**id**| [FarmId](vdi.entity.FarmId.md)|  The entityId of the Farm.   
  
**rdsServers**| [RDSServerId[]](vdi.entity.RDSServerId.md)|  The array of RDSServerIds to be added to the Farm.   
  
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_FARM_RDSSERVER_ADDED|  An RDSServer is successfully added to the Farm.   
VLSI_FARM_RDSSERVER_ADD_FAILED|  The RDSServer addition failed.   
  
Show WSDL type definition

  
  
  



Applies the current or pending image to selected rds servers machines in the farm 

Privileges 

Privilege |  Description   
---|---  
POOL_SVI_IMAGE_MANAGEMENT|  Manage maintenance operations on Automated Desktops & Farms with the corresponding access group permission is required to schedule maintenance.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Farm](vdi.resources.Farm.md) used to make the method call.   
**id**| [FarmId](vdi.entity.FarmId.md)|  unique identifier for a farm entry.   
  
**rdsServers**| [RDSServerId[]](vdi.entity.RDSServerId.md)|    
  
**pendingImage**|  xsd:boolean|  Set to true if the pending image is to be applied. Else current image is applied .   
  
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_FARM_SCHEDULE_MAINTENANCE_CREATED|  This will be sent if the new schedule is successfully created.   
VLSI_FARM_SCHEDULE_MAINTENANCE_CREATE_FAILED|  This will be sent if the schedule creation failed.   
  
Show WSDL type definition

  
  
  



Requests cancellation of the current scheduled maintenance on the specified Instant Clone Engine sourced farm.   
[operation](vdi.resources.Farm.InstantCloneProvisioningStatusData.md#operation) must be RECURRING_SCHEDULED_MAINTENANCE and this will stop further maintenance operation execution. This operation is applicable only to Instant clone engine sourced farms. If a pending image was specified as part of recurring or immediate maintenance it will also be cancelled. If the image has already been published then it will not be cancelled and will remain as the current image for this farm. 

Privileges 

Privilege |  Description   
---|---  
POOL_SVI_IMAGE_MANAGEMENT|  Manage maintenance operations on Automated Desktops & Farms with the corresponding access group permission is required to cancel schedule maintenance.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Farm](vdi.resources.Farm.md) used to make the method call.   
**id**| [FarmId](vdi.entity.FarmId.md)|  unique identifier for a farm entry.   
  
**maintenanceMode**|  xsd:string|  scheduled maintenance mode (IMMEDIATE, RECURRING) to be deleted.   
  
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_FARM_SCHEDULE_MAINTENANCE_CANCELLED|  This will be sent if the scheduled maintenance was successfully cancelled.   
VLSI_FARM_SCHEDULE_MAINTENANCE_CANCEL_FAILED|  This will be sent if the scheduled maintenance cancellation failed.   
  
Show WSDL type definition

  
  
  



Create a new Farm. 

Privileges 

Privilege |  Description   
---|---  
POOL_MANAGEMENT|  privilege is required create the Farm.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Farm](vdi.resources.Farm.md) used to make the method call.   
**spec**| [FarmSpec](vdi.resources.Farm.FarmSpec.md)|  The information required to create the new Farm   
  
  


Return Value 

Type |  Description   
---|---  
[FarmId](vdi.entity.FarmId.md)| The id of the new Farm  
  


Faults 

Type |  Description   
---|---  
[EntityAlreadyExists](vdi.fault.EntityAlreadyExists.md)| Thrown if Farm with given Id already exists.  
[EntityInUse](vdi.fault.EntityInUse.md)| Thrown if at least one RDSServerId in spec is assigned to another Farm.  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidLicense](vdi.fault.InvalidLicense.md)| Thrown in one of the following cases during Instant Clone Farm creation: 

  * License is not applied to the system.
  * Applied license is expired.
  * Applied license does not have instant clone feature enabled.

  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_FARM_CREATED|  if Farm creation succeeds.   
VLSI_FARM_CREATE_FAILED|  if Farm creation fails.   
  
Show WSDL type definition

  
  
  



Delete a given Farm. For an automated farm, all the RDS Server VMs are deleted from disk whereas for a manual farm only the RDS Server associations are removed. 

Privileges 

Privilege |  Description   
---|---  
POOL_MANAGEMENT|  privilege is required to delete the Farm.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Farm](vdi.resources.Farm.md) used to make the method call.   
**id**| [FarmId](vdi.entity.FarmId.md)|  The entityId of the Farm to delete   
  
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_FARM_DELETED|  if the Farm is successfully deleted.   
VLSI_FARM_DELETE_FAILED|  if the Farm deletion failed.   
  
Show WSDL type definition

  
  
  



Query AppTap for the list of installed applications on the given Farm. 

Privileges 

Privilege |  Description   
---|---  
POOL_VIEW|  privilege is required to discover installed Applications.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Farm](vdi.resources.Farm.md) used to make the method call.   
**id**| [FarmId](vdi.entity.FarmId.md)|  The entityId of the Farm on which to discover installed applications   
  
  


Return Value 

Type |  Description   
---|---  
[ApplicationDiscoveryData[]](vdi.resources.Application.ApplicationDiscoveryData.md)| The list of installed applications  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Get a Farm by Id. 

Privileges 

Privilege |  Description   
---|---  
POOL_VIEW|  privilege is required get the Farm information.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Farm](vdi.resources.Farm.md) used to make the method call.   
**id**| [FarmId](vdi.entity.FarmId.md)|  The entityId of the Farm to get   
  
  


Return Value 

Type |  Description   
---|---  
[FarmInfo](vdi.resources.Farm.FarmInfo.md)| requested Farm entity  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Get a farm by naming pattern. 

Privileges 

Privilege |  Description   
---|---  
POOL_VIEW|  privilege is required to get the farm information.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Farm](vdi.resources.Farm.md) used to make the method call.   
**namingPattern**|  xsd:string|  Unique virtual machine naming pattern for a farm entry.   
  
  


Return Value 

Type |  Description   
---|---  
[FarmInfo](vdi.resources.Farm.FarmInfo.md)| The FarmInfo  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Get Farm Summary View by Id. 

Privileges 

Privilege |  Description   
---|---  
POOL_VIEW|  privilege is required get the Farm Summary view.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Farm](vdi.resources.Farm.md) used to make the method call.   
**id**| [FarmId](vdi.entity.FarmId.md)|  The entityId of the Farm   
  
  


Return Value 

Type |  Description   
---|---  
[FarmSummaryView](vdi.resources.Farm.FarmSummaryView.md)| requested Farm entity  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Creates maintenance schedule for the specified Instant clone farm created using image catalog. This can be used for creating both immediate or recurring maintenance. At most one schedule of both the types can co-exist at same time. Optionally user can request an update of the Image in the specified farm. This marks the old image to be replaced by new image, which is performed asynchronously. Once the new image is successfully updated, all eligible RDS servers in the farm would also be marked for update with new image, this operation is also performed asynchronously. This operation can also be used to replace an existing scheduled maintenance. Immediate maintenance will take priority over any existing scheduled recurring maintenance. Recurring maintenance for this farm will be put on hold until immediate maintenance has completed. 

Privileges 

Privilege |  Description   
---|---  
POOL_SVI_IMAGE_MANAGEMENT|  Manage maintenance operations on Automated Desktops & Farms with the corresponding access group permission is required to schedule maintenance.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Farm](vdi.resources.Farm.md) used to make the method call.   
**id**| [FarmId](vdi.entity.FarmId.md)|  unique identifier for a farm entry.   
  
**spec**| [FarmMaintenanceSpec](vdi.resources.Farm.MaintenanceSpec.md)|  The specification for the scheduled maintenance operation.   
  
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_FARM_SCHEDULE_MAINTENANCE_CREATED|  This will be sent if the new schedule is successfully created.   
VLSI_FARM_SCHEDULE_MAINTENANCE_CREATE_FAILED|  This will be sent if the schedule creation failed.   
  
Show WSDL type definition

  
  
  



Applies the pending image to all rds servers in the farm 

Privileges 

Privilege |  Description   
---|---  
POOL_SVI_IMAGE_MANAGEMENT|  Manage maintenance operations on Automated Desktops & Farms with the corresponding access group permission is required to schedule maintenance.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Farm](vdi.resources.Farm.md) used to make the method call.   
**id**| [FarmId](vdi.entity.FarmId.md)|  unique identifier for a farm entry.   
  
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_FARM_SCHEDULE_MAINTENANCE_CREATED|  This will be sent if the new schedule is successfully created.   
VLSI_FARM_SCHEDULE_MAINTENANCE_CREATE_FAILED|  This will be sent if the schedule creation failed.   
  
Show WSDL type definition

  
  
  



Requests a recompose of RDS Servers in the specified automated farm. This marks the RDS Servers for recompose, which is performed asynchronously. 

Privileges 

Privilege |  Description   
---|---  
POOL_SVI_IMAGE_MANAGEMENT|  Manage maintenance operations on Automated Desktops & Farms privilege with the corresponding access group permission is required to recompose the farm.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Farm](vdi.resources.Farm.md) used to make the method call.   
**id**| [FarmId](vdi.entity.FarmId.md)|  unique identifier for a farm entry   
  
**spec**| [FarmRecomposeSpec](vdi.resources.Farm.RecomposeSpec.md)|  The specification for the recompose operation.   
  
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[PartialFailureFault](vdi.fault.PartialFailureFault.md)| Thrown if all operations were not successful, a PartialFailureFault will be thrown indicating which RDS servers were successfully marked for recompose and which ones failed. The index of results in the PartialFailureFault correspond to the index of the original RDS server. The result entry will contain either be the original return type (on success) or an exception (on failure).  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_FARM_RECOMPOSED|  This will be sent if all RDS servers were successfully marked for recompose.   
VLSI_RDSSERVER_RECOMPOSED|  This will be sent if an RDS server was successfully marked for recompose.   
VLSI_FARM_RECOMPOSE_FAILED|  This will be sent if any RDS server failed to be marked for recompose.   
VLSI_RDSSERVER_RECOMPOSE_FAILED|  This will be sent if an RDS server failed to be marked for recompose.   
  
Show WSDL type definition

  
  
  



Removes a set of RDS servers from the Farm. For an automated farm, removing an RDS server deletes it from disk where as for a manual farm only the association is removed. 

Privileges 

Privilege |  Description   
---|---  
POOL_MANAGEMENT|  privilege is required to remove RDSServers from the Farm.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Farm](vdi.resources.Farm.md) used to make the method call.   
**id**| [FarmId](vdi.entity.FarmId.md)|  The entityId of the Farm.   
  
**rdsServers**| [RDSServerId[]](vdi.entity.RDSServerId.md)|  The array of RDSServerIds to be removed from the Farm.   
  
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_FARM_RDSSERVER_REMOVED|  An RDSServer is successfully removed from the Farm.   
VLSI_FARM_RDSSERVER_REMOVE_FAILED|  The RDSServer removal failed.   
  
Show WSDL type definition

  
  
  



Creates maintenance schedule for the specified farm. This can be used for creating both immediate or recurring maintenance. At most one schedule of both the types can co-exist at same time. Optionally user can request an update of the Image in the specified farm. This marks the old image to be replaced by new image, which is performed asynchronously. Once the new image is successfully updated, all eligible RDS servers in the farm would also be marked for update with new image, this operation is also performed asynchronously. This operation can also be used to replace an existing scheduled maintenance. This operation is applicable only to Instant clone engine sourced farms. Immediate maintenance will take priority over any existing scheduled recurring maintenance. Recurring maintenance for this farm will be put on hold until immediate maintenance has completed. 

Privileges 

Privilege |  Description   
---|---  
POOL_SVI_IMAGE_MANAGEMENT|  Manage maintenance operations on Automated Desktops & Farms with the corresponding access group permission is required to schedule maintenance.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Farm](vdi.resources.Farm.md) used to make the method call.   
**id**| [FarmId](vdi.entity.FarmId.md)|  unique identifier for a farm entry.   
  
**spec**| [FarmMaintenanceSpec](vdi.resources.Farm.MaintenanceSpec.md)|  The specification for the scheduled maintenance operation.   
  
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_FARM_SCHEDULE_MAINTENANCE_CREATED|  This will be sent if the new schedule is successfully created.   
VLSI_FARM_SCHEDULE_MAINTENANCE_CREATE_FAILED|  This will be sent if the schedule creation failed.   
  
Show WSDL type definition

  
  
  



Update a Farm with the set of attributes in the map. 

Privileges 

Privilege |  Description   
---|---  
POOL_ENABLE|  privilege is required to update enabled flag.   
POOL_MANAGEMENT|  privilege is required on current and (to be updated) access group, to update access group.   
POOL_MANAGEMENT|  privilege is required on current access group, to update any other attributes.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Farm](vdi.resources.Farm.md) used to make the method call.   
**id**| [FarmId](vdi.entity.FarmId.md)|  The entityId of the Farm to be updated   
  
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  The key-value pairs describing attributes to be updated   


  * This parameter is an update map based on [FarmInfo](vdi.resources.Farm.FarmInfo.md "FarmInfo"). 

  
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_FARM_UPDATED|  for each Farm attribute that was updated.   
VLSI_FARM_UPDATE_FAILED|  if the Farm update failed.   
  
Show WSDL type definition

  
  
  



Validate that each application in the given list is installed on the RDS Servers belonging to the specified Farm. 

Privileges 

Privilege |  Description   
---|---  
POOL_VIEW|  privilege is required to validate installed Applications.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Farm](vdi.resources.Farm.md) used to make the method call.   
**id**| [FarmId](vdi.entity.FarmId.md)|  The entityId of the Farm on which to validate installed applications   
  
**applicationExePaths**|  xsd:string[]|  Array of applicationExePaths for the applications to be validated   
  
  


Return Value 

Type |  Description   
---|---  
[FarmMissingApplicationInstallationData[]](vdi.resources.Farm.MissingApplicationInstallationData.md)| The list of MissingApplicationInstallationData *NOT INSTALLED* on the RDS Servers belonging to the Farm.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
Top of page| | | Local Methods  
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

