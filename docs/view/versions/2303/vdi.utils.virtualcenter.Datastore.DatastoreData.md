---
layout: page
title: Data Object - DatastoreData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.virtualcenter.Datastore.DatastoreData`

Property of
> [DatastoreInfo](vdi.utils.virtualcenter.Datastore.DatastoreInfo.md#field_detail)

See also
> [DatacenterId](vdi.entity.DatacenterId.md), [DatastoreIncompatibleReasons](vdi.utils.virtualcenter.Datastore.DatastoreIncompatibleReasons.md), [HostOrClusterId](vdi.entity.HostOrClusterId.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon View 6.0


## Data Object Description

DatastoreData is a set of Datastore attributes retrieved from the VC.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**name**|  xsd:string|  Datastore name [^2]
**path**|  xsd:string|  Datastore path [^2]
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  VirtualCenter id for this datastore [^2]
**datacenter**| [DatacenterId](vdi.entity.DatacenterId.md)|  Datacenter id for this datastore [^1] [^2]
**hostOrCluster**| [HostOrClusterId](vdi.entity.HostOrClusterId.md)|  HostOrCluster id for this datastore [^2]
**diskType**|  xsd:string|  If the [fileSystemType](vdi.utils.virtualcenter.Datastore.DatastoreData.md#fileSystemType) is VMFS, the SSD disk type of the datastore. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"SSD"</td><td>SSD disk type</td></tr><tr><td>"NON_SSD"</td><td>NON-SSD disk type</td></tr><tr><td>"UNKNOWN"</td><td>Unknown disk type</td></tr><tr><td>"NON_VMFS"</td><td>NON-VMFS disk type</td></tr></table>
**fileSystemType**|  xsd:string|  File system type of the datastore. VSAN disk types can only be used in desktop creation that enables VSAN. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"VMFS"</td><td>VMFS</td></tr><tr><td>"NFS"</td><td>NFS</td></tr><tr><td>"VSAN"</td><td>VSAN</td></tr><tr><td>"VVOL"</td><td>VVOL</td></tr></table>
**vmfsMajorVersion**|  xsd:string|  If the [fileSystemType](vdi.utils.virtualcenter.Datastore.DatastoreData.md#fileSystemType) is VMFS, the VMFS major version number. [^1] [^2]
**incompatibleReasons**| [DatastoreIncompatibleReasons](vdi.utils.virtualcenter.Datastore.DatastoreIncompatibleReasons.md)|  Reasons that may preclude this Datastore from being used in desktop creation. [^2]
**localDatastore**|  xsd:boolean|  Whether or not this datastore is local to a single host. [^2]
**capacityMB**|  xsd:long|  Maximum capacity of this datastore, in MB [^2]
**freeSpaceMB**|  xsd:long|  Available capacity of this datastore, in MB [^2]
**numberOfVMs**|  xsd:int|  Indicates the number of machines the datastore has for Desktop/Farm when applicable.  **_Since_** Horizon 7.6 [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.