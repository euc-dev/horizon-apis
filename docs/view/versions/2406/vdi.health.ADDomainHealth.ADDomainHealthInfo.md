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
**domainType**|  xsd:string|  The relationship of the domain with connection server.  **_Since_** Horizon 8.1 [^233] [^2]<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"CONNECTION_SERVER_DOMAIN"</td><td>The domain having trust with connection server domain.</td></tr><tr><td>"NO_TRUST_DOMAIN"</td><td>The domain not having any trust with connection server domain.</td></tr></table>
**serviceAccounts**| [ServiceAccount[]](vdi.health.ADDomainHealth.ServiceAccount.md)|  Service accounts for the domain.  **_Since_** Horizon 8.2 [^1] [^2]
**connectionServerState**| [ADDomainHealthConnectionServerConnectionData[]](vdi.health.ADDomainHealth.ConnectionServerConnectionData.md)|  The status of the connection to the domain for each connection server.









[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^233]: This property has a default value of "CONNECTION_SERVER_DOMAIN".