---
layout: page
title: Service - ADContainer
hide:
#- navigation
- toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.ADContainer`

See also
> [ADContainerInfo](vdi.utils.ADContainer.ADContainerInfo.md), [ADDomainId](vdi.entity.ADDomainId.md), [ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)

Since
> Horizon View 6.0





## Service Description

Provides the ability to retrieve domain container information for the View Cluster.

**Methods**

Methods defined in this Service:
ADContainer_ListByDomain, ADContainer_ListByViewComposerDomainAdministrator




Lists the Active Directory containers for a specific domain. Requires at least one of the listed privileges.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  Global configuration (read-only) privilege is required to list the active directory containers.
POOL_VIEW|  privilege is required to list the active directory containers.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ADContainer](vdi.utils.ADContainer.md) used to make the method call.
**domain**| [ADDomainId](vdi.entity.ADDomainId.md)|  The domain to list containers.




**Return Value**

Type | Description
:---|:---
[ADContainerInfo[]](vdi.utils.ADContainer.ADContainerInfo.md)| A list of [ADContainerInfo](vdi.utils.ADContainer.ADContainerInfo.md) containing information about the AD containers.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Lists the Active Directory containers for a specific domain. Requires at least one of the listed privileges.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  Global configuration (read-only) privilege is required to list the active directory containers.
POOL_VIEW|  privilege is required to list the active directory containers.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ADContainer](vdi.utils.ADContainer.md) used to make the method call.
**domainAdministrator**| [ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)|  The domain administrator to list containers.




**Return Value**

Type | Description
:---|:---
[ADContainerInfo[]](vdi.utils.ADContainer.ADContainerInfo.md)| A list of [ADContainerInfo](vdi.utils.ADContainer.ADContainerInfo.md) containing information about the AD containers.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if the domain of the specified administrator is unknown to the View cluster.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
