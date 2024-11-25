---
layout: page
title: Data Object - BaseImageSnapshotInfo
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.BaseImageSnapshot.BaseImageSnapshotInfo`

Returned by
> [BaseImageSnapshot_List](vdi.utils.virtualcenter.BaseImageSnapshot.md#list)

See also
> [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md), [BaseImageSnapshotIncompatibleReasons](vdi.utils.virtualcenter.BaseImageSnapshot.BaseImageSnapshotIncompatibleReasons.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon View 6.0


## Data Object Description

BaseImageSnapshotInfo is a set of VM snapshot attributes retrieved from the VC.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md)|  VM Snapshot Id [^2]
**name**|  xsd:string|  VM Snapshot name [^2]
**path**|  xsd:string|  VM Snapshot path [^2]
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  VirtualCenter id for this snapshot [^2]
**description**|  xsd:string|  Description of the snapshot. [^1] [^2]
**createTime**|  xsd:dateTime|  Time the snapshot was created. [^1] [^2]
**hardwareVersion**|  xsd:int|  VM Snapshot hardware version. [^1] [^2]
**vGPUType**|  xsd:string|  NVIDIA GRID vGPU type configured on this snapshot, if any.  **_Since_** Horizon View 6.1 [^1] [^2]
**maxNumberOfMonitors**|  xsd:int|  Maximum number of monitors set in SVGA settings for the snapshot in vCenter.  **_Since_** Horizon 7.4 [^1] [^2]
**totalVideoMemoryMB**|  xsd:double|  Total video memory in MB set in SVGA settings for the snapshot in vCenter.  **_Since_** Horizon 7.4 [^1] [^2]
**maxResolutionOfAnyOneMonitor**|  xsd:string|  Maximum resolution of any one monitor set in SVGA settings for the snapshot in vCenter.  **_Since_** Horizon 7.4 [^1] [^2]
**enable3DSupport**|  xsd:boolean|  Flag to indicate whether the virtual video card for the snapshot supports 3D functions.  **_Since_** Horizon 7.6 [^1] [^2]
**renderer3D**|  xsd:string|  Indicate how the virtual video device for the snapshot renders 3D graphics. Will be set only if [enable3DSupport](vdi.utils.virtualcenter.BaseImageSnapshot.BaseImageSnapshotInfo.md#enable3DSupport) is true.  **_Since_** Horizon 7.6 [^17] [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"MANAGE_BY_VSPHERE_CLIENT"</td><td>3D rendering managed by vSphere Client.</td></tr><tr><td>"AUTOMATIC"</td><td>3D rendering is automatic.</td></tr><tr><td>"SOFTWARE"</td><td>3D rendering is software dependent. The software renderer is supported (at minimum) on virtual hardware version 8 in a vSphere 5.0 environment.</td></tr><tr><td>"HARDWARE"</td><td>3D rendering is hardware dependent. The hardware-based renderer is supported (at minimum) on virtual hardware version 9 in a vSphere 5.1 environment.</td></tr><tr><td>"DISABLED"</td><td>3D rendering is disabled.</td></tr></table>
**incompatibleReasons**| [BaseImageSnapshotIncompatibleReasons](vdi.utils.virtualcenter.BaseImageSnapshot.BaseImageSnapshotIncompatibleReasons.md)|  Reasons that may preclude this BaseImageSnapshot from being used in linked clone desktop or farm creation. [^2]
**memoryMB**|  xsd:int|  Memory size of the snapshot, in MB.  **_Since_** Horizon 7.4 [^1] [^2]
**diskSizeInBytes**|  xsd:long|  Sum of capacities of all the virtual disks in the snapshot, in bytes.  **_Since_** Horizon 7.4 [^1] [^2]
**memoryReservationMB**|  xsd:long|  Amount of memory that is guaranteed available to the virtual machine, in MB.  **_Since_** Horizon 7.4 [^1] [^2]
**refId**|  xsd:string|  Reference ID used for this base image snapshot.  **_Since_** Horizon 8.1 [^1] [^2]
**carbonBlackReadyToClone**|  xsd:boolean|  Indicates Carbon Black scan is complete and is ready to clone for Instant Clone desktop or farm creation.  **_Since_** Horizon 8.4 [^1] [^2]
**carbonBlackScanPercentage**|  xsd:int|  Carbon Black scan completion percentage.  **_Since_** Horizon 8.4 [^1] [^2] [^72] [^115]
**numCPU**|  xsd:int|  Number of CPU's present on the VM snapshot  **_Since_** Horizon 8.6 [^1]
**numCoresPerSocket**|  xsd:int|  Number of cores per socket present on the VM snapshot  **_Since_** Horizon 8.6 [^1]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^17]: This property has a default value of 'DISABLED'.
[^72]: This property has a minimum value of 0.
[^115]: This property has a maximum value of 100.