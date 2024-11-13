---
layout: page
title: Service - UserHomeSite
hide:
#- navigation
- toc
---







Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.federation.UserHomeSite`

See also
> [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md), [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md), [UserHomeSiteBase](vdi.federation.UserHomeSite.UserHomeSiteBase.md), [UserHomeSiteId](vdi.entity.UserHomeSiteId.md), [UserHomeSiteInfo](vdi.federation.UserHomeSite.UserHomeSiteInfo.md), [UserHomeSiteResolutionInfo](vdi.federation.UserHomeSite.UserHomeSiteResolutionInfo.md), [UserHomeSitesSpec](vdi.federation.UserHomeSite.UserHomeSitesSpec.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0





## Service Description

Representing the configured home site information for users/user groups. It can be used to determine which site the session should be assigned. And it can be configured in 2 ways:
1\. Globally configured home site for a user or a group.
2\. GlobalEntitlement specific Home site for a user or a group. When this configuration is present, it will overwrite the globally configured home site for that GlobalEntitlement.
It is possible that a user is a member of multiple groups and those groups are configured with different home sites within the same GlobalEntitlement, this essentially creates a conflict. UserHomeSite also provides helper methods to aid the discovery and resolution of conflicting home site configurations.
There's no update supported for UserHomeSite. All update to existing UserHomeSite can be done via delete and create.

Methods

Methods defined in this Service
---
UserHomeSite_Create, UserHomeSite_CreateOrUpdate, UserHomeSite_Delete, UserHomeSite_DeleteUserHomeSites, UserHomeSite_Get, UserHomeSite_GetInfos, UserHomeSite_List, UserHomeSite_Resolve, UserHomeSite_ResolveForGAE, UserHomeSite_ResolveHomeSites




Creating a home site configuration for a user or a group. When GlobalEntitlement is absent, this represents a global configuration; otherwise, it represent a home site override for that GlobalEntitlement.
If the home site is already the user or group's home site, it will not be added again.
The request will NOT fail if the specified user is a member of another group which already has a different home site.
It is OK if the specified user is an individual user if they belong to a group that is already entitled to the specified GlobalEntitlement.
It is NOT OK if the specified user is a group if it is NOT already entitled to the specified GlobalEntitlement.


Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to create a user home site.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UserHomeSite](vdi.federation.UserHomeSite.md) used to make the method call.
**base**| [UserHomeSiteBase](vdi.federation.UserHomeSite.UserHomeSiteBase.md)|  Base data for creating a UserHomeSite object




Return Value

Type |  Description
---|---
[UserHomeSiteId](vdi.entity.UserHomeSiteId.md)| Id The Id of the UserHomeSite object created.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if required entity Id in the baseData is missing.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if PodFederation has not been initialized.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_USER_HOME_SITE_ADDED|  If the user home site was successfully created.
VLSI_USER_HOME_SITE_ADD_FAILED|  If the user home site could not be created.

Show WSDL type definition







Create or update a home site configuration for a user or a group. When GlobalEntitlement is absent, this represents a global configuration; otherwise, it represent a home site override for that GlobalEntitlement.
If [allowUpdate](vdi.federation.UserHomeSite.UserHomeSitesSpec.md#allowUpdate) is set to true in UserHomeSitesSpec and home site already exists for the user, then it would be updated with the new home site
If [allowUpdate](vdi.federation.UserHomeSite.UserHomeSitesSpec.md#allowUpdate) is set to false in UserHomeSitesSpec then the behaviour would same as create api. The request will NOT fail if the specified user is a member of another group which already has a different home site.


Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to create a user home site.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UserHomeSite](vdi.federation.UserHomeSite.md) used to make the method call.
**spec**| [UserHomeSitesSpec](vdi.federation.UserHomeSite.UserHomeSitesSpec.md)|  UserHomeSitesSpec which will contain a list of UserHomeSiteBases to be added/updated




Return Value

Type |  Description
---|---
[UserHomeSiteId[]](vdi.entity.UserHomeSiteId.md)| UserHomeSiteId[]



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if the specified user or group that the user belongs to is NOT already entitled to the specified GlobalEntitlement.
[InvalidRequest](vdi.fault.InvalidRequest.md)| Thrown if the specified user or group that the user belongs to is NOT already entitled to the specified GlobalEntitlement.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if PodFederation has not been initialized.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_USER_HOME_SITE_ADDED|  If the user home site was successfully created
VLSI_USER_HOME_SITE_ADD_FAILED|  If the user home site could not be created.

Show WSDL type definition







Remove the home site configuration for the specified UserHomeSite.

Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to delete a user home site.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UserHomeSite](vdi.federation.UserHomeSite.md) used to make the method call.
**id**| [UserHomeSiteId](vdi.entity.UserHomeSiteId.md)|  the Id for the user/group's existing home site




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
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the Pod Federation has not been initialized.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_USER_HOME_SITE_DELETED|  If the user home site was successfully deleted.
VLSI_USER_HOME_SITE_DELETE_FAILED|  If the user home site could not be deleted.

Show WSDL type definition







Remove the home site configuration for all the specified UserHomeSites.

Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_MANAGE|  Global LDAP management is required to delete a user home site.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UserHomeSite](vdi.federation.UserHomeSite.md) used to make the method call.
**ids**| [UserHomeSiteId[]](vdi.entity.UserHomeSiteId.md)|  the array of Ids for the user/group's existing home sites to be deleted




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
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the Pod Federation has not been initialized.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.



Events

Event |  Description
---|---
VLSI_USER_HOME_SITE_DELETED|  If the user home site was successfully deleted.
VLSI_USER_HOME_SITE_DELETE_FAILED|  If the user home site could not be deleted.

Show WSDL type definition







Retrieve the UserHomeSiteInfo given a UserHomeSiteId. Callers would be able to get a handle of UserHomeSiteId via EntitledUserOrGroup service.

Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read a user home site.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UserHomeSite](vdi.federation.UserHomeSite.md) used to make the method call.
**id**| [UserHomeSiteId](vdi.entity.UserHomeSiteId.md)|  The id of the UserHomeSite object.




Return Value

Type |  Description
---|---
[UserHomeSiteInfo](vdi.federation.UserHomeSite.UserHomeSiteInfo.md)| UserHomeSiteInfo



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the Pod Federation has not been initialized.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Retrieve the UserHomeSiteInfo given an array of UserHomeSiteIds. Callers would be able to get a handle of UserHomeSiteId via EntitledUserOrGroup service.

Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to read multiple user home sites.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UserHomeSite](vdi.federation.UserHomeSite.md) used to make the method call.
**ids**| [UserHomeSiteId[]](vdi.entity.UserHomeSiteId.md)|  The ids of the UserHomeSite object.




Return Value

Type |  Description
---|---
[UserHomeSiteInfo[]](vdi.federation.UserHomeSite.UserHomeSiteInfo.md)| UserHomeSiteInfo



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the Pod Federation has not been initialized.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Given a user or group, retrieve their list of UserHomeSiteInfo.
All home site configurations for the UserOrGroup will be returned. They include both globally configured home sites as well as per-GlobalEntitlement overwriting home sites.
Only home site information configured directly against the specified UserOrGroup will be returned. It will not return any home site information for the groups that UserOrGroup is part of.

Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to list user home sites.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UserHomeSite](vdi.federation.UserHomeSite.md) used to make the method call.
**userOrGroup**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  Id for a user or group




Return Value

Type |  Description
---|---
[UserHomeSiteInfo[]](vdi.federation.UserHomeSite.UserHomeSiteInfo.md)| UserHomeSiteInfo



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the Pod Federation has not been initialized.
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Given a UserOrGroupId for an individual user and a GlobalEntitlementId, return the resolved home site information as well as any conflicting configurations.
This operation will look up the user home site configuration data for the specified user; as well as user home site configurations for any immediate groups that this user is a member of. It will calculate override home site configuration and apply conflict resolution algorithm appropriately.
A home site configuration is in conflict if the specified UserOrGroupId belongs to more than one group, and those groups are entitled to the same GlobalEntitlement but they have different overriding home sites.
It will return the UserHomeSiteInfo objects that represent the resolved user home site as well as any conflicting home site configurations. If there's no home site configured, null will be returned.
The resolved home site is always the first element in the returned list, any conflicting user home site configurations will follow after that.
The resolved home site will be the site that a new persistent resource assignment will take place for this UserOrGroup and GlobalEntitlement.


Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to resolve user home sites.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UserHomeSite](vdi.federation.UserHomeSite.md) used to make the method call.
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  Id for an individual user whose home site to be resolved. UserOrGroupId for group is not supported.
**globalEntitlement**| [GlobalEntitlementId](vdi.entity.GlobalEntitlementId.md)|  The Id of the GlobalEntitlement the UserOrGroup is entitled to.




Return Value

Type |  Description
---|---
[UserHomeSiteInfo[]](vdi.federation.UserHomeSite.UserHomeSiteInfo.md)| A list of user home site configurations. The resolved home site will be the first element in the list, followed by conflicting home site configurations. Return null if no home site configuration found.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the Pod Federation has not been initialized
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Given a UserOrGroupId for an individual user and a GlobalApplicationEntitlementId, return the resolved home site information as well as any conflicting configurations.
This operation will look up the user home site configuration data for the specified user; as well as user home site configurations for any immediate groups that this user is a member of. It will calculate override home site configuration and apply conflict resolution algorithm appropriately.
A home site configuration is in conflict if the specified UserOrGroupId belongs to more than one group, and those groups are entitled to the same GlobalApplicationEntitlement but they have different overriding home sites.
It will return the UserHomeSiteInfo objects that represent the resolved user home site as well as any conflicting home site configurations. If there's no home site configured, null will be returned.
The resolved home site is always the first element in the returned list, any conflicting user home site configurations will follow after that.
The resolved home site will be the site that a new persistent resource assignment will take place for this UserOrGroup and GlobalApplicationEntitlement.


Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to resolve user home sites.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UserHomeSite](vdi.federation.UserHomeSite.md) used to make the method call.
**user**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  Id for an individual user whose home site to be resolved. UserOrGroupId for group is not supported.

**globalApplicationEntitlement**| [GlobalApplicationEntitlementId](vdi.entity.GlobalApplicationEntitlementId.md)|  The Id of the GlobalApplicationEntitlement the UserOrGroup is entitled to.




Return Value

Type |  Description
---|---
[UserHomeSiteInfo[]](vdi.federation.UserHomeSite.UserHomeSiteInfo.md)| A list of user home site configurations. The resolved home site will be the first element in the list, followed by conflicting home site configurations. Return null if no home site configuration found.



Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the Pod Federation has not been initialized
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition







Given a UserOrGroupId for an individual user, return the resolved home site information as well as any conflicting configurations for each of the Use Home Site policy enabled Global Entitlement/Global Application Entitlement where the user is entitled to.
Details:

* This operation will look up the user home site configuration data for the specified user; as well as user home site configurations for any immediate groups that this user is a member of. It will calculate override home site configuration and apply conflict resolution algorithm appropriately.
* A home site configuration is in conflict if the specified UserOrGroupId belongs to more than one group, and those groups are entitled to the same GlobalEntitlement/GlobalApplicationEntitlement but they have different overriding home sites.
* It will return the UserHomeSiteResolutionInfo objects for all the Use Home Site policy enabled Global Entitlement/Global Application Entitlement where the user is entitled. [resolvedData](vdi.federation.UserHomeSite.UserHomeSiteResolutionInfo.md#resolvedData) represent the resolved user home site as well as any conflicting home site configurations.
* The resolved home site is always the first element in the returned list, any conflicting user home site configurations will follow after that.
* The resolved home site will be the site that a new persistent resource assignment will take place for the UserOrGroup and GlobalEntitlement/GlobalApplicationEntitlement.



Privileges

Privilege |  Description
---|---
FEDERATED_LDAP_VIEW|  Global LDAP read is required to resolve user home sites.



Parameters

Name| Type| Description
---|---|---
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [UserHomeSite](vdi.federation.UserHomeSite.md) used to make the method call.
**id**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  Id for an individual user whose home site to be resolved. UserOrGroupId for group is not supported.




Return Value

Type |  Description
---|---
[UserHomeSiteResolutionInfo[]](vdi.federation.UserHomeSite.UserHomeSiteResolutionInfo.md)| A list of user home site resolution information.


* [resolvedData](vdi.federation.UserHomeSite.UserHomeSiteResolutionInfo.md#resolvedData) will be available only if home site configuration exists for the Global Entitlement/Global Application Entitlement
* The resolved home site will be the first element in [resolvedData](vdi.federation.UserHomeSite.UserHomeSiteResolutionInfo.md#resolvedData) followed by conflicting home site configurations.





Faults

Type |  Description
---|---
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.
[InvalidState](vdi.fault.InvalidState.md)| Thrown if the Pod Federation has not been initialized
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.

Show WSDL type definition












 
