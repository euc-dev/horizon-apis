---
layout: page
title: Data Object - RegisteredPhysicalMachineBase
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.RegisteredPhysicalMachine.RegisteredPhysicalMachineBase  
Property of
     [RegisteredPhysicalMachineInfo](vdi.resources.RegisteredPhysicalMachine.RegisteredPhysicalMachineInfo.md#field_detail)  
Since 
    Horizon View 6.0

## Data Object Description 

The MachineBase attributes. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  The name of the Machine.   


* This property need not be set.
* This property cannot be updated.

  
**dnsName**|  xsd:string|  The DNS name of the Machine.   


* This property need not be set.
* This property cannot be updated.

  
**description**|  xsd:string|  Description of the machine.  **_Since_** Horizon 7.7  


* This property need not be set.
* This property cannot be updated.

  
**operatingSystem**|  xsd:string|  Operating system enumeration as known to View.   


* This property cannot be updated.
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

  
  
  
 
  
  

