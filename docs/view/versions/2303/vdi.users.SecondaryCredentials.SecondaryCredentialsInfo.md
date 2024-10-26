---
layout: page
title: Data Object - SecondaryCredentialsInfo
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.users.SecondaryCredentials.SecondaryCredentialsInfo`

Returned by
> [SecondaryCredentials_Get](vdi.users.SecondaryCredentials.md#get), [SecondaryCredentials_List](vdi.users.SecondaryCredentials.md#list)

See also
> [SecondaryCredentialsData](vdi.users.SecondaryCredentials.SecondaryCredentialsData.md), [SecondaryCredentialsId](vdi.entity.SecondaryCredentialsId.md)

Since
> Horizon 7.7


## Data Object Description

Secondary Credentials Info Object.

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**id**| [SecondaryCredentialsId](vdi.entity.SecondaryCredentialsId.md)|  Secondary credentials id. [^2]
**data**| [SecondaryCredentialsData](vdi.users.SecondaryCredentials.SecondaryCredentialsData.md)|  Secondary Credentials Data Object.
**refId**|  xsd:string|  Reference ID used for this Secondary credential.  **_Since_** Horizon 8.9 [^1] [^2]
 


 
