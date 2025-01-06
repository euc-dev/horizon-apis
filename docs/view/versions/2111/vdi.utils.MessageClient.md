---
layout: page
title: Service - MessageClient
hide:
#  - navigation
  - toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.MessageClient`

See also
> [MessageClientId](vdi.entity.MessageClientId.md), [MessageClientInfo](vdi.utils.MessageClient.MessageClientInfo.md)

Since
> Horizon 7.7





## Service Description

**Methods**

Methods defined in this Service:
MessageClient_Create, MessageClient_Delete, MessageClient_Get, MessageClient_Update




Create a message client.

**Privileges**

Privilege | Description
:---|:---
ADMINISTRATOR|  Administrator is required to create the message client.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [MessageClient](vdi.utils.MessageClient.md) used to make the method call.
**clientUuid**|  xsd:string|  The message client uuid, which is generated by client itself
**clientType**|  xsd:string|  The message client type, which should be a member of MessageClientType.
**pemCertificates**|  xsd:string[]|  The message client certificates in PEM format. PemCertificate should be valid now, expired after 7 days, and its subject should be CN=clientType/clientUuid, otherwise InvalidArgumentFault will be thrown.




**Return Value**

Type | Description
:---|:---
[MessageClientInfo](vdi.utils.MessageClient.MessageClientInfo.md)|



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
VLSI_CREATE_MESSAGE_CLIENT|  If the message client was created successfully.
VLSI_CREATE_MESSAGE_CLIENT_FAILED|  If the message client could not be created.

Show WSDL type definition







Delete a message client.

**Privileges**

Privilege | Description
:---|:---
ADMINISTRATOR|  Administrator is delete the message client.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [MessageClient](vdi.utils.MessageClient.md) used to make the method call.
**id**| [MessageClientId](vdi.entity.MessageClientId.md)|  The message client id.




**Return Value**

Type | Description
:---|:---
[MessageClientInfo](vdi.utils.MessageClient.MessageClientInfo.md)|



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
VLSI_DELETE_MESSAGE_CLIENT|  If the message client was deleted successfully.
VLSI_DELETE_MESSAGE_CLIENT_FAILED|  If the message client could not be deleted.

Show WSDL type definition







Get the messageClientInfo with id

**Privileges**

Privilege | Description
:---|:---
ADMINISTRATOR_VIEW|  Administrator (read-only) is required to get message client.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [MessageClient](vdi.utils.MessageClient.md) used to make the method call.
**id**| [MessageClientId](vdi.entity.MessageClientId.md)|  The message client id.




**Return Value**

Type | Description
:---|:---
[MessageClientInfo](vdi.utils.MessageClient.MessageClientInfo.md)| The messageClientInfo



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Update a message client.

**Privileges**

Privilege | Description
:---|:---
ADMINISTRATOR|  Administrator is required to update the message client.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [MessageClient](vdi.utils.MessageClient.md) used to make the method call.
**id**| [MessageClientId](vdi.entity.MessageClientId.md)|
**pemCertificates**|  xsd:string[]|  The message client certificates in PEM format. PemCertificate should be valid now, expired after 7 days, and its subject should be CN=clientType/clientUuid, otherwise InvalidArgumentFault will be thrown.




**Return Value**

Type | Description
:---|:---
[MessageClientInfo](vdi.utils.MessageClient.MessageClientInfo.md)|



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
VLSI_UPDATE_MESSAGE_CLIENT|  If the message client was updated successfully.
VLSI_UPDATE_MESSAGE_CLIENT_FAILED|  If the message client could not be updated.

Show WSDL type definition












 