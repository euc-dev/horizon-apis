---
layout: page
title: Data Object - ADUserOrGroupBase
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.ADUserOrGroup.ADUserOrGroupBase  
Property of
     [AdminUserOrGroupInfo](vdi.users.AdminUserOrGroup.AdminUserOrGroupInfo.md#field_detail), [ADUserOrGroupInfo](vdi.users.ADUserOrGroup.ADUserOrGroupInfo.md#field_detail), [ADUserOrGroupSummaryView](vdi.users.ADUserOrGroup.ADUserOrGroupSummaryView.md#field_detail), [ADUserOrGroupView](vdi.users.ADUserOrGroup.ADUserOrGroupView.md#field_detail), [EntitledUserOrGroupGlobalSummaryView](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupGlobalSummaryView.md#field_detail), [EntitledUserOrGroupInfo](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupInfo.md#field_detail), [EntitledUserOrGroupLocalSummaryView](vdi.users.EntitledUserOrGroup.EntitledUserOrGroupLocalSummaryView.md#field_detail)  
Since 
    Horizon View 6.0

## Data Object Description 

Basic active directory data for a user or group. This is populated from locally or globally cached LDAP FSPs if available, otherwise it is obtained from AD. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**sid**|  xsd:string|  Security id of this user or group.   


 * This property cannot be updated.

  
**group**|  xsd:boolean|  Whether or not this is a group or a user.   


 * This property cannot be updated.

  
**domain**|  xsd:string|  The domain the user or group is in. This will be the DNS name of the domain.   


 * This property need not be set.
 * This property cannot be updated.

  
**domainNetbiosName**|  xsd:string|  The domain netbios the user or group is in. This will be the netbios name of the domain.  **_Since_** Horizon 7.13  


 * This property need not be set.
 * This property cannot be updated.

  
**adDistinguishedName**|  xsd:string|  Active Directory distinguished name for this user or group.   


 * This property need not be set.
 * This property cannot be updated.

  
**name**|  xsd:string|  Name of the user or group.   


 * This property need not be set.
 * This property cannot be updated.

  
**firstName**|  xsd:string|  First name of the user or group.   


 * This property need not be set.
 * This property cannot be updated.

  
**lastName**|  xsd:string|  Last name of the user or group.   


 * This property need not be set.
 * This property cannot be updated.

  
**loginName**|  xsd:string|  Login name of this user or group.   


 * This property need not be set.
 * This property cannot be updated.

  
**displayName**|  xsd:string|  Login name with domain of this user or group.   


 * This property need not be set.
 * This property cannot be updated.

  
**longDisplayName**|  xsd:string|  Name and login name for a user, display name otherwise.   


 * This property need not be set.
 * This property cannot be updated.

  
**userDisplayName**|  xsd:string|  User display name. This corresponds with displayName attribute in AD.  **_Since_** Horizon 7.3  


 * This property need not be set.
 * This property cannot be updated.

  
**email**|  xsd:string|  Email address of the user or group.   


 * This property need not be set.
 * This property cannot be updated.

  
**kioskUser**|  xsd:boolean|  If this user is a "kiosk user" that supports client authentication. Client authentication is the process of supporting client devices directly logging into resources.   


 * This property cannot be updated.

  
**unauthenticatedAccessUser**|  xsd:boolean|  Whether or not this is unauthenticated access user.  **_Since_** Horizon 7.4  


 * This property need not be set.
 * This property cannot be updated.

  
**phone**|  xsd:string|  Phone number of the user or group. Only available if obtained directly from AD (not cached in LDAP), such as returned by a refresh or with the ADUserOrGroup query interface. Otherwise this will be null.   


 * This property need not be set.
 * This property cannot be updated.

  
**description**|  xsd:string|  Description of the user or group. Only available if obtained directly from AD (not cached in LDAP), such as returned by a refresh or with the ADUserOrGroup query interface. Otherwise this will be null.   


 * This property need not be set.
 * This property cannot be updated.

  
**inFolder**|  xsd:string|  AD folder for the user or group. Only available if obtained directly from AD (not cached in LDAP), such as returned by a refresh or with the ADUserOrGroup query interface. Otherwise this will be null.   


 * This property need not be set.
 * This property cannot be updated.

  
**userPrincipalName**|  xsd:string|  User Principal name(UPN) of the user.  **_Since_** Horizon 7.1  


 * This property need not be set.
 * This property cannot be updated.

  
**guid**|  xsd:string| **Deprecated.**_: Use[formattedGuid](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md#formattedGuid) since that is in RFC 4122 format. _ GUID of the user or group.  **_Since_** Horizon 7.7  


 * This property need not be set.
 * This property cannot be updated.

  
**formattedGuid**|  xsd:string|  GUID of the user or group (same as [guid](vdi.users.ADUserOrGroup.ADUserOrGroupBase.md#guid)) but in RFC 4122 format. example: 5F5A45D9-15C0-4654-8FCF-D589C0EF3ECA  **_Since_** Horizon 7.9  


 * This property need not be set.
 * This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

