---
layout: page
title: Data Object - DesktopAssignmentData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.DesktopAssignmentData`

Property of
> [DesktopAssignmentView](vdi.resources.Desktop.DesktopAssignmentView.md#field_detail)

See also
> [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)

Since
> Horizon 7.9


## Data Object Description

Core attributes of a desktop assignment data.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**name**|  xsd:string|  Unique name for the desktop
**displayName**|  xsd:string|  Desktop display name.
**enabled**|  xsd:boolean|  Determines if the desktop is enabled
**type**|  xsd:string|  Type of desktop.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>AUTOMATED</td><td>An automated desktop creates virtual machines cloned from a base template or snapshot.</td></tr><tr><td>MANUAL</td><td>A manual machine desktop allows selection of existing virtual machines and addition to the desktop of available machines to connect to.</td></tr><tr><td>RDS</td><td>An RDS Desktop.</td></tr></table>
**source**|  xsd:string|  Source of machines.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>VIRTUAL_CENTER</td><td>Virtual center virtual machines managed as view machines. This option is valid for Automated and Manual Desktop. In case of Automated Desktop, these refer to Full Virtual Machines that are created from a vCenter Server template.</td></tr><tr><td>VIEW_COMPOSER</td><td>View composer linked clones managed as view machines. They share the same base image and use less storage space than full virtual machines. The user profile for linked clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes. This option is only valid for Automated Desktop.</td></tr><tr><td>INSTANT_CLONE_ENGINE</td><td>Instant clone engine created 'instant clones' managed as view machines. Instant clone engine uses vmfork technology to create the instant clones, these clones take very less time for provisioning. Instant clones have many similarities to linked clones. This option is only valid for Automated Desktop.</td></tr><tr><td>UNMANAGED</td><td>Non-vCenter Server virtual machines managed as view machines. These can include physical computers, non-vCenter Server virtual machines, and blade PCs. This option is only valid for Manual Desktops.</td></tr><tr><td>RDS</td><td>This option is only valid for RDS Desktops.</td></tr><tr><td>AWS_CORE</td><td>AWS-core workspaces managed as view machines. This option is valid for automated desktop.</td></tr></table>
**globalEntitlement**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  Global entitlement for this desktop. This member will be null if not set or caller does not have global read permissions. [^1]
**numMachines**|  xsd:int|  Number of machines in the desktop. The machines may be queried using the query service for Machine. This field does not apply to RDS desktops. The RDS servers associated with an RDS desktop may be queried using the query service for RDSServer.
**operatingSystem**|  xsd:string|  The guest operating system. Applicable only for automated desktops. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>Unknown</td><td></td></tr><tr><td>Windows XP</td><td>Windows XP</td></tr><tr><td>Windows Vista</td><td>Windows Vista</td></tr><tr><td>Windows 7</td><td>Windows 7</td></tr><tr><td>Windows 8</td><td>Windows 8</td></tr><tr><td>Windows 10</td><td>Windows 10</td></tr><tr><td>Windows 11</td><td>Windows 11</td></tr><tr><td>Windows Server 2003</td><td>Windows Server 2003</td></tr><tr><td>Windows Server 2008</td><td>Windows Server 2008</td></tr><tr><td>Windows Server 2008R2</td><td>Windows Server 2008R2</td></tr><tr><td>Windows Server 2012</td><td>Windows Server 2012</td></tr><tr><td>Windows Server 2012R2</td><td>Windows Server 2012R2</td></tr><tr><td>Windows Server 10</td><td>null</td></tr><tr><td>Windows Server 2016</td><td>null</td></tr><tr><td>Windows Server 2016 or above</td><td>Windows Server 2016 or above</td></tr><tr><td>Linux (other)</td><td>Linux (other)</td></tr><tr><td>Linux Server (other)</td><td>Linux server (other)</td></tr><tr><td>Linux (Ubuntu)</td><td>Linux (Ubuntu)</td></tr><tr><td>Linux (Red Hat Enterprise Linux)</td><td>Linux (Red Hat Enterprise)</td></tr><tr><td>Linux (SUSE Linux Enterprise Server)</td><td>Linux (Suse)</td></tr><tr><td>Linux (CentOS)</td><td>Linux (CentOS)</td></tr></table>
**operatingSystemArchitecture**|  xsd:string|  The guest operating system architecture. Applicable only for automated desktops. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>Unknown</td><td>Operating System cannot be determined.</td></tr><tr><td>32_bit</td><td>32 bit Operating System Architecture.</td></tr><tr><td>64_bit</td><td>64 bit Operating System Architecture.</td></tr></table>
**enableGRIDvGPUs**|  xsd:boolean|  When 3D rendering is managed by the vSphere Client, this enables support for NVIDIA GRID vGPUs. This must be false if 3D rendering is not managed by the vSphere Client. If this is true, the host or cluster associated with the desktop must support NVIDIA GRID and vGPU types required by the desktop's VirtualMachines, VmTemplate, or BaseImageSnapshot. If this is false, the desktop's VirtualMachines, VmTemplate, or BaseImageSnapshot must not support NVIDIA GRID vGPUs. Since suspending VMs with passthrough devices such as vGPUs is not possible, [powerPolicy](vdi.resources.Desktop.LogoffSettings.md#powerPolicy) cannot be set to SUSPEND if this is enabled. [^5]
**renderer3D**|  xsd:string|  3D rendering is supported on Windows 7 or later guests running on VMs with virtual hardware version 8 or later. The default protocol must be PCoIP and users must not be allowed to choose their own protocol to enable 3D rendering. For instant clone source desktop 3D rendering always mapped to MANAGE_BY_VSPHERE_CLIENT [^17] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>MANAGE_BY_VSPHERE_CLIENT</td><td>3D rendering managed by vSphere Client.</td></tr><tr><td>AUTOMATIC</td><td>3D rendering is automatic.</td></tr><tr><td>SOFTWARE</td><td>3D rendering is software dependent. The software renderer is supported (at minimum) on virtual hardware version 8 in a vSphere 5.0 environment.</td></tr><tr><td>HARDWARE</td><td>3D rendering is hardware dependent. The hardware-based renderer is supported (at minimum) on virtual hardware version 9 in a vSphere 5.1 environment.</td></tr><tr><td>DISABLED</td><td>3D rendering is disabled.</td></tr></table>
**allowUsersToChooseProtocol**|  xsd:boolean|  Whether the users can choose the protocol. [^6]
**allowMultipleSessionsPerUser**|  xsd:boolean|  Whether multiple sessions are allowed per user for this pool. This is valid for RDS Desktops. For other Desktops use [allowMultipleSessionsPerUser](vdi.resources.Desktop.LogoffSettings.md#allowMultipleSessionsPerUser) [^5] [^1]
**allowUsersToResetMachines**|  xsd:boolean|  Whether users are allowed to reset/restart their machines. [^5]
**defaultDisplayProtocol**|  xsd:string|  The default display protocol for the desktop. For a managed desktop, this will default to "PCOIP". For an unmanaged desktop, this will default to "RDP".<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>RDP</td><td>Microsoft Remote Desktop Protocol.</td></tr><tr><td>PCOIP</td><td>PC over IP.</td></tr><tr><td>BLAST</td><td>BLAST.</td></tr><tr><td>ULTRA</td><td>Pcoip ULTRA, supported only when it is enabled for the desktop pool/global entitlement.</td></tr></table>
**enableHTMLAccess**|  xsd:boolean| **Deprecated.**_This property is no longer in use for Horizon Components. It is always set to true._ HTML Access, enabled by VMware Blast technology, allows users to connect to View machines from Web browsers. View Client software does not have to be installed on the client devices. To enable HTML Access, you must install the HTML Machine Access feature pack. Also, Blast must be configured as a supported protocol in #supportedDisplayProtocols. [^6] [^1]
**enableCollaboration**|  xsd:boolean|  Enable session collaboration feature. Session collaboration allows a user to share their remote session with other users. Blast must be configured as a supported protocol in #supportedDisplayProtocols. [^5] [^1]
**userAssignment**|  xsd:string|  User assignment scheme.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>DEDICATED</td><td>With dedicated assignment, a user returns to the same machine at each session.</td></tr><tr><td>FLOATING</td><td>With floating assignment, a user may return to one of the available virtual machines for the next session.</td></tr></table>
**multipleSessionAutoClean**|  xsd:boolean|  This value is used to determine if automatic session clean up is enabled. This cannot be enabled when this Global Entitlement is associated with a Desktop that has dedicated user assignment.
**cloudManaged**|  xsd:boolean|  Indicates whether this desktop is managed by Horizon Cloud Services.  **_Since_** Horizon 7.11 [^5] [^1] [^2]
**cloudAssigned**|  xsd:boolean|  Indicates whether this desktop is assigned to a workspace in Horizon Cloud Services.  **_Since_** Horizon 7.11 [^5] [^1] [^2]
**numAssignedMachines**|  xsd:int|  Number of machines in the desktop which are assigned to users. The value will be zero for floating assignment desktop.  **_Since_** Horizon 7.11 [^19] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^5]: This property has a default value of false.
[^6]: This property has a default value of true.
[^17]: This property has a default value of 'DISABLED'.
[^19]: This property has a default value of 0.