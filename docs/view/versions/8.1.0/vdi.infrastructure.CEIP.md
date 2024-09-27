---
layout: page
title: Service - CEIP
hide:
 #- navigation
 - toc
---

  
 
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.CEIP  
See also
     [CEIPInfo](vdi.infrastructure.CEIP.CEIPInfo.md), [CEIPLoginTypeSpec](vdi.infrastructure.CEIP.CEIPLoginTypeSpec.md), [MapEntry](vdi.util.MapEntry.md)  
Since 
    Horizon View 6.0

  


## Service Description

The Customer Experience Improvement Program service interface. 

Methods

Methods defined in this Service   
---  
CEIP_Get, CEIP_SetLoginType, CEIP_Update  
  



Gets the CEIP info. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration view privilege is required to retrieve the CEIP configuration.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [CEIP](vdi.infrastructure.CEIP.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[CEIPInfo](vdi.infrastructure.CEIP.CEIPInfo.md)| The CEIP info.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Set the login type for CEIP reporting. 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [CEIP](vdi.infrastructure.CEIP.md) used to make the method call.   
**type**| [CEIPLoginTypeSpec](vdi.infrastructure.CEIP.CEIPLoginTypeSpec.md)|  The login type for the current authenticated session.   
  
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Updates the CEIP info using the update map. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management privilege is required to modify the CEIP configuration.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [CEIP](vdi.infrastructure.CEIP.md) used to make the method call.   
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  The updates to apply.   


  * This parameter is an update map based on [CEIPInfo](vdi.infrastructure.CEIP.CEIPInfo.md "CEIPInfo"). 

  
  


Return Value 

Type |  Description   
---|---  
None  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
VLSI_CEIP_UPDATED|  If all members were successfully updated, this will be sent for each updated member in the update map.   
VLSI_CEIP_UPDATE_FAILED|  If any member could not be updated.   
  
Show WSDL type definition

  
  
  
  
  
  
  

