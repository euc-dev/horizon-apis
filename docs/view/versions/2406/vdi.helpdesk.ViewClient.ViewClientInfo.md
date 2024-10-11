---
layout: page
title: Data Object - ViewClientInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.helpdesk.ViewClient.ViewClientInfo`

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
**remoteIpAddress**|  xsd:string|  The uplink IP address of View client. It might be a public IP after NAT.   


 * This property need not be set.
 * This property cannot be updated.

  
**ipAddress**|  xsd:string|  The local IP address detected by View client.   


 * This property need not be set.
 * This property cannot be updated.

  
**loggedOnDomainName**|  xsd:string|  The domain name of the user logged on the endpoint machine.   


 * This property need not be set.
 * This property cannot be updated.

  
**loggedOnUserName**|  xsd:string|  The user name of the user logged on the endpoint machine.   


 * This property need not be set.
 * This property cannot be updated.

  
**macAddress**|  xsd:string|  The MAC address of the endpoint machine.   


 * This property need not be set.
 * This property cannot be updated.

  
**domainName**|  xsd:string|  The domain name of the endpoint machine.   


 * This property need not be set.
 * This property cannot be updated.

  
**machineName**|  xsd:string|  The machine name of the endpoint machine.   


 * This property need not be set.
 * This property cannot be updated.

  
**type**|  xsd:string|  The type of the client installed on endpoint machine.   


 * This property need not be set.
 * This property cannot be updated.

  
**brokerDnsName**|  xsd:string|  The DNS name of the connected connection server.   


 * This property need not be set.
 * This property cannot be updated.

  
**version**|  xsd:string|  The version of horizon client.  **_Since_** Horizon 7.8  


 * This property need not be set.
 * This property cannot be updated.

  
  

  
