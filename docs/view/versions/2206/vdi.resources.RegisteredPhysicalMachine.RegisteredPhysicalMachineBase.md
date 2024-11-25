---
layout: page
title: Data Object - RegisteredPhysicalMachineBase
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.RegisteredPhysicalMachine.RegisteredPhysicalMachineBase`

Property of
> [RegisteredPhysicalMachineInfo](vdi.resources.RegisteredPhysicalMachine.RegisteredPhysicalMachineInfo.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

The MachineBase attributes.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**name**|  xsd:string|  The name of the Machine. [^1] [^2]
**dnsName**|  xsd:string|  The DNS name of the Machine. [^1] [^2]
**description**|  xsd:string|  Description of the machine.  **_Since_** Horizon 7.7 [^1] [^2]
**operatingSystem**|  xsd:string|  Operating system enumeration as known to View. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>Unknown</td><td></td></tr><tr><td>Windows XP</td><td>Windows XP</td></tr><tr><td>Windows Vista</td><td>Windows Vista</td></tr><tr><td>Windows 7</td><td>Windows 7</td></tr><tr><td>Windows 8</td><td>Windows 8</td></tr><tr><td>Windows 10</td><td>Windows 10</td></tr><tr><td>Windows Server 2003</td><td>Windows Server 2003</td></tr><tr><td>Windows Server 2008</td><td>Windows Server 2008</td></tr><tr><td>Windows Server 2008R2</td><td>Windows Server 2008R2</td></tr><tr><td>Windows Server 2012</td><td>Windows Server 2012</td></tr><tr><td>Windows Server 2012R2</td><td>Windows Server 2012R2</td></tr><tr><td>Windows Server 10</td><td>null</td></tr><tr><td>Windows Server 2016</td><td>null</td></tr><tr><td>Windows Server 2016 or above</td><td>Windows Server 2016 or above</td></tr><tr><td>Linux (other)</td><td>Linux (other)</td></tr><tr><td>Linux Server (other)</td><td>Linux server (other)</td></tr><tr><td>Linux (Ubuntu)</td><td>Linux (Ubuntu)</td></tr><tr><td>Linux (Red Hat Enterprise Linux)</td><td>Linux (Red Hat Enterprise)</td></tr><tr><td>Linux (SUSE Linux Enterprise Server)</td><td>Linux (Suse)</td></tr><tr><td>Linux (CentOS)</td><td>Linux (CentOS)</td></tr></table>




 


[^1]: This property need not be set.
[^2]: This property cannot be updated.