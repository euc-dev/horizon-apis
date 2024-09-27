---
layout: page
title: Data Object - RegisteredPhysicalMachineRegisterSpec
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.resources.RegisteredPhysicalMachine.RegisterSpec  
Parameter to
     [RegisteredPhysicalMachine_Register](vdi.resources.RegisteredPhysicalMachine.md#register)  
Since 
    Horizon View 6.0

## Data Object Description 

The specification for registering a physical machine. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**dnsName**|  xsd:string|  The DNS name for the physical machine.   


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

  
**source**|  xsd:string|  An optional string that describes how and why this machine was registered. This will appear in the agent logs.   


* This property need not be set.
  * If specified, this property is limited to letters, numbers, punctuation, spaces, and tabs. 

  
  
  
   
  
  

