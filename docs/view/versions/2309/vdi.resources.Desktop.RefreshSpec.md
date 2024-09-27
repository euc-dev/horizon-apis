---
layout: page
title: Data Object - DesktopRefreshSpec
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.RefreshSpec  
Parameter to
     [Desktop_Refresh](vdi.resources.Desktop.md#refresh)  
See also
     [MachineId](vdi.entity.MachineId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

**Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Specification for the refresh operation. This operation is applicable only to View Composer sourced desktops. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**startTime**|  xsd:dateTime|  When to start the operation. If unset the operation will begin immediately.   


 * This property need not be set.

  
**logoffSetting**|  xsd:string|  Determines when to perform the operation on machines which have an active session.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"FORCE_LOGOFF"| Users will be forced to log off when the system is ready to operate on their virtual machines. Before being forcibly logged off, users may have a grace period in which to save their work (Global Settings).  
"WAIT_FOR_LOGOFF"| Wait for connected users to disconnect before the task starts. The operation starts immediately on machines without active sessions.  

  
**stopOnFirstError**|  xsd:boolean|  Indicates that the operation should stop on first error.   


  * This property has a default value of true.

  
**machines**| [MachineId[]](vdi.entity.MachineId.md)|  The machines to refresh. These must be associated with the desktop. MachineIds of this type must originate from the [Machine](vdi.resources.Machine.md) service, but not the [VirtualMachine](vdi.utils.virtualcenter.VirtualMachine.md) or [RegisteredPhysicalMachine](vdi.resources.RegisteredPhysicalMachine.md) services.   
  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

