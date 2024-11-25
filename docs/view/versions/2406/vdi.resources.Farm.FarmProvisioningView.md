---
layout: page
title: Data Object - FarmProvisioningView
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.resources.Farm.FarmProvisioningView`

See also
> [FarmBase](vdi.resources.Farm.FarmBase.md), [FarmId](vdi.entity.FarmId.md), [FarmVirtualCenterData](vdi.resources.Farm.VirtualCenterData.md)

Since
> Horizon 7.10


## Data Object Description

Virtual Center entities associated with this Automated Farm.

##  Queryable Data Object

This data object is queryable using [QueryService](vdi.query.QueryService.md "QueryService").

The FarmProvisioningView query service api to get provisioning data. The fields which can be used in filters are:

* [provisioningType](vdi.resources.Farm.FarmProvisioningView.md#provisioningType)
* [base](vdi.resources.Farm.FarmProvisioningView.md#base).[name](vdi.resources.Farm.FarmBase.md#name)
* [virtualCenterData](vdi.resources.Farm.FarmProvisioningView.md#virtualCenterData).[virtualCenter](vdi.resources.Farm.VirtualCenterData.md#virtualCenter)
* [virtualCenterData](vdi.resources.Farm.FarmProvisioningView.md#virtualCenterData).[imageManagementStream](vdi.resources.Farm.VirtualCenterData.md#imageManagementStream)
* [virtualCenterData](vdi.resources.Farm.FarmProvisioningView.md#virtualCenterData).[imageManagementTag](vdi.resources.Farm.VirtualCenterData.md#imageManagementTag)
* [virtualCenterData](vdi.resources.Farm.FarmProvisioningView.md#virtualCenterData).[pendingImageManagementStream](vdi.resources.Farm.VirtualCenterData.md#pendingImageManagementStream)
* [virtualCenterData](vdi.resources.Farm.FarmProvisioningView.md#virtualCenterData).[pendingImageManagementTag](vdi.resources.Farm.VirtualCenterData.md#pendingImageManagementTag)



Query **Privileges**

Privilege | Description
:---|:---
POOL_VIEW|  privilege is required to query Farm provisioning view.



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [FarmId](vdi.entity.FarmId.md)|  Farm entity ID [^2]
**provisioningType**|  xsd:string|  The Source or the Provisioning Type of RDS Servers. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>VIEW_COMPOSER</td><td>View composer linked clones managed as view RDS Servers. They share the same base image and use less storage space than full RDS Servers.</td></tr><tr><td>INSTANT_CLONE_ENGINE</td><td>Instant clone engine created 'instant clones' managed as view RDS Servers. Instant clone engine uses vmfork technology to create the instant clones, these clones take much less time for provisioning. Instant clones have many similarities to linked clones like :- [^109] [^110] This option is only valid for Automated Farm.</td></tr></table>
**operatingSystem**|  xsd:string|  The guest operating system. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"Unknown"</td><td></td></tr><tr><td>"Windows Server 2003"</td><td>Windows Server 2003</td></tr><tr><td>"Windows Server 2008"</td><td>Windows Server 2008</td></tr><tr><td>"Windows Server 2008R2"</td><td>Windows Server 2008R2</td></tr><tr><td>"Windows Server 2012"</td><td>Windows Server 2012</td></tr><tr><td>"Windows Server 2012R2"</td><td>Windows Server 2012R2</td></tr><tr><td>"Windows Server 2016"</td><td>null</td></tr><tr><td>"Linux Server (other)"</td><td>Linux server (other)</td></tr></table>
**operatingSystemArchitecture**|  xsd:string|  The guest operating system architecture. [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>Unknown</td><td>Operating System cannot be determined.</td></tr><tr><td>32_bit</td><td>32 bit Operating System Architecture.</td></tr><tr><td>64_bit</td><td>64 bit Operating System Architecture.</td></tr></table>
**base**| [FarmBase](vdi.resources.Farm.FarmBase.md)|  Farm identification information. [^2]
**virtualCenterData**| [FarmVirtualCenterData](vdi.resources.Farm.VirtualCenterData.md)|  Paths for Virtual Center entities associated with this Farm. [^2]
**refId**|  xsd:string|  Reference ID used for this farm.  **_Since_** Horizon 8.2 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^109]: Both instant and linked clones share the same base image and use less storage space than full virtual machines.
[^110]: The user profile for both types clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes.