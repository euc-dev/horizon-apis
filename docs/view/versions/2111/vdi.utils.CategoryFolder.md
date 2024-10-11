---
layout: page
title: Service - CategoryFolder
hide:
 #- navigation
 - toc
---

  
   
  



Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.CategoryFolder`

Since  
> Horizon 7.6


  


## Service Description

Methods

Methods defined in this Service   
---  
CategoryFolder_List  
  



Lists the Category Folders by iterating through the pools. 

Privileges 

Privilege |  Description   
---|---  
POOL_VIEW|  privilege is required with the corresponding access group permission to get the list of Category Folders.   
FEDERATED_LDAP_VIEW|  privilege is required for Global LDAP read.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [CategoryFolder](vdi.utils.CategoryFolder.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
xsd:string[]| A list containing the names of category folders.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  
