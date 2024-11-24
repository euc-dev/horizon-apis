---
layout: page
title: Data Object - ImageManagementTagQuerySpec
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.imagemanagement.ImageManagementTag.ImageManagementTagQuerySpec`

Parameter to
> [ImageManagementTag_ListBySpec](vdi.utils.imagemanagement.ImageManagementTag.md#listBySpec)

See also
> [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon 7.10


## Data Object Description

Query spec for filtering image management tag.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**fetchAvailableAssetsOnly**|  xsd:boolean|  When set to true, tags filtered would be having stream and version in AVAILABLE or PARTIALLY_AVAILABLE status and asset in AVAILABLE status. [^5] [^1]
**provisioningType**|  xsd:string|  Provisioning type of the desktop/farm. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>VIRTUAL_CENTER</td><td>Virtual center virtual machines managed as view machines. This option is valid for Automated and Manual Desktop. In case of Automated Desktop, these refer to Full Virtual Machines that are created from a vCenter Server template.</td></tr><tr><td>INSTANT_CLONE_ENGINE</td><td>Instant clone engine created 'instant clones' managed as view machines. Instant clone engine uses vmfork technology to create the instant clones, these clones take very less time for provisioning. Instant clones have many similarities to linked clones like :- [^109] [^110]. This option is only valid for Automated Desktop.</td></tr></table>
**resourceType**|  xsd:string|  Type of resource. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>DESKTOP</td><td>Denotes the Desktop Pool.</td></tr><tr><td>FARM</td><td>Denotes the Farm.</td></tr></table>
**imageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  Entity Id of image management stream.
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  Entity id of virtual center.


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.
[^109]: Both instant and linked clones share the same base image and use less storage space than full virtual machines.
[^110]: The user profile for both types clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes.