---
layout: page
title: Data Object - PersistentDiskGeneralData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.PersistentDisk.PersistentDiskGeneralData  
Property of
     [PersistentDiskInfo](vdi.resources.PersistentDisk.PersistentDiskInfo.md#field_detail)  
See also
     [AccessGroupId](vdi.entity.AccessGroupId.md), [DesktopId](vdi.entity.DesktopId.md), [MachineId](vdi.entity.MachineId.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

**Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

General data about the persistent disk. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  The name of the persistent disk. This is the filename of the virtual disk on Virtual Center.   


* This property cannot be updated.

  
**desktop**| [DesktopId](vdi.entity.DesktopId.md)|  The desktop associated with the persistent disk.   


* This property need not be set.

  
**desktopName**|  xsd:string|  Desktop Name corresponding to [desktop](vdi.resources.PersistentDisk.PersistentDiskGeneralData.md#desktop) **_Since_** Horizon 7.7  


* This property need not be set.

  
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  The user owning the persistent disk. This cannot be a group.   


* This property need not be set.

  
**machine**| [MachineId](vdi.entity.MachineId.md)|  The machine the disk is attached to. MachineIds of this type originate from the [Machine](vdi.resources.Machine.md) service.   


* This property need not be set.
* This property cannot be updated.

  
**machineName**|  xsd:string|  Name of the machine corresponding to [machine](vdi.resources.PersistentDisk.PersistentDiskGeneralData.md#machine) **_Since_** Horizon 7.7  


* This property need not be set.

  
**accessGroup**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  The access group of the virtual disk.   
  
**usage**|  xsd:string|  The usage of the persistent disk.   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"PRIMARY"| This data disk is attached to a Virtual Machine and the user profile is redirected to it.  
"SECONDARY"| This data disk is attached to a Virtual Machine.  
"UNATTACHED"| This data disk is not attached to a Virtual Machine.  
"DELETING"| This data disk is in the process of being deleted or archived.  

  
**status**|  xsd:string|  The status of the persistent disk.   


* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"IN_USE"| This persistent disk is in use.  
"UNATTACHED"| The persistent disk is not in use and available to attach to a virtual machine.  
"ATTACHING"| The persistent disk is attaching to a virtual machine.  
"DETACHING"| The persistent disk is being detached from a virtual machine.  
"REPLACING"| The persistent disk is being replaced.  
"ARCHIVING"| The persistent disk is being archived.  
"DELETING"| The persistent disk is being deleted.  

  
**lastAttachedTime**|  xsd:dateTime|  If detached, when this persistent disk was either last attached to a machine or created from a Virtual Disk. It will be unset otherwise.   


* This property need not be set.
* This property cannot be updated.

  
  
  
   
  
  

