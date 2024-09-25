---
layout: page
title: Service - VirtualSAN
hide:
 #- navigation
 - toc
---

  
| | | Local Methods  
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  



Java Class
    com.vmware.vdi.vlsi.binding.vdi.utils.virtualcenter.VirtualSAN
See also
     [HostOrClusterId](vdi.entity.HostOrClusterId.md), [VirtualCenterId](vdi.entity.VirtualCenterId.md), [VsanDatastoreCost](vdi.utils.virtualcenter.VirtualSAN.VsanDatastoreCost.md)
Since 
    Horizon View 6.0

  


## Service Description

Utility for obtaining information about Virtual SAN (VSAN) support from Virtual Center. 

Methods

Methods defined in this Service   
---  
VirtualSAN_GetVsanDatastoreCostForFullClone, VirtualSAN_GetVsanDatastoreCostForInstantClone, VirtualSAN_GetVsanDatastoreCostForLinkedClone, VirtualSAN_IsSupportedByHostOrCluster, VirtualSAN_IsSupportedByVirtualCenter  
  



Returns datastore cost factors for full clone pools when VSAN is used. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration (read-only) is required to get VSAN data store cost.   
VC_CONFIG_VIEW|  privilege is required to get VSAN data store cost.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VirtualSAN](vdi.utils.virtualcenter.VirtualSAN.md) used to make the method call.   
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  unique identifier for the vc   
  
**isPersistent**|  xsd:boolean|  cost factor for a persistent pool   
  
  


Return Value 

Type |  Description   
---|---  
[VsanDatastoreCost](vdi.utils.virtualcenter.VirtualSAN.VsanDatastoreCost.md)| datastore cost factor  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Returns datastore cost factors for instant clone pools when VSAN is used. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration (read-only) is required to get VSAN data store cost.   
VC_CONFIG_VIEW|  is required to get VSAN data store cost.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VirtualSAN](vdi.utils.virtualcenter.VirtualSAN.md) used to make the method call.   
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  unique identifier for the vc   
  
**isPersistent**|  xsd:boolean|  cost factor for a persistent pool   
  
  


Return Value 

Type |  Description   
---|---  
[VsanDatastoreCost](vdi.utils.virtualcenter.VirtualSAN.VsanDatastoreCost.md)| datastore cost factor  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Returns datastore cost factors for linked clone pools when VSAN is used. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration (read-only) is required to get VSAN data store cost.   
VC_CONFIG_VIEW|  privilege is required to get VSAN data store cost.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VirtualSAN](vdi.utils.virtualcenter.VirtualSAN.md) used to make the method call.   
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  unique identifier for the vc   
  
**isPersistent**|  xsd:boolean|  cost factor for a persistent pool   
  
  


Return Value 

Type |  Description   
---|---  
[VsanDatastoreCost](vdi.utils.virtualcenter.VirtualSAN.VsanDatastoreCost.md)| datastore cost factor  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Determines whether virtual SAN is supported for the given virtual center. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration (read-only) is required to get whether virtual SAN is supported.   
VC_CONFIG_VIEW|  privilege is required to get whether virtual SAN is supported.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VirtualSAN](vdi.utils.virtualcenter.VirtualSAN.md) used to make the method call.   
**hostOrCluster**| [HostOrClusterId](vdi.entity.HostOrClusterId.md)|  unique identifier for the host or cluster   
  
  


Return Value 

Type |  Description   
---|---  
xsd:string| A code that determines whether virtual SAN is supported.

  * This property will be one of:  
|  Value |  Description   
---|---  
"VSAN_VALIDATION_OK"| VirtualSAN has been validated to be supported.  
"VSAN_UNSUPPORTED_VC"| VirtualSAN is only supported on Virtual Center version 5.5 and greater.  
"VSAN_UNSUPPORTED_HOST_OR_CLUSTER"| VirtualSAN is only supported on hosts or clusters version 5.5 and greater.  
"VSAN_NOT_CONFIGURED"| VirtualSAN is only supported on Virtual Centers and hosts or clusters with at least one VSAN datastore present.  

  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  



Determines whether virtual SAN is supported for the given virtual center. Requires at least one of the listed privileges. 

Privileges 

Privilege |  Description   
---|---  
GLOBAL_CONFIG_VIEW|  Global configuration (read-only) is required to get whether virtual SAN is supported.   
VC_CONFIG_VIEW|  privilege is required to get whether virtual SAN is supported.   
  


Parameters 

Name| Type| Description  
---|---|---  
**_this**| [ManagedObjectReference](vmodl.ManagedObjectReference.md)|  A reference to the [VirtualSAN](vdi.utils.virtualcenter.VirtualSAN.md) used to make the method call.   
**virtualCenter**| [VirtualCenterId](vdi.entity.VirtualCenterId.md)|  unique identifier for the vc.   
  
  


Return Value 

Type |  Description   
---|---  
xsd:string| A code that determines whether virtual SAN is supported.

  * This property will be one of:  
|  Value |  Description   
---|---  
"VSAN_VALIDATION_OK"| VirtualSAN has been validated to be supported.  
"VSAN_UNSUPPORTED_VC"| VirtualSAN is only supported on Virtual Center version 5.5 and greater.  
"VSAN_NOT_CONFIGURED"| VirtualSAN is only supported on Virtual Centers and hosts or clusters with at least one VSAN datastore present.  

  
  


Faults 

Type |  Description   
---|---  
[EntityNotFound](vdi.fault.EntityNotFound.md)| Thrown if any specified entity cannot be found.  
[InsufficientPermission](vdi.fault.InsufficientPermission.md)| Thrown if the user does not have sufficient permission to perform the operation.  
[InvalidArgument](vdi.fault.InvalidArgument.md)| Thrown if any specified argument is invalid.  
[InvalidType](vdi.fault.InvalidType.md)| Thrown if the type of any specified argument is invalid.  
[UnexpectedFault](vdi.fault.UnexpectedFault.md)| Thrown if an unexpected error occurs while performing the operation.  
  
Show WSDL type definition

  
  
  
  
Top of page| | | Local Methods  
---|---|---|---  
[Service Types](index-mo_types.md)| [Data Object Types](index-do_types.md)| [All Properties](index-properties.md)| [All Methods](index-methods.md)  
  
  

