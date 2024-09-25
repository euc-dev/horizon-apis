---
layout: page
title: Data Object - ConnectionServerMessageSecurityData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.ConnectionServer.MessageSecurityData
Property of
     [ConnectionServerInfo](vdi.infrastructure.ConnectionServer.ConnectionServerInfo.md#field_detail)
Since 
    Horizon View 6.1

## Data Object Description 

The JMS message security data for the Connection Server. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**messageSecurityEnhancedModeSupported**|  xsd:boolean|  Indicates whether ENHANCED message security mode is currently supported by this Connection Server.   


[^2]

  
**routerSslThumbprints**|  xsd:string[]|  The JMS router SSL thumbprints  **_Since_** Horizon 7.7  


[^1]
  * This property is an unordered array of unique values.
[^2]

  
**msgSecurityPublicKey**|  xsd:string|  The JMS message security public key.  **_Since_** Horizon 7.9  


[^1]
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
