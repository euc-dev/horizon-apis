---
layout: page
title: Data Object - ImageManagementStreamQuerySpec
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.imagemanagement.ImageManagementStream.ImageManagementStreamQuerySpec  
Parameter to
     [ImageManagementStream_ListBySpec](vdi.utils.imagemanagement.ImageManagementStream.md#listBySpec)  
See also
     [VirtualCenterId](vdi.entity.VirtualCenterId.md)  
Since 
    Horizon 7.10

## Data Object Description 

Query spec for filtering image management stream. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**status**|  xsd:string|  Image management stream status.   


 * This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"AVAILABLE"| Image management stream is available for pools/farms to be created.  
"DELETED"| Image management stream is deleted.  
"DISABLED"| Image management stream is disabled and no further pools/farms can be created using the same.  
"FAILED"| Image management stream creation has failed.  
"IN_PROGRESS"| Image management stream creation is in progress.  
"PARTIALLY_AVAILABLE"| Image management version could not be created in one or more environments.  
"PENDING"| Image management stream is in pending state to be created by a task.  

  
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

  
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  Entity id of virtual center.   


 * This property need not be set.

  
  

  

