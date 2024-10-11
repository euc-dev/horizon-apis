---
layout: page
title: Data Object - ConnectionServerMessageSecurityData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.ConnectionServer.MessageSecurityData`

Property of  
> [ConnectionServerInfo](vdi.infrastructure.ConnectionServer.ConnectionServerInfo.md#field_detail)

Since  
> Horizon View 6.1


## Data Object Description 

The JMS message security data for the Connection Server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**messageSecurityEnhancedModeSupported**|  xsd:boolean|  Indicates whether ENHANCED message security mode is currently supported by this Connection Server.   


 * This property cannot be updated.

  
**routerSslThumbprints**|  xsd:string[]|  The JMS router SSL thumbprints  **_Since_** Horizon 7.7  


 * This property need not be set.
  * This property is an unordered array of unique values.
 * This property cannot be updated.

  
**msgSecurityPublicKey**|  xsd:string|  The JMS message security public key.  **_Since_** Horizon 7.9  


 * This property need not be set.
 * This property cannot be updated.

  
  

  
