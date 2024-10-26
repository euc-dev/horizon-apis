---
layout: page
title: Data Object - SecondaryCredentialsData
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.users.SecondaryCredentials.SecondaryCredentialsData`

Property of
> [SecondaryCredentialsInfo](vdi.users.SecondaryCredentials.SecondaryCredentialsInfo.md#field_detail)

See also
> [SecureString](vdi.util.SecureString.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)


## Data Object Description

SecondaryCredentials Data Object.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**ownerId**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  The owner of secondary credentials. [^2]
**domain**|  xsd:string|  One way or two way trusted domain. This will be the DNS name of the domain. [^2]
**username**|  xsd:string|  Username for secondary credentials account. [^2]
**password**| [SecureString](vdi.util.SecureString.md)|  Password for secondary credentials account.  **_Since_** Horizon 8.8
**adDistinguishedName**|  xsd:string|  DistinguishedName of secondary user account.


 
