---
layout: page
title: Service - Validator
hide:
 #- navigation
 - toc
---

  
   
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.Validator  
See also
     [ValidationResponse](vdi.utils.Validator.ValidationResponse.md), [ValidationSpec](vdi.utils.Validator.ValidationSpec.md)  
Since 
    Horizon 7.8

  


## Service Description

Methods

Methods defined in this Service   
---  
Validator_validateName  
  



Validates the name provided in the [spec](vdi.utils.Validator.ValidationSpec.md). If the [type](vdi.utils.Validator.ValidationSpec.md#type) is: 
* DESKTOP: validates if the name is unique among existing desktops, farms and applications.
* FARM: validates if the name is unique among existing desktops and farms.
* APPLICATION: validates if the name is unique among existing desktops and applications.
* MACHINE: validates if the naming pattern is unique among existing desktops and farms.

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [Validator](vdi.utils.Validator.md) used to make the method call.   
**spec**| [ValidationSpec](vdi.utils.Validator.ValidationSpec.md)|  The specification for the resource to be validated.   
  
  


Return Value 

Type |  Description   
---|---  
[ValidationResponse](vdi.utils.Validator.ValidationResponse.md)| The [ValidationResponse](vdi.utils.Validator.ValidationResponse.md).  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  

