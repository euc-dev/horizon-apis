---
layout: page
title: Data Object - SessionNamesData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.Session.SessionNamesData`

Property of
> [SessionGlobalNamesData](vdi.users.Session.SessionGlobalNamesData.md#field_detail), [SessionLocalSummaryView](vdi.users.Session.SessionLocalSummaryView.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Names of objects that reside in a session.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**userName**|  xsd:string|  User for this session. [^1]
**machineOrRDSServerName**|  xsd:string|  Machine or RDSServer name for this session. [^1]
**machineOrRDSServerDNS**|  xsd:string|  Machine or RDSServer DNS name for this session. [^1]
**agentVersion**|  xsd:string|  The agent version.  **_Since_** Horizon 7.3 [^1] [^2]
**desktopPoolCN**|  xsd:string|  Desktop Pool cn if this is a Desktop session, unset otherwise. <br>**Note:** This will not be set for RDS desktop session when using GlobalSessionQueryService.  **_Since_** Horizon 7.5 [^1] [^2]
**desktopName**|  xsd:string|  Desktop display name if this is a Desktop session, unset otherwise. <br>**Note:** When using GlobalSessionQueryService, for RDS pool this is set as the [farmName](vdi.users.Session.SessionNamesData.md#farmName). [^1]
**desktopType**|  xsd:string|  Desktop type if this is a Desktop session, unset otherwise. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>AUTOMATED</td><td>An automated desktop creates virtual machines cloned from a base template or snapshot.</td></tr><tr><td>MANUAL</td><td>A manual machine desktop allows selection of existing virtual machines and addition to the desktop of available machines to connect to.</td></tr><tr><td>RDS</td><td>An RDS Desktop Desktop.</td></tr></table>
**desktopSource**|  xsd:string|  Desktop machine source if this is a Desktop session, unset otherwise. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>VIRTUAL_CENTER</td><td>Virtual center virtual machines managed as view machines. This option is valid for Automated and Manual Desktop. In case of Automated Desktop, these refer to Full Virtual Machines that are created from a vCenter Server template.</td></tr><tr><td>VIEW_COMPOSER</td><td>View composer linked clones managed as view machines. They share the same base image and use less storage space than full virtual machines. The user profile for linked clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes. This option is only valid for Automated Desktop.</td></tr><tr><td>INSTANT_CLONE_ENGINE</td><td>Instant clone engine created 'instant clones' managed as view machines. Instant clone engine uses vmfork technology to create the instant clones, these clones take very less time for provisioning. Instant clones have many similarities to linked clones like :- [^109] [^110]. This option is only valid for Automated Desktop.</td></tr><tr><td>UNMANAGED</td><td>Non-vCenter Server virtual machines managed as view machines. These can include physical computers, non-vCenter Server virtual machines, and blade PCs. This option is only valid for Manual Desktops.</td></tr><tr><td>RDS</td><td>This option is only valid for RDS Desktops.</td></tr><tr><td>AWS_CORE</td><td>AWS-core workspaces managed as view machines. This option is valid for automated desktop.</td></tr></table>
**farmName**|  xsd:string|  Farm display name for this RDS Desktop or Application session, unset otherwise. [^1]
**clientLocationID**|  xsd:string|  Client Location for this session. [^1]
**clientType**|  xsd:string|  Client type for this session.  **_Since_** Horizon 7.7 [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>Windows</td><td>WINDOWS: client type is Windows client</td></tr><tr><td>Mac</td><td>MAC: client type is Mac client</td></tr><tr><td>htmlaccess</td><td>HTMLACCESS: client type is web client</td></tr><tr><td>Linux</td><td>LINUX: Client type is Linux client</td></tr><tr><td>iOS</td><td>IOS: Client type is iOS client</td></tr><tr><td>Android</td><td>ANDROID: Client type is Android client</td></tr><tr><td>Other</td><td>OTHER: Client type is other</td></tr></table>
**clientAddress**|  xsd:string|  IP address of the client machine for this session.  **_Since_** Horizon 7.2 [^1]
**clientName**|  xsd:string|  Client machine name for this session.  **_Since_** Horizon 7.2 [^1]
**clientVersion**|  xsd:string|  Client version for this session.  **_Since_** Horizon 7.3 [^1]
**securityGatewayDNS**|  xsd:string|  Computer machine name or DNS name of the security gateway. [^1]
**securityGatewayAddress**|  xsd:string|  IP address of the security gateway.  **_Since_** Horizon 7.3 [^1]
**securityGatewayLocation**|  xsd:string|  Location of the security gateway.  **_Since_** Horizon 7.7 [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>External</td><td>EXTERNAL: Gateway location is external</td></tr><tr><td>Internal</td><td>INTERNAL: Gateway location is internal</td></tr><tr><td>Unknown</td><td>UNKNOWN: Gateway location is unknown</td></tr></table>
**applicationNames**|  xsd:string[]|  Names of the Applications launched in this session. This will be only set when [sessionType](vdi.users.Session.SessionData.md#sessionType) is set to APPLICATION.  **_Since_** Horizon 7.11 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^109]: Both instant and linked clones share the same base image and use less storage space than full virtual machines.
[^110]: The user profile for both types clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes.