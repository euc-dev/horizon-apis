---
layout: page
title: Data Object - InstantCloneEngineDomainAdministratorInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.utils.InstantCloneEngineDomainAdministrator.InstantCloneEngineDomainAdministratorInfo`

Returned by
> [InstantCloneEngineDomainAdministrator_Get](vdi.utils.InstantCloneEngineDomainAdministrator.md#get), [InstantCloneEngineDomainAdministrator_List](vdi.utils.InstantCloneEngineDomainAdministrator.md#list)

See also
> [InstantCloneEngineDomainAdministratorBase](vdi.utils.InstantCloneEngineDomainAdministrator.DomainAdministratorBase.md), [InstantCloneEngineDomainAdministratorId](vdi.entity.InstantCloneEngineDomainAdministratorId.md), [InstantCloneEngineDomainAdministratorNamesData](vdi.utils.InstantCloneEngineDomainAdministrator.DomainAdministratorNamesData.md)

Since
> Horizon 7.0


## Data Object Description

Top level object describing Instant Clone Engine domain administrator.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [InstantCloneEngineDomainAdministratorId](vdi.entity.InstantCloneEngineDomainAdministratorId.md)|  Entity id for the Instant Clone Engine domain administrator. [^2]
**siteName**|  xsd:string|  Name of the default AD Site.  **_Since_** Horizon 8.9 [^1] [^2]
**base**| [InstantCloneEngineDomainAdministratorBase](vdi.utils.InstantCloneEngineDomainAdministrator.DomainAdministratorBase.md)|  Basic data about Instant Clone Engine domain administrator.
**namesData**| [InstantCloneEngineDomainAdministratorNamesData](vdi.utils.InstantCloneEngineDomainAdministrator.DomainAdministratorNamesData.md)|  Additional data about Instant Clone Engine domain administrator. [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.