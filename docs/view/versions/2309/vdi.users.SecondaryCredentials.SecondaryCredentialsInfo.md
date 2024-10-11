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
**id**| [SecondaryCredentialsId](vdi.entity.SecondaryCredentialsId.md)|  Secondary credentials id.   


 * This property cannot be updated.

  
**data**| [SecondaryCredentialsData](vdi.users.SecondaryCredentials.SecondaryCredentialsData.md)|  Secondary Credentials Data Object.   
  
**refId**|  xsd:string|  Reference ID used for this Secondary credential.  **_Since_** Horizon 8.9  


 * This property need not be set.
 * This property cannot be updated.

  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
