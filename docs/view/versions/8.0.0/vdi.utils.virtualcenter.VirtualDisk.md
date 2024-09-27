---
layout: page
title: Service - VirtualDisk
hide:
 #- navigation
 - toc
---

  
 
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.VirtualDisk  
See also
     [DatastoreId](vdi.entity.DatastoreId.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md), [VirtualDiskInfo](vdi.utils.virtualcenter.VirtualDisk.VirtualDiskInfo.md), [VirtualDiskListSpec](vdi.utils.virtualcenter.VirtualDisk.VirtualDiskListSpec.md)  
Since 
    Horizon View 6.0

  


## Service Description

Service for fetching Virtual Disks from VirtualCenter that are not already attached to a Linked-Clone VM. 

Methods

Methods defined in this Service   
---  
VirtualDisk_List, VirtualDisk_ListAllDisks  
  



Gets a list of VirtualDiskInfo from VC for a given datastore. If datastoreId is not specified, it gets the VirtualDisks for all datastores. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  privilege is required to get the list of VirtualDiskInfo.   
VC_CONFIG_VIEW|  privilege is required to get the list of VirtualDiskInfo.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VirtualDisk](vdi.utils.virtualcenter.VirtualDisk.md) used to make the method call.   
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  unique identifier for vc entry   
  
**datastore**| [DatastoreId](vdi.entity.DatastoreId.md)|  datastore entityId (optional)   


  * This parameter need not be set.

  
  


Return Value 

Type |  Description   
---|---  
[VirtualDiskInfo[]](vdi.utils.virtualcenter.VirtualDisk.VirtualDiskInfo.md)| Array of VirtualDiskInfo  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Gets a list of all VirtualDiskInfo from VC for a given datastore. If datastoreId is not specified, it gets the VirtualDisks for all datastores. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  privilege is required to get the list of VirtualDiskInfo.   
VC_CONFIG_VIEW|  privilege is required to get the list of VirtualDiskInfo.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VirtualDisk](vdi.utils.virtualcenter.VirtualDisk.md) used to make the method call.   
**virtualDiskListSpec**| [VirtualDiskListSpec](vdi.utils.virtualcenter.VirtualDisk.VirtualDiskListSpec.md)|    
  
  


Return Value 

Type |  Description   
---|---  
[VirtualDiskInfo[]](vdi.utils.virtualcenter.VirtualDisk.VirtualDiskInfo.md)| Array of VirtualDiskInfo  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  

