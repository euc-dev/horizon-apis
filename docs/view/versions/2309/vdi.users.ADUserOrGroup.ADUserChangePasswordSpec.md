---
layout: page
title: Data Object - ADUserChangePasswordSpec
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.ADUserOrGroup.ADUserChangePasswordSpec`

See also
> [SecureString](vdi.util.SecureString.md)

Since
> Horizon 7.11


## Data Object Description

AD User change password

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**domain**|  xsd:string|  The domain of user. Note that domain is optional if UPN is supplied. [^1]
**username**|  xsd:string|  The username or UPN.
**oldPassword**| [SecureString](vdi.util.SecureString.md)|  Old password.
**newPassword**| [SecureString](vdi.util.SecureString.md)|  New password.
**protectedPasswordKey**|  xsd:string|  Decryption key for the password. This key is itself encrypted with cluster's SSO keypair. Pls note that if this key is specified, it means passwords are sent in encrypted form else it is in plain text. [^1]
**keyId**|  xsd:string|  The keyId of the cluster's SSO KeyPair used to encrypt the [protectedPasswordKey](vdi.users.ADUserOrGroup.ADUserChangePasswordSpec.md#protectedPasswordKey). Pls note that this is required if [protectedPasswordKey](vdi.users.ADUserOrGroup.ADUserChangePasswordSpec.md#protectedPasswordKey) is specified. [^1]
 


 


[^1]: This property need not be set.