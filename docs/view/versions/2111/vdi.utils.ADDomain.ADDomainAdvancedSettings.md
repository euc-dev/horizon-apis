---
layout: page
title: Data Object - ADDomainAdvancedSettings
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.ADDomain.ADDomainAdvancedSettings`

Property of
> [ADDomainInfo](vdi.utils.ADDomain.ADDomainInfo.md#field_detail), [ADDomainSpec](vdi.utils.ADDomain.ADDomainSpec.md#field_detail)

Since
> Horizon 8.1


## Data Object Description

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**port**|  xsd:int|  Port of the server to connect to. [^72] [^189]
**adDomainContext**|  xsd:string|  Active directory domain Context. e.g: dc=abc,dc=com.
**adDomainAutoDiscovery**|  xsd:boolean|  Auto discovers domain controllers . Auto discovery, AD domain controllers and preferred site name are mutually exclusive. Only one of them can be defined at a time. [^6]
**adDomainControllers**|  xsd:string[]|  One or more AD domain controllers. Auto discovery, AD domain controllers and preferred site name are mutually exclusive. Only one of them can be defined at a time. [^1] [^140]
**adDomainPreferredSite**|  xsd:string|  ADDomain preferred domain site. Auto discovery, AD domain controllers and preferred site name are mutually exclusive. Only one of them can be defined at a time. [^1]


 


[^1]: This property need not be set.
[^6]: This property has a default value of true.
[^72]: This property has a minimum value of 0.
[^140]: This property must be a valid IP address or DNS name.
[^189]: This property has a maximum value of 65535.