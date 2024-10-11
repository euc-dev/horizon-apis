---
layout: page
title: Data Object - DesktopDetailData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Desktop.DesktopDetailData`

Property of  
> [DesktopDetailView](vdi.resources.Desktop.DesktopDetailView.md#field_detail)

Since  
> Horizon 7.4


## Data Object Description 

Core attributes of a desktop detail instance. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  Unique name for the desktop.   
  
**displayName**|  xsd:string|  Desktop display name.   
  
**type**|  xsd:string|  Type of desktop.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"AUTOMATED"| An automated desktop creates virtual machines cloned from a base template or snapshot.  
"MANUAL"| A manual machine desktop allows selection of existing virtual machines and addition to the desktop of available machines to connect to.  
"RDS"| An RDS Desktop Desktop.  

  
**enabled**|  xsd:boolean|  Determines if the desktop is enabled.   
  
**renderer3D**|  xsd:string|  3D rendering is supported on Windows 7 or later guests running on VMs with virtual hardware version 8 or later. The default protocol must be PCoIP and users must not be allowed to choose their own protocol to enable 3D rendering.   


  * This property has a default value of "DISABLED".
  * This property will be one of:  
|  Value |  Description   
---|---  
"MANAGE_BY_VSPHERE_CLIENT"| 3D rendering managed by vSphere Client.  
"AUTOMATIC"| 3D rendering is automatic.  
"SOFTWARE"| 3D rendering is software dependent. The software renderer is supported (at minimum) on virtual hardware version 8 in a vSphere 5.0 environment.  
"HARDWARE"| 3D rendering is hardware dependent. The hardware-based renderer is supported (at minimum) on virtual hardware version 9 in a vSphere 5.1 environment.  
"DISABLED"| 3D rendering is disabled.  

  
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
"Windows 11"| Windows 11  
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

  
**avmEndpoints**|  xsd:string[]|  App Volumes manager endpoints. Applicable only for automated desktops.   


 * This property need not be set.
  * This property is an unordered array of unique values.

  
**supportedDomains**|  xsd:string[]|  Supported domains for the desktop. Applicable only for automated desktops.   


 * This property need not be set.
  * This property is an unordered array of unique values.

  
**uemAgentVersion**|  xsd:string|  UEM agent version. Applicable only for automated desktops.   


 * This property need not be set.

  
**vcenterUrl**|  xsd:string|  URL of associated Vcenter for this desktop.   


 * This property need not be set.

  
**creationTime**|  xsd:dateTime|  Desktop creation time.   


 * This property need not be set.

  
**lastModifiedTime**|  xsd:dateTime|  Desktop last modified time.   


 * This property need not be set.

  
**numOfEntitledUsers**|  xsd:int|  Number of entitled users for the desktop.   


 * This property need not be set.

  
**numMachines**|  xsd:int|  Number of machines in the desktop. The machines may be queried using the query service for Machine. This field does not apply to RDS desktops. The RDS servers associated with an RDS desktop may be queried using the query service for RDSServer.   
  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
