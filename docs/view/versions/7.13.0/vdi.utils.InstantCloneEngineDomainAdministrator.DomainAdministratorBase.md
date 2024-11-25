---
layout: page
title: Data Object - InstantCloneEngineDomainAdministratorBase
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.InstantCloneEngineDomainAdministrator.DomainAdministratorBase`

Property of
> [InstantCloneEngineDomainAdministratorInfo](vdi.utils.InstantCloneEngineDomainAdministrator.InstantCloneEngineDomainAdministratorInfo.md#field_detail), [InstantCloneEngineDomainAdministratorSpec](vdi.utils.InstantCloneEngineDomainAdministrator.InstantCloneEngineDomainAdministratorSpec.md#field_detail)

See also
> [ADDomainId](vdi.entity.ADDomainId.md), [SecureString](vdi.util.SecureString.md)

Since
> Horizon 7.0


## Data Object Description

Basic data about a instant clone engine domain administrator.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**domain**| [ADDomainId](vdi.entity.ADDomainId.md)|  Domain Id for the domain administrator account. [^2]
**userName**|  xsd:string|  Logon user name. This user must not be associated with another instant clone domain administrator on the same domain. [^2] [^152]
**password**| [SecureString](vdi.util.SecureString.md)|  Logon password.


 


[^2]: This property cannot be updated.
[^152]: This property must not be empty and has a maximum length of 256 characters.