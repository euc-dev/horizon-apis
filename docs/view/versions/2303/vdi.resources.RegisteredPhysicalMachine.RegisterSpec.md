---
layout: page
title: Data Object - RegisteredPhysicalMachineRegisterSpec
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.RegisteredPhysicalMachine.RegisterSpec`

Parameter to
> [RegisteredPhysicalMachine_Register](vdi.resources.RegisteredPhysicalMachine.md#register)

Since
> Horizon View 6.0


## Data Object Description

The specification for registering a physical machine.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**dnsName**|  xsd:string|  The DNS name for the physical machine. [^127]
**operatingSystem**|  xsd:string|  The operating system of the machine. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"Windows XP"</td><td>Windows XP</td></tr><tr><td>"Windows Vista"</td><td>Windows Vista</td></tr><tr><td>"Windows 7"</td><td>Windows 7</td></tr><tr><td>"Windows 8"</td><td>Windows 8</td></tr><tr><td>"Windows 10"</td><td>Windows 10</td></tr><tr><td>"Windows 11"</td><td>Windows 11</td></tr><tr><td>"Windows Server 2008R2"</td><td>Windows Server 2008R2</td></tr><tr><td>"Windows Server 2012"</td><td>Windows Server 2012</td></tr><tr><td>"Windows Server 2012R2"</td><td>Windows Server 2012R2</td></tr><tr><td>"Windows Server 10"</td><td>null</td></tr><tr><td>"Windows Server 2016"</td><td>null</td></tr><tr><td>"Linux (other)"</td><td>Linux (other)</td></tr><tr><td>"Linux Server (other)"</td><td>Linux server (other)</td></tr></table>
**source**|  xsd:string|  An optional string that describes how and why this machine was registered. This will appear in the agent logs. [^1] [^7]
 


 


[^1]: This property need not be set.
[^7]: If specified, this property is limited to letters, numbers, punctuation, spaces, and tabs.
[^127]: This must be between 1 and 255 characters.