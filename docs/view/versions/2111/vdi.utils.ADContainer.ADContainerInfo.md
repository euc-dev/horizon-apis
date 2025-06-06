---
layout: page
title: Data Object - ADContainerInfo
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.ADContainer.ADContainerInfo`

Returned by
> [ADContainer_ListByDomain](vdi.utils.ADContainer.md#listByDomain), [ADContainer_ListByViewComposerDomainAdministrator](vdi.utils.ADContainer.md#listByViewComposerDomainAdministrator)

See also
> [ADContainerId](vdi.entity.ADContainerId.md)

Since
> Horizon View 6.0


## Data Object Description

Information about an active directory container.
 [^167]



## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**id**| [ADContainerId](vdi.entity.ADContainerId.md)|  The ID of the active directory container.
**rdn**|  xsd:string|  The rdn of the active directory container, relative to the root of the domain.


 


[^167]: This data object must be updated as a whole.