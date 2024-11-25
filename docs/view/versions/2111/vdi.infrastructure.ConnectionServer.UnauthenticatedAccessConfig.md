---
layout: page
title: Data Object - UnauthenticatedAccessConfig
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.infrastructure.ConnectionServer.UnauthenticatedAccessConfig`

Property of
> [ConnectionServerAuthenticationData](vdi.infrastructure.ConnectionServer.AuthenticationData.md#field_detail)

See also
> [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon 7.1


## Data Object Description

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**enabled**|  xsd:boolean|  Indicates whether unauthenticated access is enabled in this connection server.
**defaultUser**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  Default user for unauthenticated access in this connection server. It is optional when the unauthenticated access is being enabled and no unauthenticated access users were created. [^1]
**userIdleTimeout**|  xsd:int|  Unauthenticated Access user idle session timeout in minutes. The default value is 10 minutes. [^45] [^1]
**clientPuzzleDifficulty**|  xsd:int|  Client puzzle difficulty for DoS attack prevention for Unauthenticated Access. Higher difficulty might increase login time and affect user experience. The default value is 21.  **_Since_** Horizon 7.6 [^254] [^1] [^255] [^119]
**blockUnsupportedClients**|  xsd:boolean|  Block older clients which don't support client puzzles to prevent DOS attack on RDSH servers for Unauthenticated Access. The default value is false.  **_Since_** Horizon 7.6 [^5] [^1]


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.
[^45]: This property has a default value of 10.
[^119]: This property has a maximum value of 31.
[^254]: This property has a default value of 21.
[^255]: This property has a minimum value of 14.