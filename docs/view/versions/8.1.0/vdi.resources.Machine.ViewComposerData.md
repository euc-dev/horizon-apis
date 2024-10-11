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
**baseImagePath**|  xsd:string|  The base image.   


* This property need not be set.
* This property cannot be updated.

  
**baseImageSnapshotPath**|  xsd:string|  The base image snapshot.   


* This property need not be set.
* This property cannot be updated.

  
**pendingBaseImagePath**|  xsd:string|  The pending base image.   


* This property need not be set.
* This property cannot be updated.

  
**pendingBaseImageSnapshotPath**|  xsd:string|  The pending base image snapshot.   


* This property need not be set.
* This property cannot be updated.

  
**imageManagementStreamName**|  xsd:string|  Name of the image management stream. This will be populated only for instant clone machines provisioned from pools created using image catalog.  **_Since_** Horizon 7.10  


* This property need not be set.
* This property cannot be updated.

  
**imageManagementTagName**|  xsd:string|  Name of the image management tag. This will be populated only for instant clone machines provisioned from pools created using image catalog.  **_Since_** Horizon 7.10  


* This property need not be set.
* This property cannot be updated.

  
**pendingImageManagementStreamName**|  xsd:string|  Name of the pending image management stream. This will be populated only for instant clone machines provisioned from pools created using image catalog.  **_Since_** Horizon 7.10  


* This property need not be set.
* This property cannot be updated.

  
**pendingImageManagementTagName**|  xsd:string|  Name of the pending image management tag. This will be populated only for instant clone machines provisioned from pools created using image catalog.  **_Since_** Horizon 7.10  


* This property need not be set.
* This property cannot be updated.

  
**lastMaintenanceTime**|  xsd:dateTime|  The time of last maintenance operation.   


* This property need not be set.
* This property cannot be updated.

  
**operation**|  xsd:string|  The current maintenance operation.   


* This property need not be set.
* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"REFRESH"| A refresh operation.  
"RESYNC"| A resync operation.  
"REBALANCE"| A rebalance operation.  
"ATTACH"| A persistent disk attach operation.  
"DETACH"| A persistent disk detach operation.  
"REPLACE"| A persistent disk replace operation.  
"CHECKPOINT"| A checkpoint operation.  
"PUSH_IMAGE"| A push image operation (Instant Clone Engine only).  

  
**autoRefreshLogOffSetting**|  xsd:string|  The logoff setting for auto refresh operation.  **_Since_** Horizon 7.4  


* This property need not be set.
* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"FORCE_LOGOFF"| Users will be forced to log off when the system is ready to operate on their virtual machines. Before being forcibly logged off, users may have a grace period in which to save their work (Global Settings).  
"WAIT_FOR_LOGOFF"| Wait for connected users to disconnect before the task starts. The operation starts immediately on machines without active sessions.  

  
**operationState**|  xsd:string|  The maintenance operation state.   


* This property need not be set.
* This property cannot be updated.
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

  
**datastorePaths**|  xsd:string[]|  The name(s) of the datastore(s) occupied by the virtual machine.   


* This property need not be set.
  * This property is an unordered array of unique values.
* This property cannot be updated.

  
**persistentDisks**| [PersistentDiskId[]](vdi.entity.PersistentDiskId.md)|  The persistent disk(s).   


* This property need not be set.
  * This property is an unordered array of unique values.
* This property cannot be updated.

  
  
  
  
  
  
