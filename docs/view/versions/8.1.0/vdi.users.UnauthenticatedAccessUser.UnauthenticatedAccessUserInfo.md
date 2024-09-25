---
layout: page
title: Data Object - UnauthenticatedAccessUserInfo
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.UnauthenticatedAccessUser.UnauthenticatedAccessUserInfo
Returned by
     [UnauthenticatedAccessUser_Get](vdi.users.UnauthenticatedAccessUser.md#get), [UnauthenticatedAccessUser_List](vdi.users.UnauthenticatedAccessUser.md#list)
See also
     [PodId](vdi.entity.PodId.md), [UnauthenticatedAccessUserData](vdi.users.UnauthenticatedAccessUser.UnauthenticatedAccessUserData.md)

## Data Object Description 

Unauthenticated Access User Info Object. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**userData**| [UnauthenticatedAccessUserData](vdi.users.UnauthenticatedAccessUser.UnauthenticatedAccessUserData.md)|  Unauthenticated Access User Data Object.   
  
**sourcePods**| [PodId[]](vdi.entity.PodId.md)|  Pods in which user was created. The value would be null if the cloud pod architecture is not enabled or if the user does not have FEDERATED_LDAP_VIEW privilege.   


[^1]
  * This property is an unordered array of unique values.
[^2]

  
  
  
Top of page| | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
