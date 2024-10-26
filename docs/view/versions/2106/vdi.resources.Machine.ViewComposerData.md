---
layout: page
title: Data Object - MachineViewComposerData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Machine.ViewComposerData`

Property of
> [MachineManagedMachineData](vdi.resources.Machine.ManagedMachineData.md#field_detail)

See also
> [PersistentDiskId](vdi.entity.PersistentDiskId.md)

Since
> Horizon View 6.0


## Data Object Description

Fields specific to View Composer

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**baseImagePath**|  xsd:string|  The base image. [^1] [^2]
**baseImageSnapshotPath**|  xsd:string|  The base image snapshot. [^1] [^2]
**pendingBaseImagePath**|  xsd:string|  The pending base image. [^1] [^2]
**pendingBaseImageSnapshotPath**|  xsd:string|  The pending base image snapshot. [^1] [^2]
**imageManagementStreamName**|  xsd:string|  Name of the image management stream. This will be populated only for instant clone machines provisioned from pools created using image catalog.  **_Since_** Horizon 7.10 [^1] [^2]
**imageManagementTagName**|  xsd:string|  Name of the image management tag. This will be populated only for instant clone machines provisioned from pools created using image catalog.  **_Since_** Horizon 7.10 [^1] [^2]
**pendingImageManagementStreamName**|  xsd:string|  Name of the pending image management stream. This will be populated only for instant clone machines provisioned from pools created using image catalog.  **_Since_** Horizon 7.10 [^1] [^2]
**pendingImageManagementTagName**|  xsd:string|  Name of the pending image management tag. This will be populated only for instant clone machines provisioned from pools created using image catalog.  **_Since_** Horizon 7.10 [^1] [^2]
**lastMaintenanceTime**|  xsd:dateTime|  The time of last maintenance operation. [^1] [^2]
**operation**|  xsd:string|  The current maintenance operation. [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"REFRESH"</td><td>A refresh operation.</td></tr><tr><td>"RESYNC"</td><td>A resync operation.</td></tr><tr><td>"REBALANCE"</td><td>A rebalance operation.</td></tr><tr><td>"ATTACH"</td><td>A persistent disk attach operation.</td></tr><tr><td>"DETACH"</td><td>A persistent disk detach operation.</td></tr><tr><td>"REPLACE"</td><td>A persistent disk replace operation.</td></tr><tr><td>"CHECKPOINT"</td><td>A checkpoint operation.</td></tr><tr><td>"PUSH_IMAGE"</td><td>A push image operation (Instant Clone Engine only).</td></tr></table>
**autoRefreshLogOffSetting**|  xsd:string|  The logoff setting for auto refresh operation.  **_Since_** Horizon 7.4 [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"FORCE_LOGOFF"</td><td>Users will be forced to log off when the system is ready to operate on their virtual machines. Before being forcibly logged off, users may have a grace period in which to save their work (Global Settings).</td></tr><tr><td>"WAIT_FOR_LOGOFF"</td><td>Wait for connected users to disconnect before the task starts. The operation starts immediately on machines without active sessions.</td></tr></table>
**operationState**|  xsd:string|  The maintenance operation state. [^1] [^2]
* This property will be one of:
|  Value |  Description
---|---
"UNDEFINED"| The operation state is unrecognized.
"SCHEDULED"| The operation is scheduled for future execution.
"PROGRESSING"| The operation is in progress.
"COMPLETED"| The operation has completed.
"FAULT"| The operation has encountered an error.
"CANCELLING"| The operation has been cancelled.
"HOLDING"| The operation has been paused.
"CREATE"| The operation is being initiated.
**datastorePaths**|  xsd:string[]|  The name(s) of the datastore(s) occupied by the virtual machine. [^1] [^14] [^2]
**persistentDisks**| [PersistentDiskId[]](vdi.entity.PersistentDiskId.md)|  The persistent disk(s). [^1] [^14] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^14]: This property is an unordered array of unique values.