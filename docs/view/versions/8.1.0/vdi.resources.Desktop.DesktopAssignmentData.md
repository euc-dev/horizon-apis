---
layout: page
title: Data Object - DesktopAssignmentData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.DesktopAssignmentData  
Property of
     [DesktopAssignmentView](vdi.resources.Desktop.DesktopAssignmentView.md#field_detail)  
See also
     [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)  
Since 
    Horizon 7.9

## Data Object Description 

Core attributes of a desktop assignment data. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  Unique name for the desktop   
  
**displayName**|  xsd:string|  Desktop display name.   
  
**enabled**|  xsd:boolean|  Determines if the desktop is enabled   
  
**type**|  xsd:string|  Type of desktop.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"AUTOMATED"| An automated desktop creates virtual machines cloned from a base template or snapshot.  
"MANUAL"| A manual machine desktop allows selection of existing virtual machines and addition to the desktop of available machines to connect to.  
"RDS"| An RDS Desktop Desktop.  

  
**source**|  xsd:string|  Source of machines.   


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

  
**globalEntitlement**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  Global entitlement for this desktop. This member will be null if not set or caller does not have global read permissions.   


* This property need not be set.

  
**numMachines**|  xsd:int|  Number of machines in the desktop. The machines may be queried using the query service for Machine. This field does not apply to RDS desktops. The RDS servers associated with an RDS desktop may be queried using the query service for RDSServer.   
  
**operatingSystem**|  xsd:string|  The guest operating system. Applicable only for automated desktops.   


* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"Unknown"|   
"Windows XP"| Windows XP  
"Windows Vista"| Windows Vista  
"Windows 7"| Windows 7  
"Windows 8"| Windows 8  
"Windows 10"| Windows 10  
"Windows Server 2003"| Windows Server 2003  
"Windows Server 2008"| Windows Server 2008  
"Windows Server 2008R2"| Windows Server 2008R2  
"Windows Server 2012"| Windows Server 2012  
"Windows Server 2012R2"| Windows Server 2012R2  
"Windows Server 10"| null  
"Windows Server 2016"| null  
"Windows Server 2016 or above"| Windows Server 2016 or above  
"Linux (other)"| Linux (other)  
"Linux Server (other)"| Linux server (other)  
"Linux (Ubuntu)"| Linux (Ubuntu)  
"Linux (Red Hat Enterprise Linux)"| Linux (Red Hat Enterprise)  
"Linux (SUSE Linux Enterprise Server)"| Linux (Suse)  
"Linux (CentOS)"| Linux (CentOS)  

  
**operatingSystemArchitecture**|  xsd:string|  The guest operating system architecture. Applicable only for automated desktops.   


* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"Unknown"| Operating System cannot be determined.  
"32_bit"| 32 bit Operating System Architecture.  
"64_bit"| 64 bit Operating System Architecture.  

  
**enableGRIDvGPUs**|  xsd:boolean|  When 3D rendering is managed by the vSphere Client, this enables support for NVIDIA GRID vGPUs. This must be false if 3D rendering is not managed by the vSphere Client. If this is true, the host or cluster associated with the desktop must support NVIDIA GRID and vGPU types required by the desktop's VirtualMachines, VmTemplate, or BaseImageSnapshot. If this is false, the desktop's VirtualMachines, VmTemplate, or BaseImageSnapshot must not support NVIDIA GRID vGPUs. Since suspending VMs with passthrough devices such as vGPUs is not possible, [powerPolicy](vdi.resources.Desktop.LogoffSettings.md#powerPolicy) cannot be set to SUSPEND if this is enabled.   


  * This property has a default value of false.

  
**renderer3D**|  xsd:string|  3D rendering is supported on Windows 7 or later guests running on VMs with virtual hardware version 8 or later. The default protocol must be PCoIP and users must not be allowed to choose their own protocol to enable 3D rendering. For instant clone source desktop 3D rendering always mapped to MANAGE_BY_VSPHERE_CLIENT   


  * This property has a default value of "DISABLED".
  * This property will be one of:  
|  Value |  Description   
---|---  
"MANAGE_BY_VSPHERE_CLIENT"| 3D rendering managed by vSphere Client.  
"AUTOMATIC"| 3D rendering is automatic.  
"SOFTWARE"| 3D rendering is software dependent. The software renderer is supported (at minimum) on virtual hardware version 8 in a vSphere 5.0 environment.  
"HARDWARE"| 3D rendering is hardware dependent. The hardware-based renderer is supported (at minimum) on virtual hardware version 9 in a vSphere 5.1 environment.  
"DISABLED"| 3D rendering is disabled.  

  
**allowUsersToChooseProtocol**|  xsd:boolean|  Whether the users can choose the protocol.   


  * This property has a default value of true.

  
**allowMultipleSessionsPerUser**|  xsd:boolean|  Whether multiple sessions are allowed per user for this pool. This is valid for RDS Desktops. For other Desktops use [allowMultipleSessionsPerUser](vdi.resources.Desktop.LogoffSettings.md#allowMultipleSessionsPerUser)   


  * This property has a default value of false.
* This property need not be set.

  
**allowUsersToResetMachines**|  xsd:boolean|  Whether users are allowed to reset/restart their machines.   


  * This property has a default value of false.

  
**defaultDisplayProtocol**|  xsd:string|  The default display protocol for the desktop. For a managed desktop, this will default to "PCOIP". For an unmanaged desktop, this will default to "RDP".   


  * This property will be one of:  
|  Value |  Description   
---|---  
"RDP"| Microsoft Remote Desktop Protocol.  
"PCOIP"| PC over IP.  
"BLAST"| BLAST.  

  
**enableHTMLAccess**|  xsd:boolean| **Deprecated.**_This property is no longer in use for Horizon Components. It is always set to true._ HTML Access, enabled by VMware Blast technology, allows users to connect to View machines from Web browsers. View Client software does not have to be installed on the client devices. To enable HTML Access, you must install the HTML Machine Access feature pack. Also, Blast must be configured as a supported protocol in #supportedDisplayProtocols.  
  


  * This property has a default value of true.
* This property need not be set.

  
**enableCollaboration**|  xsd:boolean|  Enable session collaboration feature. Session collaboration allows a user to share their remote session with other users. Blast must be configured as a supported protocol in #supportedDisplayProtocols.   


  * This property has a default value of false.
* This property need not be set.

  
**userAssignment**|  xsd:string|  User assignment scheme.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"DEDICATED"| With dedicated assignment, a user returns to the same machine at each session.  
"FLOATING"| With floating assignment, a user may return to one of the available virtual machines for the next session.  

  
**multipleSessionAutoClean**|  xsd:boolean|  This value is used to determine if automatic session clean up is enabled. This cannot be enabled when this Global Entitlement is associated with a Desktop that has dedicated user assignment.   
  
**cloudManaged**|  xsd:boolean|  Indicates whether this desktop is managed by Horizon Cloud Services.  **_Since_** Horizon 7.11  


  * This property has a default value of false.
* This property need not be set.
* This property cannot be updated.

  
**cloudAssigned**|  xsd:boolean|  Indicates whether this desktop is assigned to a workspace in Horizon Cloud Services.  **_Since_** Horizon 7.11  


  * This property has a default value of false.
* This property need not be set.
* This property cannot be updated.

  
**numAssignedMachines**|  xsd:int|  Number of machines in the desktop which are assigned to users. The value will be zero for floating assignment desktop.  **_Since_** Horizon 7.11  


  * This property has a default value of 0.
* This property cannot be updated.

  
  
  
  
  
  

