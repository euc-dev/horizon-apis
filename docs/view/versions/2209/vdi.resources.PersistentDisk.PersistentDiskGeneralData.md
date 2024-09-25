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


[^2]

  
**desktop**| [DesktopId](vdi.entity.DesktopId.md)|  The desktop associated with the persistent disk.   


[^1]

  
**desktopName**|  xsd:string|  Desktop Name corresponding to [desktop](vdi.resources.PersistentDisk.PersistentDiskGeneralData.md#desktop) **_Since_** Horizon 7.7  


[^1]

  
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  The user owning the persistent disk. This cannot be a group.   


[^1]

  
**machine**| [MachineId](vdi.entity.MachineId.md)|  The machine the disk is attached to. MachineIds of this type originate from the [Machine](vdi.resources.Machine.md) service.   


[^1]
[^2]

  
**machineName**|  xsd:string|  Name of the machine corresponding to [machine](vdi.resources.PersistentDisk.PersistentDiskGeneralData.md#machine) **_Since_** Horizon 7.7  


[^1]

  
**accessGroup**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  The access group of the virtual disk.   
  
**usage**|  xsd:string|  The usage of the persistent disk.   


[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"PRIMARY"| This data disk is attached to a Virtual Machine and the user profile is redirected to it.  
"SECONDARY"| This data disk is attached to a Virtual Machine.  
"UNATTACHED"| This data disk is not attached to a Virtual Machine.  
"DELETING"| This data disk is in the process of being deleted or archived.  

  
**status**|  xsd:string|  The status of the persistent disk.   


[^2]
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


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

