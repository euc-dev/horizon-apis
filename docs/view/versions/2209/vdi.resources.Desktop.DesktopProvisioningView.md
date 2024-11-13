---
layout: page
title: Data Object - DesktopProvisioningView
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Desktop.DesktopProvisioningView`

See also
> [DesktopBase](vdi.resources.Desktop.DesktopBase.md), [DesktopId](vdi.entity.DesktopId.md), [DesktopVirtualCenterData](vdi.resources.Desktop.VirtualCenterData.md)

Since
> Horizon 7.10


## Data Object Description

Virtual Center entities associated with the automated Desktop.

##  Queryable Data Object

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService").

The DesktopProvisioningView query service api to get provisioning data.

* [provisioningType](vdi.resources.Desktop.DesktopProvisioningView.md#provisioningType)
* [base](vdi.resources.Desktop.DesktopProvisioningView.md#base).[name](vdi.resources.Desktop.DesktopBase.md#name)
* [virtualCenterData](vdi.resources.Desktop.DesktopProvisioningView.md#virtualCenterData).[virtualCenter](vdi.resources.Desktop.VirtualCenterData.md#virtualCenter)
* [virtualCenterData](vdi.resources.Desktop.DesktopProvisioningView.md#virtualCenterData).[imageManagementStream](vdi.resources.Desktop.VirtualCenterData.md#imageManagementStream)
* [virtualCenterData](vdi.resources.Desktop.DesktopProvisioningView.md#virtualCenterData).[imageManagementTag](vdi.resources.Desktop.VirtualCenterData.md#imageManagementTag)
* [virtualCenterData](vdi.resources.Desktop.DesktopProvisioningView.md#virtualCenterData).[pendingImageManagementStream](vdi.resources.Desktop.VirtualCenterData.md#pendingImageManagementStream)
* [virtualCenterData](vdi.resources.Desktop.DesktopProvisioningView.md#virtualCenterData).[pendingImageManagementTag](vdi.resources.Desktop.VirtualCenterData.md#pendingImageManagementTag)



Query Privileges

Privilege |  Description
---|---
POOL_VIEW|  This query will return results only for desktops the caller has desktop read privilege on with the corresponding access group permission.



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [DesktopId](vdi.entity.DesktopId.md)|  Desktop entity ID. [^2]
**provisioningType**|  xsd:string|  The Source or the Provisioning Type of machines. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>VIRTUAL_CENTER</td><td>Virtual center virtual machines managed as view machines. This option is valid for Automated and Manual Desktop. In case of Automated Desktop, these refer to Full Virtual Machines that are created from a vCenter Server template.</td></tr><tr><td>VIEW_COMPOSER</td><td>View composer linked clones managed as view machines. They share the same base image and use less storage space than full virtual machines. The user profile for linked clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes. This option is only valid for Automated Desktop.</td></tr><tr><td>INSTANT_CLONE_ENGINE</td><td>Instant clone engine created 'instant clones' managed as view machines. Instant clone engine uses vmfork technology to create the instant clones; these clones take very little time for provisioning. Instant clones have many similarities to linked clones. This option is only valid for Automated Desktop.</td></tr></table>
**operatingSystem**|  xsd:string|  The guest operating system. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>Unknown</td><td></td></tr><tr><td>Windows XP</td><td>Windows XP</td></tr><tr><td>Windows Vista</td><td>Windows Vista</td></tr><tr><td>Windows 7</td><td>Windows 7</td></tr><tr><td>Windows 8</td><td>Windows 8</td></tr><tr><td>Windows 10</td><td>Windows 10</td></tr><tr><td>Windows 11</td><td>Windows 11</td></tr><tr><td>Windows Server 2003</td><td>Windows Server 2003</td></tr><tr><td>Windows Server 2008</td><td>Windows Server 2008</td></tr><tr><td>Windows Server 2008R2</td><td>Windows Server 2008R2</td></tr><tr><td>Windows Server 2012</td><td>Windows Server 2012</td></tr><tr><td>Windows Server 2012R2</td><td>Windows Server 2012R2</td></tr><tr><td>Windows Server 10</td><td>null</td></tr><tr><td>Windows Server 2016</td><td>null</td></tr><tr><td>Windows Server 2016 or above</td><td>Windows Server 2016 or above</td></tr><tr><td>Linux (other)</td><td>Linux (other)</td></tr><tr><td>Linux Server (other)</td><td>Linux server (other)</td></tr><tr><td>Linux (Ubuntu)</td><td>Linux (Ubuntu)</td></tr><tr><td>Linux (Red Hat Enterprise Linux)</td><td>Linux (Red Hat Enterprise)</td></tr><tr><td>Linux (SUSE Linux Enterprise Server)</td><td>Linux (Suse)</td></tr><tr><td>Linux (CentOS)</td><td>Linux (CentOS)</td></tr></table>
**operatingSystemArchitecture**|  xsd:string|  The guest operating system architecture. [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>Unknown</td><td>Operating System cannot be determined.</td></tr><tr><td>32_bit</td><td>32 bit Operating System Architecture.</td></tr><tr><td>64_bit</td><td>64 bit Operating System Architecture.</td></tr></table>
**base**| [DesktopBase](vdi.resources.Desktop.DesktopBase.md)|  Desktop identification information. [^2]
**virtualCenterData**| [DesktopVirtualCenterData](vdi.resources.Desktop.VirtualCenterData.md)|  Paths for Virtual Center entities associated with this Desktop. [^2]
**refId**|  xsd:string|  Reference ID used for this desktop pool.  **_Since_** Horizon 8.1 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.