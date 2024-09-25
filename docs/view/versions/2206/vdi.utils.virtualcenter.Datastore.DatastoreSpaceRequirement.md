---
layout: page
title: Data Object - DatastoreSpaceRequirement
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.Datastore.DatastoreSpaceRequirement
Returned by
     [Datastore_GetDatastoreRequirements](vdi.utils.virtualcenter.Datastore.md#getDatastoreRequirements)
Since 
    Horizon 7.6

## Data Object Description 

Datastore Requirements specified in GB. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**DiskType**|  xsd:string|  Disk Type used for storage.   


[^2]
  * This property will be one of:  
|  Value |  Description   
---|---  
"REPLICA"| Identifies disk for the placement of the replica that View Composer and Instant clone engine sourced desktops use as their base image.  
"PERSISTENT"| Identifies disk to preserves the user information when the OS data is updated, refreshed, or rebalanced for View Composer.  
"OS"| Identifies disk to store the Operating System related data.  

  
**minDiskSize**|  xsd:double|  Minimum recommended Disk Space, in GB.   


[^2]

  
**midDiskSize**|  xsd:double|  Recommended Disk Space with 50% utilization, in GB.   


[^1]
[^2]

  
**maxDiskSize**|  xsd:double|  Maximum recommended Disk Space, in GB.   


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
