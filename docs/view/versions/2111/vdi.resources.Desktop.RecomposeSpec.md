---
layout: page
title: Data Object - DesktopRecomposeSpec
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.RecomposeSpec
Parameter to
     [Desktop_Recompose](vdi.resources.Desktop.md#recompose)
See also
     [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md), [BaseImageVmId](vdi.entity.BaseImageVmId.md), [MachineId](vdi.entity.MachineId.md)
Since 
    Horizon View 6.0

## Data Object Description 

**Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Specification for the recompose operation. This operation is applicable only to View Composer sourced desktops. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**parentVm**| [BaseImageVmId](vdi.entity.BaseImageVmId.md)|  New base image VM for View Composer VMs. This must be in the same datacenter as the base image of the desktop.   
  
**snapshot**| [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md)|  Base image snapshot for the View Composer desktop.   
  
**startTime**|  xsd:dateTime|  When to start the operation. If unset the operation will begin immediately.   


[^1]

  
**logoffSetting**|  xsd:string|  Determines when to perform the operation on machines which have an active session.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"FORCE_LOGOFF"| Users will be forced to log off when the system is ready to operate on their virtual machines. Before being forcibly logged off, users may have a grace period in which to save their work (Global Settings).  
"WAIT_FOR_LOGOFF"| Wait for connected users to disconnect before the task starts. The operation starts immediately on machines without active sessions.  

  
**stopOnFirstError**|  xsd:boolean|  Indicates that the operation should stop on first error.   


  * This property has a default value of true.

  
**machines**| [MachineId[]](vdi.entity.MachineId.md)|  The machines to recompose. These must be associated with the desktop. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service, but not the [VirtualMachine](vdi.utils.virtualcenter.VirtualMachine.md) or [RegisteredPhysicalMachine](vdi.resources.RegisteredPhysicalMachine.md) services.   
  
**changeImageForNewVMs**|  xsd:boolean|  Change the default image for new machines. If this flag set to TRUE, existing machines in the pool get re-composed to the selected snapshot and new machines creates from the latest snapshot. If this flag is set to FALSE, existing machines in the pool gets re-composed to the selected snapshot and new machines creates from the older snapshot which is selected while creating pool  **_Since_** Horizon 7.7  


  * This property has a default value of true.
[^1]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
