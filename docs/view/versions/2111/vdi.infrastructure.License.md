---
layout: page
title: Service - License
hide:
 #- navigation
 - toc
---

  
   
  



Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.License`

See also  
> [LicenseInfo](vdi.infrastructure.License.LicenseInfo.md)

Since  
> Horizon View 6.0


  


## Service Description

The license service interface. 

Methods

Methods defined in this Service   
---  
License_Get, License_Set  
  



Gets the license information. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration view is required to read [licenseKey](vdi.infrastructure.License.LicenseInfo.md#licenseKey) and [expirationTime](vdi.infrastructure.License.LicenseInfo.md#expirationTime) properties. These properties will be unset otherwise.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [License](vdi.infrastructure.License.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[LicenseInfo](vdi.infrastructure.License.LicenseInfo.md)| The information on the license  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Sets the license key for the View instance. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to set the license.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [License](vdi.infrastructure.License.md) used to make the method call.   
**licenseKey**|  xsd:string|  The license key to set.   
  
  


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
[InvalidLicense](vdi.fault.InvalidLicense.md)| Thrown if the license is invalid  
[InvalidState](vdi.fault.InvalidState.md)| when #licenseMode set to SUBSCRIPTION value  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
ADMIN_ADD_LICENSE|  If the license key was successfully set.   
ADMIN_ADD_LICENSE_FAILED|  If the license key could not be set.   
  
Show WSDL type definition

  
  
  
  
  
  
  
