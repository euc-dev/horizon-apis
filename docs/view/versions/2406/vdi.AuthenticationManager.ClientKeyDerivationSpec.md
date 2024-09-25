---
layout: page
title: Data Object - ClientKeyDerivationSpec
hide:
 #- navigation
 - toc
---



Java Class
    com.vmware.vdi.vlsi.binding.vdi.AuthenticationManager.ClientKeyDerivationSpec
Parameter to
     [AuthenticationManager_GenerateKeyMaterial](vdi.AuthenticationManager.md#generateKeyMaterial)
Since 
    Horizon 8.4

## Data Object Description 

Specification for Client's Key Derivation 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**publicKey**|  xsd:string|  Base64 encoded Diffie Hellman/Elliptic-curve Diffie Hellman public key   
  
**nonce**|  xsd:string|  Base64 encoded nonce   
  
**identifier**|  xsd:string|  Base64 encoded identifier   
  
**algoRequested**|  xsd:string[]|  List of client requested algorithms for key derivation   


  * This property will be one of:  
|  Value |  Description   
---|---  
"SCHEME-AES1"| Diffie Hellman algo used by low power clients  
"SCHEME-AES2"| Diffie Hellman algo used by high power clients  
"SCHEME-EC-AES1"| Elliptic-curve Diffie Hellman algo used by low power clients  
"SCHEME-EC-AES2"| Elliptic-curve Diffie Hellman algo used by high power clients  

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

