---
layout: page
title: Data Object - ADUserCredentialSpec
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.ADUserOrGroup.ADUserCredentialSpec
Parameter to
     [ADUserOrGroup_ValidateCredentials](vdi.users.ADUserOrGroup.md#validateCredentials)
See also
     [SecureString](vdi.util.SecureString.md)
Since 
    Horizon 7.7

## Data Object Description 

AD User Credential 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**domain**|  xsd:string|  The domain of user. Note that domain is optional if UPN is supplied.   


[^1]

  
**username**|  xsd:string|  The username or UPN.   
  
**password**| [SecureString](vdi.util.SecureString.md)|  The password.   
  
**protectedPasswordKey**|  xsd:string|  Decryption key for the password. This key is itself encrypted with cluster's SSO keypair. Pls note that if this key is specified, it means password is sent in encrypted form else it is in plain text.  **_Since_** Horizon 7.11  


[^1]

  
**keyId**|  xsd:string|  The keyId of the cluster's SSO KeyPair used to encrypt the [protectedPasswordKey](vdi.users.ADUserOrGroup.ADUserCredentialSpec.md#protectedPasswordKey). Pls note that this is required if [protectedPasswordKey](vdi.users.ADUserOrGroup.ADUserCredentialSpec.md#protectedPasswordKey) is specified.  **_Since_** Horizon 7.11  


[^1]

  
  

  

