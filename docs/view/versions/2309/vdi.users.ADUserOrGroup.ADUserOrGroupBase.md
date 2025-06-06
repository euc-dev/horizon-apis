---
layout: page
title: Data Object - ADUserOrGroupBase
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.ADUserOrGroup.ADUserOrGroupBase`

Property of
> [AdminUserOrGroupInfo](vdi.users.AdminUserOrGroup.AdminUserOrGroupInfo.md#field_detail), [ADUserOrGroupInfo](vdi.users.ADUserOrGroup.ADUserOrGroupInfo.md#field_detail), [ADUserOrGroupSummaryView](vdi.users.ADUserOrGroup.ADUserOrGroupSummaryView.md#field_detail), [ADUserOrGroupView](vdi.users.ADUserOrGroup.ADUserOrGroupView.md#field_detail), [EntitledUserOrGroupGlobalSummaryView](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupGlobalSummaryView.md#field_detail), [EntitledUserOrGroupInfo](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupInfo.md#field_detail), [EntitledUserOrGroupLocalSummaryView](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupLocalSummaryView.md#field_detail)

Since
> Horizon View 6.0


## Data Object Description

Basic active directory data for a user or group. This is populated from locally or globally cached LDAP FSPs if available, otherwise it is obtained from AD.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**sid**|  xsd:string|  Security id of this user or group. [^2]
**group**|  xsd:boolean|  Whether or not this is a group or a user. [^2]
**domain**|  xsd:string|  The domain the user or group is in. This will be the DNS name of the domain. [^1] [^2]
**domainNetbiosName**|  xsd:string|  The domain netbios the user or group is in. This will be the netbios name of the domain.  **_Since_** Horizon 7.13 [^1] [^2]
**adDistinguishedName**|  xsd:string|  Active Directory distinguished name for this user or group. [^1] [^2]
**name**|  xsd:string|  Name of the user or group. [^1] [^2]
**firstName**|  xsd:string|  First name of the user or group. [^1] [^2]
**lastName**|  xsd:string|  Last name of the user or group. [^1] [^2]
**loginName**|  xsd:string|  Login name of this user or group. [^1] [^2]
**displayName**|  xsd:string|  Login name with domain of this user or group. [^1] [^2]
**longDisplayName**|  xsd:string|  Name and login name for a user, display name otherwise. [^1] [^2]
**userDisplayName**|  xsd:string|  User display name. This corresponds with displayName attribute in AD.  **_Since_** Horizon 7.3 [^1] [^2]
**email**|  xsd:string|  Email address of the user or group. [^1] [^2]
**kioskUser**|  xsd:boolean|  If this user is a "kiosk user" that supports client authentication. Client authentication is the process of supporting client devices directly logging into resources. [^2]
**unauthenticatedAccessUser**|  xsd:boolean|  Whether or not this is unauthenticated access user.  **_Since_** Horizon 7.4 [^1] [^2]
**phone**|  xsd:string|  Phone number of the user or group. Only available if obtained directly from AD (not cached in LDAP), such as returned by a refresh or with the ADUserOrGroup query interface. Otherwise this will be null. [^1] [^2]
**description**|  xsd:string|  Description of the user or group. Only available if obtained directly from AD (not cached in LDAP), such as returned by a refresh or with the ADUserOrGroup query interface. Otherwise this will be null. [^1] [^2]
**inFolder**|  xsd:string|  AD folder for the user or group. Only available if obtained directly from AD (not cached in LDAP), such as returned by a refresh or with the ADUserOrGroup query interface. Otherwise this will be null. [^1] [^2]
**userPrincipalName**|  xsd:string|  User Principal name(UPN) of the user.  **_Since_** Horizon 7.1 [^1] [^2]
**guid**|  xsd:string| **Deprecated.**_: Use[formattedGuid](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md#formattedGuid) since that is in RFC 4122 format. _ GUID of the user or group.  **_Since_** Horizon 7.7 [^1] [^2]
**formattedGuid**|  xsd:string|  GUID of the user or group (same as [guid](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md#guid)) but in RFC 4122 format. example: 5F5A45D9-15C0-4654-8FCF-D589C0EF3ECA  **_Since_** Horizon 7.9 [^1] [^2]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.