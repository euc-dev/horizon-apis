---
layout: page
title: Data Object - DesktopRecomposeSpec
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.RecomposeSpec`

Parameter to
> [Desktop_Recompose](vdi.resources.Desktop.md#recompose)

See also
> [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md), [BaseImageVmId](vdi.entity.BaseImageVmId.md), [MachineId](vdi.entity.MachineId.md)

Since
> Horizon View 6.0


## Data Object Description

Specification for the recompose operation. This operation is applicable only to View Composer sourced desktops.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**parentVm**| [BaseImageVmId](vdi.entity.BaseImageVmId.md)|  New base image VM for View Composer VMs. This must be in the same datacenter as the base image of the desktop.
**snapshot**| [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md)|  Base image snapshot for the View Composer desktop.
**startTime**|  xsd:dateTime|  When to start the operation. If unset the operation will begin immediately. [^1]
**logoffSetting**|  xsd:string|  Determines when to perform the operation on machines which have an active session.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>FORCE_LOGOFF</td><td>Users will be forced to log off when the system is ready to operate on their virtual machines. Before being forcibly logged off, users may have a grace period in which to save their work (Global Settings).</td></tr><tr><td>WAIT_FOR_LOGOFF</td><td>Wait for connected users to disconnect before the task starts. The operation starts immediately on machines without active sessions.</td></tr></table>
**stopOnFirstError**|  xsd:boolean|  Indicates that the operation should stop on first error. [^6]
**machines**| [MachineId[]](vdi.entity.MachineId.md)|  The machines to recompose. These must be associated with the desktop. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service, but not the [VirtualMachine](vdi.utils.virtualcenter.VirtualMachine.md) or [RegisteredPhysicalMachine](vdi.resources.RegisteredPhysicalMachine.md) services.
**changeImageForNewVMs**|  xsd:boolean|  Change the default image for new machines. If this flag set to TRUE, existing machines in the pool get re-composed to the selected snapshot and new machines creates from the latest snapshot. If this flag is set to FALSE, existing machines in the pool gets re-composed to the selected snapshot and new machines creates from the older snapshot which is selected while creating pool  **_Since_** Horizon 7.7 [^6] [^1]


 


[^1]: This property need not be set.
[^6]: This property has a default value of true.