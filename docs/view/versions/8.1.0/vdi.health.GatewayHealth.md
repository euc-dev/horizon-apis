---
layout: page
title: Service - GatewayHealth
hide:
 #- navigation
 - toc
---

  
 
  



Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.health.GatewayHealth`

See also  
> [GatewayHealthInfo](vdi.health.GatewayHealth.GatewayHealthInfo.md), [GatewayId](vdi.entity.GatewayId.md)

Since  
> Horizon 7.7


  


## Service Description

Service for retrieving health information on Gateway. 

Methods

Methods defined in this Service   
---  
GatewayHealth_Get, GatewayHealth_List  
  



Gets the health information of the registered gateway. 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GatewayHealth](vdi.health.GatewayHealth.md) used to make the method call.   
**id**| [GatewayId](vdi.entity.GatewayId.md)|  The Id of the gateway.   
  
  


Return Value 

Type |  Description   
---|---  
[GatewayHealthInfo](vdi.health.GatewayHealth.GatewayHealthInfo.md)| Health information of the specified gateway.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Gets the health information of all the registered gateways. 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GatewayHealth](vdi.health.GatewayHealth.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[GatewayHealthInfo[]](vdi.health.GatewayHealth.GatewayHealthInfo.md)| A list of health information of all the registered gateways.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  
