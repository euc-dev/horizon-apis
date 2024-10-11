---
layout: page
title: Service - Gateway
hide:
 #- navigation
 - toc
---

  
 
  



Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.Gateway`

See also  
> [GatewayId](vdi.entity.GatewayId.md), [GatewayInfo](vdi.infrastructure.Gateway.GatewayInfo.md), [GatewaySpec](vdi.infrastructure.Gateway.GatewaySpec.md)

Since  
> Horizon 7.7


  


## Service Description

Service interface for Gateway. 

Methods

Methods defined in this Service   
---  
Gateway_Get, Gateway_List, Gateway_Register, Gateway_Unregister  
  



Get the GatewayInfo of registered gateway. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration view privilege is required to retrieve information about the gateway.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Gateway](vdi.infrastructure.Gateway.md) used to make the method call.   
**id**| [GatewayId](vdi.entity.GatewayId.md)|  The Id of the gateway.   
  
  


Return Value 

Type |  Description   
---|---  
[GatewayInfo](vdi.infrastructure.Gateway.GatewayInfo.md)| Details of the gateway.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



List the GatewayInfo objects of all the registered gateways. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration view privilege is required to retrieve information about the gateways.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Gateway](vdi.infrastructure.Gateway.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[GatewayInfo[]](vdi.infrastructure.Gateway.GatewayInfo.md)| List of all gateway objects.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Add a gateway to the view instance. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to register/add a gateway.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Gateway](vdi.infrastructure.Gateway.md) used to make the method call.   
**spec**| [GatewaySpec](vdi.infrastructure.Gateway.GatewaySpec.md)|  attributes needed to add gateway.   
  
  


Return Value 

Type |  Description   
---|---  
[GatewayId](vdi.entity.GatewayId.md)| unique identifier for the gateway  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Unregister gateway for the input gateway id. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management privilege is required to unregister the gateway.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Gateway](vdi.infrastructure.Gateway.md) used to make the method call.   
**id**| [GatewayId](vdi.entity.GatewayId.md)|  The Id of the gateway.   
  
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  
