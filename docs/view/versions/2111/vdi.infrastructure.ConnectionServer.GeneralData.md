---
layout: page
title: Data Object - ConnectionServerGeneralData
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.infrastructure.ConnectionServer.GeneralData`

Property of
> [ConnectionServerInfo](vdi.infrastructure.ConnectionServer.ConnectionServerInfo.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

The General Configuration for the Connection Server.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**name**|  xsd:string|  Name of the connection server [^2]
**serverAddress**|  xsd:string|  General URL for the connection server. [^2]
**enabled**|  xsd:boolean|  Indicate whether the connection server is enabled. A disabled connection server will not accept connection requests from View Clients.
**tags**|  xsd:string[]|  Tags to restrict accessibility to desktops through this server. [^1] [^14]
**externalURL**|  xsd:string|  View Clients use the External URL to establish a secure tunnel to this Connection Server instance. If a server name is specified, it must be resolvable by each View Client. The External URL must not be load balanced. <br>If [bypassTunnel](vdi.infrastructure.ConnectionServer.GeneralData.md#bypassTunnel) is set to true, this is ignored.<br>This should be in the form "<(DNS name)|(IPv4)|(IPv6)><:(port)>". IPv6 addresses must be enclosed in square brackets. [^1]
**externalPCoIPURL**|  xsd:string|  View Clients use the PCoIP External URL to establish a PCoIP connection through this Connection Server instance. The PCoIP External URL must not be load balanced.<br>If [bypassPCoIPGateway](vdi.infrastructure.ConnectionServer.GeneralData.md#bypassPCoIPGateway) is set to true, this is ignored. <br>This should be in the form "<(DNS name)|(IPv4)|(IPv6)>[:(port encoding)]". The port encoding part may be omitted, may specify a single port to represent both the TCP and UDP ports, or may specify them individually in the form "(TCP port)?(UDP port)". Unspecified ports default to 4172. IPv6 addresses must be enclosed in square brackets. [^1]
**hasPCoIPGatewaySupport**|  xsd:boolean|  Whether PCoIP gateway is supported or not.  **_Since_** Horizon 7.8 [^2]
**hasBlastGatewaySupport**|  xsd:boolean|  Whether Blast gateway is supported or not.  **_Since_** Horizon 7.8 [^2]
**auxillaryExternalPCoIPIPv4Address**|  xsd:string|  This can only be set if [externalPCoIPURL](vdi.infrastructure.ConnectionServer.GeneralData.md#externalPCoIPURL) is set and contains a host part that represents an IPv6 address or DNS name. As legacy clients may not support IPv6 or DNS names for external PCoIP URLs, this IPv4 address, if set, will be presented to them as an alternative. The same port will be used and should not be specified.<br>If [bypassPCoIPGateway](vdi.infrastructure.ConnectionServer.GeneralData.md#bypassPCoIPGateway) is set to true, this is ignored.  **_Since_** Horizon View 6.1 [^1]
**externalAppblastURL**|  xsd:string|  The Blast External URL enables browser access to View machines through this Connection Server instance. To enable Blast, you must install HTML Access.<br>The Blast External URL must not be load balanced.<br>If [bypassAppBlastGateway](vdi.infrastructure.ConnectionServer.GeneralData.md#bypassAppBlastGateway) is set to true, this is ignored.<br>This should be in the form "<(DNS name)|(IPv4)|(IPv6)>[:(port)]". Unspecified ports default to 8443. IPv6 addresses must be enclosed in square brackets. [^1]
**localConnectionServer**|  xsd:boolean|  Indicates whether this is the local connection server that handled the ConnectionServer service request.  **_Since_** Horizon 7.4 [^1] [^2]
**bypassTunnel**|  xsd:boolean|  Setting this to false enables a secure tunnel on this Connection Server instance.<br>If this is set to false, View Clients connect to desktops through the secure tunnel, which carries RDP and other data over HTTPS. PCoIP and HTML Access connections use separate secure gateways.
**bypassPCoIPGateway**|  xsd:boolean|  Whether the PCoIP traffic bypasses the secure gateway.
**bypassAppBlastGateway**|  xsd:boolean|  Setting this to false enables clients that browse to View machines to use the Blast Secure Gateway to establish a secure tunnel to this Connection Server instance.<br>If this is set to true, web browsers make direct connections to View machines, bypassing Connection Server.
**directHTMLABSG**|  xsd:boolean|  Setting this to true enables only html clients that browse to view machines to use Blast Secure Gateway to establish a secure tunnel to this Connection Server instance.<br>If [bypassAppBlastGateway](vdi.infrastructure.ConnectionServer.GeneralData.md#bypassAppBlastGateway) is set to false, this is ignored.  **_Since_** Horizon 7.7 [^5] [^1]
**version**|  xsd:string|  'Version number' attribute to indicate functionalities supported by current connection server. [^2]
**ipMode**|  xsd:string|  Indicates the Connection Server IP environment.  **_Since_** Horizon 7.6 [^1] [^2]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"IPv4"</td><td>This Connection Server is running in IPv4 environment.</td></tr><tr><td>"IPv6"</td><td>This Connection Server is running in IPv6 environment.</td></tr></table>
**fipsModeEnabled**|  xsd:boolean|  Indicates whether this server has FIPS mode enabled.  **_Since_** Horizon 7.6 [^5] [^1] [^2]
**fqhn**|  xsd:string|  Fully qualified host name  **_Since_** Horizon 7.6 [^2]
**clusterName**|  xsd:string|  Cluster name  **_Since_** Horizon 7.10 [^2]
**discloseServicePrincipalName**|  xsd:boolean|  Indicates whether the connection server's service principal name will be sent to the client prior to the user authentication. When set to true Connection Server discloses its service principal name to the client.  **_Since_** Horizon 7.10 [^5] [^1]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^5]: This property has a default value of false.
[^14]: This property is an unordered array of unique values.