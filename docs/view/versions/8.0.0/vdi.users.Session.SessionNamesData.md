---
layout: page
title: Data Object - SessionNamesData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.Session.SessionNamesData
Property of
     [SessionGlobalNamesData](vdi.users.Session.SessionGlobalNamesData.md#field_detail), [SessionLocalSummaryView](vdi.users.Session.SessionLocalSummaryView.md#field_detail)
Since 
    Horizon View 6.0

## Data Object Description 

Names of objects that reside in a session. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**userName**|  xsd:string|  User for this session.   


[^1]

  
**machineOrRDSServerName**|  xsd:string|  Machine or RDSServer name for this session.   


[^1]

  
**machineOrRDSServerDNS**|  xsd:string|  Machine or RDSServer DNS name for this session.   


[^1]

  
**agentVersion**|  xsd:string|  The agent version.  **_Since_** Horizon 7.3  


[^1]
[^2]

  
**desktopPoolCN**|  xsd:string|  Desktop Pool cn if this is a Desktop session, unset otherwise.  **_Since_** Horizon 7.5  


[^1]
[^2]

  
**desktopName**|  xsd:string|  Desktop display name if this is a Desktop session, unset otherwise.   


[^1]

  
**desktopType**|  xsd:string|  Desktop type if this is a Desktop session, unset otherwise.   


[^1]
  * This property will be one of:  
|  Value |  Description   
---|---  
"AUTOMATED"| An automated desktop creates virtual machines cloned from a base template or snapshot.  
"MANUAL"| A manual machine desktop allows selection of existing virtual machines and addition to the desktop of available machines to connect to.  
"RDS"| An RDS Desktop Desktop.  

  
**desktopSource**|  xsd:string|  Desktop machine source if this is a Desktop session, unset otherwise.   


[^1]
  * This property will be one of:  
|  Value |  Description   
---|---  
"VIRTUAL_CENTER"| Virtual center virtual machines managed as view machines. This option is valid for Automated and Manual Desktop. In case of Automated Desktop, these refer to Full Virtual Machines that are created from a vCenter Server template.  
"VIEW_COMPOSER"| View composer linked clones managed as view machines. They share the same base image and use less storage space than full virtual machines. The user profile for linked clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes. This option is only valid for Automated Desktop.  
"INSTANT_CLONE_ENGINE"| Instant clone engine created 'instant clones' managed as view machines. Instant clone engine uses vmfork technology to create the instant clones, these clones take very less time for provisioning. Instant clones have many similarities to linked clones like :-  

    * Both instant and linked clones share the same base image and use less storage space than full virtual machines.
    * The user profile for both types clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes.
This option is only valid for Automated Desktop.  
"UNMANAGED"| Non-vCenter Server virtual machines managed as view machines. These can include physical computers, non-vCenter Server virtual machines, and blade PCs. This option is only valid for Manual Desktops.  
"RDS"| This option is only valid for RDS Desktops.  

  
**farmName**|  xsd:string|  Farm display name for this RDS Desktop or Application session, unset otherwise.   


[^1]

  
**clientLocationID**|  xsd:string|  Client Location for this session.   


[^1]

  
**clientType**|  xsd:string|  Client type for this session.  **_Since_** Horizon 7.7  


[^1]
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"Windows"| WINDOWS: client type is Windows client  
"Mac"| MAC: client type is Mac client  
"htmlaccess"| HTMLACCESS: client type is web client  
"Linux"| LINUX: Client type is Linux client  
"iOS"| IOS: Client type is iOS client  
"Android"| ANDROID: Client type is Android client  
"Other"| OTHER: Client type is other  

  
**clientAddress**|  xsd:string|  IP address of the client machine for this session.  **_Since_** Horizon 7.2  


[^1]

  
**clientName**|  xsd:string|  Client machine name for this session.  **_Since_** Horizon 7.2  


[^1]

  
**clientVersion**|  xsd:string|  Client version for this session.  **_Since_** Horizon 7.3  


[^1]

  
**securityGatewayDNS**|  xsd:string|  Computer machine name or DNS name of the security gateway.   


[^1]

  
**securityGatewayAddress**|  xsd:string|  IP address of the security gateway.  **_Since_** Horizon 7.3  


[^1]

  
**securityGatewayLocation**|  xsd:string|  Location of the security gateway.  **_Since_** Horizon 7.7  


[^1]
[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"External"| EXTERNAL: Gateway location is external  
"Internal"| INTERNAL: Gateway location is internal  
"Unknown"| UNKNOWN: Gateway location is unknown  

  
**applicationNames**|  xsd:string[]|  Names of the Applications launched in this session. This will be only set when [sessionType](vdi.users.Session.SessionData.md#sessionType) is set to APPLICATION.  **_Since_** Horizon 7.11  


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
