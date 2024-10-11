---
layout: page
title: Data Object - ConnectionServerWorkspaceOneData
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.ConnectionServer.WorkspaceOneData`

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
**workspaceOneModeEnabled**|  xsd:boolean|  Whether Workspace ONE mode is enabled.   


  * This property has a default value of false.
* This property need not be set.

  
**workspaceOneHostName**|  xsd:string|  The hostname of the Workspace ONE Server.   


* This property need not be set.
  * This property is required if workspaceOneModeEnabled is set to true.

  
**workspaceOneBlockOldClients**|  xsd:boolean|  Block old clients that don't support Workspace ONE mode   


  * This property has a default value of false.
* This property need not be set.

  
  
  
 
  
  
