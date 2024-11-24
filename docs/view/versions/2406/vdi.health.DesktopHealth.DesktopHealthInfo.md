---
layout: page
title: Data Object - DesktopHealthInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.DesktopHealth.DesktopHealthInfo`

Returned by
> [DesktopHealth_Get](vdi.health.DesktopHealth.md#get)

See also
> [AccessGroupId](vdi.entity.AccessGroupId.md), [ApplicationStatusInfo](vdi.health.DesktopHealth.ApplicationStatusInfo.md), [DesktopId](vdi.entity.DesktopId.md)

Since
> Horizon View 6.0


## Data Object Description

Desktop health Information. This data will be populated only for the desktops which support application remoting.

##  Queryable Data Object

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService").

Query **Privileges**

Privilege | Description
:---|:---
POOL_VIEW|  privilege is required to query information



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [DesktopId](vdi.entity.DesktopId.md)|  Desktop entity ID [^2]
**name**|  xsd:string|  Desktop name [^2]
**type**|  xsd:string|  Desktop type [^2]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"AUTOMATED"</td><td>An automated desktop creates virtual machines cloned from a base template or snapshot.</td></tr><tr><td>"MANUAL"</td><td>A manual machine desktop allows selection of existing virtual machines and addition to the desktop of available machines to connect to.</td></tr><tr><td>"RDS"</td><td>An RDS Desktop Desktop.</td></tr></table>
**health**|  xsd:string|  Desktop health [^2]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"OK"</td><td>Desktop is enabled and no machines are in WARNING or ERROR state. One or more machine(s) may be DISABLED (including the case where all of them are DISABLED).</td></tr><tr><td>"WARNING"</td><td>Desktop is enabled. One or more machine(s) is either in WARNING or ERROR (not exceeding the predefined threshold) state.</td></tr><tr><td>"ERROR"</td><td>Desktop is enabled. One or more machine(s) (exceeding the predefined threshold) is in ERROR state, or, for Automated Desktops, there could be a provisioning error.</td></tr><tr><td>"DISABLED"</td><td>Desktop is disabled.</td></tr></table>
**source**|  xsd:string|  Source of machines. [^1] [^2] [^29]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"VIRTUAL_CENTER"</td><td>Virtual center virtual machines managed as view machines. This option is valid for Automated and Manual Desktop. In case of Automated Desktop, these refer to Full Virtual Machines that are created from a vCenter Server template.</td></tr><tr><td>"VIEW_COMPOSER"</td><td>View composer linked clones managed as view machines. They share the same base image and use less storage space than full virtual machines. The user profile for linked clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes. This option is only valid for Automated Desktop.</td></tr><tr><td>"INSTANT_CLONE_ENGINE"</td><td>Instant clone engine created 'instant clones' managed as view machines. Instant clone engine uses vmfork technology to create the instant clones, these clones take very less time for provisioning. Instant clones have many similarities to linked clones like :- [^109] [^110] This option is only valid for Automated Desktop.</td></tr><tr><td>"UNMANAGED"</td><td>Non-vCenter Server virtual machines managed as view machines. These can include physical computers, non-vCenter Server virtual machines, and blade PCs. This option is only valid for Manual Desktops.</td></tr><tr><td>"RDS"</td><td>This option is only valid for RDS Desktops.</td></tr><tr><td>"AWS_CORE"</td><td>AWS-core workspaces managed as view machines. This option is valid for automated desktop.</td></tr></table>
**accessGroup**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  Access group associated with this Desktop. [^2]
**enableAppRemoting**|  xsd:boolean|  True, if this desktop can be used for application pool creation. [^5] [^1]
**applicationStatus**| [ApplicationStatusInfo[]](vdi.health.DesktopHealth.ApplicationStatusInfo.md)|  Application status [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^5]: This property has a default value of false.
[^29]: This property is required if type is set to 'AUTOMATED'.
[^109]: Both instant and linked clones share the same base image and use less storage space than full virtual machines.
[^110]: The user profile for both types clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes.