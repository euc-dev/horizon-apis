---
layout: page
title: Data Object - ServerKeyDerivationInfo
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.AuthenticationManager  .ServerKeyDerivationInfo`

Returned by
> [AuthenticationManager_GenerateKeyMaterial](vdi.AuthenticationManager.md#generateKeyMaterial)

Since
> Horizon 8.4


## Data Object Description

Specification for Server's Key Derivation
 [^167]



## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**publicKey**|  xsd:string|  Base64 encoded Diffie Hellman public key
**proof**|  xsd:string|  Base64 encoded proof
**identifier**|  xsd:string|  Base64 encoded identifier
**algoSelected**|  xsd:string|  Selected algorithm for key derivation
* This property will be one of:
|  Value |  Description
---|---
"SCHEME-AES1"| Algo used by low power clients
"SCHEME-AES2"| Algo used by high power clients


 
