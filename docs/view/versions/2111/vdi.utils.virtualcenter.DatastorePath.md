---
layout: page
title: Service - DatastorePath
hide:
 #- navigation
 - toc
---

  
   
  



Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.DatastorePath`

See also  
> [DatastoreId](vdi.entity.DatastoreId.md), [DatastorePathInfo](vdi.utils.virtualcenter.DatastorePath.DatastorePathInfo.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since  
> Horizon View 6.0


  


## Service Description

Service for fetching all folder paths within a Datastore from VirtualCenter. 

Methods

Methods defined in this Service   
---  
DatastorePath_List  
  



Gets a list of DatastorePathInfo from VC for a given datastore. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  privilege is required to get the list of DatastorePathInfo.   
VC_CONFIG_VIEW|  privilege is required to get the list of DatastorePathInfo.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [DatastorePath](vdi.utils.virtualcenter.DatastorePath.md) used to make the method call.   
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  unique identifier for vc entry   
  
**datastore**| [DatastoreId](vdi.entity.DatastoreId.md)|  datastore entityId   
  
  


Return Value 

Type |  Description   
---|---  
[DatastorePathInfo[]](vdi.utils.virtualcenter.DatastorePath.DatastorePathInfo.md)| Array of DatastorePathInfo  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  
