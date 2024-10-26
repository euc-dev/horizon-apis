---
layout: page
title: Data Object - MessageClientInfo
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.utils.MessageClient.MessageClientInfo`

Returned by
> [MessageClient_Create](vdi.utils.MessageClient.md#create), [MessageClient_Delete](vdi.utils.MessageClient.md#delete), [MessageClient_Get](vdi.utils.MessageClient.md#get), [MessageClient_Update](vdi.utils.MessageClient.md#update)

See also
> [MessageClientId](vdi.entity.MessageClientId.md)

Since
> Horizon 7.7


## Data Object Description

Information describing the message client.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [MessageClientId](vdi.entity.MessageClientId.md)|  The identity of the client. [^2]
**clientType**|  xsd:string|  The type of the client. [^2] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"csms"</td><td>Message Client is csms. CSMS, abbreviation for Connection Server Monitor Service, runs on Cloud Connector Appliance. It collects messages from Desktop Agent from all Desktop and RDSH servers, and forward them to Cloud Monitoring Service.</td></tr></table>
**pemCertificates**|  xsd:string[]|  The client certificates in PEM format. [^2]
 


 


[^2]: This property cannot be updated.