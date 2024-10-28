---
layout: page
title: Service - AccessGroup
hide:
#- navigation
- toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.users.AccessGroup`

See also
> [AccessGroupBase](vdi.users.AccessGroup.AccessGroupBase.md), [AccessGroupId](vdi.entity.AccessGroupId.md), [AccessGroupInfo](vdi.users.AccessGroup.AccessGroupInfo.md)

Since
> Horizon View 6.0





## Service Description

Information about an access group. This primarily represents a hierarchical storage concept for desktops, applications, farms, machines, and persistent disks on which to base admin user permissions. For instance, an admin with root access group permissions could interact with desktops assigned to any access group under that root.

Methods

Methods defined in this Service
---
AccessGroup_Create, AccessGroup_Delete, AccessGroup_Get, AccessGroup_List




Add a new access group. delete/create should be used instead of update. Only access groups with root as a parent are supported.

Privileges

Privilege |  Description
---|---
FOLDER_MANAGEMENT|  Access group management privilege on the new access group's parent or its ancestors is required to create an access group.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [AccessGroup](vdi.users.AccessGroup.md) used to make the method call.
**base**| [AccessGroupBase](vdi.users.AccessGroup.AccessGroupBase.md)|  attributes needed to add an access group




Return Value

Type |  Description
---|---
[AccessGroupId](vdi.entity.AccessGroupId.md)| unique identifier



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
ADMIN_FOLDER_ADDED|  Sent when successfully creating an access group.
ADMIN_FOLDER_ADD_FAILED|  Sent when an access group failed to be created.

Show WSDL type definition







Delete a given access group and all permissions associated with it. This also deletes all children of the access group. delete/create should be used instead of update. The access group must not be associated with any Desktops, Farms, Applications, or Persistent Disks.

Privileges

Privilege |  Description
---|---
FOLDER_MANAGEMENT|  Access group management privilege on the specified access group or its ancestors is required to delete an access group.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [AccessGroup](vdi.users.AccessGroup.md) used to make the method call.
**entityId**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  Id of the access group to delete.




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
ADMIN_FOLDER_DELETED|  Sent when successfully deleting an access group.
ADMIN_FOLDER_DELETE_FAILED|  Sent when an access group failed to be deleted.

Show WSDL type definition







Get an access group by Id.

Privileges

Privilege |  Description
---|---
GLOBAL_PERMISSION_VIEW|  Read access to permissions is sufficient to read any access group. This is also necessary to read permissions that belong to the specified access group.
FOLDER_VIEW|  Read access to a specific access group or its ancestors is necessary to read an access group without the above privilege.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [AccessGroup](vdi.users.AccessGroup.md) used to make the method call.
**id**| [AccessGroupId](vdi.entity.AccessGroupId.md)|  Access group id of entity to get.




Return Value

Type |  Description
---|---
[AccessGroupInfo](vdi.users.AccessGroup.AccessGroupInfo.md)| requested access group entity.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







List all permitted access groups via their allowed ancestor closest to the root access group. If the client has permission to read the root access group, this will return just the root access group, which can be traversed to list all access groups.

Privileges

Privilege |  Description
---|---
GLOBAL_PERMISSION_VIEW|  Read access to permissions is sufficient to read all access groups. This is also necessary to read permissions that belong to an access group.
FOLDER_VIEW|  Read access to a specific access group or its ancestors is necessary to read an access group without the above privilege.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [AccessGroup](vdi.users.AccessGroup.md) used to make the method call.



Return Value

Type |  Description
---|---
[AccessGroupInfo[]](vdi.users.AccessGroup.AccessGroupInfo.md)| The permitted access groups, listed by their ancestors closest to the root.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
