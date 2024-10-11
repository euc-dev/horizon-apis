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
> [ADDomainHealthConnectionServerConnectionData](vdi.health.ADDomainHealth.ConnectionServerConnectionData.md)

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
  
**connectionServerState**| [ADDomainHealthConnectionServerConnectionData[]](vdi.health.ADDomainHealth.ConnectionServerConnectionData.md)|  The status of the connection to the domain for each connection server.   
  
  
  

  
  
