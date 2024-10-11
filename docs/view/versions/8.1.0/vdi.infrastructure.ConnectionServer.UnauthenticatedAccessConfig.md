---
layout: page
title: Data Object - UnauthenticatedAccessConfig
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.ConnectionServer.UnauthenticatedAccessConfig`

Property of  
> [ConnectionServerAuthenticationData](vdi.infrastructure.ConnectionServer.AuthenticationData.md#field_detail)

See also  
> [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since  
> Horizon 7.1


## Data Object Description 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**enabled**|  xsd:boolean|  Indicates whether unauthenticated access is enabled in this connection server.   
  
**defaultUser**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  Default user for unauthenticated access in this connection server. It is optional when the unauthenticated access is being enabled and no unauthenticated access users were created.   


* This property need not be set.

  
**userIdleTimeout**|  xsd:int|  Unauthenticated Access user idle session timeout in minutes. The default value is 10 minutes.   


  * This property has a default value of 10.
* This property need not be set.

  
**clientPuzzleDifficulty**|  xsd:int|  Client puzzle difficulty for DoS attack prevention for Unauthenticated Access. Higher difficulty might increase login time and affect user experience. The default value is 21.  **_Since_** Horizon 7.6  


  * This property has a default value of 21.
* This property need not be set.
  * This property has a minimum value of 14. 
  * This property has a maximum value of 31. 

  
**blockUnsupportedClients**|  xsd:boolean|  Block older clients which don't support client puzzles to prevent DOS attack on RDSH servers for Unauthenticated Access. The default value is false.  **_Since_** Horizon 7.6  


  * This property has a default value of false.
* This property need not be set.

  
  
  
  
  
  
