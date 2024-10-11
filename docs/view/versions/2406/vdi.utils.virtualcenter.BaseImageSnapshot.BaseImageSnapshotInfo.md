---
layout: page
title: Data Object - BaseImageSnapshotInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.BaseImageSnapshot.BaseImageSnapshotInfo`

Returned by  
> [BaseImageSnapshot_List](vdi.utils.virtualcenter.BaseImageSnapshot.md#list)

See also  
> [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md), [BaseImageSnapshotIncompatibleReasons](vdi.utils.virtualcenter.BaseImageSnapshot.BaseImageSnapshotIncompatibleReasons.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since  
> Horizon View 6.0


## Data Object Description 

BaseImageSnapshotInfo is a set of VM snapshot attributes retrieved from the VC. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md)|  VM Snapshot Id   


 * This property cannot be updated.

  
**name**|  xsd:string|  VM Snapshot name   


 * This property cannot be updated.

  
**path**|  xsd:string|  VM Snapshot path   


 * This property cannot be updated.

  
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  VirtualCenter id for this snapshot   


 * This property cannot be updated.

  
**description**|  xsd:string|  Description of the snapshot.   


 * This property need not be set.
 * This property cannot be updated.

  
**createTime**|  xsd:dateTime|  Time the snapshot was created.   


 * This property need not be set.
 * This property cannot be updated.

  
**hardwareVersion**|  xsd:int|  VM Snapshot hardware version.   


 * This property need not be set.
 * This property cannot be updated.

  
**vGPUType**|  xsd:string|  NVIDIA GRID vGPU type configured on this snapshot, if any.  **_Since_** Horizon View 6.1  


 * This property need not be set.
 * This property cannot be updated.

  
**maxNumberOfMonitors**|  xsd:int|  Maximum number of monitors set in SVGA settings for the snapshot in vCenter.  **_Since_** Horizon 7.4  


 * This property need not be set.
 * This property cannot be updated.

  
**totalVideoMemoryMB**|  xsd:double|  Total video memory in MB set in SVGA settings for the snapshot in vCenter.  **_Since_** Horizon 7.4  


 * This property need not be set.
 * This property cannot be updated.

  
**maxResolutionOfAnyOneMonitor**|  xsd:string|  Maximum resolution of any one monitor set in SVGA settings for the snapshot in vCenter.  **_Since_** Horizon 7.4  


 * This property need not be set.
 * This property cannot be updated.

  
**enable3DSupport**|  xsd:boolean|  Flag to indicate whether the virtual video card for the snapshot supports 3D functions.  **_Since_** Horizon 7.6  


 * This property need not be set.
 * This property cannot be updated.

  
**renderer3D**|  xsd:string|  Indicate how the virtual video device for the snapshot renders 3D graphics. Will be set only if [enable3DSupport](vdi.utils.virtualcenter.BaseImageSnapshot.BaseImageSnapshotInfo.md#enable3DSupport) is true.  **_Since_** Horizon 7.6  


  * This property has a default value of "DISABLED".
 * This property need not be set.
 * This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"MANAGE_BY_VSPHERE_CLIENT"| 3D rendering managed by vSphere Client.  
"AUTOMATIC"| 3D rendering is automatic.  
"SOFTWARE"| 3D rendering is software dependent. The software renderer is supported (at minimum) on virtual hardware version 8 in a vSphere 5.0 environment.  
"HARDWARE"| 3D rendering is hardware dependent. The hardware-based renderer is supported (at minimum) on virtual hardware version 9 in a vSphere 5.1 environment.  
"DISABLED"| 3D rendering is disabled.  

  
**incompatibleReasons**| [BaseImageSnapshotIncompatibleReasons](vdi.utils.virtualcenter.BaseImageSnapshot.BaseImageSnapshotIncompatibleReasons.md)|  Reasons that may preclude this BaseImageSnapshot from being used in linked clone desktop or farm creation.   


 * This property cannot be updated.

  
**memoryMB**|  xsd:int|  Memory size of the snapshot, in MB.  **_Since_** Horizon 7.4  


 * This property need not be set.
 * This property cannot be updated.

  
**diskSizeInBytes**|  xsd:long|  Sum of capacities of all the virtual disks in the snapshot, in bytes.  **_Since_** Horizon 7.4  


 * This property need not be set.
 * This property cannot be updated.

  
**memoryReservationMB**|  xsd:long|  Amount of memory that is guaranteed available to the virtual machine, in MB.  **_Since_** Horizon 7.4  


 * This property need not be set.
 * This property cannot be updated.

  
**refId**|  xsd:string|  Reference ID used for this base image snapshot.  **_Since_** Horizon 8.1  


 * This property need not be set.
 * This property cannot be updated.

  
**carbonBlackReadyToClone**|  xsd:boolean|  Indicates Carbon Black scan is complete and is ready to clone for Instant Clone desktop or farm creation.  **_Since_** Horizon 8.4  


 * This property need not be set.
 * This property cannot be updated.

  
**carbonBlackScanPercentage**|  xsd:int|  Carbon Black scan completion percentage.  **_Since_** Horizon 8.4  


 * This property need not be set.
 * This property cannot be updated.
  * This property has a minimum value of 0. 
  * This property has a maximum value of 100. 

  
**numCPU**|  xsd:int|  Number of CPU's present on the VM snapshot  **_Since_** Horizon 8.6  


 * This property need not be set.

  
**numCoresPerSocket**|  xsd:int|  Number of cores per socket present on the VM snapshot  **_Since_** Horizon 8.6  


 * This property need not be set.

  
  

  
