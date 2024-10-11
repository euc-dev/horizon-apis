---
layout: page
title: Data Object - SecurityServerInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.SecurityServer.SecurityServerInfo`

Returned by  
> [SecurityServer_Get](vdi.infrastructure.SecurityServer.md#get), [SecurityServer_List](vdi.infrastructure.SecurityServer.md#list)

See also  
> [SecurityServerGeneralData](vdi.infrastructure.SecurityServer.GeneralData.md), [SecurityServerId](vdi.entity.SecurityServerId.md), [SecurityServerMessageSecurityData](vdi.infrastructure.SecurityServer.MessageSecurityData.md)

Since  
> Horizon View 6.0


## Data Object Description 

**Deprecated.**_This is being deprecated since Security Server will no longer be supported in future releases. Please consider using Unified Access Gateway (UAG) instead._

Description of the security server 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**id**| [SecurityServerId](vdi.entity.SecurityServerId.md)|  Client reference to a specific security server   
  
**general**| [SecurityServerGeneralData](vdi.infrastructure.SecurityServer.GeneralData.md)|  General data for the security server   
  
**messageSecurity**| [SecurityServerMessageSecurityData](vdi.infrastructure.SecurityServer.MessageSecurityData.md)|  The message security data for the Security Server.  **_Since_** Horizon View 6.1  
  
  
  
 
  
  
