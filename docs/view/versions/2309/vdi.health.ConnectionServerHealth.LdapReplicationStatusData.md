---
layout: page
title: Data Object - ConnectionServerHealthLdapReplicationStatusData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.health.ConnectionServerHealth.LdapReplicationStatusData`

Property of
> [ConnectionServerHealthInfo](vdi.health.ConnectionServerHealth.ConnectionServerHealthInfo.md#field_detail)

Since
> Horizon 7.10


## Data Object Description

Information about the LDAP replication status of the Connection Server.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**serverName**|  xsd:string|  Replica Server name.
**status**|  xsd:string|  Status of the server.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"OK"</td><td>The connection to the connection server is working properly.</td></tr><tr><td>"ERROR"</td><td>Error occurred when connecting to connection server.</td></tr></table>
**message**|  xsd:string|  Status message. [^1]
 


 
