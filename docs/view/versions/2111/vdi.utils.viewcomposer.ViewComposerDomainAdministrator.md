---
layout: page
title: Service - ViewComposerDomainAdministrator
hide:
#- navigation
- toc
---







Java Class
> `com.vmware.vdi.vlsi.binding.vdi.utils.viewcomposer.ViewComposerDomainAdministrator`

See also
> [MapEntry](vdi.util.MapEntry.md), [ServerDefinition](vdi.utils.Certificate.ServerDefinition.md), [ViewComposerDomainAdministratorBase](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.DomainAdministratorBase.md), [ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md), [ViewComposerDomainAdministratorInfo](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.ViewComposerDomainAdministratorInfo.md), [ViewComposerDomainAdministratorSpec](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.ViewComposerDomainAdministratorSpec.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since
> Horizon View 6.0





## Service Description

**Deprecated.**_This is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

The view composer domain administrator service interface for processing accounts capable of adding/deleting computer accounts.

Methods

Methods defined in this Service
---
ViewComposerDomainAdministrator_Create, ViewComposerDomainAdministrator_CreateByServerDefinition, ViewComposerDomainAdministrator_Delete, ViewComposerDomainAdministrator_DeleteByServerDefinition, ViewComposerDomainAdministrator_Get, ViewComposerDomainAdministrator_List, ViewComposerDomainAdministrator_ListByServerDefinition, ViewComposerDomainAdministrator_listFarmAndDesktopNames, ViewComposerDomainAdministrator_Update, ViewComposerDomainAdministrator_UpdateByServerDefinition




**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Add a view composer domain administrator.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to create a View Composer administrator.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ViewComposerDomainAdministrator](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.md) used to make the method call.
**spec**| [ViewComposerDomainAdministratorSpec](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.ViewComposerDomainAdministratorSpec.md)|  attributes needed to add a view composer domain administrator




Return Value

Type |  Description
---|---
[ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)| Entity id for the view composer domain administrator.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
ADMIN_SVI_ADMIN_ADDED|  If the View Composer administrator is added.

Show WSDL type definition







**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Adds a view composer domain administrator. This method can be used prior to adding View Composer in Horizon and hence it always expects View Composer Server details as input.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to create a View Composer administrator.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ViewComposerDomainAdministrator](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.md) used to make the method call.
**serverDefinition**| [ServerDefinition](vdi.utils.Certificate.ServerDefinition.md)|  Details required to connect to View Composer server.
**base**| [ViewComposerDomainAdministratorBase](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.DomainAdministratorBase.md)|  Domain administrator details to be added.




Return Value

Type |  Description
---|---
[ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)| Entity id for the view composer domain administrator.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
ADMIN_SVI_ADMIN_ADDED|  If the View Composer administrator is added.

Show WSDL type definition







**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Delete a view composer admin.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to delete a View Composer administrator.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ViewComposerDomainAdministrator](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.md) used to make the method call.
**id**| [ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)|  entity id for the view composer admin entry




Return Value

Type |  Description
---|---
None



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
ADMIN_SVI_ADMIN_REMOVED|  If the administrator is removed.

Show WSDL type definition







**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Delete a view composer admin from the specified View Composer server. This method can be used prior to adding View Composer in Horizon and hence it always expects View Composer Server details as input.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to delete a View Composer administrator.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ViewComposerDomainAdministrator](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.md) used to make the method call.
**id**| [ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)|  entity id for the view composer admin entry.
**serverDefinition**| [ServerDefinition](vdi.utils.Certificate.ServerDefinition.md)|  Details required to connect to View Composer server.




Return Value

Type |  Description
---|---
None



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
ADMIN_SVI_ADMIN_REMOVED|  If the administrator is removed.

Show WSDL type definition







**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Gets the View Composer domain administrator information (primarily the list of attributes about configured view composer administrator). Requires at least one of the listed privileges.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_VIEW|  Global configuration view is required to get a View Composer domain administrator.
POOL_VIEW|  privilege is required to get a View Composer domain administrator.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ViewComposerDomainAdministrator](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.md) used to make the method call.
**id**| [ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)|  entity id for the view composer admin entry.




Return Value

Type |  Description
---|---
[ViewComposerDomainAdministratorInfo](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.ViewComposerDomainAdministratorInfo.md)| ViewComposerDomainAdministratorInfo (attributes about configured view composer administrator)



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Gets list of info (primarily the list of attributes about configured view composer administrators). Requires at least one of the listed privileges.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_VIEW|  Global configuration view is required to list View Composer administrators.
POOL_VIEW|  privilege is required to list View Composer administrators.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ViewComposerDomainAdministrator](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.md) used to make the method call.
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  entity id for the virtual center related to the view composer server




Return Value

Type |  Description
---|---
[ViewComposerDomainAdministratorInfo[]](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.ViewComposerDomainAdministratorInfo.md)| list of ViewComposerDomainAdministratorInfo (attributes about configured view composer administrators)



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Lists the View Composer domain administrators from the specified View Composer server. This method can be used prior to adding View Composer in Horizon and hence it always expects View Composer Server details as input.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_VIEW|  Global configuration view is required to list View Composer administrators.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ViewComposerDomainAdministrator](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.md) used to make the method call.
**serverDefinition**| [ServerDefinition](vdi.utils.Certificate.ServerDefinition.md)|  Details required to connect to View Composer server.




Return Value

Type |  Description
---|---
[ViewComposerDomainAdministratorInfo[]](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.ViewComposerDomainAdministratorInfo.md)| list of ViewComposerDomainAdministratorInfo (attributes about configured view composer administrators)



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

List the name of Farms and Desktops for the given View Composer domain administrator alongwith the authorized user

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_VIEW|  Global configuration view is required to fetch the Desktop and Farm names for a given View Composer domain administrator alongwith the authorized user



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ViewComposerDomainAdministrator](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.md) used to make the method call.
**id**| [ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)|  entity id for the View Composer domain administrator entry




Return Value

Type |  Description
---|---
xsd:string[]| Array of the String containing name of Farms and Desktops for the given View Composer domain administrator alongwith the authorized user



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Update view composer admin with the set of attributes in the map.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to update a View Composer administrator.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ViewComposerDomainAdministrator](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.md) used to make the method call.
**id**| [ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)|  entity id for the view composer admin entry
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  key value pairs describing attributes to be updated [^166]





Return Value

Type |  Description
---|---
None



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
ADMIN_SVI_ADMIN_UPDATED|  If the update is completed.

Show WSDL type definition







**Deprecated.**_This API is being deprecated since View Composer will no longer be supported from Horizon version 2012 onwards._

Update view composer admin with the set of attributes in the map. This method can be used prior to adding View Composer in Horizon and hence it always expects View Composer Server details as input.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to update a View Composer administrator.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [ViewComposerDomainAdministrator](vdi.utils.viewcomposer.ViewComposerDomainAdministrator.md) used to make the method call.
**id**| [ViewComposerDomainAdministratorId](vdi.entity.ViewComposerDomainAdministratorId.md)|  entity id for the view composer admin entry.
**serverDefinition**| [ServerDefinition](vdi.utils.Certificate.ServerDefinition.md)|  Details required to connect to View Composer server.
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  key value pairs describing attributes to be updated [^166]





Return Value

Type |  Description
---|---
None



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
ADMIN_SVI_ADMIN_UPDATED|  If the update is completed.

Show WSDL type definition












 
