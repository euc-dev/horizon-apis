---
layout: page
title: Service - GlobalSettings
hide:
 #- navigation
 - toc
---

  
  
  



Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.infrastructure.GlobalSettings`

See also  
> [EnvironmentSettings](vdi.infrastructure.GlobalSettings.EnvironmentSettings.md), [GatewayCertificateInfo](vdi.infrastructure.GlobalSettings.GatewayCertificateInfo.md), [GatewayCertificateSpec](vdi.infrastructure.GlobalSettings.GatewayCertificateSpec.md), [GlobalFeatureSettings](vdi.infrastructure.GlobalSettings.FeatureSettings.md), [GlobalPreLogonSettings](vdi.infrastructure.GlobalSettings.PreLogonSettings.md), [GlobalSettingsInfo](vdi.infrastructure.GlobalSettings.GlobalSettingsInfo.md), [MapEntry](vdi.util.MapEntry.md)

Since  
> Horizon View 6.0


  


## Service Description

Service for specifying global settings. 

Methods

Methods defined in this Service   
---  
GlobalSettings_AddGatewayCertificate, GlobalSettings_DeleteGatewayCertificate, GlobalSettings_Get, GlobalSettings_GetEnvironmentSettings, GlobalSettings_GetFeatureSettings, GlobalSettings_GetPreLogonSettings, GlobalSettings_ListGatewayCertificates, GlobalSettings_Update  
  



Add gateway certificate. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global management is required to add gateway certificate.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalSettings](vdi.infrastructure.GlobalSettings.md) used to make the method call.   
**gatewayCertificateSpec**| [GatewayCertificateSpec](vdi.infrastructure.GlobalSettings.GatewayCertificateSpec.md)|  attributes needed to add gateway certificate.   
  
  


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
VLSI_GATEWAY_CERTIFICATE_ADDED|  If gateway certificate was added successfully.   
  
Show WSDL type definition

  
  
  



Delete gateway certificate. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global management is required to add gateway certificate.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalSettings](vdi.infrastructure.GlobalSettings.md) used to make the method call.   
**certificateName**|  xsd:string|  Certificate identifier in the system.   
  
  


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
VLSI_GATEWAY_CERTIFICATE_DELETED|  If gateway certificate was deleted successfully.   
  
Show WSDL type definition

  
  
  



Gets the Global Settings info for this View cluster. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration (read-only) is required to get global settings information.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalSettings](vdi.infrastructure.GlobalSettings.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[GlobalSettingsInfo](vdi.infrastructure.GlobalSettings.GlobalSettingsInfo.md)| The GlobalSettingsInfo object.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Fetches the settings of the environment. 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalSettings](vdi.infrastructure.GlobalSettings.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[EnvironmentSettings](vdi.infrastructure.GlobalSettings.EnvironmentSettings.md)| The EnvironmentSettingsInfo object.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Gets the feature settings. 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalSettings](vdi.infrastructure.GlobalSettings.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[GlobalFeatureSettings](vdi.infrastructure.GlobalSettings.FeatureSettings.md)| The FeatureSettings object.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Gets the Global Settings info that are required without any user authentication on the login page. 

Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalSettings](vdi.infrastructure.GlobalSettings.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[GlobalPreLogonSettings](vdi.infrastructure.GlobalSettings.PreLogonSettings.md)| The PreLogonSettings object.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



List of gateway certificates configured. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration (read-only) is required to list gateway certificates information.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalSettings](vdi.infrastructure.GlobalSettings.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[GatewayCertificateInfo[]](vdi.infrastructure.GlobalSettings.GatewayCertificateInfo.md)| List of GatewayCertificateInfo objects.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Updates the global settings for this View cluster. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global management is required to update global settings information.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [GlobalSettings](vdi.infrastructure.GlobalSettings.md) used to make the method call.   
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  key value pairs describing attributes to be updated   


  * This parameter is an update map based on [GlobalSettingsInfo](vdi.infrastructure.GlobalSettings.GlobalSettingsInfo.md "GlobalSettingsInfo"). 

  
  


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
VLSI_GLOBAL_SETTINGS_UPDATED|  If all members were successfully updated, this will be sent for each updated member in the update map.   
VLSI_GLOBAL_SETTINGS_UPDATE_FAILED|  If any member could not be updated.   
  
Show WSDL type definition

  
  
  
  
  
  
  
