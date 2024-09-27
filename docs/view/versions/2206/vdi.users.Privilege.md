---
layout: page
title: Service - Privilege
hide:
 #- navigation
 - toc
---

  
  
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.users.Privilege  
See also
     [PrivilegeInfo](vdi.users.Privilege.PrivilegeInfo.md)  
Since 
    Horizon 7.8

  


## Service Description

Represents Privilege service. 

Methods

Methods defined in this Service   
---  
Privilege_ListSelectablePrivileges  
  



Lists the selectable privileges in the system. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_ROLE_VIEW|  Role read access privilege is required to read selectable privileges.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Privilege](vdi.users.Privilege.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[PrivilegeInfo[]](vdi.users.Privilege.PrivilegeInfo.md)| The list of selectable privileges.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  

