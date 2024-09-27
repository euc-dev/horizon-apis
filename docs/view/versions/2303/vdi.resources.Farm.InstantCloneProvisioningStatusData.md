---
layout: page
title: Data Object - FarmInstantCloneProvisioningStatusData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Farm.InstantCloneProvisioningStatusData  
Property of
     [FarmProvisioningStatusData](vdi.resources.Farm.ProvisioningStatusData.md#field_detail)  
See also
     [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md), [BaseImageVmId](vdi.entity.BaseImageVmId.md), [FarmComputeProfileSpec](vdi.resources.Farm.ComputeProfileSpec.md), [FarmScheduledMaintenanceData](vdi.resources.Farm.ScheduledMaintenanceData.md), [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md), [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)  
Since 
    Horizon 7.1

## Data Object Description 

Read-only operation and provisioning status data for instant clone farms. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**operation**|  xsd:string|  The operation that this instant clone farm is undergoing.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"NONE"| There is no current operation on the farm.  
"INITIAL_PUBLISH"| The farm has just been created and is undergoing initial publishing.  
"RECURRING_SCHEDULED_MAINTENANCE"| A recurring maintenance operation is scheduled on the farm.  
"CANCEL_SCHEDULED_MAINTENANCE"| The recurring maintenance operation on the farm is being cancelled.  
"INFRASTRUCTURE_CHANGE"| A cluster or datastore change operation was requested for the farm.  
"FINAL_UNPUBLISH"| A farm has been deleted and is undergoing final unpublishing.  

  
**operationTime**|  xsd:dateTime|  Time of the operation that instant clone farm is undergoing  **_Since_** Horizon 7.7  


* This property need not be set.

  
**instantClonePendingImageState**|  xsd:string|  This represents the state of the pending image. This will be null when there is no pending image for the farm.   


* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"PENDING_PUBLISH"| This is the initial transient state of the pending image before instant clone farm creation operation has started.  
"PUBLISHING"| This is the transient state of the pending image when creation of instant clone farm operation is going on.  
"READY"| This is the state of the pending image after successful publish of the pending image and before that image has been upgraded to the current image. This is normally seen after successful publish for a push image which has been scheduled to trigger at a later time.  
"READY_HELD"| This is the state of the pending image after performing a selective resync operation in which the image might be applied to some of the macines in the farm.  
"FAILED"| This is the state of the pending image if creation of instant clone farm operation has failed or timed out.  

  
**instantCloneCurrentImageState**|  xsd:string|  This represents the state of the current image.   


* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"READY"| This is the state of the current image after successful completion of farm creation operation. At this stage the current image is ready to be used to create the instant clones. Please note that this state is also reached from {@link InstantCloneCurrentImageStates#UNPUBLISHING} state on successful completion of editing of cluster or editing of datastore(s) operations.  
"FAILED"| This is the state of the current image if instant clone farm delete operation has failed or timed out.  
"PENDING_UNPUBLISH"| This is the state of the current image before instant clone farm delete or cluster edit or datastore(s) edit operation(s) begins.  
"UNPUBLISHING"| This is the transient state of the current image when instant clone farm delete or cluster edit or datastore(s) edit operation(s) is going on.  

  
**pendingImageParentVm**| [BaseImageVmId](vdi.entity.BaseImageVmId.md)|  Pending base image VM for Instant clone farms. This is used to return the information about the parent VM of the pending Image. To update base image VM of instant clone farms use Farm#scheduleRecurringMaintenance method.   


* This property need not be set.
  * This property is required if operation is set to "INITIAL_PUBLISH", "CANCEL_SCHEDULED_MAINTENANCE", or "INFRASTRUCTURE_CHANGE".

  
**pendingImageSnapshot**| [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md)|  Pending base image snapshot for Instant clone farms. This is used to return the information about the snapshot of the pending Image. To update base image snapshot of instant clone farms use Farm#scheduleRecurringMaintenance method.   


* This property need not be set.
  * This property is required if operation is set to "INITIAL_PUBLISH", "CANCEL_SCHEDULED_MAINTENANCE", or "INFRASTRUCTURE_CHANGE".

  
**pendingImageParentVmPath**|  xsd:string|  Pending [pendingImageParentVm](vdi.resources.Farm.InstantCloneProvisioningStatusData.md#pendingImageParentVm) path. The name is the last element of the path.   


* This property need not be set.
  * This property is required if operation is set to "INITIAL_PUBLISH", "CANCEL_SCHEDULED_MAINTENANCE", or "INFRASTRUCTURE_CHANGE".

  
**pendingImageSnapshotPath**|  xsd:string|  Pending [pendingImageSnapshot](vdi.resources.Farm.InstantCloneProvisioningStatusData.md#pendingImageSnapshot) path. The name is the last element of the path.   


* This property need not be set.
  * This property is required if operation is set to "INITIAL_PUBLISH", "CANCEL_SCHEDULED_MAINTENANCE", or "INFRASTRUCTURE_CHANGE".

  
**pendingImageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  Pending image management stream for Instant clone farms. To update image management stream of instant clone farms use Farm#scheduleRecurringMaintenance method.  **_Since_** Horizon 7.10  


* This property need not be set.
* This property cannot be updated.

  
**pendingImageManagementTag**| [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)|  Pending image management tag for Instant clone farms. To update image management tag of instant clone farms use Farm#scheduleRecurringMaintenance method.  **_Since_** Horizon 7.10  


* This property need not be set.
* This property cannot be updated.

  
**pendingImageManagementStreamName**|  xsd:string|  Pending [pendingImageManagementStream](vdi.resources.Farm.InstantCloneProvisioningStatusData.md#pendingImageManagementStream) name.  **_Since_** Horizon 7.10  


* This property need not be set.
* This property cannot be updated.

  
**pendingImageManagementTagName**|  xsd:string|  Pending [pendingImageManagementTag](vdi.resources.Farm.InstantCloneProvisioningStatusData.md#pendingImageManagementTag) name.  **_Since_** Horizon 7.10  


* This property need not be set.
* This property cannot be updated.

  
**scheduledMaintenanceData**| [FarmScheduledMaintenanceData](vdi.resources.Farm.ScheduledMaintenanceData.md)|  Scheduled maintenance settings for automated instant clone farm.   


* This property need not be set.

  
**pendingImageError**|  xsd:string|  This represents the error message if publishing of PushImage is failed.  **_Since_** Horizon 7.8  


* This property need not be set.

  
**pendingImageProgress**|  xsd:int|  This represents the pending image publish progress in percentage for an instant clone farm.  **_Since_** Horizon 7.11  


* This property need not be set.

  
**pendingComputeProfile**| [FarmComputeProfileSpec](vdi.resources.Farm.ComputeProfileSpec.md)|  Pending compute Profile used to specify the CPU, RAM and cores per socket configuration to create VMs with.  **_Since_** Horizon 8.6  


* This property need not be set.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

