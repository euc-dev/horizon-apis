---
layout: page
title: Data Object - MachineDesktopData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Machine.MachineDesktopData`

Property of
> [MachineDetailsView](vdi.resources.Machine.MachineDetailsView.md#field_detail)

See also
> [DesktopId](vdi.entity.DesktopId.md)

Since
> Horizon 7.7


## Data Object Description

Data about the desktop that the Machine belongs to.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [DesktopId](vdi.entity.DesktopId.md)|  The id of the desktop that the machine belongs to. [^2]
**name**|  xsd:string|  The name of the desktop that the machine belongs to. [^1] [^2]
**type**|  xsd:string|  Type of desktop. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>AUTOMATED</td><td>An automated desktop creates virtual machines cloned from a base template or snapshot.</td></tr><tr><td>MANUAL</td><td>A manual machine desktop allows selection of existing virtual machines and addition to the desktop of available machines to connect to.</td></tr><tr><td>RDS</td><td>An RDS Desktop.</td></tr></table>
**source**|  xsd:string|  Source of machines. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>VIRTUAL_CENTER</td><td>Virtual center virtual machines managed as view machines. This option is valid for Automated and Manual Desktop. In case of Automated Desktop, these refer to Full Virtual Machines that are created from a vCenter Server template.</td></tr><tr><td>VIEW_COMPOSER</td><td>View composer linked clones managed as view machines. They share the same base image and use less storage space than full virtual machines. The user profile for linked clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes. This option is only valid for Automated Desktop.</td></tr><tr><td>INSTANT_CLONE_ENGINE</td><td>Instant clone engine created 'instant clones' managed as view machines. Instant clone engine uses vmfork technology to create the instant clones, these clones take very less time for provisioning. Instant clones have many similarities to linked clones. This option is only valid for Automated Desktop.</td></tr><tr><td>UNMANAGED</td><td>Non-vCenter Server virtual machines managed as view machines. These can include physical computers, non-vCenter Server virtual machines, and blade PCs. This option is only valid for Manual Desktops.</td></tr><tr><td>RDS</td><td>This option is only valid for RDS Desktops.</td></tr></table>
**userAssignment**|  xsd:string|  User assignment scheme. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>DEDICATED</td><td>With dedicated assignment, a user returns to the same machine at each session.</td></tr><tr><td>FLOATING</td><td>With floating assignment, a user may return to one of the available virtual machines for the next session.</td></tr></table>
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.