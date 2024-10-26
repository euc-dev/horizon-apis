---
layout: page
title: Data Object - ImageManagementStreamQuerySpec
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.utils.imagemanagement.ImageManagementStream.ImageManagementStreamQuerySpec`

Parameter to
> [ImageManagementStream_ListBySpec](vdi.utils.imagemanagement.ImageManagementStream.md#listBySpec)

See also
> [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon 7.10


## Data Object Description

Query spec for filtering image management stream.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**status**|  xsd:string|  Image management stream status. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>AVAILABLE</td><td>Image management stream is available for pools/farms to be created.</td></tr><tr><td>DELETED</td><td>Image management stream is deleted.</td></tr><tr><td>DISABLED</td><td>Image management stream is disabled and no further pools/farms can be created using the same.</td></tr><tr><td>FAILED</td><td>Image management stream creation has failed.</td></tr><tr><td>IN_PROGRESS</td><td>Image management stream creation is in progress.</td></tr><tr><td>PARTIALLY_AVAILABLE</td><td>Image management version could not be created in one or more environments.</td></tr><tr><td>PENDING</td><td>Image management stream is in pending state to be created by a task.</td></tr></table>
**provisioningType**|  xsd:string|  Provisioning type of the desktop/farm. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>VIRTUAL_CENTER</td><td>Virtual center virtual machines managed as view machines. This option is valid for Automated and Manual Desktop. In case of Automated Desktop, these refer to Full Virtual Machines that are created from a vCenter Server template.</td></tr><tr><td>INSTANT_CLONE_ENGINE</td><td>Instant clone engine created 'instant clones' managed as view machines. Instant clone engine uses vmfork technology to create the instant clones, these clones take very less time for provisioning. Instant clones have many similarities to linked clones like :- [^109] [^110]. This option is only valid for Automated Desktop.</td></tr></table>
**resourceType**|  xsd:string|  Type of resource. [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>DESKTOP</td><td>Denotes the Desktop Pool.</td></tr><tr><td>FARM</td><td>Denotes the Farm.</td></tr></table>
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  Entity id of virtual center. [^1]


 
