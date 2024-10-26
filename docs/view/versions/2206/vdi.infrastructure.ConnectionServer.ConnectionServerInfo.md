---
layout: page
title: Data Object - ConnectionServerInfo
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.ConnectionServer.ConnectionServerInfo`

Returned by
> [ConnectionServer_Get](vdi.infrastructure.ConnectionServer.md#get), [ConnectionServer_List](vdi.infrastructure.ConnectionServer.md#list)

See also
> [ConnectionServerAuthenticationData](vdi.infrastructure.ConnectionServer.AuthenticationData.md), [ConnectionServerBackupData](vdi.infrastructure.ConnectionServer.BackupData.md), [ConnectionServerGeneralData](vdi.infrastructure.ConnectionServer.GeneralData.md), [ConnectionServerId](vdi.entity.ConnectionServerId.md), [ConnectionServerMessageSecurityData](vdi.infrastructure.ConnectionServer.MessageSecurityData.md), [ConnectionServerSecurityServerPairingData](vdi.infrastructure.ConnectionServer.SecurityServerPairingData.md)

Since
> Horizon View 6.0


## Data Object Description

Description of the Connection Server.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [ConnectionServerId](vdi.entity.ConnectionServerId.md)|  Client reference to a specified Connection Server. [^2]
**general**| [ConnectionServerGeneralData](vdi.infrastructure.ConnectionServer.GeneralData.md)|  General Settings for the Connection Server.
**authentication**| [ConnectionServerAuthenticationData](vdi.infrastructure.ConnectionServer.AuthenticationData.md)|  Authentication Settings for the Connection Server.
**backup**| [ConnectionServerBackupData](vdi.infrastructure.ConnectionServer.BackupData.md)|  Backup Settings for the Connection Server.
**securityServerPairing**| [ConnectionServerSecurityServerPairingData](vdi.infrastructure.ConnectionServer.SecurityServerPairingData.md)| **Deprecated.**_This property is being deprecated since Security Server will no longer be supported in future releases. Please consider using Unified Access Gateway (UAG) instead._ Security Server pairing data for the Connection Server. [^1]
**messageSecurity**| [ConnectionServerMessageSecurityData](vdi.infrastructure.ConnectionServer.MessageSecurityData.md)|  The message security data for the Connection Server.  **_Since_** Horizon View 6.1


 
