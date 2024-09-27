---
layout: page
title: Data Object - DesktopManualDesktopSpec
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.ManualDesktopSpec  
Property of
     [DesktopSpec](vdi.resources.Desktop.DesktopSpec.md#field_detail)  
See also
     [DesktopUserAssignment](vdi.resources.Desktop.UserAssignment.md), [DesktopViewStorageAcceleratorSettings](vdi.resources.Desktop.ViewStorageAcceleratorSettings.md), [DesktopVirtualCenterManagedCommonSettings](vdi.resources.Desktop.VirtualCenterManagedCommonSettings.md), [MachineId](vdi.entity.MachineId.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

Specification of a manual desktop. A manual desktop is a desktop of machine sources that is not provisioned automatically. Multiple users are mapped to multiple machines. However, only one user is active on a machine at a time. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**userAssignment**| [DesktopUserAssignment](vdi.resources.Desktop.UserAssignment.md)|  User assignment scheme.   
  
**source**|  xsd:string|  The Source of machines.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"VIRTUAL_CENTER"| Virtual center virtual machines managed as view machines. This option is valid for Automated and Manual Desktop. In case of Automated Desktop, these refer to Full Virtual Machines that are created from a vCenter Server template.  
"UNMANAGED"| Non-vCenter Server virtual machines managed as view machines. These can include physical computers, non-vCenter Server virtual machines, and blade PCs. This option is only valid for Manual Desktops.  

  
**machines**| [MachineId[]](vdi.entity.MachineId.md)|  List of machines to add to this desktop during creation. MachineIds of this type must originate from the [VirtualMachine](vdi.utils.virtualcenter.VirtualMachine.md) or [RegisteredPhysicalMachine](vdi.resources.RegisteredPhysicalMachine.md) services, but not the [Machine](vdi.resources.Machine.md) service.   
  
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  Virtual Center server.   


 * This property need not be set.
  * This property is required if source is set to "VIRTUAL_CENTER".

  
**viewStorageAcceleratorSettings**| [DesktopViewStorageAcceleratorSettings](vdi.resources.Desktop.ViewStorageAcceleratorSettings.md)|  View Storage Accelerator settings. Sets default values if unset.   


 * This property need not be set.

  
**virtualCenterManagedCommonSettings**| [DesktopVirtualCenterManagedCommonSettings](vdi.resources.Desktop.VirtualCenterManagedCommonSettings.md)|  Common settings for Desktops managed by Virtual Center sources.  **_Since_** Horizon View 6.1  


 * This property need not be set.
  * This property is required if source is set to "VIRTUAL_CENTER".

  
  

  

