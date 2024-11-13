---
layout: page
title: Service - GlobalAccessGroup
hide:
#- navigation
- toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.users.GlobalAccessGroup`

See also
> [GlobalAccessGroupBase](vdi.users.GlobalAccessGroup.GlobalAccessGroupBase.md), [GlobalAccessGroupId](vdi.entity.GlobalAccessGroupId.md), [GlobalAccessGroupInfo](vdi.users.GlobalAccessGroup.GlobalAccessGroupInfo.md)

Since
> Horizon 8.2





## Service Description

Information about a global access group. This primarily represents a hierarchical storage concept for global entities like global entitlements, on which to base admin user permissions. For instance, an admin with root global access group permissions could interact with global entitlement assigned to any global access group under that root.

Methods

Methods defined in this Service
---
GlobalAccessGroup_Create, GlobalAccessGroup_Delete, GlobalAccessGroup_Get, GlobalAccessGroup_List




Add a new global access group. Delete/create should be used instead of update. Only global access groups with root as a parent are supported.

Privileges

Privilege |  Description
---|---
FOLDER_MANAGEMENT|  Global Access group management privilege on the new access group's parent or its ancestors is required to create an access group.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalAccessGroup](vdi.users.GlobalAccessGroup.md) used to make the method call.
**base**| [GlobalAccessGroupBase](vdi.users.GlobalAccessGroup.GlobalAccessGroupBase.md)|  attributes needed to add a global access group




Return Value

Type |  Description
---|---
[GlobalAccessGroupId](vdi.entity.GlobalAccessGroupId.md)| unique identifier



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
ADMIN_GLOBAL_FOLDER_ADDED|  Sent when successfully creating a global access group.

Show WSDL type definition







Delete a given global access group. Global access group can be deleted only if it is not in use (across PODs).

Privileges

Privilege |  Description
---|---
FOLDER_MANAGEMENT|  Global Access group management privilege on the specified global access group or its ancestors is required to delete a global access group.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalAccessGroup](vdi.users.GlobalAccessGroup.md) used to make the method call.
**entityId**| [GlobalAccessGroupId](vdi.entity.GlobalAccessGroupId.md)|  Id of the global access group to delete.




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
ADMIN_GLOBAL_FOLDER_DELETED|  Sent when successfully deleting a global access group

Show WSDL type definition







Get a global access group by Id.

Privileges

Privilege |  Description
---|---
GLOBAL_PERMISSION_VIEW|  Read access to permissions is sufficient to read any global access group. This is also necessary to read permissions that belong to the specified global access group.
FOLDER_VIEW|  Read access to a specific global access group or its ancestors is necessary to read a global access group without the above privilege.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalAccessGroup](vdi.users.GlobalAccessGroup.md) used to make the method call.
**id**| [GlobalAccessGroupId](vdi.entity.GlobalAccessGroupId.md)|  Global Access group id.




Return Value

Type |  Description
---|---
[GlobalAccessGroupInfo](vdi.users.GlobalAccessGroup.GlobalAccessGroupInfo.md)| requested global access group entity.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







List all global access groups.

Privileges

Privilege |  Description
---|---
GLOBAL_PERMISSION_VIEW|  Read access to permissions is sufficient to read all global access groups. This is also necessary to read permissions that belong to a global access group.
FOLDER_VIEW|  Read access to a specific global access group or its ancestors is necessary to read a global access group without the above privilege.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalAccessGroup](vdi.users.GlobalAccessGroup.md) used to make the method call.



Return Value

Type |  Description
---|---
[GlobalAccessGroupInfo[]](vdi.users.GlobalAccessGroup.GlobalAccessGroupInfo.md)| The global access groups.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
