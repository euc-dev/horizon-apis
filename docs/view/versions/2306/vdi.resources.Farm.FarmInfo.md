---
layout: page
title: Data Object - FarmInfo
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.resources.Farm.FarmInfo`

Returned by
> [Farm_Get](vdi.resources.Farm.md#get), [Farm_GetByNamingPattern](vdi.resources.Farm.md#getByNamingPattern)

See also
> [FarmAutomatedFarmData](vdi.resources.Farm.AutomatedFarmData.md), [FarmData](vdi.resources.Farm.FarmData.md), [FarmId](vdi.entity.FarmId.md)

Since
> Horizon View 6.0


## Data Object Description

Farm info

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [FarmId](vdi.entity.FarmId.md)|  Farm entity ID [^2]
**type**|  xsd:string|  Type of farm.  **_Since_** Horizon View 6.2 [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>AUTOMATED</td><td>An automated farm creates RDS Servers cloned from a snapshot.</td></tr><tr><td>MANUAL</td><td>A manual farm allows selection and addition of existing RDS Servers to the farm.</td></tr></table>
**source**|  xsd:string|  Source of farm machines.  **_Since_** Horizon 7.1 [^1] [^2] [^29] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"VIEW_COMPOSER"</td><td>View composer linked clones managed as view RDS Servers. They share the same base image and use less storage space than full RDS Servers.</td></tr><tr><td>"INSTANT_CLONE_ENGINE"</td><td>Instant clone engine created 'instant clones' managed as view RDS Servers. Instant clone engine uses vmfork technology to create the instant clones, these clones take much less time for provisioning. Instant clones have many similarities to linked clones like :- [^109] [^110]. This option is only valid for Automated Farm.</td></tr></table>
**imageSource**|  xsd:string|  Source of image used in the farm. Applicable for automated farm.  **_Since_** Horizon 7.10 [^1] [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"VIRTUAL_CENTER"</td><td>Image was created in virtual center.</td></tr><tr><td>"IMAGE_CATALOG"</td><td>Image was created in image catalog.</td></tr></table>
**data**| [FarmData](vdi.resources.Farm.FarmData.md)|  Farm data
**automatedFarmData**| [FarmAutomatedFarmData](vdi.resources.Farm.AutomatedFarmData.md)|  Automated farm data.  **_Since_** Horizon View 6.2 [^1] [^29]
**refId**|  xsd:string|  Reference ID used for this farm.  **_Since_** Horizon 8.2 [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^29]: This property is required if type is set to 'AUTOMATED'.
[^109]: Both instant and linked clones share the same base image and use less storage space than full virtual machines.
[^110]: The user profile for both types clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes.