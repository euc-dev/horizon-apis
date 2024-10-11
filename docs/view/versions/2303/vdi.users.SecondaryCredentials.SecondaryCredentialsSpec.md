---
layout: page
title: Data Object - SecondaryCredentialsSpec
hide:
 #- navigation
 - toc
---





Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.users.SecondaryCredentials.SecondaryCredentialsSpec`

Parameter to  
> [SecondaryCredentials_Create](vdi.users.SecondaryCredentials.md#create)

See also  
> [SecureString](vdi.util.SecureString.md), [UserOrGroupId](vdi.entity.UserOrGroupId.md)


## Data Object Description 

SecondaryCredentials Spec Object. 

## Data Object Properties

Properties

Name |  Type |  Description   
---|---|---  
**ownerId**| [UserOrGroupId](vdi.entity.UserOrGroupId.md)|  The owner of secondary credentials.   
  
**domain**|  xsd:string|  One way or two way trusted domain. This will be the DNS name of the domain.   
  
**username**|  xsd:string|  Username for secondary credentials account.   
  
**password**| [SecureString](vdi.util.SecureString.md)|  Password for secondary credentials account.   
  
  
  
 | Local Properties|   
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  
