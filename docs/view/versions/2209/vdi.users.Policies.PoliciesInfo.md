---
layout: page
title: Data Object - PoliciesInfo
hide:
#- navigation
- toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.Policies.PoliciesInfo`

Returned by
> [Policies_Get](vdi.users.Policies.md#get), [Policies_List](vdi.users.Policies.md#list), [Policies_ListUnentitledPolicies](vdi.users.Policies.md#listUnentitledPolicies)

See also
> [EntityId](vdi.EntityId.md), [PoliciesSettings](vdi.users.Policies.PoliciesSettings.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0


## Data Object Description

Complete policies specification. The resourceId and userId identify the object to which this policy applies. If neither is specified, these will be only the global policies. The userId cannot be specified without the resourceId, as user overrides are per-resource. The policies settings object are overrides specifically set on the associated resource or user or group, the effective settings object is the result of applying each override successively on top of the global policies.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**globalPolicies**| [PoliciesSettings](vdi.users.Policies.PoliciesSettings.md)|  Global policies object. Describes default policies for all resources, users, or groups if no overrides are specified.
**resource**| [EntityId](vdi.EntityId.md)|  Entity Id of a resource which may have some set of overrides applied to it. If the resourceId is specified, resourcePolicies may be populated with overrides specific to that resource. Note that it is possible for a resource to have no overrides, but a user or group for that resource may have overrides. [^1]
**resourcePolicies**| [PoliciesSettings](vdi.users.Policies.PoliciesSettings.md)|  Resource policies object. Describes default policies for all users or groups in this resource if no user or group overrides are specified. [^1]
**userOrGroup**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  User or group which may have some set of overrides applied to it. If the userId is specified, the resourceId must be specified as well. Note that is is possible for a resource to have no overrides, but a user or group for that resource may have overrides. [^1]
**userPolicies**| [PoliciesSettings](vdi.users.Policies.PoliciesSettings.md)|  User policies object. Describes policies for the given user or group Id. [^1]
**effectivePolicies**| [PoliciesSettings](vdi.users.Policies.PoliciesSettings.md)|  Effective policies object. The result of applying any resource or user overrides (if present) to the global policies. Will always be set.


 


[^1]: This property need not be set.