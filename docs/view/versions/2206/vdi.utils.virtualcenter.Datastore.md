---
layout: page
title: Service - Datastore
hide:
 #- navigation
 - toc
---

  
  
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.Datastore  
See also
     [DatastoreClusterInfo](vdi.utils.virtualcenter.Datastore.DatastoreClusterInfo.md), [DatastoreId](vdi.entity.DatastoreId.md), [DatastoreInfo](vdi.utils.virtualcenter.Datastore.DatastoreInfo.md), [DatastoreRequirementSpec](vdi.utils.virtualcenter.Datastore.DatastoreRequirementSpec.md), [DatastoreSpaceRequirement](vdi.utils.virtualcenter.Datastore.DatastoreSpaceRequirement.md), [DatastoreSpec](vdi.utils.virtualcenter.Datastore.DatastoreSpec.md), [DesktopOrFarmDatastoreUsageInfo](vdi.utils.virtualcenter.Datastore.DesktopOrFarmDatastoreUsageInfo.md), [HostOrClusterId](vdi.entity.HostOrClusterId.md)  
Since 
    Horizon View 6.0

  


## Service Description

The object for fetching Datastores from VirtualCenter. 

Methods

Methods defined in this Service   
---  
Datastore_GetDatastoreRequirements, Datastore_GetUsage, Datastore_ListDatastoreClustersByHostOrCluster, Datastore_ListDatastoresByDesktopOrFarm, Datastore_ListDatastoresByHostOrCluster  
  



DatastoreSpaceRequirement can be in following combinations. Datastore type returned will be: 

  * **OS** : When there are no separate disks for OS and replica or persisten diskt.
  * **OS, REPLICA** : When the Pool has separate disk for replica and OS.
  * **OS, REPLICA, PERSISTENT** : When Pool has separate OS, replica and persistent disks.



Privileges 

Privilege |  Description   
---|---  
VC_CONFIG_VIEW|  privilege is required for computing the space requirements.   
POOL_VIEW|  privilege is required for accessing Desktop or Farm mentioned via [desktopId](vdi.utils.virtualcenter.Datastore.DatastoreRequirementSpec.md#desktopId) or [farmId](vdi.utils.virtualcenter.Datastore.DatastoreRequirementSpec.md#farmId).   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Datastore](vdi.utils.virtualcenter.Datastore.md) used to make the method call.   
**spec**| [DatastoreRequirementSpec](vdi.utils.virtualcenter.Datastore.DatastoreRequirementSpec.md)|  DatastoreRequirementSpec   
  
  


Return Value 

Type |  Description   
---|---  
[DatastoreSpaceRequirement[]](vdi.utils.virtualcenter.Datastore.DatastoreSpaceRequirement.md)| Array of DatastoreSpaceRequirement  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Gets the Desktop or Farm and its usage details for a given datastore. For now, it will lists the automated Desktops and Farms only. 

Privileges 

Privilege |  Description   
---|---  
POOL_VIEW|  privilege on corresponding access group is required to get the usage information of a Desktop and/or Farm.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Datastore](vdi.utils.virtualcenter.Datastore.md) used to make the method call.   
**id**| [DatastoreId](vdi.entity.DatastoreId.md)|  The resource id of the datastore.   
  
  


Return Value 

Type |  Description   
---|---  
[DesktopOrFarmDatastoreUsageInfo[]](vdi.utils.virtualcenter.Datastore.DesktopOrFarmDatastoreUsageInfo.md)| An array of DesktopOrFarmUsageInfo  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Gets a list of datastore clusters from VC for the given host or cluster that may be suitable for use in full clone desktop creation. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  privilege is required to get the list of DatastoreClusterInfo.   
VC_CONFIG_VIEW|  privilege is required to get the list of DatastoreClusterInfo.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Datastore](vdi.utils.virtualcenter.Datastore.md) used to make the method call.   
**hostOrCluster**| [HostOrClusterId](vdi.entity.HostOrClusterId.md)|  host or cluster to list datastore clusters for   
  
  


Return Value 

Type |  Description   
---|---  
[DatastoreClusterInfo[]](vdi.utils.virtualcenter.Datastore.DatastoreClusterInfo.md)| Array of DatastoreClusterInfo  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Gets a list of datastores from VC for the given host or cluster that may be suitable for use during desktop/farm updates. Skips the VMs calculation for the following cases: 

  * DesktopId provided is manual or RDS type
  * FarmId provided is of manual type

Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  privilege is required to get the list of DatastoreInfo.   
VC_CONFIG_VIEW|  privilege is required to get the list of DatastoreInfo.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Datastore](vdi.utils.virtualcenter.Datastore.md) used to make the method call.   
**spec**| [DatastoreSpec](vdi.utils.virtualcenter.Datastore.DatastoreSpec.md)|    
  
  


Return Value 

Type |  Description   
---|---  
[DatastoreInfo[]](vdi.utils.virtualcenter.Datastore.DatastoreInfo.md)| Array of DatastoreInfo  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Gets a list of datastores from VC for the given host or cluster that may be suitable for use in full or linked clone desktop creation. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  privilege is required to get the list of DatastoreInfo.   
VC_CONFIG_VIEW|  privilege is required to get the list of DatastoreClusterInfo.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Datastore](vdi.utils.virtualcenter.Datastore.md) used to make the method call.   
**hostOrCluster**| [HostOrClusterId](vdi.entity.HostOrClusterId.md)|  host or cluster to list datastores for   
  
  


Return Value 

Type |  Description   
---|---  
[DatastoreInfo[]](vdi.utils.virtualcenter.Datastore.DatastoreInfo.md)| Array of DatastoreInfo  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  

