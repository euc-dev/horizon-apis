---
layout: page
title: Service - SAMLAuthenticator
hide:
#- navigation
- toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.SAMLAuthenticator`

See also
> [MapEntry](vdi.util.MapEntry.md), [SAMLAuthenticatorId](vdi.entity.SAMLAuthenticatorId.md), [SAMLAuthenticatorInfo](vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorInfo.md), [SAMLAuthenticatorSpec](vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorSpec.md)

Since
> Horizon View 6.0





## Service Description

Service for managing SAML authenticators.

**Methods**

Methods defined in this Service:
SAMLAuthenticator_Create, SAMLAuthenticator_Delete, SAMLAuthenticator_Get, SAMLAuthenticator_List, SAMLAuthenticator_Update




Creates a SAML authenticator.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to create a SAML authenticator.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [SAMLAuthenticator](vdi.infrastructure.SAMLAuthenticator.md) used to make the method call.
**spec**| [SAMLAuthenticatorSpec](vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorSpec.md)|  The specification of the SAML authenticator.




**Return Value**

Type | Description
:---|:---
[SAMLAuthenticatorId](vdi.entity.SAMLAuthenticatorId.md)| The ID of the newly created SAML authenticator.



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
VLSI_SAML_AUTHENTICATOR_CREATED|  If the SAML authenticator was successfully created.
VLSI_SAML_AUTHENTICATOR_CREATE_FAILED|  If the SAML authenticator could not be created.

Show WSDL type definition







Deletes the specified SAML authenticator.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to delete a SAML authenticator.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [SAMLAuthenticator](vdi.infrastructure.SAMLAuthenticator.md) used to make the method call.
**id**| [SAMLAuthenticatorId](vdi.entity.SAMLAuthenticatorId.md)|  The ID of the SAML authenticator to delete.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityInUse](vdi.fault.EntityInUse.md)| Thrown if the SAML authentication is currently being used by a connection server.
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_SAML_AUTHENTICATOR_DELETED|  If the SAML authenticator was successfully deleted.
VLSI_SAML_AUTHENTICATOR_DELETE_FAILED|  If the SAML authenticator could not be deleted.

Show WSDL type definition







Retrieves information about a SAML authenticator.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  Global configuration view is required to retrieve information about a SAML authenticator.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [SAMLAuthenticator](vdi.infrastructure.SAMLAuthenticator.md) used to make the method call.
**id**| [SAMLAuthenticatorId](vdi.entity.SAMLAuthenticatorId.md)|  The ID of the SAML authenticator.




**Return Value**

Type | Description
:---|:---
[SAMLAuthenticatorInfo](vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorInfo.md)| Information about the specified SAML authenticator.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Lists the configured SAML authenticators.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  Global configuration view is required to list SAML authenticators.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [SAMLAuthenticator](vdi.infrastructure.SAMLAuthenticator.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[SAMLAuthenticatorInfo[]](vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorInfo.md)| Information about the configured SAML authenticators.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Updates a SAML authenticator.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to update a SAML authenticator.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [SAMLAuthenticator](vdi.infrastructure.SAMLAuthenticator.md) used to make the method call.
**id**| [SAMLAuthenticatorId](vdi.entity.SAMLAuthenticatorId.md)|  The ID of the SAML authenticator to update.
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  Key value pairs describing attributes to be updated. [^298]





**Return Value**

Type | Description
:---|:---
None



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
VLSI_SAML_AUTHENTICATOR_UPDATED|  If the SAML authenticator was successfully updated.
VLSI_SAML_AUTHENTICATOR_UPDATE_FAILED|  If the SAML authenticator could not be updated.

Show WSDL type definition












 


[^298]: This parameter is an update map based on [SAMLAuthenticatorInfo](vdi.infrastructure.SAMLAuthenticator.SAMLAuthenticatorInfo.md "SAMLAuthenticatorInfo").