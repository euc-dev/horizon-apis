---
layout: page
title: Service - VirtualCenter
hide:
 #- navigation
 - toc
---

  
| | | Local Methods  
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.infrastructure.VirtualCenter
See also
     [MapEntry](vdi.util.MapEntry.md), [ServerDefinition](vdi.utils.Certificate.ServerDefinition.md), [UnsupportedDesktopOrFarmDetails](vdi.infrastructure.VirtualCenter.UnsupportedDesktopOrFarmDetails.md), [VirtualCenterFeatureDetails](vdi.infrastructure.VirtualCenter.VirtualCenterFeatureDetails.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md), [VirtualCenterInfo](vdi.infrastructure.VirtualCenter.VirtualCenterInfo.md), [VirtualCenterSpec](vdi.infrastructure.VirtualCenter.VirtualCenterSpec.md)
Since 
    Horizon View 6.0

  


## Service Description

The virtual center service interface. 

Methods

Methods defined in this Service   
---  
VirtualCenter_Create, VirtualCenter_Delete, VirtualCenter_Get, VirtualCenter_GetFeatureDetailsByServerDefinition, VirtualCenter_List, VirtualCenter_ListUnsupportedDesktopsAndFarmsForVMC, VirtualCenter_Update  
  



Add a virtual center server to the view instance. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to create a Virtual Center server.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VirtualCenter](vdi.infrastructure.VirtualCenter.md) used to make the method call.   
**spec**| [VirtualCenterSpec](vdi.infrastructure.VirtualCenter.VirtualCenterSpec.md)|  attributes needed to add a virtual center server   
  
  


Return Value 

Type |  Description   
---|---  
[VirtualCenterId](vdi.entity.VirtualCenterId.md)| unique identifier for the vc server  
  


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
ADMIN_VC_ADDED|  If the Virtual Center was successfully created.   
ADMIN_VC_LICINV_ALARM_DISABLED|  If the Virtual Center Inventory License Alarm was successfully disabled as part of the creation.   
ADMIN_VC_ADD_FAILED|  If the Virtual Center could not be created.   
  
Show WSDL type definition

  
  
  



Delete a virtual center server from the view instance. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to delete a Virtual Center server.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VirtualCenter](vdi.infrastructure.VirtualCenter.md) used to make the method call.   
**id**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  unique identifier for a virtual center entry   
  
  


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
[InvalidState](vdi.fault.InvalidState.md)| Thrown when there are Desktops present in the Pod with this Virtual Center Id.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  


Events 

Event |  Description   
---|---  
ADMIN_VC_REMOVED|  If the Virtual Center was successfully deleted.   
ADMIN_VC_REMOVE_FAILED|  If the Virtual Center could not be deleted.   
  
Show WSDL type definition

  
  
  



Gets the VcInformation for a specific virtual center entry. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration view is required to retrieve information about a Virtual Center server.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VirtualCenter](vdi.infrastructure.VirtualCenter.md) used to make the method call.   
**id**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  unique identifier for vc entry   
  
  


Return Value 

Type |  Description   
---|---  
[VirtualCenterInfo](vdi.infrastructure.VirtualCenter.VirtualCenterInfo.md)| The VirtualCenterInfo  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Gets the Virtual Center feature details. Using a ServerDefinition allows querying the virtualCenter before it has been added to the environment. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration (read-only) is required to get information on View Storage Accelerator.   
VC_CONFIG_VIEW|  privilege is required to get information about View Storage Accelerator support on a Virtual Center.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VirtualCenter](vdi.infrastructure.VirtualCenter.md) used to make the method call.   
**serverDefinition**| [ServerDefinition](vdi.utils.Certificate.ServerDefinition.md)|  Object needed to connect to a server.   
  
  


Return Value 

Type |  Description   
---|---  
[VirtualCenterFeatureDetails](vdi.infrastructure.VirtualCenter.VirtualCenterFeatureDetails.md)| VirtualCenterFeatureDetails.  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Gets list of VcInfo (primarily the list of attributes about configured virtual center servers). Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration view is required to list Virtual Center servers.   
VC_CONFIG_VIEW|  privilege is required to list Virtual Center servers.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VirtualCenter](vdi.infrastructure.VirtualCenter.md) used to make the method call.   
  


Return Value 

Type |  Description   
---|---  
[VirtualCenterInfo[]](vdi.infrastructure.VirtualCenter.VirtualCenterInfo.md)| The VirtualCenterInfo list  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



List the details of farms and/or desktops which are unsupported for VMC. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  configuration view is required to list the desktop and farms   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VirtualCenter](vdi.infrastructure.VirtualCenter.md) used to make the method call.   
**id**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  virtual center id   
  
  


Return Value 

Type |  Description   
---|---  
[UnsupportedDesktopOrFarmDetails[]](vdi.infrastructure.VirtualCenter.UnsupportedDesktopOrFarmDetails.md)| The array containing the details of farms and desktops which are unsupported for VMC  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Update virtual center server with the set of attributes in the map. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_MANAGEMENT|  Global configuration management is required to update a Virtual Center server.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VirtualCenter](vdi.infrastructure.VirtualCenter.md) used to make the method call.   
**id**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  unique identifier for virtual center entry   
  
**updates**| [MapEntry[]](vdi.util.MapEntry.md)|  key value pairs describing attributes to be updated   


  * This parameter is an update map based on [VirtualCenterInfo](vdi.infrastructure.VirtualCenter.VirtualCenterInfo.md "VirtualCenterInfo"). 

  
  


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
ADMIN_VC_EDITED|  If the Virtual Center was successfully updated.   
  
Show WSDL type definition

  
  
  
  
Top of page| | | Local Methods  
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

