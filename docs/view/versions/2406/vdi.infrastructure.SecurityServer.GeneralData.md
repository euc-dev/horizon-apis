---
layout: page
title: Data Object - SecurityServerGeneralData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.SecurityServer.GeneralData`

Property of
> [SecurityServerInfo](vdi.infrastructure.SecurityServer.SecurityServerInfo.md#field_detail)

See also
> [ConnectionServerId](vdi.entity.ConnectionServerId.md)

Since
> Horizon View 6.0


## Data Object Description

**Deprecated.**_This property is being deprecated since Security Server will no longer be supported in future releases. Please consider using Unified Access Gateway (UAG) instead._

Security server data

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**name**|  xsd:string|  Name of the security server [^2]
**serverAddress**|  xsd:string|  General URL for the security server. [^2]
**connectionServer**| [ConnectionServerId](vdi.entity.ConnectionServerId.md)|  Connection server paired with this security server [^2]
**version**|  xsd:string|  Version of the security server. [^1] [^2]
**connectionServerName**|  xsd:string|  Name of the connection server paired with this security server [^2]
**pcoipSecureGatewayInstalled**|  xsd:boolean|  Whether or not PCoIP secure gateway is installed [^2]
**externalURL**|  xsd:string|  View Clients use the External URL to establish a secure tunnel to this Security Server instance. If a server name is specified, it must be resolvable by each View Client. The External URL must not be load balanced. <br>If [bypassTunnel](vdi.infrastructure.ConnectionServer.GeneralData.md#bypassTunnel) on this Security Server's paired Connection Server is set to true, this is ignored. <br>This should be in the form "<(DNS name)|(IPv4)|(IPv6)><:(port)>". IPv6 addresses must be enclosed in square brackets. [^1]
**externalPCoIPURL**|  xsd:string|  View Clients use the PCoIP External URL to establish a PCoIP connection through this Connection Server instance. The PCoIP External URL must not be load balanced. <br>If [bypassPCoIPGateway](vdi.infrastructure.ConnectionServer.GeneralData.md#bypassPCoIPGateway) on this Security Server's paired Connection Server is set to true, this is ignored. <br>This should be in the form "<(DNS name)|(IPv4)|(IPv6)>[:(port encoding)]". The port encoding part may be omitted, may specify a single port to represent both the TCP and UDP ports, or may specify them individually in the form "(TCP port)?(UDP port)". Unspecified ports default to 4172. IPv6 addresses must be enclosed in square brackets. [^1]
**auxillaryExternalPCoIPIPv4Address**|  xsd:string|  This can only be set if [externalPCoIPURL](vdi.infrastructure.SecurityServer.GeneralData.md#externalPCoIPURL) is set and contains a host part that represents an IPv6 address or DNS name. As legacy clients may not support IPv6 or DNS names for external PCoIP URLs, this IPv4 address, if set, will be presented to them as an alternative. The same port will be used and should not be specified.<br>If [bypassPCoIPGateway](vdi.infrastructure.ConnectionServer.GeneralData.md#bypassPCoIPGateway) on this Security Server's paired Connection Server is set to true, this is ignored.  **_Since_** Horizon View 6.1 [^1]
**externalAppblastURL**|  xsd:string|  The Blast External URL enables browser access to View machines through this Connection Server instance or a paired security server. To enable Blast, you must install HTML Access. The Blast External URL must not be load balanced.<br>* If [bypassAppBlastGateway](vdi.infrastructure.ConnectionServer.GeneralData.md#bypassAppBlastGateway) on this Security Server's paired Connection Server is set to true, this is ignored.<br>This should be in the form "<(DNS name)|(IPv4)|(IPv6)>[:(port)]". Unspecified ports default to 8443. IPv6 addresses must be enclosed in square brackets. [^1]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.