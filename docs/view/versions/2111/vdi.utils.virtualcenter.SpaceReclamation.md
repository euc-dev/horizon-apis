---
layout: page
title: Service - SpaceReclamation
hide:
 #- navigation
 - toc
---

  
   
  



Java Class  
> `com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.SpaceReclamation`

See also  
> [ServerDefinition](vdi.utils.Certificate.ServerDefinition.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md)

Since  
> Horizon View 6.0


  


## Service Description

The object for fetching space reclamation attributes from virtual center. 

Methods

Methods defined in this Service   
---  
SpaceReclamation_IsSupportedByServerDefinition, SpaceReclamation_IsSupportedByVirtualCenter  
  



Determines whether space reclamation is supported for the given virtual center. Using a ServerDefinition allows querying the server before it has been added to the broker. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration (read-only) is required to get whether space reclamation is supported.   
VC_CONFIG_VIEW|  privilege is required to get whether space reclamation is supported.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [SpaceReclamation](vdi.utils.virtualcenter.SpaceReclamation.md) used to make the method call.   
**serverDefinition**| [ServerDefinition](vdi.utils.Certificate.ServerDefinition.md)|  Details (ip, user, passord, etc.) needed to connect to a server.   
  
  


Return Value 

Type |  Description   
---|---  
xsd:string| A code that determines whether space reclamation is supported.

  * This property will be one of:  
|  Value |  Description   
---|---  
"SR_VALIDATION_OK"| Virtual center supports space reclamation.  
"SR_UNSUPPORTED_VC"| Virtual center does not support space reclamation.  
"SR_RECLAMATION_DISABLED"| The feature has been disabled for the virtual center.  
"SR_FEATURE_DISABLED"| Space reclamation has been disabled globally.  

  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Determines whether space reclamation is supported for the given virtual center. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration (read-only) is required to get whether space reclamation is supported.   
VC_CONFIG_VIEW|  privilege is required to get whether space reclamation is supported.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [SpaceReclamation](vdi.utils.virtualcenter.SpaceReclamation.md) used to make the method call.   
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  unique identifier for vc entry   
  
  


Return Value 

Type |  Description   
---|---  
xsd:string| A code that determines whether space reclamation is supported.

  * This property will be one of:  
|  Value |  Description   
---|---  
"SR_VALIDATION_OK"| Virtual center supports space reclamation.  
"SR_UNSUPPORTED_VC"| Virtual center does not support space reclamation.  
"SR_RECLAMATION_DISABLED"| The feature has been disabled for the virtual center.  
"SR_FEATURE_DISABLED"| Space reclamation has been disabled globally.  

  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
  
  
  
