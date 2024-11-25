---
layout: page
title: Data Object - DesktopDetailData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.DesktopDetailData`

Property of
> [DesktopDetailView](vdi.resources.Desktop.DesktopDetailView.md#field_detail)

Since
> Horizon 7.4


## Data Object Description

Core attributes of a desktop detail instance.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**name**|  xsd:string|  Unique name for the desktop.
**displayName**|  xsd:string|  Desktop display name.
**type**|  xsd:string|  Type of desktop.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>AUTOMATED</td><td>An automated desktop creates virtual machines cloned from a base template or snapshot.</td></tr><tr><td>MANUAL</td><td>A manual machine desktop allows selection of existing virtual machines and addition to the desktop of available machines to connect to.</td></tr><tr><td>RDS</td><td>An RDS Desktop.</td></tr></table>
**enabled**|  xsd:boolean|  Determines if the desktop is enabled.
**renderer3D**|  xsd:string|  3D rendering is supported on Windows 7 or later guests running on VMs with virtual hardware version 8 or later. The default protocol must be PCoIP and users must not be allowed to choose their own protocol to enable 3D rendering. [^17] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>MANAGE_BY_VSPHERE_CLIENT</td><td>3D rendering managed by vSphere Client.</td></tr><tr><td>AUTOMATIC</td><td>3D rendering is automatic.</td></tr><tr><td>SOFTWARE</td><td>3D rendering is software dependent. The software renderer is supported (at minimum) on virtual hardware version 8 in a vSphere 5.0 environment.</td></tr><tr><td>HARDWARE</td><td>3D rendering is hardware dependent. The hardware-based renderer is supported (at minimum) on virtual hardware version 9 in a vSphere 5.1 environment.</td></tr><tr><td>DISABLED</td><td>3D rendering is disabled.</td></tr></table>
**operatingSystem**|  xsd:string|  The guest operating system. Applicable only for automated desktops. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>Unknown</td><td></td></tr><tr><td>Windows XP</td><td>Windows XP</td></tr><tr><td>Windows Vista</td><td>Windows Vista</td></tr><tr><td>Windows 7</td><td>Windows 7</td></tr><tr><td>Windows 8</td><td>Windows 8</td></tr><tr><td>Windows 10</td><td>Windows 10</td></tr><tr><td>Windows 11</td><td>Windows 11</td></tr><tr><td>Windows Server 2003</td><td>Windows Server 2003</td></tr><tr><td>Windows Server 2008</td><td>Windows Server 2008</td></tr><tr><td>Windows Server 2008R2</td><td>Windows Server 2008R2</td></tr><tr><td>Windows Server 2012</td><td>Windows Server 2012</td></tr><tr><td>Windows Server 2012R2</td><td>Windows Server 2012R2</td></tr><tr><td>Windows Server 10</td><td>null</td></tr><tr><td>Windows Server 2016</td><td>null</td></tr><tr><td>Windows Server 2016 or above</td><td>Windows Server 2016 or above</td></tr><tr><td>Linux (other)</td><td>Linux (other)</td></tr><tr><td>Linux Server (other)</td><td>Linux server (other)</td></tr><tr><td>Linux (Ubuntu)</td><td>Linux (Ubuntu)</td></tr><tr><td>Linux (Red Hat Enterprise Linux)</td><td>Linux (Red Hat Enterprise)</td></tr><tr><td>Linux (SUSE Linux Enterprise Server)</td><td>Linux (Suse)</td></tr><tr><td>Linux (CentOS)</td><td>Linux (CentOS)</td></tr></table>
**operatingSystemArchitecture**|  xsd:string|  The guest operating system architecture. Applicable only for automated desktops. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>Unknown</td><td>Operating System cannot be determined.</td></tr><tr><td>32_bit</td><td>32 bit Operating System Architecture.</td></tr><tr><td>64_bit</td><td>64 bit Operating System Architecture.</td></tr></table>
**avmEndpoints**|  xsd:string[]|  App Volumes manager endpoints. Applicable only for automated desktops. [^1] [^14]
**supportedDomains**|  xsd:string[]|  Supported domains for the desktop. Applicable only for automated desktops. [^1] [^14]
**uemAgentVersion**|  xsd:string|  UEM agent version. Applicable only for automated desktops. [^1]
**vcenterUrl**|  xsd:string|  URL of associated Vcenter for this desktop. [^1]
**creationTime**|  xsd:dateTime|  Desktop creation time. [^1]
**lastModifiedTime**|  xsd:dateTime|  Desktop last modified time. [^1]
**numOfEntitledUsers**|  xsd:int|  Number of entitled users for the desktop. [^1]
**numMachines**|  xsd:int|  Number of machines in the desktop. The machines may be queried using the query service for Machine. This field does not apply to RDS desktops. The RDS servers associated with an RDS desktop may be queried using the query service for RDSServer.


 


[^1]: This property need not be set.
[^14]: This property is an unordered array of unique values.
[^17]: This property has a default value of 'DISABLED'.