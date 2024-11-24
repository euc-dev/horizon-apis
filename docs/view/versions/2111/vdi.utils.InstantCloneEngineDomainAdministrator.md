---
layout: page
title: Service - InstantCloneEngineDomainAdministrator
hide:
#- navigation
- toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.utils.InstantCloneEngineDomainAdministrator`

See also
> [InstantCloneEngineDomainAdministratorId](vdi.entity.InstantCloneEngineDomainAdministratorId.md), [InstantCloneEngineDomainAdministratorInfo](vdi.utils.InstantCloneEngineDomainAdministrator.InstantCloneEngineDomainAdministratorInfo.md), [InstantCloneEngineDomainAdministratorSpec](vdi.utils.InstantCloneEngineDomainAdministrator.InstantCloneEngineDomainAdministratorSpec.md), [MapEntry](vdi.util.MapEntry.md)

Since
> Horizon 7.0





## Service Description

The Instant Clone Engine domain administrator service interface for processing accounts capable of adding/deleting computer accounts.

**Methods**

Methods defined in this Service:
InstantCloneEngineDomainAdministrator_Create, InstantCloneEngineDomainAdministrator_Delete, InstantCloneEngineDomainAdministrator_Get, InstantCloneEngineDomainAdministrator_List, InstantCloneEngineDomainAdministrator_Update




Add Instant Clone Engine domain administrator.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to create Instant Clone Engine domain administrator.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [InstantCloneEngineDomainAdministrator](vdi.utils.InstantCloneEngineDomainAdministrator.md) used to make the method call.
**spec**| [InstantCloneEngineDomainAdministratorSpec](vdi.utils.InstantCloneEngineDomainAdministrator.InstantCloneEngineDomainAdministratorSpec.md)|  attributes needed to add Instant Clone Engine domain administrator.




**Return Value**

Type | Description
:---|:---
[InstantCloneEngineDomainAdministratorId](vdi.entity.InstantCloneEngineDomainAdministratorId.md)| Entity id for the Instant Clone Engine domain administrator.



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_INSTANT_CLONE_ADMIN_CREATED|  If the instant clone domain administrator was successfully created.
VLSI_INSTANT_CLONE_ADMIN_CREATE_FAILED|  If the instant clone domain administrator could not be created.

Show WSDL type definition







Delete Instant Clone Engine domain administrator. There must be no desktops associated with it.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to delete Instant Clone Engine domain administrator.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [InstantCloneEngineDomainAdministrator](vdi.utils.InstantCloneEngineDomainAdministrator.md) used to make the method call.
**id**| [InstantCloneEngineDomainAdministratorId](vdi.entity.InstantCloneEngineDomainAdministratorId.md)|  entity id for the Instant Clone Engine domain administrator entry.




**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityInUse](vdi.fault.EntityInUse.md)| Thrown if a desktop is associated with this instant clone engine domain administrator.
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_INSTANT_CLONE_ADMIN_DELETED|  If the instant clone domain administrator was successfully deleted.
VLSI_INSTANT_CLONE_ADMIN_DELETE_FAILED|  If the instant clone domain administrator could not be deleted.

Show WSDL type definition







Gets info (primarily the list of attributes about configured Instant Clone Engine domain administrator).

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  Global configuration view is sufficient to get a Instant Clone Engine domain administrator.
POOL_VIEW|  Desktop read privilege with any access group is sufficient to get a Instant Clone Engine domain administrator.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [InstantCloneEngineDomainAdministrator](vdi.utils.InstantCloneEngineDomainAdministrator.md) used to make the method call.
**id**| [InstantCloneEngineDomainAdministratorId](vdi.entity.InstantCloneEngineDomainAdministratorId.md)|  entity id for the Instant Clone Engine domain administrator entry.




**Return Value**

Type | Description
:---|:---
[InstantCloneEngineDomainAdministratorInfo](vdi.utils.InstantCloneEngineDomainAdministrator.InstantCloneEngineDomainAdministratorInfo.md)| InstantCloneEngineDomainAdministratorInfo (attributes about configured Instant Clone Engine domain administrator).



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Gets list of Instant Clone Engine domain administrators.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_VIEW|  Global configuration view is sufficient to list Instant Clone Engine domain administrators.
POOL_VIEW|  Desktop read privilege with any access group is sufficient to list Instant Clone Engine domain administrators.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [InstantCloneEngineDomainAdministrator](vdi.utils.InstantCloneEngineDomainAdministrator.md) used to make the method call.



**Return Value**

Type | Description
:---|:---
[InstantCloneEngineDomainAdministratorInfo[]](vdi.utils.InstantCloneEngineDomainAdministrator.InstantCloneEngineDomainAdministratorInfo.md)| list of InstantCloneEngineDomainAdministratorInfo (attributes about configured Instant Clone Engine domain administrators).



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Update Instant Clone Engine domain administrator with the set of attributes in the map.

**Privileges**

Privilege | Description
:---|:---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to update Instant Clone Engine domain administrator.



**Parameters**

 Name | Type | Description
:---|:---|:---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [InstantCloneEngineDomainAdministrator](vdi.utils.InstantCloneEngineDomainAdministrator.md) used to make the method call.
**id**| [InstantCloneEngineDomainAdministratorId](vdi.entity.InstantCloneEngineDomainAdministratorId.md)|  entity id for the Instant Clone Engine domain administrator entry.
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  key value pairs describing attributes to be updated [^153]





**Return Value**

Type | Description
:---|:---
None



**Faults**

Type | Description
:---|:---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



**Events**

Event | Description
:---|:---
VLSI_INSTANT_CLONE_ADMIN_UPDATED|  If the instant clone domain administrator was successfully updated.
VLSI_INSTANT_CLONE_ADMIN_UPDATE_FAILED|  If the instant clone domain administrator could not be updated.

Show WSDL type definition












 


[^153]: This parameter is an update map based on [InstantCloneEngineDomainAdministratorInfo](vdi.utils.InstantCloneEngineDomainAdministrator.InstantCloneEngineDomainAdministratorInfo.md "InstantCloneEngineDomainAdministratorInfo").