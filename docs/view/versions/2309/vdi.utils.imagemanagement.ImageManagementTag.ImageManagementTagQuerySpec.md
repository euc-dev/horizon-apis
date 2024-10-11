---
layout: page
title: Data Object - ImageManagementTagQuerySpec
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.imagemanagement.ImageManagementTag.ImageManagementTagQuerySpec`

Parameter to  
> [ImageManagementTag_ListBySpec](vdi.utils.imagemanagement.ImageManagementTag.md#listBySpec)

See also  
> [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since  
> Horizon 7.10


## Data Object Description 

Query spec for filtering image management tag. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**fetchAvailableAssetsOnly**|  xsd:boolean|  When set to true, tags filtered would be having stream and version in AVAILABLE or PARTIALLY_AVAILABLE status and asset in AVAILABLE status.   


  * This property has a default value of false.
 * This property need not be set.

  
**provisioningType**|  xsd:string|  Provisioning type of the desktop/farm.   


 * This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"VIRTUAL_CENTER"| Virtual center virtual machines managed as view machines. This option is valid for Automated and Manual Desktop. In case of Automated Desktop, these refer to Full Virtual Machines that are created from a vCenter Server template.  
"INSTANT_CLONE_ENGINE"| Instant clone engine created 'instant clones' managed as view machines. Instant clone engine uses vmfork technology to create the instant clones, these clones take very less time for provisioning. Instant clones have many similarities to linked clones like :-  

    * Both instant and linked clones share the same base image and use less storage space than full virtual machines.
    * The user profile for both types clones can be redirected to persistent disks that will be unaffected by OS updates and refreshes.
This option is only valid for Automated Desktop.  

  
**resourceType**|  xsd:string|  Type of resource.   


 * This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"DESKTOP"| Denotes the Desktop Pool.  
"FARM"| Denotes the Farm.  

  
**imageManagementStream**| [ImageManagementStreamId](vdi.entity.ImageManagementStreamId.md)|  Entity Id of image management stream.   
  
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  Entity id of virtual center.   
  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
