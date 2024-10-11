---
layout: page
title: Data Object - RDSServerRegisterSpec
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.resources.RDSServer.RegisterSpec`

Parameter to  
> [RDSServer_Register](vdi.resources.RDSServer.md#register)

See also  
> [FarmId](vdi.entity.FarmId.md)

Since  
> Horizon View 6.0


## Data Object Description 

The specification for registering an RDSServer. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**dnsName**|  xsd:string|  The DNS name for the RDS Server.   


  * This must be between 1 and 255 characters. 

  
**operatingSystem**|  xsd:string|  The operating system of the machine.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"Windows Server 2003"| Windows Server 2003  
"Windows Server 2008"| Windows Server 2008  
"Windows Server 2008R2"| Windows Server 2008R2  
"Windows Server 2012"| Windows Server 2012  
"Windows Server 2012R2"| Windows Server 2012R2  
"Windows Server 10"| null  
"Windows Server 2016"| null  
"Linux Server (other)"| Linux server (other)  

  
**farm**| [FarmId](vdi.entity.FarmId.md)|  If specified, will add the machine to the specified Farm.   


 * This property need not be set.

  
**source**|  xsd:string|  An optional string that describes how and why this machine was registered. This will appear in the agent logs.   


 * This property need not be set.
  * If specified, this property is limited to letters, numbers, punctuation, spaces, and tabs. 

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
