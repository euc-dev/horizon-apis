---
layout: page
title: Fault - InvalidDomainCredentials
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.fault.InvalidDomainCredentials`

Extends
> [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)

See also
> [ADDomainId](vdi.entity.ADDomainId.md), [EntityId](vdi.EntityId.md)

Since
> Horizon View 6.0


## Fault Description

Thrown if the caller does not have the correct secondary credentials to access a one-way trusted domain.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [EntityId](vdi.EntityId.md)|  Entity, if any, whose access caused the error. [^1]
**domain**| [ADDomainId](vdi.entity.ADDomainId.md)|  Domain that caused the error, if known. [^1]
**netbiosDomainName**|  xsd:string|  Netbios domain name of domain that caused the error, if known. [^1]
**dnsDomainName**|  xsd:string|  DNS domain name of domain that caused the error, if known. [^1]
Properties inherited from [ViewRuntimeFault](vdi.fault.ViewRuntimeFault.md)
[errorMessage](vdi.fault.ViewRuntimeFault.md#errorMessage)
Properties inherited from [RuntimeFault](vmodl.RuntimeFault.md)
None
Properties inherited from [MethodFault](vmodl.MethodFault.md)
None


 


[^1]: This property need not be set.