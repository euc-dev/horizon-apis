---
layout: page
title: Data Object - ConnectionServerWorkspaceOneData
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.infrastructure.ConnectionServer.WorkspaceOneData`

Property of
> [ConnectionServerSAMLData](vdi.infrastructure.ConnectionServer.SAMLData.md#field_detail)

Since
> Horizon 7.2


## Data Object Description

The Workspace ONE data for the connection server.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**workspaceOneModeEnabled**|  xsd:boolean|  Whether Workspace ONE mode is enabled. [^5] [^1]
**workspaceOneHostName**|  xsd:string|  The hostname of the Workspace ONE Server. [^1] [^256]
**workspaceOneBlockOldClients**|  xsd:boolean|  Block old clients that don't support Workspace ONE mode [^5] [^1]
 


 


[^1]: This property need not be set.
[^5]: This property has a default value of false.
[^256]: This property is required if workspaceOneModeEnabled is set to true.