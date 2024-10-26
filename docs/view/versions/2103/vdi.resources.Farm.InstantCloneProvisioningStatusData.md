---
layout: page
title: Data Object - FarmInstantCloneProvisioningStatusData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.InstantCloneProvisioningStatusData`

Property of
> [FarmProvisioningStatusData](vdi.resources.Farm.ProvisioningStatusData.md#field_detail)

See also
> [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md), [BaseImageVmId](vdi.entity.BaseImageVmId.md), [FarmScheduledMaintenanceData](vdi.resources.Farm.ScheduledMaintenanceData.md), [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md), [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)

Since
> Horizon 7.1


## Data Object Description

Read-only operation and provisioning status data for instant clone farms.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**operation**|  xsd:string|  The operation that this instant clone farm is undergoing. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"NONE"</td><td>There is no current operation on the farm.</td></tr><tr><td>"INITIAL_PUBLISH"</td><td>The farm has just been created and is undergoing initial publishing.</td></tr><tr><td>"RECURRING_SCHEDULED_MAINTENANCE"</td><td>A recurring maintenance operation is scheduled on the farm.</td></tr><tr><td>"CANCEL_SCHEDULED_MAINTENANCE"</td><td>The recurring maintenance operation on the farm is being cancelled.</td></tr><tr><td>"INFRASTRUCTURE_CHANGE"</td><td>A cluster or datastore change operation was requested for the farm.</td></tr><tr><td>"FINAL_UNPUBLISH"</td><td>A farm has been deleted and is undergoing final unpublishing.</td></tr></table>
**operationTime**|  xsd:dateTime|  Time of the operation that instant clone farm is undergoing  **_Since_** Horizon 7.7 [^1]
**instantClonePendingImageState**|  xsd:string|  This represents the state of the pending image. This will be null when there is no pending image for the farm. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"PENDING_PUBLISH"</td><td>This is the initial transient state of the pending image before instant clone farm creation operation has started.</td></tr><tr><td>"PUBLISHING"</td><td>This is the transient state of the pending image when creation of instant clone farm operation is going on.</td></tr><tr><td>"READY"</td><td>This is the state of the pending image after successful publish of the pending image and before that image has been upgraded to the current image. This is normally seen after successful publish for a push image which has been scheduled to trigger at a later time.</td></tr><tr><td>"FAILED"</td><td>This is the state of the pending image if creation of instant clone farm operation has failed or timed out.</td></tr></table>
**instantCloneCurrentImageState**|  xsd:string|  This represents the state of the current image. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"READY"</td><td>This is the state of the current image after successful completion of farm creation operation. At this stage the current image is ready to be used to create the instant clones. Please note that this state is also reached from {@link InstantCloneCurrentImageStates#UNPUBLISHING} state on successful completion of editing of cluster or editing of datastore(s) operations.</td></tr><tr><td>"FAILED"</td><td>This is the state of the current image if instant clone farm delete operation has failed or timed out.</td></tr><tr><td>"PENDING_UNPUBLISH"</td><td>This is the state of the current image before instant clone farm delete or cluster edit or datastore(s) edit operation(s) begins.</td></tr><tr><td>"UNPUBLISHING"</td><td>This is the transient state of the current image when instant clone farm delete or cluster edit or datastore(s) edit operation(s) is going on.</td></tr></table>
**pendingImageParentVm**| [BaseImageVmId](vdi.entity.BaseImageVmId.md)|  Pending base image VM for Instant clone farms. This is used to return the information about the parent VM of the pending Image. To update base image VM of instant clone farms use Farm#scheduleRecurringMaintenance method. [^1] [^114]
**pendingImageSnapshot**| [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md)|  Pending base image snapshot for Instant clone farms. This is used to return the information about the snapshot of the pending Image. To update base image snapshot of instant clone farms use Farm#scheduleRecurringMaintenance method. [^1] [^114]
**pendingImageParentVmPath**|  xsd:string|  Pending [pendingImageParentVm](vdi.resources.Farm.InstantCloneProvisioningStatusData.md#pendingImageParentVm) path. The name is the last element of the path. [^1] [^114]
**pendingImageSnapshotPath**|  xsd:string|  Pending [pendingImageSnapshot](vdi.resources.Farm.InstantCloneProvisioningStatusData.md#pendingImageSnapshot) path. The name is the last element of the path. [^1] [^114]
**pendingImageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  Pending image management stream for Instant clone farms. To update image management stream of instant clone farms use Farm#scheduleRecurringMaintenance method.  **_Since_** Horizon 7.10 [^1] [^2]
**pendingImageManagementTag**| [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)|  Pending image management tag for Instant clone farms. To update image management tag of instant clone farms use Farm#scheduleRecurringMaintenance method.  **_Since_** Horizon 7.10 [^1] [^2]
**pendingImageManagementStreamName**|  xsd:string|  Pending [pendingImageManagementStream](vdi.resources.Farm.InstantCloneProvisioningStatusData.md#pendingImageManagementStream) name.  **_Since_** Horizon 7.10 [^1] [^2]
**pendingImageManagementTagName**|  xsd:string|  Pending [pendingImageManagementTag](vdi.resources.Farm.InstantCloneProvisioningStatusData.md#pendingImageManagementTag) name.  **_Since_** Horizon 7.10 [^1] [^2]
**scheduledMaintenanceData**| [FarmScheduledMaintenanceData](vdi.resources.Farm.ScheduledMaintenanceData.md)|  Scheduled maintenance settings for automated instant clone farm. [^1]
**pendingImageError**|  xsd:string|  This represents the error message if publishing of PushImage is failed.  **_Since_** Horizon 7.8 [^1]
**pendingImageProgress**|  xsd:int|  This represents the pending image publish progress in percentage for an instant clone farm.  **_Since_** Horizon 7.11 [^1]


 
