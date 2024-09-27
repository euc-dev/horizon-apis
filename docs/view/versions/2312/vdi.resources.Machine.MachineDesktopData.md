---
layout: page
title: Data Object - MachineDesktopData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Machine.MachineDesktopData  
Property of
     [MachineDetailsView](vdi.resources.Machine.MachineDetailsView.md#field_detail)  
See also
     [DesktopId](vdi.entity.DesktopId.md)  
Since 
    Horizon 7.7

## Data Object Description 

Data about the desktop that the Machine belongs to. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [DesktopId](vdi.entity.DesktopId.md)|  The id of the desktop that the machine belongs to.   


 * This property cannot be updated.

  
**name**|  xsd:string|  The name of the desktop that the machine belongs to.   


 * This property need not be set.
 * This property cannot be updated.

  
**type**|  xsd:string|  Type of desktop.   


 * This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"AUTOMATED"| An automated desktop creates virtual machines cloned from a base template or snapshot.  
"MANUAL"| A manual machine desktop allows selection of existing virtual machines and addition to the desktop of available machines to connect to.  
"RDS"| An RDS Desktop Desktop.  

  
**source**|  xsd:string|  Source of machines.   


 * This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"VIRTUAL_CENTER"| Virtual center virtual machines managed as view machines. This option is valid for Automated and Manual Desktop. In case of Automated Desktop, these refer to Full Virtual Machines that are created from a vCenter Server template.  
"VIEW_COMPOSER"| View composer linked clones managed as view machines. They share the same base image and use less storage space than full virtual machines. The user profile for linked clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes. This option is only valid for Automated Desktop.  
"INSTANT_CLONE_ENGINE"| Instant clone engine created 'instant clones' managed as view machines. Instant clone engine uses vmfork technology to create the instant clones, these clones take very less time for provisioning. Instant clones have many similarities to linked clones like :-  

    * Both instant and linked clones share the same base image and use less storage space than full virtual machines.
    * The user profile for both types clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes.
This option is only valid for Automated Desktop.  
"UNMANAGED"| Non-vCenter Server virtual machines managed as view machines. These can include physical computers, non-vCenter Server virtual machines, and blade PCs. This option is only valid for Manual Desktops.  
"RDS"| This option is only valid for RDS Desktops.  

  
**userAssignment**|  xsd:string|  User assignment scheme.   


 * This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"DEDICATED"| With dedicated assignment, a user returns to the same machine at each session.  
"FLOATING"| With floating assignment, a user may return to one of the available virtual machines for the next session.  

  
  
  
   
  
  

