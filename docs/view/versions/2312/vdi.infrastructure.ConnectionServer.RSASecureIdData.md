---
layout: page
title: Data Object - ConnectionServerRSASecureIdData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.ConnectionServer.RSASecureIdData`

Property of  
> [ConnectionServerAuthenticationData](vdi.infrastructure.ConnectionServer.AuthenticationData.md#field_detail)

Since  
> Horizon View 6.0


## Data Object Description 

The RSA SecurID settings for authentication to a connection server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**secureIdEnabled**|  xsd:boolean|  Whether SecurID authentication is required.   
  
**nameMapping**|  xsd:boolean|  Indicates how SecurID names map to AD usernames. It is False for not mapped.   


 * This property need not be set.

  
**clearNodeSecret**|  xsd:boolean|  When set to 1 the SecurID Node Secret is cleared   


 * This property need not be set.

  
**securityFileData**|  xsd:base64Binary|  Binary contents of the SecurID sdconf.rec file   


 * This property need not be set.

  
**securityFileUploaded**|  xsd:boolean|  If SecurID sdconf.rec file is already uploaded. The client can never download the file.   


 * This property cannot be updated.

  
  
  
   
  
  
