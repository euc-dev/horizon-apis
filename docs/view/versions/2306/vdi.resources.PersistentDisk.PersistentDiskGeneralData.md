---
layout: page
title: Data Object - PersistentDiskGeneralData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.PersistentDisk.PersistentDiskGeneralData`

Property of
> [PersistentDiskInfo](vdi.resources.PersistentDisk.PersistentDiskInfo.md#field_detail)

See also
> [AccessGroupId](vdi.entity.AccessGroupId.md), [DesktopId](vdi.entity.DesktopId.md), [MachineId](vdi.entity.MachineId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0


## Data Object Description

**Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

General data about the persistent disk.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**name**|  xsd:string|  The name of the persistent disk. This is the filename of the virtual disk on Virtual Center. [^2]
**desktop**| [DesktopId](vdi.entity.DesktopId.md)|  The desktop associated with the persistent disk. [^1]
**desktopName**|  xsd:string|  Desktop Name corresponding to [desktop](vdi.resources.PersistentDisk.PersistentDiskGeneralData.md#desktop) **_Since_** Horizon 7.7 [^1]
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  The user owning the persistent disk. This cannot be a group. [^1]
**machine**| [MachineId](vdi.entity.MachineId.md)|  The machine the disk is attached to. MachineIds of this type originate from the [Machine](vdi.resources.Machine.md) service. [^1] [^2]
**machineName**|  xsd:string|  Name of the machine corresponding to [machine](vdi.resources.PersistentDisk.PersistentDiskGeneralData.md#machine) **_Since_** Horizon 7.7 [^1]
**accessGroup**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  The access group of the virtual disk.
**usage**|  xsd:string|  The usage of the persistent disk. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"PRIMARY"</td><td>This data disk is attached to a Virtual Machine and the user profile is redirected to it.</td></tr><tr><td>"SECONDARY"</td><td>This data disk is attached to a Virtual Machine.</td></tr><tr><td>"UNATTACHED"</td><td>This data disk is not attached to a Virtual Machine.</td></tr><tr><td>"DELETING"</td><td>This data disk is in the process of being deleted or archived.</td></tr></table>
**status**|  xsd:string|  The status of the persistent disk. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"IN_USE"</td><td>This persistent disk is in use.</td></tr><tr><td>"UNATTACHED"</td><td>The persistent disk is not in use and available to attach to a virtual machine.</td></tr><tr><td>"ATTACHING"</td><td>The persistent disk is attaching to a virtual machine.</td></tr><tr><td>"DETACHING"</td><td>The persistent disk is being detached from a virtual machine.</td></tr><tr><td>"REPLACING"</td><td>The persistent disk is being replaced.</td></tr><tr><td>"ARCHIVING"</td><td>The persistent disk is being archived.</td></tr><tr><td>"DELETING"</td><td>The persistent disk is being deleted.</td></tr></table>
**lastAttachedTime**|  xsd:dateTime|  If detached, when this persistent disk was either last attached to a machine or created from a Virtual Disk. It will be unset otherwise. [^1] [^2]
 


 
