---
layout: page
title: Data Object - SecondaryCredentialsData
hide:
#  - navigation
  - toc
---





Java Class
> ` com.omnissa.vdi.vlsi.binding.vdi.users.SecondaryCredentials.SecondaryCredentialsData`

Property of
> [SecondaryCredentialsInfo](vdi.users.SecondaryCredentials.SecondaryCredentialsInfo.md#field_detail)

See also
> [UserOrGroupId](vdi.entity.UserOrGroupId.md)


## Data Object Description

SecondaryCredentials Data Object.

## Data Object Properties

 Name | Type | Description
:---|:---:|:---
**ownerId**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  The owner of secondary credentials. [^2]
**domain**|  xsd:string|  One way or two way trusted domain. This will be the DNS name of the domain. [^2]
**username**|  xsd:string|  Username for secondary credentials account.
**adDistinguishedName**|  xsd:string|  DistinguishedName of secondary user account.


 


[^2]: This property cannot be updated.