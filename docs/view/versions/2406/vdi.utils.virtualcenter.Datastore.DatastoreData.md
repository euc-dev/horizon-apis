---
layout: page
title: Data Object - DatastoreData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.Datastore.DatastoreData  
Property of
     [DatastoreInfo](vdi.utils.virtualcenter.Datastore.DatastoreInfo.md#field_detail)  
See also
     [DatacenterId](vdi.entity.DatacenterId.md), [DatastoreIncompatibleReasons](vdi.utils.virtualcenter.Datastore.DatastoreIncompatibleReasons.md), [HostOrClusterId](vdi.entity.HostOrClusterId.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)  
Since 
    Horizon View 6.0

## Data Object Description 

DatastoreData is a set of Datastore attributes retrieved from the VC. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**name**|  xsd:string|  Datastore name   


 * This property cannot be updated.

  
**path**|  xsd:string|  Datastore path   


 * This property cannot be updated.

  
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  VirtualCenter id for this datastore   


 * This property cannot be updated.

  
**datacenter**| [DatacenterId](vdi.entity.DatacenterId.md)|  Datacenter id for this datastore   


 * This property need not be set.
 * This property cannot be updated.

  
**hostOrCluster**| [HostOrClusterId](vdi.entity.HostOrClusterId.md)|  HostOrCluster id for this datastore   


 * This property cannot be updated.

  
**diskType**|  xsd:string|  If the [fileSystemType](vdi.utils.virtualcenter.Datastore.DatastoreData.md#fileSystemType) is VMFS, the SSD disk type of the datastore.   


 * This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"SSD"| SSD disk type  
"NON_SSD"| NON-SSD disk type  
"UNKNOWN"| Unknown disk type  
"NON_VMFS"| NON-VMFS disk type  

  
**fileSystemType**|  xsd:string|  File system type of the datastore. VSAN disk types can only be used in desktop creation that enables VSAN.   


 * This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"VMFS"| VMFS  
"NFS"| NFS  
"VSAN"| VSAN  
"VVOL"| VVOL  

  
**vmfsMajorVersion**|  xsd:string|  If the [fileSystemType](vdi.utils.virtualcenter.Datastore.DatastoreData.md#fileSystemType) is VMFS, the VMFS major version number.   


 * This property need not be set.
 * This property cannot be updated.

  
**incompatibleReasons**| [DatastoreIncompatibleReasons](vdi.utils.virtualcenter.Datastore.DatastoreIncompatibleReasons.md)|  Reasons that may preclude this Datastore from being used in desktop creation.   


 * This property cannot be updated.

  
**localDatastore**|  xsd:boolean|  Whether or not this datastore is local to a single host.   


 * This property cannot be updated.

  
**capacityMB**|  xsd:long|  Maximum capacity of this datastore, in MB   


 * This property cannot be updated.

  
**freeSpaceMB**|  xsd:long|  Available capacity of this datastore, in MB   


 * This property cannot be updated.

  
**numberOfVMs**|  xsd:int|  Indicates the number of machines the datastore has for Desktop/Farm when applicable.  **_Since_** Horizon 7.6  


 * This property need not be set.
 * This property cannot be updated.

  
  

  

