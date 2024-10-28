---
layout: page
title: Data Object - ViewClientInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.helpdesk.ViewClient.ViewClientInfo`

Returned by
> [ViewClient_Get](vdi.helpdesk.ViewClient.md#get)

Since
> Horizon 7.2


## Data Object Description

Information about View client.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**remoteIpAddress**|  xsd:string|  The uplink IP address of View client. It might be a public IP after NAT. [^1] [^2]
**ipAddress**|  xsd:string|  The local IP address detected by View client. [^1] [^2]
**loggedOnDomainName**|  xsd:string|  The domain name of the user logged on the endpoint machine. [^1] [^2]
**loggedOnUserName**|  xsd:string|  The user name of the user logged on the endpoint machine. [^1] [^2]
**macAddress**|  xsd:string|  The MAC address of the endpoint machine. [^1] [^2]
**domainName**|  xsd:string|  The domain name of the endpoint machine. [^1] [^2]
**machineName**|  xsd:string|  The machine name of the endpoint machine. [^1] [^2]
**type**|  xsd:string|  The type of the client installed on endpoint machine. [^1] [^2]
**brokerDnsName**|  xsd:string|  The DNS name of the connected connection server. [^1] [^2]
**version**|  xsd:string|  The version of horizon client.  **_Since_** Horizon 7.8 [^1] [^2]


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.