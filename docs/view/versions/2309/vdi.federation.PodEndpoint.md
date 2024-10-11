---
layout: page
title: Service - PodEndpoint
hide:
 #- navigation
 - toc
---

  
  
  



Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.federation.PodEndpoint`

See also  
> [PodEndpointId](vdi.entity.PodEndpointId.md), [PodEndpointInfo](vdi.federation.PodEndpoint.PodEndpointInfo.md), [PodId](vdi.entity.PodId.md)

Since  
> Horizon View 6.0


  


## Service Description

Interface representing an endpoint in a pod. 

Methods

Methods defined in this Service   
---  
PodEndpoint_Get, PodEndpoint_List  
  



Get information about a specific podEndpoint. 

Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read a pod endpoint.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PodEndpoint](vdi.federation.PodEndpoint.md) used to make the method call.   
**id**| [PodEndpointId](vdi.entity.PodEndpointId.md)|  id of the pod endpoint to get   
  
  


Return Value 

Type |  Description   
---|---  
[PodEndpointInfo](vdi.federation.PodEndpoint.PodEndpointInfo.md)| podEndpointInfo for the endpoint  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the Pod Federation has not been initialized.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



List all pod endpoints in the specified pod. 

Privileges 

Privilege |  Description   
---|---  
FEDERATED_LDAP_VIEW|  Global LDAP read is required to list pod endpoints.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [PodEndpoint](vdi.federation.PodEndpoint.md) used to make the method call.   
**pod**| [PodId](vdi.entity.PodId.md)|  The pod id   
  
  


Return Value 

Type |  Description   
---|---  
[PodEndpointInfo[]](vdi.federation.PodEndpoint.PodEndpointInfo.md)| list of podEndpoints in the specified pod.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the Pod Federation has not been initialized.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  
