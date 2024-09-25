---
layout: page
title: Data Object - ManagedMachineDetailsData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Machine.ManagedMachineDetailsData
Property of
     [MachineDetailsView](vdi.resources.Machine.MachineDetailsView.md#field_detail)
See also
     [MachineVirtualDiskData](vdi.resources.Machine.VirtualDiskData.md), [PersistentDiskId](vdi.entity.PersistentDiskId.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)
Since 
    Horizon 7.7

## Data Object Description 

Details specific to managed machine. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  The Id of the Virtual Center managing this Machine.   


[^2]

  
**hostName**|  xsd:string|  The name of the host on which this virtual machine is registered.   


[^1]
[^2]

  
**datastorePaths**|  xsd:string[]|  The name(s) of the datastore(s) occupied by the virtual machine.   


[^1]
  * This property is an unordered array of unique values.
[^2]

  
**virtualDisks**| [MachineVirtualDiskData[]](vdi.resources.Machine.VirtualDiskData.md)|  The virtual disk(s) comprising the virtual machine.   


[^1]
  * This property is an unordered array of unique values.
[^2]

  
**persistentDisks**| [PersistentDiskId[]](vdi.entity.PersistentDiskId.md)| **Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._ The persistent disk(s) attached to this machine. This will be populated only for Linked clone provisioned machine.   


[^1]
  * This property is an unordered array of unique values.
[^2]

  
**lastMaintenanceTime**|  xsd:dateTime|  The time of last maintenance operation. This will be populated only for Linked clone or Instant clone provisioned machine.   


[^1]
[^2]

  
**operation**|  xsd:string|  The current maintenance operation. This will be populated only for Linked clone or Instant clone provisioned machine.   


[^1]
[^2]
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

  
**operationState**|  xsd:string|  The maintenance operation state. This will be populated only for Linked clone or Instant clone provisioned machine.   


[^1]
[^2]
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
"STANDBY"| The operation is on standby for selective push.  

  
**autoRefreshLogOffSetting**|  xsd:string|  The logoff setting for auto refresh operation. This will be populated only for Linked clone or Instant clone provisioned machine.   


[^1]
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"FORCE_LOGOFF"| Users will be forced to log off when the system is ready to operate on their virtual machines. Before being forcibly logged off, users may have a grace period in which to save their work (Global Settings).  
"WAIT_FOR_LOGOFF"| Wait for connected users to disconnect before the task starts. The operation starts immediately on machines without active sessions.  

  
**inHoldCustomization**|  xsd:boolean|  While a machine is in a particular basic state, it can be subject to further conditions. This condition determines if this virtual machine should hold before customization is started.   


[^2]

  
**missingInVCenter**|  xsd:boolean|  While a machine is in a particular basic state, it can be subject to further conditions. This condition determines if the virtual machine is missing in vCenter Server.   


[^2]

  
**createTime**|  xsd:dateTime|  Time the machine was created.   


[^1]
[^2]

  
**cloneErrorMessage**|  xsd:string|  Cloning error message for this machine. This will be set for machine belonging to automated desktops when the machine's [basicState](vdi.resources.Machine.MachineData.md#basicState) is in PROVISIONING_ERROR or ERROR state.   


[^1]
[^2]

  
**cloneErrorTime**|  xsd:dateTime|  Cloning error time for this machine. This will be set for machine belonging to automated desktops when the machine's [basicState](vdi.resources.Machine.MachineData.md#basicState) is in PROVISIONING_ERROR or ERROR state.   


[^1]
[^2]

  
**baseImagePath**|  xsd:string|  The base image. This will be populated only for Linked clone or Instant clone provisioned machine.   


[^1]
[^2]

  
**baseImageSnapshotPath**|  xsd:string|  The base image snapshot. This will be populated only for Linked clone or Instant clone provisioned machine.   


[^1]
[^2]

  
**pendingBaseImagePath**|  xsd:string|  The pending base image. This will be populated only for Linked clone or Instant clone provisioned machine.   


[^1]
[^2]

  
**pendingBaseImageSnapshotPath**|  xsd:string|  The pending base image snapshot. This will be populated only for Linked clone or Instant clone provisioned machine.   


[^1]
[^2]

  
**imageManagementStreamName**|  xsd:string|  Name of the image management stream. This will be populated only for instant clone machines provisioned from pools created using image catalog.  **_Since_** Horizon 7.10  


[^1]
[^2]

  
**imageManagementTagName**|  xsd:string|  Name of the image management tag. This will be populated only for instant clone machines provisioned from pools created using image catalog.  **_Since_** Horizon 7.10  


[^1]
[^2]

  
**pendingImageManagementStreamName**|  xsd:string|  Name of the pending image management stream. This will be populated only for instant clone machines provisioned from pools created using image catalog.  **_Since_** Horizon 7.10  


[^1]
[^2]

  
**pendingImageManagementTagName**|  xsd:string|  Name of the pending image management tag. This will be populated only for instant clone machines provisioned from pools created using image catalog.  **_Since_** Horizon 7.10  


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

