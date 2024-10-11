---
layout: page
title: Service - StorageAccelerator
hide:
 #- navigation
 - toc
---

  
   
  



Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.StorageAccelerator`

See also  
> [ServerDefinition](vdi.utils.Certificate.ServerDefinition.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since  
> Horizon 7.8


  


## Service Description

The object for fetching View Storage Accelerator attributes for virtual center. 

Methods

Methods defined in this Service   
---  
StorageAccelerator_IsSupportedByServerDefinition, StorageAccelerator_IsSupportedByVirtualCenter  
  



Determines whether View Storage Accelerator is supported for the given virtual center. Using a ServerDefinition allows querying the server before it has been added to the Connection Server. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration (read-only) is required to get information on View Storage Accelerator.   
VC_CONFIG_VIEW|  privilege is required to get information about View Storage Accelerator support on a Virtual Center.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [StorageAccelerator](vdi.utils.virtualcenter.StorageAccelerator.md) used to make the method call.   
**serverDefinition**| [ServerDefinition](vdi.utils.Certificate.ServerDefinition.md)|  Details (ip, user, password, etc.) needed to connect to a server.   
  
  


Return Value 

Type |  Description   
---|---  
xsd:string| String that determines whether storage accelerator is supported.

  * This property will be one of:  
|  Value |  Description   
---|---  
"SA_VALIDATION_OK"| Virtual center supports View Storage Accelerator.  
"SA_UNSUPPORTED_VC"| Virtual center does not support View Storage Accelerator.  

  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Determines whether View Storage Accelerator is supported for the given virtual center. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration (read-only) is required to get information on View Storage Accelerator.   
VC_CONFIG_VIEW|  privilege is required to get information about View Storage Accelerator support on a Virtual Center.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [StorageAccelerator](vdi.utils.virtualcenter.StorageAccelerator.md) used to make the method call.   
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  unique identifier for vc entry.   
  
  


Return Value 

Type |  Description   
---|---  
xsd:string| String that determines whether storage accelerator is supported.

  * This property will be one of:  
|  Value |  Description   
---|---  
"SA_VALIDATION_OK"| Virtual center supports View Storage Accelerator.  
"SA_UNSUPPORTED_VC"| Virtual center does not support View Storage Accelerator.  

  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  
