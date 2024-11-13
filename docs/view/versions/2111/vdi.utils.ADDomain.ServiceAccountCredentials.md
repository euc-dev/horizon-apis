---
layout: page
title: Data Object - ServiceAccountCredentials
hide:
#- navigation
- toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.ADDomain.ServiceAccountCredentials`

Property of
> [ADDomainAuxiliaryAccountSpec](vdi.utils.ADDomain.ADDomainAuxiliaryAccountSpec.md#field_detail), [ADDomainInfo](vdi.utils.ADDomain.ADDomainInfo.md#field_detail), [ADDomainSpec](vdi.utils.ADDomain.ADDomainSpec.md#field_detail), [ServiceAccountCredentialsInfo](vdi.utils.ADDomain.ServiceAccountCredentialsInfo.md#field_detail)

See also
> [SecureString](vdi.util.SecureString.md)

Since
> Horizon 8.1


## Data Object Description

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**username**|  xsd:string|  service account username. [^152]
**password**| [SecureString](vdi.util.SecureString.md)|  Service account user password.


 


[^152]: This property must not be empty and has a maximum length of 256 characters.