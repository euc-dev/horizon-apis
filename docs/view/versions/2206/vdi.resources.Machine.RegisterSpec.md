---
layout: page
title: Data Object - MachineRegisterSpec
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.Machine.RegisterSpec`

Parameter to  
> [Machine_Register](vdi.resources.Machine.md#register)

See also  
> [DesktopId](vdi.entity.DesktopId.md)

Since  
> Horizon View 6.0


## Data Object Description 

The specification for registering a machine. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**dnsName**|  xsd:string|  The DNS name for the machine.   


  * This must be between 1 and 255 characters. 

  
**operatingSystem**|  xsd:string|  The operating system of the machine.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"Windows XP"| Windows XP  
"Windows Vista"| Windows Vista  
"Windows 7"| Windows 7  
"Windows 8"| Windows 8  
"Windows 10"| Windows 10  
"Windows Server 2008R2"| Windows Server 2008R2  
"Windows Server 2012"| Windows Server 2012  
"Windows Server 2012R2"| Windows Server 2012R2  
"Windows Server 10"| null  
"Windows Server 2016"| null  
"Linux (other)"| Linux (other)  
"Linux Server (other)"| Linux server (other)  
"Linux (Ubuntu)"| Linux (Ubuntu)  
"Linux (Red Hat Enterprise Linux)"| Linux (Red Hat Enterprise)  
"Linux (SUSE Linux Enterprise Server)"| Linux (Suse)  
"Linux (CentOS)"| Linux (CentOS)  

  
**desktop**| [DesktopId](vdi.entity.DesktopId.md)|  The ID of the desktop to add the machine to. This must be a manual, unmanaged desktop.   
  
**source**|  xsd:string|  An optional string that describes how and why this machine was registered. This will appear in the agent logs.   


* This property need not be set.
  * If specified, this property is limited to letters, numbers, punctuation, spaces, and tabs. 

  
  
  
 
  
  
