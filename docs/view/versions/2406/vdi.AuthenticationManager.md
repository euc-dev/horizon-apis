---
layout: page
title: Service - AuthenticationManager
hide:
#- navigation
- toc
---







Java Class
> `com.vmware.vdi.vlsi.binding.vdi.AuthenticationManager`


See also
> [ClientKeyDerivationSpec](vdi.AuthenticationManager.ClientKeyDerivationSpec.md), [JwtTokenData](vdi.infrastructure.JwtToken.JwtTokenData.md), [SecureString](vdi.util.SecureString.md), [ServerKeyDerivationInfo](vdi.AuthenticationManager.ServerKeyDerivationInfo.md)


Since
> Horizon View 6.0





## Service Description

AuthenticationManager provides administrative login capability.

Methods

Methods defined in this Service
---
AuthenticationManager_GenerateKeyMaterial, AuthenticationManager_Login, AuthenticationManager_LoginByToken, AuthenticationManager_Logout, AuthenticationManager_SetLocale




Generate the secret key for encryption/decryption of the sensitive data.

Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [AuthenticationManager](vdi.AuthenticationManager.md) used to make the method call.
**spec**| [ClientKeyDerivationSpec](vdi.AuthenticationManager.ClientKeyDerivationSpec.md)|  The Key Derivation spec of the Client.




Return Value

Type |  Description
---|---
[ServerKeyDerivationInfo](vdi.AuthenticationManager.ServerKeyDerivationInfo.md)| Server Key Derivation Spec.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Login using supplied credentials.

Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [AuthenticationManager](vdi.AuthenticationManager.md) used to make the method call.
**username**|  xsd:string|  The username
**password**| [SecureString](vdi.util.SecureString.md)|  The password
**domain**|  xsd:string|  The domain




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







Login using supplied JWT token.

Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [AuthenticationManager](vdi.AuthenticationManager.md) used to make the method call.
**data**| [JwtTokenData](vdi.infrastructure.JwtToken.JwtTokenData.md)|  The token data.




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







Logout session.

Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [AuthenticationManager](vdi.AuthenticationManager.md) used to make the method call.



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







Used to specify the locale for the user messages. If locale is not set with this method, the messages will default to English language.

Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [AuthenticationManager](vdi.AuthenticationManager.md) used to make the method call.
**locale**|  xsd:string|  The locale of the user messages.<br>* This can take the values:<br><table><thead><tr><th>Value</th><th>Description</th></tr></thead><tbody><tr><td>de</td><td>German Language</td></tr><tr><td>en</td><td>English Language</td></tr><tr><td>es</td><td>Spanish Language</td></tr><tr><td>fr</td><td>French Language</td></tr><tr><td>ja</td><td>Japanese Language</td></tr><tr><td>ko</td><td>Korean Language</td></tr><tr><td>zh</td><td>Chinese Language</td></tr><tr><td>zh_TW</td><td>Chinese-Taiwan Language</td></tr></tbody></table>






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












 
