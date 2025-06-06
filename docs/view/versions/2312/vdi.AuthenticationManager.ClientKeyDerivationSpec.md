---
layout: page
title: Data Object - ClientKeyDerivationSpec
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.AuthenticationManager  .ClientKeyDerivationSpec`

Parameter to
> [AuthenticationManager_GenerateKeyMaterial](vdi.AuthenticationManager.md#generateKeyMaterial)

Since
> Horizon 8.4


## Data Object Description

Specification for Client's Key Derivation
 [^167]



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**publicKey**|  xsd:string|  Base64 encoded Diffie Hellman/Elliptic-curve Diffie Hellman public key
**nonce**|  xsd:string|  Base64 encoded nonce
**identifier**|  xsd:string|  Base64 encoded identifier
**algoRequested**|  xsd:string[]|  List of client requested algorithms for key derivation<br>* This property will be one of:<br><table><thead><tr><th>Value</th><th>Description</th></tr></thead><tbody><tr><td>"SCHEME-AES1"</td><td>Diffie Hellman algo used by low power clients</td></tr><tr><td>"SCHEME-AES2"</td><td>Diffie Hellman algo used by high power clients</td></tr><tr><td>"SCHEME-EC-AES1"</td><td>Elliptic-curve Diffie Hellman algo used by low power clients</td></tr><tr><td>"SCHEME-EC-AES2"</td><td>Elliptic-curve Diffie Hellman algo used by high power clients</td></tr></tbody></table>


 


[^167]: This data object must be updated as a whole.