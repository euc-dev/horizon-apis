---
layout: page
title: Service - StorageAcceleratorHost
hide:
 #- navigation
 - toc
---

  
  
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.StorageAcceleratorHost  
See also
     [ServerDefinition](vdi.utils.Certificate.ServerDefinition.md), [StorageAcceleratorHostInfo](vdi.utils.virtualcenter.StorageAcceleratorHost.StorageAcceleratorHostInfo.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)  
Since 
    Horizon View 6.0

  


## Service Description

The object for fetching View Storage Accelerator attributes from virtual center. 

Methods

Methods defined in this Service   
---  
StorageAcceleratorHost_ListByServerDefinition, StorageAcceleratorHost_ListByVirtualCenter  
  



Gets list of HypervisorHost for a VC that has not yet been added to the connection broker. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration (read-only) is required to get information on hosts which support View Storage Accelerator.   
VC_CONFIG_VIEW|  privilege is required to get information on hosts which support View Storage Accelerator.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [StorageAcceleratorHost](vdi.utils.virtualcenter.StorageAcceleratorHost.md) used to make the method call.   
**serverDefinition**| [ServerDefinition](vdi.utils.Certificate.ServerDefinition.md)|  Details (ip, user, password, etc.) needed to connect to a server.   
  
  


Return Value 

Type |  Description   
---|---  
[StorageAcceleratorHostInfo[]](vdi.utils.virtualcenter.StorageAcceleratorHost.StorageAcceleratorHostInfo.md)| Information on hosts which support View Storage Accelerator.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Gets list of information on hosts which support View Storage Accelerator. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration (read-only) is required to get information on hosts which support View Storage Accelerator.   
VC_CONFIG_VIEW|  privilege is required to get information on hosts which support View Storage Accelerator.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [StorageAcceleratorHost](vdi.utils.virtualcenter.StorageAcceleratorHost.md) used to make the method call.   
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  unique identifier for vc entry   
  
  


Return Value 

Type |  Description   
---|---  
[StorageAcceleratorHostInfo[]](vdi.utils.virtualcenter.StorageAcceleratorHost.StorageAcceleratorHostInfo.md)| Information on hosts which support View Storage Accelerator.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  

