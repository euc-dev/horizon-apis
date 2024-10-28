---
layout: page
title: Data Object - ADDomainSpec
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.ADDomain.ADDomainSpec`

See also
> [ADDomainAdvancedSettings](vdi.utils.ADDomain.ADDomainAdvancedSettings.md), [ServiceAccountCredentials](vdi.utils.ADDomain.ServiceAccountCredentials.md)

Since
> Horizon 8.1


## Data Object Description

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**dnsName**|  xsd:string|  The DNS name of the domain. [^141]
**netBiosName**|  xsd:string|  The NetBIOS name of the domain.
**primaryAccount**| [ServiceAccountCredentials](vdi.utils.ADDomain.ServiceAccountCredentials.md)|  Primary service account credentials.
**adDomainAdvancedSettings**| [ADDomainAdvancedSettings](vdi.utils.ADDomain.ADDomainAdvancedSettings.md)|  Advanced information of no trust domain.


 


[^141]: This property must be a valid DNS name.