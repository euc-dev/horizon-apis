---
layout: page
title: Service - JwtToken
hide:
#- navigation
- toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.infrastructure.JwtToken`

See also
> [JwtPublicKeyInfo](vdi.infrastructure.JwtToken.JwtPublicKeyInfo.md), [JwtTokenGenerationSpec](vdi.infrastructure.JwtToken.JwtTokenGenerationSpec.md), [JwtTokenInfo](vdi.infrastructure.JwtToken.JwtTokenInfo.md)

Since
> Horizon 7.4





## Service Description

Service interface for JWT Token.

**Methods**

Methods defined in this Service:
JwtToken_Generate, JwtToken_GetPublicKeys




Generates JWT token.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [JwtToken](vdi.infrastructure.JwtToken.md) used to make the method call.
**spec**| [JwtTokenGenerationSpec](vdi.infrastructure.JwtToken.JwtTokenGenerationSpec.md)| [^135]





**Return Value**

Type | Description
:---|:---
[JwtTokenInfo](vdi.infrastructure.JwtToken.JwtTokenInfo.md)| The generated JWT token.



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
VLSI_JWT_TOKEN_GENERATED|  if JWT token creation succeeds.
VLSI_JWT_TOKEN_GENERATION_FAILED|  if JWT token generation fails.

Show WSDL type definition







Retrieves public keys for validating JWT token. This API can be used by unauthenticated sessions to retrieves public keys for validating JWT tokens.

**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [JwtToken](vdi.infrastructure.JwtToken.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[JwtPublicKeyInfo[]](vdi.infrastructure.JwtToken.JwtPublicKeyInfo.md)| The JwtPublicKeyInfo list.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 


[^135]: This parameter need not be set.