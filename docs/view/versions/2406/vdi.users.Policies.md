---
layout: page
title: Service - Policies
hide:
#- navigation
- toc
---







Java Class
> `com.vmware.vdi.vlsi.binding.vdi.users.Policies`

See also
> [EntityId](vdi.EntityId.md), [MapEntry](vdi.util.MapEntry.md), [PoliciesInfo](vdi.users.Policies.PoliciesInfo.md), [PoliciesSettings](vdi.users.Policies.PoliciesSettings.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0





## Service Description

Service for reading and specifying policy settings for resources, and users or groups. Covers policies for multimedia redirection, USB access, remote mode, and PCoIP hardware acceleration.

Methods

Methods defined in this Service
---
Policies_Clear, Policies_Get, Policies_List, Policies_ListUnentitledPolicies, Policies_Set, Policies_Update




Clear overrides for the given resource, or user or group on a given resource. Clearing overrides for a resource will not delete any overrides for specific users or groups on that resource. Cannot clear global policies.

Privileges

Privilege |  Description
---|---
POOL_MANAGEMENT|  Requires pool management to clear pool or user policies



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Policies](vdi.users.Policies.md) used to make the method call.
**resource**| [EntityId](vdi.EntityId.md)|  Entity Id of resource to clear policy overrides for.
**userOrGroup**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User or Group Id of user or group to clear policy overrides for. [^135]





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

Show WSDL type definition







Get the overrides for the given (optional, as long as userId is not present) resource and (optional) user or group. Global policies and effective policies will always exist. If there is a resource or user or group policies object, these are the overrides specific to the resource or user or group, respectively. The resourceId and userId of the returned object should always match the passed-in resourceId and userId. However, if no overrides exist specifically for that resource, or for that user or group on that resource, the associated policies object will be null.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_VIEW|  Requires global configuration view or pool view to get global policies
POOL_VIEW|  Requires pool view or global configuration view to get global policies. Requires pool view to get pool or user overrides



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Policies](vdi.users.Policies.md) used to make the method call.
**resource**| [EntityId](vdi.EntityId.md)|  Entity Id of resource to get policies for. [^135]
**userOrGroup**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User or Group Id of user or group to get policies for. [^135]





Return Value

Type |  Description
---|---
[PoliciesInfo](vdi.users.Policies.PoliciesInfo.md)| PoliciesInfo object describing policy overrides and effective policies for given resourceId and userId.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Get all overrides for users or groups on a given resource. May be null if there are no overrides for this users or groups on this resource.

Privileges

Privilege |  Description
---|---
POOL_VIEW|  Requires pool view to list user policy overrides on a specific pool.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Policies](vdi.users.Policies.md) used to make the method call.
**resource**| [EntityId](vdi.EntityId.md)|  Entity Id of resource to get policies for.




Return Value

Type |  Description
---|---
[PoliciesInfo[]](vdi.users.Policies.PoliciesInfo.md)| List of complete policies for all users that have specific overrides for this resource.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Get all unentitled policies. May be null if there are no unentitled policies present. Unentitled policies are the policy overrides for the users, who are no longer entitled to their resources.

Privileges

Privilege |  Description
---|---
POOL_VIEW|  Requires pool view to list unentitled policy overrides for various users.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Policies](vdi.users.Policies.md) used to make the method call.



Return Value

Type |  Description
---|---
[PoliciesInfo[]](vdi.users.Policies.PoliciesInfo.md)| List of complete unentitled policies for all users that have specific overrides for this resource.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Create an override for the associated policies settings for the specified (optional, as long as userId is not present) resource and (optional) user or group. Global policies may be set as long as none of the values are set to INHERIT.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  Requires global configuration management to set global policies
POOL_MANAGEMENT|  Requires pool management to set pool or user policies



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Policies](vdi.users.Policies.md) used to make the method call.
**resource**| [EntityId](vdi.EntityId.md)|  Entity Id of resource to set policies for. [^135]
**userOrGroup**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User or Group Id of user or group to set policies for. [^135]
**settings**| [PoliciesSettings](vdi.users.Policies.PoliciesSettings.md)|  Policies object to use as overrides.




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

Show WSDL type definition







Update the associated policies settings for the specified (optional, as long as userId is not present) resource and (optional) user or group. Global policies may be updated as long as none of the values are set to INHERIT. If there are no overrides for the specified resource and user or group, a new set of overrides will be created, and the default value of INHERIT will be assumed for any policies which are not specifically included in the update. If there are existing overrides for the specified resource and user or group, no policies which are not specified in the update map will be changed.

Privileges

Privilege |  Description
---|---
GLOBAL_CONFIG_MANAGEMENT|  Requires global configuration management to update global policies
POOL_MANAGEMENT|  Requires pool management to update pool or user policies



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Policies](vdi.users.Policies.md) used to make the method call.
**resource**| [EntityId](vdi.EntityId.md)|  Entity Id of resource to apply this update to. [^135]
**userOrGroup**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User or Group Id of user or group to apply this update to. [^135]
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  Update map. [^200]





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

Show WSDL type definition












 


[^135]: This parameter need not be set.
[^200]: This parameter is an update map based on [PoliciesSettings](vdi.users.Policies.PoliciesSettings.md "PoliciesSettings").