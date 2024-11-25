---
layout: page
title: Data Object - UnauthenticatedAccessUserData
hide:
#  - navigation
  - toc
---





Java Class
> `com.omnissa.vdi.vlsi.binding.vdi.users.UnauthenticatedAccessUser.UnauthenticatedAccessUserData`

Property of
> [UnauthenticatedAccessUserInfo](vdi.users.UnauthenticatedAccessUser.UnauthenticatedAccessUserInfo.md#field_detail)

Parameter to
> [UnauthenticatedAccessUser_Create](vdi.users.UnauthenticatedAccessUser.md#create), [UnauthenticatedAccessUser_Update](vdi.users.UnauthenticatedAccessUser.md#update)

See also
> [SecureString](vdi.util.SecureString.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon View 6.0


## Data Object Description

Unauthenticated Access User Data Object.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**loginName**|  xsd:string|  Login name which is used for login from client. If the value is null then loginName of the AD user would be used. [^1]
**userId**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  AD user id to associate with Unauthenticated Access. [^2]
**description**|  xsd:string|  Description of the Unauthenticated Access log on user. [^1]
**hybridLogonConfig**|  xsd:string|  Hybrid logon config value. If the value is null then hybrid logon is disabled  **_Since_** Horizon 7.7 [^1] <br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>password</td><td>PASSWORD: Authentication via user name and password</td></tr><tr><td>truesso</td><td>TRUESSO: Authentication via TrueSSO</td></tr><tr><td>unknown</td><td>UNKNOWN: Authentication method is unknown</td></tr></table>
**hybridLogonPassword**| [SecureString](vdi.util.SecureString.md)|  User's domain password in encrypted format. This is used if we setup Hybrid logon to use username & password. This is null when Hybrid logon is disabled or used in modes other than password  **_Since_** Horizon 7.7 [^1] [^138]
 


 


[^1]: This property need not be set.
[^2]: This property cannot be updated.
[^138]: This property is required if hybridLogonConfig is set to "password".