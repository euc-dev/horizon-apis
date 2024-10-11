---
layout: page
title: Data Object - ADDomainHealthInfo
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.health.ADDomainHealth.ADDomainHealthInfo`

Returned by  
> [ADDomainHealth_List](vdi.health.ADDomainHealth.md#list)

See also  
> [ADDomainHealthConnectionServerConnectionData](vdi.health.ADDomainHealth.ConnectionServerConnectionData.md), [ServiceAccount](vdi.health.ADDomainHealth.ServiceAccount.md)

Since  
> Horizon View 6.0


## Data Object Description 

The health information on a single domain. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**netBiosName**|  xsd:string|  The NetBIOS name for the domain.   
  
**dnsName**|  xsd:string|  The DNS name for the domain.   
  
**nt4Domain**|  xsd:boolean|  Is this an NT4 domain?   
  
**domainType**|  xsd:string|  The relationship of the domain with connection server.  **_Since_** Horizon 8.1  


  * This property has a default value of "CONNECTION_SERVER_DOMAIN".
* This property cannot be updated.
  * This property will be one of:  
|  Value |  Description   
---|---  
"CONNECTION_SERVER_DOMAIN"| The domain having trust with connection server domain.  
"NO_TRUST_DOMAIN"| The domain not having any trust with connection server domain.  

  
**serviceAccounts**| [ServiceAccount[]](vdi.health.ADDomainHealth.ServiceAccount.md)|  Service accounts for the domain.  **_Since_** Horizon 8.2  


* This property need not be set.
* This property cannot be updated.

  
**connectionServerState**| [ADDomainHealthConnectionServerConnectionData[]](vdi.health.ADDomainHealth.ConnectionServerConnectionData.md)|  The status of the connection to the domain for each connection server.   
  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
