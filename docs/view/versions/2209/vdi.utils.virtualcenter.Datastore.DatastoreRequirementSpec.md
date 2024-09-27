---
layout: page
title: Data Object - DatastoreRequirementSpec
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.Datastore.DatastoreRequirementSpec  
Parameter to
     [Datastore_GetDatastoreRequirements](vdi.utils.virtualcenter.Datastore.md#getDatastoreRequirements)  
See also
     [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md), [BaseImageVmId](vdi.entity.BaseImageVmId.md), [DesktopId](vdi.entity.DesktopId.md), [FarmId](vdi.entity.FarmId.md), [VmTemplateId](vdi.entity.VmTemplateId.md)  
Since 
    Horizon 7.6

## Data Object Description 

Datastore requirements specification. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**desktopId**| [DesktopId](vdi.entity.DesktopId.md)|  Desktop Id to be supplied when editing a Desktop Pool.   


* This property need not be set.

  
**farmId**| [FarmId](vdi.entity.FarmId.md)|  Farm Id to be supplied when editing a Farm.   


* This property need not be set.

  
**isFarm**|  xsd:boolean|  Set to true when creating/editing a Farm.   


  * This property has a default value of false.

  
**source**|  xsd:string|  The Source or the Provisioning Type of machines.   
**Note:** The value FULL_CLONE is not allowed in case of farms.   


  * This property will be one of:  
|  Value |  Description   
---|---  
"VIEW_COMPOSER"| View composer linked clones managed as view machines.  
"INSTANT_CLONE_ENGINE"| Instant clone engine created 'instant clones' managed as view machines.  
"FULL_CLONE"| Full Virtual Machines that are created from a vCenter Server template.  

  
**vmId**| [BaseImageVmId](vdi.entity.BaseImageVmId.md)|  Parent VM Id.   
Applicable in case of Linked Clones and Instant Clones.   


* This property need not be set.
  * This property is required if source is set to "VIEW_COMPOSER"or "INSTANT_CLONE_ENGINE".

  
**snapshotId**| [BaseImageSnapshotId](vdi.entity.BaseImageSnapshotId.md)|  VM Snapshot Id.   
Applicable in case of Linked Clones and Instant Clones.   


* This property need not be set.
  * This property is required if source is set to "VIEW_COMPOSER"or "INSTANT_CLONE_ENGINE".

  
**vmTemplateId**| [VmTemplateId](vdi.entity.VmTemplateId.md)|  VM Template Id.   
Applicable in case of Full Clones.   


* This property need not be set.
  * This property is required if source is set to "FULL_CLONE".

  
**poolSize**|  xsd:int|  The desired size of the Pool/Farm.   
  
**isPersistent**|  xsd:boolean|  User assignment of the pool: Dedicated (Persistent) / Floating.   
Ignored in case of Farm.   


  * This property has a default value of false.

  
**userDiskSize**|  xsd:double|  Size of Persistent Disk (in MB). 

  * This value will be considered only in case of Dedicated Linked Pool.
  * It will be ignored for other Pools and Farms.

  


* This property need not be set.
  * This property is required if isPersistent is set to true.

  
**useVsan**|  xsd:boolean|  When Vmware Virtual SAN is used.   
Set to true when Virtual SAN is configured and in use for the pool.   


  * This property has a default value of false.

  
**useSeparateReplicaAndOSDisk**|  xsd:boolean|  Set to true when separate datastores for replica and OS disks are used. 
* Applicable only in case of Linked Clones and Instant Clones.
  


  * This property has a default value of false.

  
**useSeparatePersistentAndOSDisk**|  xsd:boolean|  When the Separate datastores for persistent and OS disks are used. 

  * Set to true only in case of DEDICATED LINKED_CLONE Pool.
  * It will be ignored in case of Farms and other Pools.

  


  * This property has a default value of false.

  
  
  
 
  
  

