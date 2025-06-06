---
layout: page
title: Service - SAMLAuthenticatorHealth
hide:
#  - navigation
  - toc
---







Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.health.SAMLAuthenticatorHealth`

See also
> [SAMLAuthenticatorHealthInfo](vdi.health.SAMLAuthenticatorHealth.SAMLAuthenticatorHealthInfo.md), [SAMLAuthenticatorId](vdi.entity.SAMLAuthenticatorId.md)

Since
> Horizon View 6.0





## Service Description

Service for retrieving health information on SAML authenticators.

**Methods**

Methods defined in this Service:
SAMLAuthenticatorHealth_Get, SAMLAuthenticatorHealth_List




Gets the health of the specified SAML authenticator.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](../2406/../2406/vmodl.ManagedObjectReference.md)|  A reference to the [SAMLAuthenticatorHealth](vdi.health.SAMLAuthenticatorHealth.md) used to make the method call.
**id**| [SAMLAuthenticatorId](../2406/vdi.entity.SAMLAuthenticatorId.md)|  The ID of the SAML authenticator.




**Return Value**

Type | Description
:---|:---
[SAMLAuthenticatorHealthInfo](vdi.health.SAMLAuthenticatorHealth.SAMLAuthenticatorHealthInfo.md)| The health of the SAML authenticator.



**Faults**

Type | Description
:---|:---
[EntityNotFound](../2406/vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](../2406/vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](../2406/vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](../2406/vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](../2406/vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets the health of all SAML authenticators associated with this View cluster.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](../2406/vmodl.ManagedObjectReference.md)|  A reference to the [SAMLAuthenticatorHealth](vdi.health.SAMLAuthenticatorHealth.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[SAMLAuthenticatorHealthInfo[]](vdi.health.SAMLAuthenticatorHealth.SAMLAuthenticatorHealthInfo.md)| The health of all SAML authenticators.



**Faults**

Type | Description
:---|:---
[EntityNotFound](../2406/vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](../2406/vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](../2406/vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](../2406/vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](../2406/vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
