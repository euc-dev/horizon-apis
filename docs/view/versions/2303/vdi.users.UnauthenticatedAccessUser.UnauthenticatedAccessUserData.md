---
layout: page
title: Data Object - UnauthenticatedAccessUserData
hide:
 #- navigation
 - toc
---





Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.UnauthenticatedAccessUser.UnauthenticatedAccessUserData  
Property of
     [UnauthenticatedAccessUserInfo](vdi.users.UnauthenticatedAccessUser.UnauthenticatedAccessUserInfo.md#field_detail)  
Parameter to
     [UnauthenticatedAccessUser_Create](vdi.users.UnauthenticatedAccessUser.md#create), [UnauthenticatedAccessUser_Update](vdi.users.UnauthenticatedAccessUser.md#update)  
See also
     [SecureString](vdi.util.SecureString.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)  

## Data Object Description 

Unauthenticated Access User Data Object. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**loginName**|  xsd:string|  Login name which is used for login from client. If the value is null then loginName of the AD user would be used.   


* This property need not be set.

  
**userId**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  AD user id to associate with Unauthenticated Access.   


* This property cannot be updated.

  
**description**|  xsd:string|  Description of the Unauthenticated Access log on user.   


* This property need not be set.

  
**hybridLogonConfig**|  xsd:string|  Hybrid logon config value. If the value is null then hybrid logon is disabled  **_Since_** Horizon 7.7  


* This property need not be set.
  * This property will be one of:  
|  Value |  Description   
---|---  
"password"| PASSWORD: Authentication via user name and password  
"truesso"| TRUESSO: Authentication via TrueSSO  
"unknown"| UNKNOWN: Authentication method is unknown  

  
**hybridLogonPassword**| [SecureString](vdi.util.SecureString.md)|  User's domain password in encrypted format. This is used if we setup Hybrid logon to use username & password. This is null when Hybrid logon is disabled or used in modes other than password  **_Since_** Horizon 7.7  


* This property need not be set.
  * This property is required if hybridLogonConfig is set to "password".

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

