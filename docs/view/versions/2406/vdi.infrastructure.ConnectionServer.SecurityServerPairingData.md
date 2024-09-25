---
layout: page
title: Data Object - ConnectionServerSecurityServerPairingData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.ConnectionServer.SecurityServerPairingData
Property of
     [ConnectionServerInfo](vdi.infrastructure.ConnectionServer.ConnectionServerInfo.md#field_detail)
See also
     [SecureString](vdi.util.SecureString.md)
Since 
    Horizon View 6.0

## Data Object Description 

**Deprecated.**_This property is being deprecated since Security Server will no longer be supported in future releases. Please consider using Unified Access Gateway (UAG) instead._

The Security Server pairing data. 

  * This data object must be updated as a whole.



## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**pairingPassword**| [SecureString](vdi.util.SecureString.md)|  The Security Server pairing password.   
  
**timeoutMinutes**|  xsd:int|  The timeout of the pairing password (in minutes).   


  * This property has a minimum value of 1. 
  * This property has a maximum value of 1440. 

  
  

  

