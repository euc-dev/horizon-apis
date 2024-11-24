---
layout: page
title: Data Object - DesktopInstantCloneDesktopProvisioningStatusData
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.InstantCloneProvisioningStatusData`

Property of
> [DesktopProvisioningStatusData](vdi.resources.Desktop.ProvisioningStatusData.md#field_detail)

See also
> [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md), [BaseImageVmId](vdi.entity.BaseImageVmId.md), [DesktopPushImageSettings](vdi.resources.Desktop.PushImageSettings.md), [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md), [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)

Since
> Horizon 7.0


## Data Object Description

Read-only operation and provisioning status data for instant clone desktops.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**operation**|  xsd:string|  The operation that this instant clone desktop is undergoing. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>NONE</td><td>There is no current operation on the desktop.</td></tr><tr><td>INITIAL_PUBLISH</td><td>The desktop has just been created and is undergoing initial publishing.</td></tr><tr><td>SCHEDULE_PUSH_IMAGE</td><td>The push operation is scheduled on the desktop.</td></tr><tr><td>CANCEL_SCHEDULED_PUSH_IMAGE</td><td>The scheduled push operation on the desktop is being cancelled.</td></tr><tr><td>INFRASTRUCTURE_CHANGE</td><td>A cluster or datastore change operation was requested for the desktop.</td></tr><tr><td>FINAL_UNPUBLISH</td><td>A desktop has been deleted and is undergoing final unpublishing.</td></tr></table>
**instantClonePendingImageState**|  xsd:string|  This represents the state of the pending image. This will be null when there is no pending image for the desktop. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>PENDING_PUBLISH</td><td>This is the initial transient state of the pending image before instant clone pool creation operation has started.</td></tr><tr><td>PUBLISHING</td><td>This is the transient state of the pending image when creation of instant clone pool operation is going on.</td></tr><tr><td>READY</td><td>This is the state of the pending image after successful publish of the pending image and before that image has been upgraded to the current image. This is normally seen after successful publish for a push image which has been scheduled to trigger at a later time.</td></tr><tr><td>READY_HELD</td><td>This is the state of the pending image after performing a selective resync operation in which the image might be applied to some of the VMs in the pool.</td></tr><tr><td>FAILED</td><td>This is the state of the pending image if creation of instant clone pool operation has failed or timed out.</td></tr><tr><td>UNPUBLISHING</td><td>This is the transient state of the pending image when instant clone pool push image operation fails or is cancelled.</td></tr></table>
**instantCloneCurrentImageState**|  xsd:string|  This represents the state of the current image. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>READY</td><td>This is the state of the current image after successful completion of pool creation operation. At this stage the current image is ready to be used to create the instant clones. Please note that this state is also reached from {@link InstantCloneCurrentImageStates#UNPUBLISHING} state on successful completion of editing of cluster or editing of datastore(s) operations.</td></tr><tr><td>FAILED</td><td>This is the state of the current image if instant clone pool delete operation has failed or timed out.</td></tr><tr><td>PENDING_UNPUBLISH</td><td>This is the state of the current image before instant clone pool delete or cluster edit or datastore(s) edit operation(s) begins.</td></tr><tr><td>UNPUBLISHING</td><td>This is the transient state of the current image when instant clone pool delete or cluster edit or datastore(s) edit operation(s) is going on.</td></tr></table>
**pendingImageParentVm**| [BaseImageVmId](vdi.entity.BaseImageVmId.md)|  Pending base image VM for Instant clone desktops. This is used to return the information about the parent VM of the pending Image. To update base image VM of instant clone desktops use [Desktop_SchedulePushImage](vdi.resources.Desktop.md#schedulePushImage) method. [^1] [^31]
**pendingImageSnapshot**| [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md)|  Pending base image snapshot for Instant clone desktops. This is used to return the information about the snapshot of the pending Image. To update base image snapshot of instant clone desktops use [Desktop_SchedulePushImage](vdi.resources.Desktop.md#schedulePushImage) method. [^1] [^31]
**pendingImageParentVmPath**|  xsd:string|  Pending [pendingImageParentVm](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md#pendingImageParentVm) path. The name is the last element of the path. [^1] [^31]
**pendingImageSnapshotPath**|  xsd:string|  Pending [pendingImageSnapshot](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md#pendingImageSnapshot) path. The name is the last element of the path. [^1] [^31]
**pendingImageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  Pending image management stream for Instant clone desktops. To update image management stream of instant clone desktops use [Desktop_SchedulePushImage](vdi.resources.Desktop.md#schedulePushImage) method.  **_Since_** Horizon 7.10 [^1] [^2]
**pendingImageManagementTag**| [ImageManagementTagId](vdi.entity.ImageManagementTagId.md)|  Pending image management tag for Instant clone desktops. To update image management tag of instant clone desktops use [Desktop_SchedulePushImage](vdi.resources.Desktop.md#schedulePushImage) method.  **_Since_** Horizon 7.10 [^1] [^2]
**pendingImageManagementStreamName**|  xsd:string|  Pending [pendingImageManagementStream](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md#pendingImageManagementStream) name.  **_Since_** Horizon 7.10 [^1] [^2]
**pendingImageManagementTagName**|  xsd:string|  Pending [pendingImageManagementTag](vdi.resources.Desktop.InstantCloneProvisioningStatusData.md#pendingImageManagementTag) name.  **_Since_** Horizon 7.10 [^1] [^2]
**pushImageSettings**| [DesktopPushImageSettings](vdi.resources.Desktop.PushImageSettings.md)|  If the current operation is a push image, the settings for that operation. [^1] [^32]
**pendingImageError**|  xsd:string|  This represents the error message if publishing of PushImage is failed.  **_Since_** Horizon 7.8 [^1]
**pendingImageProgress**|  xsd:int|  This represents the pending image publish progress in percentage for an instant clone desktop pool.  **_Since_** Horizon 7.11 [^1]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^31]: This property is required if operation is set to 'INITIAL_PUBLISH', 'SCHEDULE_PUSH_IMAGE', 'CANCEL_SCHEDULED_PUSH_IMAGE', or 'INFRASTRUCTURE_CHANGE'.
[^32]: This property is required if operation is set to 'SCHEDULE_PUSH_IMAGE'.