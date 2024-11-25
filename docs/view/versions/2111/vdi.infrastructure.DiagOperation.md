---
layout: page
title: Service - DiagOperation
hide:
#  - navigation
  - toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.infrastructure.DiagOperation`

See also
> [DiagOperationRequest](vdi.infrastructure.DiagOperation.DiagOpRequest.md), [DiagOperationResponse](vdi.infrastructure.DiagOperation.DiagOpResponse.md)

Since
> Horizon 7.2





## Service Description

The Diagnostic operation service interface used for interacting with Omnissa Horizon Diagnostic Agent.

**Methods**

Methods defined in this Service:
DiagOperation_Send




Sends the diagnostic request to Omnissa Horizon Diagnostic Agent.

**Privileges**

Privilege | Description
:---|:---
ADMINISTRATOR_VIEW|  Administrator view privilege is required to retrieve information.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [DiagOperation](vdi.infrastructure.DiagOperation.md) used to make the method call.
**request**| [DiagOperationRequest](vdi.infrastructure.DiagOperation.DiagOpRequest.md)|  Diagnostic operation Request




**Return Value**

Type | Description
:---|:---
[DiagOperationResponse](vdi.infrastructure.DiagOperation.DiagOpResponse.md)| Diagnostic operation Response



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
ADMIN_DIAG_OPERATION_SEND_SUCCEEDED|  is fired if the send operation has succeeded.
ADMIN_DIAG_OPERATION_SEND_FAILED|  is fired if the send operation has failed.

Show WSDL type definition












 
