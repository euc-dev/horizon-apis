---
layout: page
title: Data Object - ServiceAccount
hide:
#- navigation
- toc
---





Java Class
> `com.vmware.vdi.vlsi.binding.vdi.health.ADDomainHealth.ServiceAccount`

Property of
> [ADDomainHealthInfo](vdi.health.ADDomainHealth.ADDomainHealthInfo.md#field_detail)

See also
> [UserOrGroupId](vdi.entity.UserOrGroupId.md)

Since
> Horizon 8.2


## Data Object Description

## Data Object Properties
Properties
Name |  Type |  Description
---|---|---
**ownerId**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  The owner of secondary credentials. [^1]
**username**|  xsd:string|  Service account username.
**status**|  xsd:string|  Status of the service account.<br>* This property will be one of:<br><table><tr><th>Value</th><th>Description</th></tr><tr><td>"ACTIVE"</td><td>The service account credentials are working properly.</td></tr><tr><td>"ERROR"</td><td>The service account credentials are not working.</td></tr><tr><td>"UNKNOWN"</td><td>Status of the service account credentials is unknown.</td></tr></table>


 
