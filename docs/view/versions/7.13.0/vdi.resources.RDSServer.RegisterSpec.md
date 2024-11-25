---
layout: page
title: Data Object - RDSServerRegisterSpec
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.RDSServer.RegisterSpec`

Parameter to
> [RDSServer_Register](vdi.resources.RDSServer.md#register)

See also
> [FarmId](vdi.entity.FarmId.md)

Since
> Horizon View 6.0


## Data Object Description

The specification for registering an RDSServer.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**dnsName**|  xsd:string|  The DNS name for the RDS Server. [^126]
**operatingSystem**|  xsd:string|  The operating system of the machine. <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>Windows Server 2003</td><td>Windows Server 2003</td></tr><tr><td>Windows Server 2008</td><td>Windows Server 2008</td></tr><tr><td>Windows Server 2008R2</td><td>Windows Server 2008R2</td></tr><tr><td>Windows Server 2012</td><td>Windows Server 2012</td></tr><tr><td>Windows Server 2012R2</td><td>Windows Server 2012R2</td></tr><tr><td>Windows Server 10</td><td>null</td></tr><tr><td>Windows Server 2016</td><td>null</td></tr><tr><td>Linux Server (other)</td><td>Linux server (other)</td></tr></table>
**farm**| [FarmId](vdi.entity.FarmId.md)|  If specified, will add the machine to the specified Farm. [^1]
**source**|  xsd:string|  An optional string that describes how and why this machine was registered. This will appear in the agent logs. [^1] [^7]


 


[^1]: This property need not be set.
[^7]: If specified, this property is limited to letters, numbers, punctuation, spaces, and tabs.
[^126]: For Instant clone farms, this can be modified only if there are no current operations ( [operation](vdi.resources.Farm.InstantCloneProvisioningStatusData.md#operation) is NONE).